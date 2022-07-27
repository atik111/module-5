from calc import monthly_compounding

def app():
    initial_investment = float(input("Please input initial value: "))
    monthly_deposit = float(input("Please input the value of consistent monthly contributions: "))
    years = int(input("Please input how many years you will be invested for: "))
    interest_rate = float(input("Please input the annual percent floaterest rate, as a decimal between 0 and 1: "))
    final_sum = monthly_compounding(initial_investment, monthly_deposit, years, interest_rate)
    print(f"Your final value is {final_sum}")


if __name__ == "__main__":
    app()

