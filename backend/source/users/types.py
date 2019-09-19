from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .models import UserProfile, UserImage
from ..events.types import EventType


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserImageType(DjangoObjectType):
    class Meta:
        model = UserImage
