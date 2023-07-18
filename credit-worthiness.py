def calculate_creditworthiness():
    points = 0
    
    # Metric 1: Income Point ratio
    weekly_income = float(input("Weekly after-tax income amount: "))
    if weekly_income > 1187:
        points += 40
    elif weekly_income > 996:
        points += 30
    elif weekly_income > 650:
        points += 20
    elif weekly_income > 399:
        points += 10
    else:
        points += 5
    
    employment_years = int(input("Years of employment: "))
    # Metric 2: Length of Employment
    if employment_years >= 4:
        points += 20
    elif employment_years >= 1:
        points += 10
    else:
        points += 5
    
    # Metric 3: Home Ownership
    homeownership = input("Home Ownership (yes/no): ").lower()
    if homeownership == "yes":
        cep = float(input("Current equity in the property (CEP): "))
        if cep > 50000:
            points += 10
        elif cep > 25000:
            points += 5
        else:
            points += 1
    
    # Metric 4: Other Personal Income
    cmbab = float(input("Combined monthly bank account balances (CMBAB): "))
    loan_amount = float(input("Loan amount: "))
    if cmbab > 0.5 * loan_amount:
        points += 10
    elif cmbab > 0.25 * loan_amount:
        points += 5
    else:
        points += 1
    
    retirement_income = input("Do you receive retirement income? (yes/no): ").lower()
    if retirement_income == "yes":
        wri = float(input("Weekly retirement income (WRI): "))
        if wri > 0.5 * loan_amount:
            points += 10
        elif wri > 0.25 * loan_amount:
            points += 5
        else:
            points += 1
    
    investment_income = input("Do you receive investment income? (yes/no): ").lower()
    if investment_income == "yes":
        wii = float(input("Weekly investment income (WII): "))
        if wii > 0.5 * loan_amount:
            points += 10
        elif wii > 0.25 * loan_amount:
            points += 5
        else:
            points += 1
    
    age = int(input("Age of Applicant: "))
    # Metric 5: Age of Applicant
    if age >= 65:
        points += 4
    elif age >= 26:
        points += 10
    else:
        points += 5
    
    return points

credit_points = calculate_creditworthiness()
print("Credit-worthiness points:", credit_points)

# still working on the set of calcs for liabilities
# calculate_creditworthiness - calculate_liabilites
# So far I feel like I still have to do a big piece of the code for the full idea to come to fruition. Up to this point what I have been able to complete is what I would consider to be 60% of the code because the biggest portion of it was to calculate the actual credit worthiness based on the income information provided.
#Now all I have to do is to create a negative calculator to come up with a final score system and relate that result to a range of credit amount approval
