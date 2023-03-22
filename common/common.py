import os
from typing import Any

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_auto_update import check_driver
from selenium.webdriver.chrome.options import Options

import time

from behave import *

def create_driver(context):
    options = Options()
    # options.add_argument('--headless') <== commenting out for test creation purpose, might remove later
    chromedriver_autoinstaller.install()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.root_path = "D:\Repozytoria\Vehicle Insurance" # do zmiany na dynamiczny folder
    # context.root_path = os.path.abspath(os.getcwd())
    # check_driver()
    return webdriver.Chrome(options=options)

