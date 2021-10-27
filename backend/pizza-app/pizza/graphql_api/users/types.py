from django.contrib.auth import get_user_model
from graphene import relay
from graphene_django.types import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        filter_fields = {"email": ["exact", "icontains", "istartswith"]}
        interfaces = (relay.Node,)
