from pip._internal.vcs import git

# import datetime
# def dep_factor(year_construction):
#     age_house = datetime.datetime.now().year - year_construction
#     if (age_house < 10):
#         depreciation = 0.0
#     elif (age_house >= 10 and age_house < 15):
#         depreciation = 0.05
#     elif (age_house >= 15 and age_house < 25):
#         depreciation = 0.1
#     else:
#         depreciation = 0.15
    
#     return depreciation

# while True:
#     value_of_house = float(input("Enter the value of your house without a comma to separate the thousands: "))
#     year_built =  float(input("Enter the year your house was built: "))
#     tax_rate = 0.025
#     depreciation_factor = dep_factor(year_built)
#     total_property_tax = tax_rate * (value_of_house * (1 - dep_factor(year_built)))
#     print("Property tax amount you owe is: ", total_property_tax)
#     continuation_answer = input("Would you like to continue yes or no? ").lower()
#     if (continuation_answer == "no"):
#         break

# def is_binary(binary_string):
#     decimal, i = 0, 0
#     while(binary_string != 0): 
#         dec = binary_string % 10
#         decimal = decimal + dec * pow(2, i) 
#         binary_string = binary_string//10
#         i += 1
#     print(decimal)

# while True:
#     binary_string = int(input("Please enter a binary string: "))
#     is_binary(binary_string)
#     continuation_answer =  input("Would you like to continue yes or no? ").lower()
#     if (continuation_answer == "no"):
#          break

# def isPalindrome(S):
#     if S[0] == S[-1]:
#         return print("True")
#     elif S[0] == S[-1] and S[1] == S[-2] :
#         return print("True")
#     else:
#         return print("False")
# while True:
#     your_string = str(input("Please enter a string: "))
#     isPalindrome(your_string)
#     continuation_answer =  input("Would you like to continue yes or no? ").lower()
#     if (continuation_answer == "no"):
#          break

# value = input("enter number: ")
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = float(value)))