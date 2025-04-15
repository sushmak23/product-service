Feature: Product Management

  Scenario: Reading a product by ID
    Given we have the following products in the database
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |
      | Product 2 | Category B | 20.0  | false     |
    When I request the product with ID 1
    Then the response status should be 200
    And the product name should be "Product 1"
    And the product category should be "Category A"
    And the product price should be 10.0
    And the product availability should be true
