set_of_values = set()
print('''Napisz "exit", by zamknąć program.''')
while True:
	print("Aktualna ilość wprowadzonych różnych liczb: " + str(len(set_of_values)))
	received_line = input("Wprowadź liczbę całkowitą.\n")
	if received_line.lower() == "exit":
		break
	try:
		whole_number = int(received_line)
		set_of_values.add(whole_number)
	except:
		print("To nie jest liczba całkowita.")
