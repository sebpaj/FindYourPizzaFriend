import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id

from users.models import User
from graphql_api.api import schema

USERS_QUERY = """
  query Users{
    users{
      edges{
        node{
          firstName
          lastName
          imageUrl
          email
        }
      }
    }
  }
"""


class UsersQueryTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = "/"
    fixtures = ("tests/data/test_data.json",)

    def test_users_query(self):
        # setup

        # execute
        response = self.query(USERS_QUERY, op_name="Users")

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["users"]["edges"]

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["node"]["firstName"], "test_user")
        self.assertEqual(result[0]["node"]["lastName"], "")
        self.assertEqual(result[0]["node"]["imageUrl"], "")
        self.assertEqual(result[0]["node"]["email"], "test_user@test.com")

