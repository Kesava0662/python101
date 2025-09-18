# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=broad-exception-raised
# pylint: disable=broad-exception-caught
# pylint: disable=line-too-long
# pylint: disable=unused-import
import os
import re
import subprocess
import time
import glob
import json
import random
from datetime import datetime, timedelta
from collections.abc import Mapping
import pandas as pd
import pyperclip
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from openpyxl.reader.excel import load_workbook
from percy.snapshot import percy_snapshot
from PyPDF2 import PdfReader
import common
import request_util
import image_compare_util
import logger


def attach_page(context,page_name):
    all_window_handles = context.driver.window_handles
    page_name = int(re.search(r'\d+', page_name).group())
    if 0 <= (page_name - 1) < len(all_window_handles):
        context.driver.switch_to_window(all_window_handles[int(page_name) - 1])
        return
    for handle in all_window_handles:
        context.driver.switch_to_window(handle)
        page_title = context.driver.title
        if page_name in page_title:
            break
  
        
def link_form_auth_link_scroll_and_click(context):
    try:
        attach_page(context,'New Feature')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"New Feature","FormAuthlinkLinkXPATH",context))
    common.scroll_and_click(context,"XPATH",xpath)
    
def textbox_username_tb_entered(context,var_username_tb1):
    try:
        attach_page(context,'New Feature')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"New Feature","Username_TBTextBoxXPATH",context))
    common.entered_text(context,var_username_tb1,"XPATH",xpath)
    
def textbox_username_tb_clear_text(context):
    try:
        attach_page(context,'New Feature')
    except:
        pass  
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"New Feature","Username_TBTextBoxXPATH",context))
    xpath = common.get_frames(context,xpath)
    i = 0
    while i < int(context.max_seconds_to_wait_for_control):
        try:
            element = common.web_element(context,"XPATH",xpath)
            context.element_html = common.get_attribute(element,"outerHTML")
            common.store_element_in_json(xpath, context.element_html)
            common.send_keys_to_element(element,Keys.CONTROL + 'a')
            logger.info(context, f"Selected all text in Username_TB")
            common.send_keys_to_element(element,Keys.DELETE)
            logger.info(context, f"Cleared text in Username_TB")
            break
        except Exception as e:
            time.sleep(int(context.time_interval_in_ms))
            logger.error(context, f"Retry {i+1}/{context.max_seconds_to_wait_for_control}, Error: {str(e)}")
        i += 1
        if i >= int(context.max_seconds_to_wait_for_control):
            raise Exception("Unable to clear Text Box , XPath is ",xpath)
    
def textbox_username_tb_enter_copied_text(context):
    try:
        attach_page(context,'New Feature')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"New Feature","Username_TBTextBoxXPATH",context))
    xpath = common.get_frames(context,xpath)
    i = 0
    while i < int(context.max_seconds_to_wait_for_control):
        try:
            element = common.web_element(context,"XPATH",xpath) 
            context.element_html = common.get_attribute(element, "outerHTML")
            common.store_element_in_json(xpath, context.element_html)
            common.send_keys_to_element(element,context.label_text)
            logger.info(context,"Enter Copied Text :" + str(context.label_text))
            break
        except Exception as e:
            time.sleep(int(context.time_interval_in_ms))
            logger.error(context, f"Retry {i+1}/{context.max_seconds_to_wait_for_control}, Error: {str(e)}")
        i += 1
        if i >= int(context.max_seconds_to_wait_for_control):
            raise Exception("Unable to perform enter copied text, XPath is :",xpath)
    
def textbox_username_tb_clear_and_enter_text(context,var_username_tb2):
    try:
        attach_page(context,'New Feature')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"New Feature","Username_TBTextBoxXPATH",context))
    common.clear_and_enter_text(context,var_username_tb2,"XPATH",xpath)
    