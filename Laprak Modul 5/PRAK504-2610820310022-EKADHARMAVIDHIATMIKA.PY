def reverse(angka):
    rev = 0
    while angka > 0:
        rev = rev * 10 + (angka % 10)
        angka //= 10
    return rev

def main():
    A, B = map(int, input().split())
    A = reverse(A)
    B = reverse(B)
    C = A + B
    print(reverse(C))

if __name__ == "__main__":
    main()