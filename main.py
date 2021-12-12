def function():

    total = 0

    numbers = []
    total_numbers = int(input("How many numbers you want to enter?: "))
    print("This programm will ask you to enter number(s)",total_numbers,"time")

    for num in range(total_numbers):
        append_number = int(input("Enter the number: "))
        numbers.append(append_number)

    #Remove the comment of the below print function if you want the list to be shown in the output
    #print(numbers)

    for value in numbers:
        total+=value
    print('The total of the elements is', total)

function()