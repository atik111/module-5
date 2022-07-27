def monthly_compounding(initial_investment, monthly_deposit, years, interest_rate):
    
    final_sum = initial_investment
    interest_rate = interest_rate/100
    monthly_rate = pow(1 + interest_rate, 1/12) - 1
    for _ in range(0, years*12):
        final_sum = final_sum*(1 + monthly_rate) + monthly_deposit

    return round(final_sum, 2)
