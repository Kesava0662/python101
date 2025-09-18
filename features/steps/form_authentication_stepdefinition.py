# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=unused-import

import os
import sys
from behave import *
import assertion
import form_authentication_workflow

current_dir = os.getcwd()
previous_dir = os.path.join(os.path.dirname(current_dir), 'shared', 'steps')
sys.path.append(previous_dir)


def parse_string(text):
    return text.strip()


register_type(Name=parse_string)
use_step_matcher("cfparse")


        

@when("I copied text Login page_TB in form authentication")
def step(context):
     form_authentication_workflow.textbox_login_page_tb_copied_text(context)
    

@when("I selected Login_button in form authentication")
def step(context):
     form_authentication_workflow.button_login_button_selected(context)
    

@when("I copied text password head_label in form authentication")
def step(context):
     form_authentication_workflow.label_password_head_label_copied_text(context)
    

@when("I entered Password_TA in form authentication as '{var_password_ta:Name?}'")
def step(context,var_password_ta):
     form_authentication_workflow.textarea_password_ta_entered(context,var_password_ta)
    

@when("I clear text Password_TA in form authentication")
def step(context):
     form_authentication_workflow.textarea_password_ta_clear_text(context)
    

@when("I clear and enter text Password_TA in form authentication as '{var_password_ta4:Name?}'")
def step(context,var_password_ta4):
     form_authentication_workflow.textarea_password_ta_clear_and_enter_text(context,var_password_ta4)
    

@when("I copied text usename head_link in form authentication")
def step(context):
     form_authentication_workflow.link_usename_head_link_copied_text(context)
    

@then("'{var_page:Name?}' is displayed with '{var_content:Name?}'")
def step(context,var_page,var_content):
    assertion.assert_true(context,form_authentication_workflow.page_default_page_displayed(context,var_page))
    assertion.assert_true(context, form_authentication_workflow.label_message_displayed(context,var_content))
    if str(context.soft_assertion).lower() == 'true':
        assertion.assert_all(context)