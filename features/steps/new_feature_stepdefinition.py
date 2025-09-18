# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=undefined-variable
# pylint: disable=wildcard-import
# pylint: disable=unused-import

import os
import sys
from behave import *
import assertion
import new_feature_workflow

current_dir = os.getcwd()
previous_dir = os.path.join(os.path.dirname(current_dir), 'shared', 'steps')
sys.path.append(previous_dir)


def parse_string(text):
    return text.strip()


register_type(Name=parse_string)
use_step_matcher("cfparse")


        

@when("I scroll and click Form Auth link in the internet")
def step(context):
     new_feature_workflow.link_form_auth_link_scroll_and_click(context)
    

@when("I entered Username_TB in form authentication as '{var_username_tb1:Name?}'")
def step(context,var_username_tb1):
     new_feature_workflow.textbox_username_tb_entered(context,var_username_tb1)
    

@when("I clear text Username_TB in form authentication")
def step(context):
     new_feature_workflow.textbox_username_tb_clear_text(context)
    

@when("I enter copied text Username_TB in form authentication")
def step(context):
     new_feature_workflow.textbox_username_tb_enter_copied_text(context)
    

@when("I clear and enter text Username_TB in form authentication as '{var_username_tb2:Name?}'")
def step(context,var_username_tb2):
     new_feature_workflow.textbox_username_tb_clear_and_enter_text(context,var_username_tb2)
    