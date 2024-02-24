pos_name = input()
price = int(input())
mass = int(input())
cust_money = int(input())

cost = price * mass
exch = cust_money - cost
print("Чек", 
      f"{pos_name} - {mass}кг - {price}руб/кг", 
      f"Итого: {cost}руб", 
      f"Внесено: {cust_money}руб", 
      f"Сдача: {exch}руб", 
      sep='\n')