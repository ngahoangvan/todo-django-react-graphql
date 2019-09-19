import graphene
from django.contrib.auth.models import User
from graphene import relay, AbstractType, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import UserProfile, UserImage
from .types import UserProfileType, UserType, UserImageType
from .mutation import CreateUser, UpdateUser


class Query(ObjectType):
    userprofile = graphene.Field(UserProfileType, id=graphene.Int())
    # userprofiles = graphene.List(UserProfileType)
    userimage = graphene.List(UserImageType)
    images = graphene.List(UserImageType)
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    # def resolve_userprofile(self, info, **kwargs):
    #     id = kwargs.get("id")
    #     try:
    #         return UserProfile.objects.get(pk=id)
    #     except UserProfile.DoesNotExist:
    #         return None

    #     return None

    # def resolve_userprofiles(self, info, **kwargs):
    #     return UserProfile.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get("id")
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

        return None

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_images(self, info, **kwargs):
        return UserImage.objects.all()


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
