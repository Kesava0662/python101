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
  
        
def textbox_login_page_tb_copied_text(context):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","Loginpage_TBTextBoxXPATH",context))
    common.copied_text(context,"XPATH",xpath)
    
def button_login_button_selected(context):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","Login_buttonButtonXPATH",context))
    common.click_action(context,"XPATH",xpath)
    logger.info(context,f"Login_button selected successfully")
    
def label_password_head_label_copied_text(context):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","passwordhead_labelLabelXPATH",context))
    common.copied_text(context,"XPATH",xpath)
    
def textarea_password_ta_entered(context,var_password_ta):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","Password_TATextAreaXPATH",context))
    common.entered_text(context,var_password_ta,"XPATH",xpath)
    
def textarea_password_ta_clear_text(context):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass  
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","Password_TATextAreaXPATH",context))
    xpath = common.get_frames(context,xpath)
    i = 0
    while i < int(context.max_seconds_to_wait_for_control):
        try:
            element = common.web_element(context,"XPATH",xpath)
            context.element_html = common.get_attribute(element,"outerHTML")
            common.store_element_in_json(xpath, context.element_html)
            common.send_keys_to_element(element,Keys.CONTROL + 'a')
            logger.info(context, f"Selected all text in Password_TA")
            common.send_keys_to_element(element,Keys.DELETE)
            logger.info(context, f"Cleared text in Password_TA")
            break
        except Exception as e:
            time.sleep(int(context.time_interval_in_ms))
            logger.error(context, f"Retry {i+1}/{context.max_seconds_to_wait_for_control}, Error: {str(e)}")
        i += 1
        if i >= int(context.max_seconds_to_wait_for_control):
            raise Exception("Unable to clear Text Box , XPath is ",xpath)
    
def textarea_password_ta_clear_and_enter_text(context,var_password_ta4):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","Password_TATextAreaXPATH",context))
    common.clear_and_enter_text(context,var_password_ta4,"XPATH",xpath)
    
def link_usename_head_link_copied_text(context):
    try:
        attach_page(context,'Form Authentication')
    except:
        pass
    xpath = str(common.get_yml_object_repository_value(context.yml_data_object,"Form Authentication","usenamehead_linkLinkXPATH",context))
    common.copied_text(context,"XPATH",xpath)
    
def page_default_page_displayed(context,var_page):
    i = 0
    page =  str(common.get_data(context,var_page))
    title = context.driver.title
    if "NA" in page or "Form Authentication" in page:
        return True
    else:
        all_window_handles = context.driver.window_handles
        while i < int(context.max_seconds_to_wait_for_control):
            try:
                if len(all_window_handles) > 1:
                    for handle in all_window_handles:
                        context.driver.switch_to_window(handle)
                        page_title = context.driver.title
                        if page in page_title:
                            return True
                        return False
                else:
                    if page in title:
                        return True
                    return False
            except Exception as e:
                time.sleep(int(context.time_interval_in_ms))
                logger.error(context, f"Retry {i+1}/{context.max_seconds_to_wait_for_control}, Error: {str(e)}")
            i += 1
            if i >= int(context.max_seconds_to_wait_for_control):
                raise Exception(" Unable to find the element ")
    
def label_message_displayed(context,var_message):
    i = 0   
    value_to_be_enter = str(common.get_data(context,var_message)) 
    if "NA" in value_to_be_enter:
        return True
    while i < int(int(context.max_seconds_to_wait_for_control)):
        try:
            xpath = "//*[contains(text(), '" + value_to_be_enter + "')]"
            elements = common.web_elements(context, "XPATH", xpath)
            for element in elements:
                if common.is_element_displayed(element):
                    return True
        except Exception as e:
            logger.error(context, f"Retry {i+1}/{context.max_seconds_to_wait_for_control}, Error: {str(e)}")
            time.sleep(int(context.time_interval_in_ms))
        i += 1
        if i >= int(context.max_seconds_to_wait_for_control):
            raise Exception(" Unable to find the element ")
    