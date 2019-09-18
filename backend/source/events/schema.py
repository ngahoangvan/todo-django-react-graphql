import graphene
from graphene import relay, AbstractType, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Event
from .mutations import CreateEvent, UpdateEvent, DeleteEvent
from .types import EventType
from ..users.types import UserType


class Query(ObjectType):
    event = graphene.Field(EventType, id=graphene.Int())
    events = graphene.List(EventType)
    users = graphene.List(UserType)

    def resolve_event(self, info, **kwargs):
        id = kwargs.get("id")
        try:
            return Event.objects.get(pk=id)
        except Event.DoesNotExist:
            return None

        return None

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()


class Mutation(ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()
