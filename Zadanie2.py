def check_if_binary(string):
	for element in string:
		if element != "0" and element != "1":
			return False
	return True

def count_binary_holes(binary_string):
	number_of_holes = 0
	state = 0
	for bit in binary_string:
		if state == 0 and bit == "1":
			state = 1
		elif state == 1 and bit == "0":
			state = 2
		elif state == 2 and bit == "1":
			state = 1
			number_of_holes += 1
	return number_of_holes
			
print('''Napisz "exit", by zamknąć program.''')
while True:
	received_line = input("Podaj ciąg binarny.\n")
	if received_line.lower() == "exit":
		break
	if check_if_binary(received_line):
		number_of_holes = count_binary_holes(received_line)
		print("Ilość dziur: " + str(number_of_holes))
	else:
		print("To nie jest ciąg binarny.")
