if __name__ == '__main__':
    n = int(input())
    a = sorted(map(int, input().split()))
    print(max(a[-1] * a[-2], a[-1] * a[-2] * a[-3], a[0] * a[1] * a[-1]))