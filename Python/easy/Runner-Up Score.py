def fun(arr):
    sarr = sorted(set(arr),reverse=True)
    return sarr[1]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(fun(arr))