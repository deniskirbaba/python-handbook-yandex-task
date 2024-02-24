pos_name = input()
price = int(input())
mass = int(input())
cust_money = int(input())

cost = price * mass
exch = cust_money - cost
print(f"{'Чек':=^35}", 
      f"Товар:{pos_name: >29}",
      f"Цена:{str(mass)+'кг * '+str(price)+'руб/кг': >30}",
      f"Итого:{str(cost)+'руб': >29}", 
      f"Внесено:{str(cust_money)+'руб': >27}", 
      f"Сдача:{str(exch)+'руб': >29}", 
      35 * '=',
      sep='\n')