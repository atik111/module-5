# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:55:38 2022

@author: Atik
"""


from calc import monthly_compounding

def test_zeros():
    # Arrange
    initial_investment = 0
    interest_rate = 0
    monthly_deposit = 0
    years = 0
    expected_output = 0

    # Act
    actual_output = monthly_compounding(initial_investment, interest_rate, monthly_deposit, years)

    # Asset
    assert actual_output == expected_output


def test_one_year_zero_interest():
     # Arrange
    initial_investment = 100
    interest_rate = 0
    monthly_deposit = 0
    years = 1
    expected_output = 100

    # Act
    actual_output = monthly_compounding(initial_investment, interest_rate, monthly_deposit, years)

    # Asset
    assert actual_output == expected_output


def test_one_year_5percent_interest():
     # Arrange
    initial_investment = 100
    interest_rate = 5
    monthly_deposit = 0
    years = 1
    expected_output = 105

    # Act
    actual_output = monthly_compounding(initial_investment, interest_rate, monthly_deposit, years)

    # Asset
    assert actual_output == expected_output

def test_2_year_5percent_interest_200monthly():
     # Arrange
    initial_investment = 100
    interest_rate = 5
    monthly_deposit = 200
    years = 2
    expected_output = 5142.01

    # Act
    actual_output = monthly_compounding(initial_investment, interest_rate, monthly_deposit, years)

    # Asset
    assert actual_output == expected_output