Feature: Product Management

  Scenario: Updating a product by ID
    Given we have the following products in the database
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |
      | Product 2 | Category B | 20.0  | false     |
    When I update the product with ID 1 to have the following details
      | name      | category   | price | available |
      | Updated Product | Category A | 12.0  | true  |
    Then the response status should be 200
    And the product name should be "Updated Product"
    And the product category should be "Category A"
    And the product price should be 12.0
    And the product availability should be true

