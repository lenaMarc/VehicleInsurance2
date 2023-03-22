# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:59:17 2023

@author: Sixsentix
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_auto_update import check_driver
from selenium.webdriver.chrome.options import Options
import \Repozytoria\Vehicle Insurance\common
from selectors import *
import time
from behave import *

@given('I click on Automobile tab')
def go_to_automobile_card(context):
    NavigationBarSelectors.get_automobile_button().click()
    
@when('I enter "{mark}" in "Make" field')
def complete_make_field(context, mark):
    VehicleDataSelectors.get_select_field("Make").send_keys(mark)

@when('I enter "{engine_performance}" in "Engine Performance" field')
def complete_engine_field(context, engine_performance):
    VehicleDataSelectors.get_input_field("Engine Performance").send_keys(engine_performance)
    
#@then('A number next to Enter Vehicle Data tab is equal 5')
#def check_counter(context):
   #current_counter = VehicleDataSelectors.get_active_counter().int
  # assert current_counter == 5
   #, str(current_counter) + " is not equal to " + 5