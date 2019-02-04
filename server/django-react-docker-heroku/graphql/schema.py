import graphene


class Query(graphene.ObjectType):
    yay = graphene.String()

    def resolve_yay(self, info, **kwargs):
        return "woot"
