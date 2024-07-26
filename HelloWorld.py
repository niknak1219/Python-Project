print("Apple Counter")
apple_count = input("How many apples for the day: \n")
number_of_apples_converted = int(apple_count)
while True:
    number_of_customers = input("How many customers: \n")
    number_of_customers_converted = int(number_of_customers)
    number_of_apples_converted = number_of_apples_converted - number_of_customers_converted
    print(number_of_apples_converted)

