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

p = float(input("Initial Investment: \n"))
r = int(input("Interest rate (as a pecentage): \n"))
r = r/100
ask = input("Would you like to enter the length of time as years, months or days?\n")

if ask == "years":
  t = float(input("Length of Time (in years): \n"))

elif ask == "months":
  t = float(input("Length of Time (in months): \n"))
  t = t/12

elif ask == "days":
  t = float(input("Length of Time (in days): \n"))
  t = t/365
  
i = p*r*t
print("The amount of interest is", i)