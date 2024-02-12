def number_checker(question):
    error = '\n Sorry Please Enter A Integer'
    number = ''
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


total = 0
first_number = number_checker("Enter the first number in the range: ")
second_number = number_checker("Enter the second number in the range: ")

if first_number < second_number:
    for number in range(first_number, second_number + 1):
        sub_total = total + number
        print(f"{number} added to {total} = {sub_total}")
        total = sub_total

else:
    for number in range(second_number, first_number + 1):
        sub_total = total - number
        print(f"{number} subtracted from {total} = {sub_total}")
        total = sub_total
