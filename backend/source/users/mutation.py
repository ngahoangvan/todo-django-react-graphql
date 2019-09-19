import graphene
from django.contrib.auth.models import User
from graphql import GraphQLError
from .models import UserImage, UserProfile
from .types import UserType, UserProfileType, UserImageType
from ..commons.helpers import update_create_instance


class UserImageInput(graphene.InputObjectType):
    id = graphene.ID()
    original = graphene.String()


class UserProfileInput(graphene.InputObjectType):
    id = graphene.ID()
    birthday = graphene.String()
    address = graphene.String()
    phone_number = graphene.String()
    image = graphene.List(UserImageInput)


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    profile = graphene.Field(UserProfileInput)


class CreateUser(graphene.Mutation):
    class Arguments:
        userInput = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, userInput=None):
        ok = True
        user_instace = update_create_instance(User(), userInput)
        if userInput.profile:
            update_create_instance(UserProfile.objects.create(user=user_instace), userInput.profile)
        else:
            UserProfile.objects.create(user=user_instace)
        return CreateUser(ok=ok, user=user_instace)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        userInput = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, userInput=None):
        ok = False
        try:
            if userInput.password is not None and len(userInput.password) >= 78:
                raise GraphQLError("Your password is so long")
            user_instace = User.objects.get(pk=id)
            ok = True
            update_create_instance(user_instace, userInput)
            if userInput.profile:
                update_create_instance(UserProfile.objects.get(user=user_instace), userInput.profile)
            return UpdateUser(ok=ok, user=user_instace)
        except User.DoesNotExist:
            raise GraphQLError("User with id {} doesn't exist".format(id))
