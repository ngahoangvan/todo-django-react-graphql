import graphene
from django.contrib.auth.models import User
from graphene import ObjectType
from .models import UserProfile, UserImage
from .types import UserProfileType, UserType, UserImageType
from .mutation import CreateUser, UpdateUser


class Query(ObjectType):
    """Define a User Query
    """
    userprofile = graphene.Field(UserProfileType, id=graphene.Int())
    userimage = graphene.List(UserImageType)
    images = graphene.List(UserImageType)
    user = graphene.Field(UserType, id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        """Graphene resolve user
        # Parameters
            info: graphql.execution.base.ResolveInfo
        # Return
            A User object if exist
            Null if not exist
        """
        id = kwargs.get("id")
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def resolve_users(self, info, **kwargs):
        """Graphene resolve users
        # Parameters
            info: graphql.execution.base.ResolveInfo
        # Return
            A List of User object
        """
        return User.objects.all()

    def resolve_images(self, info, **kwargs):
        return UserImage.objects.all()


class Mutation(ObjectType):
    """Define a User Mutation
    """
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
