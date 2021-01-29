loop = 0
print("==== Leap Year Calculator ====")
while loop == 0:
	print("==============================")
	error = 0
	year = input("Enter a year: ")
	try:
		year = int(year)
	except ValueError:
		print("That is not a integer please input a number!\n")
		error = 1
	if error == 0:
		year = int(year)
		if year >= 0:
			if year % 4 != 0:
				print("That year is not a leap year")
			elif year % 100 != 0:
				print("That year is a leap year")
			elif year % 400 != 0:
				print("That year is not a leap year")
			else:
				print("That year is a leap year")
			loop = int(input("\nWould you like to continue?\n0-> Yes 1-> No: "))
		else:
			print("Please input a year that is greater than 0!\n")