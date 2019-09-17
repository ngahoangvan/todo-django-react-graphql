import graphene
import graphql_jwt
import source.events.schema as event_schema


class Query(event_schema.Query, graphene.ObjectType):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to our project
    """

    pass


class Mutation(event_schema.Mutation, graphene.ObjectType):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to our project
    """

    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
