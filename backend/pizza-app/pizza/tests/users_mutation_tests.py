import json

from graphene_django.utils.testing import GraphQLTestCase

from users.models import User
from graphql_api.api import schema

LOGIN_MUTATION = """
    mutation Login($input: LoginMutationInput!) {
        login(input: $input) {
        success
        }
    }
"""


class UsersMutationTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = "/"
    fixtures = ("tests/data/test_data.json",)

    def test_login_mutation_existing_user(self):
        # setup
        first_name = "test_user_1"
        email = "test_user_1@test.com"
        image_url = ""

        # execute
        response = self.query(
            LOGIN_MUTATION,
            op_name="Login",
            variables={"input": {"firstName": first_name, "email": email, "imageUrl": image_url}},
        )

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)

        self.assertEqual(content["data"]["login"]["success"], True)
        self.assertEqual(User.objects.all().count(), 6)

    def test_login_mutation_new_user(self):
        # setup
        first_name = "test_user_7"
        email = "test_user_7@test.com"
        image_url = ""

        # execute
        response = self.query(
            LOGIN_MUTATION,
            op_name="Login",
            variables={"input": {"firstName": first_name, "email": email, "imageUrl": image_url}},
        )

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)

        self.assertEqual(content["data"]["login"]["success"], True)
        self.assertEqual(User.objects.all().count(), 7)
