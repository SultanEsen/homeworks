from module1 import binary_search, buble_sort, selection_sort
import random


answer = None
while answer != 0:
    answer = int(input((f'Choose an algorithm :'
                        f'\n1 - binary search'
                        f'\n2 - bubble sort'
                        f'\n3 - selection sort'
                        f'\n0 - exit'
                        f'\nyour choice: ')))
    if answer == 1:
        print("Here is Binary Search algorithm")
        print(binary_search(int(input('Enter length of range: ')), int(input(f'Enter number for search in range: '))))

    elif answer == 2:
        print("Here is Bubble Sort algorithm")
        print(buble_sort(random.sample(range(100), (int(input("Enter number of elements for non sorted list: "))))))

    elif answer == 3:
        print("Here is Selection Sort algorithm")
        print(selection_sort(random.sample(range(100), (int(input("Enter number of elements for non sorted list: "))))))
