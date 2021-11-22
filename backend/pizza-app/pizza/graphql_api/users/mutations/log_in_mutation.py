import graphene
from graphene import relay

from ....users.models import User


class LoginMutation(relay.ClientIDMutation):
    class Input:
        first_name = graphene.String(required=True)
        email = graphene.String(required=True)
        image_url = graphene.String(required=True)

    success = graphene.Boolean(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        result = User.objects.create(**input)
        print('yup dones')
