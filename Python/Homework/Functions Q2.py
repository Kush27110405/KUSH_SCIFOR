# Question 2 :- function to determine whether loan should be approved based on income, credit score and loan amount :

def loan_approval(income,credit_score,loan_amount):
  if income < 30000:
    return "Loan Denied"
  else:
    if income > 60000 or credit_score >= 600 :
      if loan_amount < (income/2):
        return "Loan approved"
      else:
        return "Loan Denied"
    else:
      return "Loan Denied"

income = float(input("Enter your income :"))
credit_score = int(input("Enter your credit score :"))
loan_amount = float(input("Enter the loan amount :"))

message = loan_approval(income,credit_score,loan_amount)
print(message)
