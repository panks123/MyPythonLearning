if __name__ == '__main__':
    n = int(input("Enter no. of elements"))
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(t)
    print(list(integer_list))