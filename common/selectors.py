# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:08:25 2023

@author: Sixsentix
"""

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class VehicleDataSelectors:
    
    @staticmethod
    def get_input_field(parametr_name):
        return GetElement(PathProducer.div()
                   .suffix(f"[contains(@class='field idealforms-field idealforms-field-text')]/label[@class='main''>{parametr_name}<']/input")
                   .get_path()).get_element()
    
    @staticmethod
    def get_select_field(parametr_name):
        return GetElement(PathProducer.div()
                   .suffix(f"[contains(@class='field idealforms-field idealforms-field-select-one valid')]/label[@class='main''>{parametr_name}<']/select")
                   .get_path()).get_element()
    
    @staticmethod
    def get_active_counter():
        return GetElement(PathProducer.div()
                   .suffix(f"[contains(@class='idealsteps-step-active')]/a/span")
                   .get_path()).get_element()
    
class NavigationBarSelectors:
    
    def get_automobile_button(self):
        return self.driver.find_element(By.ID, 'nav_automobile')
    
class PathProducer:
    driver = ""
    temp_path = ""

    @staticmethod
    def element_type(element_type):
        PathProducer.temp_path = f"//{element_type}"
        return PathProducer

    @staticmethod
    def button():
        PathProducer.temp_path = f"//button"
        return PathProducer

    @staticmethod
    def input():
        PathProducer.temp_path = f"//input"
        return PathProducer

    @staticmethod
    def div():
        PathProducer.temp_path = f"//div"
        return PathProducer

   # @staticmethod
   # def data_name(data_name):
        #data_name = check_dictionary(data_name, name_to_dataname)
        #PathProducer.temp_path += f"[@data-name='{data_name}']"
        #return PathProducer

    @staticmethod
    def custom_kwargs(**kwargs):
        for key, value in kwargs.items():
            key = key.replace("___", "-")  # w key nie da się korzystać z "-" a niektóre atrybuty mają "-"
            key = key.replace("class_",
                              "class")  # nie można użyć "class" gdyż takie słowo kluczowe istnieje już w Pythonie
            if key == "class":
                PathProducer.temp_path += f".{value}"
            elif key == "innerText":
                PathProducer.temp_path += f":contains('{value}')"
            else:
                PathProducer.temp_path += f"[{key}='{value}']"
        return PathProducer

    @staticmethod
    def suffix(suffix):
        PathProducer.temp_path += f"{suffix}"
        return PathProducer

    @staticmethod
    def get_path():
        return PathProducer.temp_path


class GetElement:
    produced_path=""
    def __init__(self, produced_path):
        self.produced_path = produced_path
    def wait_for_element_to_be_visible(self, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, self.produced_path)),
                                                      f"{self.produced_path} does not exists.")

    def wait_for_element_to_be_hidden(self, wait_time=5):
        return WebDriverWait(self.driver, wait_time).until_not(EC.presence_of_element_located((By.XPATH, self.produced_path)),
                                                          f"{self.produced_path} still exists.")

    def get_element(self):
        return self.wait_for_element_to_be_visible()

    def get_element_without_wait(self):
        print("print new")
        print(self.produced_path)
        return self.driver.find_element(self.produced_path)

    def get_element_or_empty(self):
        try:
            element_or_empty = self.driver.find_element(By.XPATH, self.produced_path)
        except NoSuchElementException:
            return ""
        return element_or_empty