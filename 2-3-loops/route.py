position = [0, 0]
while (command := input()) != 'СТОП':
	dist = int(input())
	match command:
		case "СЕВЕР":
			position[1] += dist
		case "ЮГ":
			position[1] -= dist
		case "ВОСТОК":
			position[0] += dist
		case "ЗАПАД":
			position[0] -= dist
print(position[1])
print(position[0])
