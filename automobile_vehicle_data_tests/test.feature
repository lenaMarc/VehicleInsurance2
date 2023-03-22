# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:15:42 2023

@author: Sixsentix
"""

Feature: Enter Data in Automobile
    Scenario Outline: As an user I want to enter velicle data and see that they are set.
        Given I go to "http://www.sparkstone.co.nz/sampleapp/101/" page
            And I click on Automobile tab
        When I drop down list in "Make" field
            And I click on "<mark>"
            And I enter "<engine performance>" in "Engine Performance" field
            And I enter "<date>" in "Date of Manufacture" field
            And I enter "<number of seats>" in "Number of Seats" field
            And I drop down list in "Fuel Type" field
            And I click on "<fuel type>"
            And I enter "<price>" in "Price" field
            And I enter "<lpn>" in "License Plate Number" field
            And I enter "<mi>" in "Annual Mileage" field
        Then A number next to Enter Vehicle Data tab is equal 0
        Examples: Vehicle Data
        | mark    | engine performance    | date       | number of seats    | fuel type   | price    | lpn     | mi   |
        | BMW     | 2000                  | 03/17/2022 | 4                  | Petrol      | 500      | WW 2023 | 100  |
        | Audi    |     