#User Inputs
principal=float(input("Please enter the loan principal: "))
interest_rate=float(input("Please enter the interest rate as a percentage: "))
term=float(input("Please enter the term for your loan in years: "))
#Calculations for Equation
decimal_rate=interest_rate/100
month_rate=decimal_rate/12
term_month=term*12
#Calculations for fixed pay
fixed_pay_eq1=month_rate*((1+month_rate)**term_month)
fixed_pay_eq2=((1+month_rate)**term_month)-1
fixed_pay=principal*(fixed_pay_eq1/fixed_pay_eq2)
#Calculations for equal principal
equal_pay_month_principal= (principal/term_month)
intial_balance=equal_pay_month_principal + (principal*month_rate)
balance=intial_balance
total_paid=principal
i=1
#This is supposed to determine the total balance
while i<=term_month:
    monthly_interest=balance*month_rate
    monthly_payment=equal_pay_month_principal+monthly_interest
    total_paid += monthly_payment
    balance -= equal_pay_month_principal
    i += 1
#Calculations for total payments
total_fixed_pay=fixed_pay*term_month
total_equal_pay=total_paid
#Results are displayed here
print(f"Your monthly payment for a fixed payment plan is: {fixed_pay:.2f}")
print(f"Your total amount payed for a fixed payment plan at the end of your term would be: {total_fixed_pay:.2f}")
print(f"Your total amount payed for an equal principal payment plan at the end of your term would be: {total_equal_pay:.2f}")
#This section preforms comparisons and displays the results
if (total_fixed_pay<total_equal_pay):{
    print(f"It would be cheaper to get a fixed payment plan by: {total_equal_pay-total_fixed_pay:.2f}")
}
if (total_equal_pay<total_fixed_pay):{
    print(f"It would be cheaper to get a equal principal payment plan by: {total_fixed_pay-total_equal_pay:.2f}")
}