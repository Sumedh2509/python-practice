# To practice all previous days on sunday!!

# The username must start with a letter, be under 10 chars, and contain no digits.

# username = input("Enter your username: ")


# while True:
#     username = input("Enter your username: ")
#     if username[0].isalpha():
#         if username.isalpha()== False:
#             print("Username must not contain any digits")
#         elif len(username)>= 10:
#             print("Username must be less than 10 characters")
#         else:
#             print(f"Your username is {username}")
#             break
#     else:
#         # print("Your username must start with a letter")

# for i in range(3):
#     for j in range(2):
#         print(f"({i},{j})", end=" ")
# # output - first row -(1,1) (1,2)
# #         second row - (2,1) (2,2)
# #         thir row  - (3,1) (3,2)

balance = 100
print(f"Welcome to the python slot your initial balance is {balance}")
while balance > 0:
    print(f"Your current balance is {balance}")
    bet = input("Enter the amount you want to bet: ")
    
    print(f"DEBUG: You entered: '{bet}'")  # See exactly what was entered
    print(f"DEBUG: bet.isdigit() = {bet.isdigit()}")  # Check if isdigit works
    print(f"DEBUG: repr of bet: {repr(bet)}")  # See any hidden characters
    
    if not bet.isdigit():
        print("Thats an Invalid amount")
        continue
    # ... rest of your code