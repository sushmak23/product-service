from selenium import webdriver
from behave import given, when, then

@given('I have opened the product page')
def step_given_opened_product_page(context):
    context.driver = webdriver.Chrome()  # or your preferred browser driver
    context.driver.get("http://localhost:5000/products")  # URL to your product page

@when('I click on the "{button_name}" button')
def step_when_click_button(context, button_name):
    button = context.driver.find_element_by_name(button_name)
    button.click()

@then('I should see "{text}" on the page')
def step_then_should_see_text(context, text):
    assert text in context.driver.page_source
    context.driver.quit()

@then('I should not see "{text}" on the page')
def step_then_should_not_see_text(context, text):
    assert text not in context.driver.page_source
    context.driver.quit()
