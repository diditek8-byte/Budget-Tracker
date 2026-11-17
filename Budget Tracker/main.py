import json
import os

def calculate_budget(budget_dict):
    total_budget = budget_dict["rent"] + budget_dict["electricity"] + budget_dict["gas"] + budget_dict["water"] + budget_dict["internet"] + budget_dict["grocery"]+ budget_dict["commuting"] + budget_dict["credit"]
    minus = budget_dict["income"] - total_budget
    print("You earn", budget_dict["income"])
    print("This is how much you have to pay", total_budget)
    print("You have left", minus)


if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
     income = float(input("How much do you earn? "))
     rent = float(input("How much is rent/mortgage? "))
     electricity = float(input("How much is your electricity? "))
     gas = float(input("How much do you pay for gas? "))
     water = float(input("How much do you pay for water? "))
     internet = float(input("How much do you pay for wifi/mobile data? "))
     grocery = float(input("How much do you pay for groceries? "))
     commuting = float(input("How much do you pay for public transit? "))
     credit = float(input("How much is your credit card? "))

     budget_dict = {
       "income": income,
       "rent": rent,
       "credit": credit,
       "electricity": electricity,
       "gas": gas,
       "water": water,
       "internet": internet,
       "grocery": grocery,
       "commuting": commuting,
    }
     
     with open('data.json', 'w') as data:
      json.dump(budget_dict, data, indent=4)      
else:
    with open("data.json", "r") as data:
        budget_dict = json.load(data)
    calculate_budget(budget_dict)

def update_budget(budget_dict):
    for expense in budget_dict.items():
       expense = input("Which expense would you like to change? ")
       amount = input("change expense ")
       if not expense:
            break
       budget_dict[expense] = float(amount)
       with open("data.json", "w") as data:
            json.dump(budget_dict, data, indent=4)


def add_expense(budget_dict):
    for expense, value in list(budget_dict.items()):
        expense = input("Add expense! ")
        value = input("How much does it cost? ")
        if not expense:
            break
        budget_dict[expense] = float(value)
        with open("data.json", "w") as data:
            json.dump(budget_dict, data, indent=4)

def delete_expense(budget_dict):
    for expense in list(budget_dict.items()):
        expense = input("Delete expense! ")
        if not expense:
            break
        del budget_dict[expense]
        with open("data.json", "w") as data:
            json.dump(budget_dict, data, indent=4)

answer = input("Anything else? ")
if answer == "change expense":
  update_budget(budget_dict)
elif answer == "add expense":
    add_expense(budget_dict)
elif answer == "delete expense":
    delete_expense(budget_dict)
elif answer == "no":
  print("Have a good day!")
   
