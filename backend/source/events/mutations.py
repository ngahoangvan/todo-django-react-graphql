import graphene
from graphene_django.types import DjangoObjectType
from .types import EventType
from ..events.models import Event
from ..commons.helpers import update_create_instance
from graphql import GraphQLError


class EventInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    price = graphene.Float()
    date = graphene.String()


class CreateEvent(graphene.Mutation):
    class Arguments:
        eventInput = EventInput(required=True)

    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    @staticmethod
    def mutate(root, info, eventInput=None):
        ok = True
        event_instance = Event()
        update_create_instance(event_instance, eventInput)
        return CreateEvent(ok=ok, event=event_instance)


class UpdateEvent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        eventInput = EventInput(required=True)

    ok = graphene.Boolean()
    event = graphene.Field(EventType)

    @staticmethod
    def mutate(root, info, id, eventInput=None):
        ok = False
        try:
            event_instance = Event.objects.get(pk=id)
            ok = True
            update_create_instance(event_instance, eventInput)
            return UpdateEvent(ok=ok, event=event_instance)
        except Event.DoesNotExist:
            return GraphQLError("Event with id {} doesn't exist".format(id))


class DeleteEvent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info, id):
        ok = False
        try:
            event_instance = Event.objects.get(pk=id)
            ok = True
            event_instance.delete()
            return DeleteEvent(ok=ok, message="Delete event {} successfull".format(id))
        except Event.DoesNotExist:
            return GraphQLError("Event with id {} doesn't exist".format(id))
