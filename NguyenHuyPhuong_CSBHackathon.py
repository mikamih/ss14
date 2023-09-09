# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
# total = num1 + num2
# print (total)

# import math
# def solve_quadratic_equation(a, b, c):
#     delta = b**2 - 4*a*c
#     if delta >0 :
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return x1, x2
#     elif delta == 0:
#         x = -b / (2*a)
#         return x
#     else:
#         return "no real roots"
    
# a = float(input("input a: "))
# b = float(input("input b: "))
# c = float(input("input c: "))

# result = solve_quadratic_equation(a, b, c)
# print("The equation has 2 solutions.")
# print(result)

# def is_palindrome(string):
#     reversed_string = string[::-1]
#     if string == reversed_string:
#         return True
#     else:
#         return False
# input_string = input("Input a text:")
# if is_palindrome(input_string):
#     print ("This is a palindrome.")
# else:
#     print("this is not palindrome. ")

# print ("== Welcome to MindX Restaurant ==")
# def order_taker():
#     order_items = set()
#     while True:
#         item = input("please choose a dish: ")
#         if item in order_items:
#             print("monsier this dish is  already ordered")
#         else:
#             order_items.add(item)

#         choice = input("Great choice! Anything else? (y/n): ")
#         if choice.lower() == "no":
#             break
#     print("Well done! Your order:")
#     for item in order_items:
#         print (item)
# order_taker()

# phone_prices = {
#     "Iphone12": 28000000,
#     "Samsung N10": 16000000,
#     "Oppo 93": 7500000,
#     "Vsmart": 7400000,
#     "Vivo": 4200000,
# }

# def find_phone_price():
#     phone_name = input("Input name of a phone: ")
#     if phone_name in phone_prices:
#         print(f"price of {phone_name}:{phone_prices[phone_name]}")
#     else:
#         print("phone not found :< ")

# def find_phone_withinbudget():
#     budget = int(input("Input your budget:"))
#     matching_phones = []
#     for phone, price in phone_prices.items():
#         if price <= budget:
#             matching_phones.append(phone)
#     if len(matching_phones) > 0:
#         print("Phones that fit your budget: ")
#         for phone in matching_phones:
#             print(f"- {phone}: {phone_prices[phone]}")
#     else:
#         print("no phone found within your budget")
 
# find_phone_price()
# find_phone_withinbudget()

# number = int(input("Input a number: "))
# count = 0
# while number > 0:
#     count += 1
#     number = number // 10
# print(f"This number has {count} digit (s).")

# def sorted_list(lst):
#     n = len(lst)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]

# lst = [5, 1, 8, 92, -1, 30]
# print(f"Original list: ", lst)
# sorted_list(lst)
# print("Sorted list:", lst)

def fibonaci(n):
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list
n = int(input("Input a number: "))
result = fibonaci(n)
print(result)
