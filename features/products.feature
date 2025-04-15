Feature: Product Management

  Scenario: Searching a product by name
    Given we have the following products in the database
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |
      | Product 2 | Category B | 20.0  | false     |
    When I search for a product with the name "Product 1"
    Then the response status should be 200
    And the response should contain the following product:
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |

