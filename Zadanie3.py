def set_operations():
	print('''Napisz "exit", by zamknąć program.''')
	while True:
		first_set = set()
		second_set = set()
		print("Pierwszy zbiór.")
		while True:
			received_line = input("Wprowadź string. By przejść do drugiego zbioru, wprowadź pusty string.\n")
			if received_line.lower() == "exit":
				return
			if received_line == "":
				break
			first_set.add(received_line)
		print("Drugi zbiór")
		while True:
			received_line = input("Wprowadź string. By otrzymać wynik, wprowadź pusty string.\n")
			if received_line.lower() == "exit":
				return
			if received_line == "":
				break
			second_set.add(received_line)
		sum_of_sets = set.union(first_set, second_set)
		diffence_of_sets = set.difference(first_set, second_set)
		intersection_of_sets = set.intersection(first_set, second_set)
		symmetric_diffence_of_sets = set.symmetric_difference(first_set, second_set)
		print("Suma: " + str(sum_of_sets))
		print("Różnica: " + str(diffence_of_sets))
		print("Część wspólna: " + str(intersection_of_sets))
		print("Różnica symetryczna: " + str(symmetric_diffence_of_sets))
set_operations()
