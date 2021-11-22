import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id

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

    def test_login_mutation(self):
        # setup
        first_name = "test_user"
        email = "test_user@test.com"
        image_url = ""

        # execute
        print("am i calling?")
        response = self.query(
            LOGIN_MUTATION,
            op_name="Login",
            variables={"input": {"firstName": first_name, "email": email, "imageUrl": image_url}},
        )
        print(response)
        content = json.loads(response.content)
        print(content)
        #
        # # assert
        # self.assertResponseNoErrors(response)
        # content = json.loads(response.content)
        # result = content["data"]["users"]["edges"]
        #
        # self.assertEqual(len(result), 1)
        # self.assertEqual(result[0]["node"]["firstName"], "test_user")
        # self.assertEqual(result[0]["node"]["lastName"], "")
        # self.assertEqual(result[0]["node"]["imageUrl"], "")
        # self.assertEqual(result[0]["node"]["email"], "test_user@test.com")
