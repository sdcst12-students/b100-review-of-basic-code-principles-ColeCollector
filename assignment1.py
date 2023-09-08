"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

principal = float(input("Initial Investment: \n"))
rate = int(input("Interest rate (as a pecentage): \n"))
rate = rate/100
ask = input("Would you like to enter the length of time as years, months or days?\n")

if ask == "years":
  time = float(input("Length of Time (in years): \n"))

elif ask == "months":
  time = float(input("Length of Time (in months): \n"))
  time = time/12

elif ask == "days":
  time = float(input("Length of Time (in days): \n"))
  time = time/365
  
interest = principal*rate*time
print("The amount of interest is", interest)