def maksimal(a, b):
    return a if a > b else b

def minimal(a, b):
    return a if a < b else b

def main():
    bilangan = int(input())
    nilai_list = []
    while len(nilai_list) < bilangan:
        nilai_list.extend(list(map(int, input().split())))
    
    batas = 0
    maks = -10000
    minim = 10000
    
    while batas < bilangan:
        nilai = nilai_list[batas]
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas += 1
        
    print(f"{maks} {minim}")

if __name__ == "__main__":
    main()