dist = 43872
pedestal_width = 8

cyclists = dict()

cyclists['Петя'] = float(input())
cyclists['Вася'] = float(input())
cyclists['Толя'] = float(input())

rating_asc = [name for name, speed in sorted(cyclists.items(), key=lambda item: item[1])]

print(f"{' ' * pedestal_width}{rating_asc[2]: ^{pedestal_width}}{' ' * pedestal_width}",
      f"{rating_asc[1]: ^{pedestal_width}}{' ' * pedestal_width}{' ' * pedestal_width}",
      f"{' ' * pedestal_width}{' ' * pedestal_width}{rating_asc[0]: ^{pedestal_width}}",
      f"{'II': ^{pedestal_width}}{'I': ^{pedestal_width}}{'III': ^{pedestal_width}}",
      sep='\n')