import json

from graphene_django.utils.testing import GraphQLTestCase

class MyFancyTestCase(GraphQLTestCase):
    def test_some_query(self):
        response = self.query(
            '''
            query {
                allCategories {
                   edges {
                      node {
                         name
                        ingredients {
                            edges {
                                node {
                                    name
                                    }
                                }
                            }
                        }
                    
                }
            }
            ''',
            op_name='allCategories'
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)