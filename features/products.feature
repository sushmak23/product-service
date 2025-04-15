Feature: Product Management

  Scenario: Searching a product by category
    Given we have the following products in the database
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |
      | Product 2 | Category B | 20.0  | false     |
    When I search for products in the category "Category A"
    Then the response status should be 200
    And the response should contain the following products:
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |

