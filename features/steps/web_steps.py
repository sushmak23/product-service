from selenium import webdriver
from behave import given, when, then

@given('I have opened the product page')
def step_given_opened_product_page(context):
    context.driver = webdriver.Chrome()  # or your preferred browser driver
    context.driver.get("http://localhost:5000/products")  # URL to the page

@when('I click on the "{button_name}" button')
def step_when_click_button(context, button_name):
    button = context.driver.find_element_by_name(button_name)  # Locate the button by its name
    button.click()  # Simulate a button click

@then('I should see "{text}" on the page')
def step_then_check_text(context, text):
    # Verify that the expected text is present on the page
    assert text in context.driver.page_source  # Check if the specific text is present in the page source
    context.driver.quit()  # Close the browser after test

