__author__ = 'biswajit'

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time


@given(u'I launch tutorialspoint.com')
def step_impl(context):
    time.sleep(5)
    context.driver.get(context.launch_url)


@when(u'I view all courses')
def step_impl(context):
    action_chain = ActionChains(context.driver)
    elm_tutpoint = context.driver.find_element_by_css_selector("span.tut-lib")
    action_chain.move_to_element(elm_tutpoint).click(elm_tutpoint).perform()
    elm_viewall = context.driver.find_element_by_link_text("View All")
    elm_viewall.click()
    #time.sleep(5)


@when(u'I select "{content}" under "{parent_course}"')
def step_impl(context, content, parent_course):
    parent_course = parent_course.lower().replace(' ', '_')
    attempts = 0
    while attempts < 2:
        try:
            elm_parent_course = context.driver.find_element_by_css_selector('ul#' + parent_course)
            elm_content = elm_parent_course.find_element_by_xpath("li/a[@title='" + content + "']")
            # context.driver.execute_script('arguments[0].scrollIntoView();', elm_content)
            elm_content.click()
            break
        except StaleElementReferenceException:
            pass
        attempts += 1

    '''
    is_visible = WebDriverWait(context.driver,10).until(lambda elm_parent_course : elm_parent_course.find_element_by_xpath("li/a[@title='" + content + "']").is_displayed())
    if is_visible == True:
    else:
        raise "content is not available"
    '''


@then(u'it shows "{course_header}" page')
def step_impl(context, course_header):
    header_found = False
    elm_headers = context.driver.find_elements_by_tag_name('h1')
    for header in elm_headers:
        if header.text == course_header:
            header_found = True
            break

    assert header_found == True