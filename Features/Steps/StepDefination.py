from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



@given(u'User is on Registration page')
def step_impl(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.thetestingworld.com/testings/")
    context.driver.find_element(By.ID, "fld_username").send_keys("swetha")

@when(u'User enter Username')
def step_impl(context):

    raise NotImplementedError(u'STEP: When User enter Username')


@when(u'User enters email id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters email id')


@when(u'User enters Password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters Password')


@when(u'User click on signup button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User click on signup button')


@then(u'user should be registered successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should be registered successfully')
