import time


def binary_search(a, x):
    range1 = [i for i in range(1, a+1)]
    # print(range1)
    first = range1[0]
    last = range1[len(range1)-1]
    steps = 0
    middle = int()
    while x != middle:
        steps +=1
        print(f'First: {first}, Last: {last}')
        middle = (first + last) // 2
        print(f'Middle: {middle}')
        time.sleep(1)
        if x == middle:
            break
        elif x > middle:
            first = middle + 1
        else:
            last = middle -1
    return f'Your number "{x}" was found for {steps} steps.\n'


def buble_sort(a):
    print(f'Initial list: {a}')
    n = len(a)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            pass
    return f'Sorted list: {a}\n'


def selection_sort(a):
    print(f'Initial list: {a}')
    for i, e in enumerate(a):
        mn = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[mn] = a[mn], e
    return f'Sorted list: {a}\n'