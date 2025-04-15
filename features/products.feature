Feature: Product Management

  Scenario: Deleting a product by ID
    Given we have the following products in the database
      | name      | category   | price | available |
      | Product 1 | Category A | 10.0  | true      |
      | Product 2 | Category B | 20.0  | false     |
    When I delete the product with ID 1
    Then the response status should be 200
    And the message should be "Product deleted successfully"
    And the product with ID 1 should not exist in the database

