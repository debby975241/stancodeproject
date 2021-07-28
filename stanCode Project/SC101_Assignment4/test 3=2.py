
def main():
    lst = [1, 4, 2, 7, 3]
    mystery(lst)
    # lst1 = [1, 8, 4, 7, 3]
    # mystery(lst1)
    # lst2 = [2, 8, 0, 7, 3]
    # mystery(lst2)
    # lst3 = [2, 0, 10, 1, 0]
    # mystery(lst3)


def mystery(lst):
    n = len(lst)

    for i in range(1, n):
        temp = lst[i]
        j = i-1

        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp

    print(lst)


if __name__ == '__main__':
    main()