user_monthly_savings = input("How much do you save monthly?")
user_years = input("For how many years?")
total_savings = int(user_monthly_savings * 12) * int(user_years)
print(f"In {user_years} years, you will have saved {total_savings} dollars.")