name = input()
closet = int(input())

ord_n = closet % 10
bed_n = closet // 10 % 10
gr_n = closet // 100

print(f"Группа №{gr_n}.",
      f"{ord_n}. {name}.",
      f"Шкафчик: {closet}.",
      f"Кроватка: {bed_n}.",
      sep='\n')
