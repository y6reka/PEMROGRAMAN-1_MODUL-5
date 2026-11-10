def MaxBilangan(a, b, c, d):
    return max(a, b, c, d)
def main():
    a, b, c, d = map(int, input().split())
    hasil = MaxBilangan(a, b, c, d)
    print(hasil)

if __name__ == "__main__":
    main()