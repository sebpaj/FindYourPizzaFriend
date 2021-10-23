import json
from graphene_django.utils.testing import GraphQLTestCase

from graphql_api.api import schema

ALL_CATEGORIES_QUERY = """
query AllCategories{
  allCategories{
    edges{
      node{
        name
        ingredients{
          edges{
            node{
              name
            }
          }
        }
      }
    }
  }
}
"""


class CommonQueryTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = "/"

    def test_some_query(self):
        response = self.query(ALL_CATEGORIES_QUERY, op_name="AllCategories")

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
