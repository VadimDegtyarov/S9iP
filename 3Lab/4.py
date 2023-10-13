import json


with open("Companies.txt", 'r',encoding='utf-8') as file:
    lines = file.readlines()


profits = []
total_profit = 0
count_profitable = 0


for line in lines:
    data = line.strip().split()
    name, ownership, revenue, expenses = data

    revenue, expenses = int(revenue), int(expenses)
    profit = revenue - expenses

    if profit >= 0:
        total_profit += profit
        count_profitable += 1

    profits.append({name: profit})


average_profit = total_profit / count_profitable if count_profitable > 0 else 0


company_list = [profit_dict for profit_dict in profits]


company_list.append({"average_profit": average_profit})


with open('companies.json', 'w') as json_file:
    json.dump(company_list, json_file)
