import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay, AbstractType, ObjectType
from source.events.models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
