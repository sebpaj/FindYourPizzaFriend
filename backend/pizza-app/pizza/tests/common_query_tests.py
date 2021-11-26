import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id

from common.models import Category, Pizza
from graphql_api.api import schema
from users.models import User

ALL_CATEGORIES_QUERY = """
query AllCategories{
  allCategories{
    edges{
      node{
        name
      }
    }
  }
}
"""


CATEGORY_QUERY = """
query Category($id: ID!){
  category(id: $id){
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
"""


ALL_PIZZAS_QUERY = """
query AllPizzas{
  allPizzas{
    edges{
      node{
        name
      }
    }
  }
}
"""


PIZZA_QUERY = """
query Pizza($id: ID!){
  pizza(id: $id){
    name
    user{
        firstName
    }
    ingredients{
      edges{
        node{
          name
        }
      }
    }
     usersWithSamePizza{
      user{
        firstName
      }
      pizza 
    }
  }
}
"""


class CommonQueryTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = "/"
    fixtures = ("tests/data/test_data.json",)

    def test_all_categories_query(self):
        # setup

        # execute
        response = self.query(ALL_CATEGORIES_QUERY, op_name="AllCategories")

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["allCategories"]["edges"]

        self.assertEqual(len(result), 5)
        self.assertEqual(result[0]["node"]["name"], "Cheeses")
        self.assertEqual(result[1]["node"]["name"], "Meat")
        self.assertEqual(result[2]["node"]["name"], "Sauce")
        self.assertEqual(result[3]["node"]["name"], "Extras")
        self.assertEqual(result[4]["node"]["name"], "Vegetables")

    def test_category_query(self):
        # setup
        cheeses_category = Category.objects.get(name="Cheeses")
        cheeses_category_id = to_global_id("CategoryType", cheeses_category.id)

        # execute
        response = self.query(
            CATEGORY_QUERY, op_name="Category", variables={"id": cheeses_category_id}
        )

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["category"]

        self.assertEqual(result["name"], "Cheeses")
        self.assertEqual(len(result["ingredients"]["edges"]), 7)
        self.assertEqual(result["ingredients"]["edges"][0]["node"]["name"], "Cheese")
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"],
            "Smoked ewe's milk cheese made in the Tatra Mountains",
        )
        self.assertEqual(result["ingredients"]["edges"][2]["node"]["name"], "Camembert")
        self.assertEqual(result["ingredients"]["edges"][3]["node"]["name"], "Cheese XL")
        self.assertEqual(result["ingredients"]["edges"][4]["node"]["name"], "Parmesan")
        self.assertEqual(result["ingredients"]["edges"][5]["node"]["name"], "Feta")
        self.assertEqual(
            result["ingredients"]["edges"][6]["node"]["name"], "Magic cheese"
        )

    def test_all_pizzas_query(self):
        # setup

        # execute
        response = self.query(ALL_PIZZAS_QUERY, op_name="AllPizzas")

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["allPizzas"]["edges"]
        print(result)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0]["node"]["name"], "Capriciosa")
        self.assertEqual(result[1]["node"]["name"], "Ham and mushrooms")
        self.assertEqual(result[2]["node"]["name"], "Pepperoni")
        self.assertEqual(result[3]["node"]["name"], "Cheese and salami")
        self.assertEqual(result[4]["node"]["name"], "Salami with cheese")
        self.assertEqual(result[5]["node"]["name"], "Capriciosa")

    def test_pizza_user_1_query(self):
        # setup
        pizza_name = "Capriciosa"
        pizza_user = User.objects.get(first_name="test_user_1")

        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic cheese"
        )
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"], "Magic mushrooms"
        )
        self.assertEqual(result["ingredients"]["edges"][2]["node"]["name"], "Magic ham")
        self.assertEqual(result["usersWithSamePizza"][0]["user"]["firstName"], "test_user_2")
        self.assertEqual(result["usersWithSamePizza"][0]["pizza"], "Ham and mushrooms")
        self.assertEqual(result["usersWithSamePizza"][1]["user"]["firstName"], "test_user_6")
        self.assertEqual(result["usersWithSamePizza"][1]["pizza"], "Capriciosa")

    def test_pizza_user_2_query(self):
        # setup
        pizza_name = "Ham and mushrooms"
        pizza_user = User.objects.get(first_name="test_user_2")
        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic cheese"
        )
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"], "Magic mushrooms"
        )
        self.assertEqual(result["ingredients"]["edges"][2]["node"]["name"], "Magic ham")
        self.assertEqual(result["usersWithSamePizza"][0]["user"]["firstName"], "test_user_1")
        self.assertEqual(result["usersWithSamePizza"][0]["pizza"], "Capriciosa")
        self.assertEqual(result["usersWithSamePizza"][1]["user"]["firstName"], "test_user_6")
        self.assertEqual(result["usersWithSamePizza"][1]["pizza"], "Capriciosa")

    def test_pizza_user_3_query(self):
        # setup
        pizza_name = "Pepperoni"
        pizza_user = User.objects.get(first_name="test_user_3")
        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic salami"
        )

        self.assertEqual(result["usersWithSamePizza"], [])

    def test_pizza_user_4_query(self):
        # setup
        pizza_name = "Cheese and salami"
        pizza_user = User.objects.get(first_name="test_user_4")
        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic cheese"
        )
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"], "Magic salami"
        )
        self.assertEqual(result["usersWithSamePizza"][0]["user"]["firstName"], "test_user_5")
        self.assertEqual(result["usersWithSamePizza"][0]["pizza"], "Salami with cheese")

    def test_pizza_user_5_query(self):
        # setup
        pizza_name = "Salami with cheese"
        pizza_user = User.objects.get(first_name="test_user_5")
        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic cheese"
        )
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"], "Magic salami"
        )
        self.assertEqual(result["usersWithSamePizza"][0]["user"]["firstName"], "test_user_4")
        self.assertEqual(result["usersWithSamePizza"][0]["pizza"], "Cheese and salami")

    def test_pizza_user_6_query(self):
        # setup
        pizza_name = "Capriciosa"
        pizza_user = User.objects.get(first_name="test_user_6")
        pizza = Pizza.objects.get(name=pizza_name, user=pizza_user)
        pizza_id = to_global_id("PizzaType", pizza.id)

        # execute
        response = self.query(PIZZA_QUERY, op_name="Pizza", variables={"id": pizza_id})

        # assert
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        result = content["data"]["pizza"]

        self.assertEqual(result["name"], pizza_name)
        self.assertEqual(result["user"]["firstName"], pizza_user.first_name)
        self.assertEqual(
            result["ingredients"]["edges"][0]["node"]["name"], "Magic cheese"
        )
        self.assertEqual(
            result["ingredients"]["edges"][1]["node"]["name"], "Magic mushrooms"
        )
        self.assertEqual(result["ingredients"]["edges"][2]["node"]["name"], "Magic ham")
        self.assertEqual(result["usersWithSamePizza"][0]["user"]["firstName"], "test_user_1")
        self.assertEqual(result["usersWithSamePizza"][0]["pizza"], "Capriciosa")
        self.assertEqual(result["usersWithSamePizza"][1]["user"]["firstName"], "test_user_2")
        self.assertEqual(result["usersWithSamePizza"][1]["pizza"], "Ham and mushrooms")
