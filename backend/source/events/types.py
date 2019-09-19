from graphene_django.types import DjangoObjectType
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
