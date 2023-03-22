# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:45:04 2023

@author: Sixsentix
"""

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_auto_update import check_driver
from selenium.webdriver.chrome.options import Options
from common.common import *
from common.selectors import *
#from common.utilities import *
import time
from datetime import date

from common.common import create_driver
from common.selectors import *
from behave import *


@given('I go to "{url}" page')
def open_page(context, url):
    context.driver = create_driver(context)
    VehicleDataSelectors.driver = context.driver
    NavigationBarSelectors.driver = context.driver
    PathProducer.driver = context.driver
    GetElement.driver = context.driver
    context.driver.maximize_window()
    context.driver.get(url)
    time.sleep(2)
