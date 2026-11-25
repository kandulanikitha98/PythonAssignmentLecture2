def remove_uneven(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers_list = remove_uneven(my_list)
    print("Original list:", my_list)
    print("Cut-down list:", even_numbers_list)
main()