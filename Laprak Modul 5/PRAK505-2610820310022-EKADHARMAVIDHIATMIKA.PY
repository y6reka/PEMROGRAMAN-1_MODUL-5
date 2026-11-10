def Biodata(tahunLahir, A, B):
    tahun_sekarang = 2026
    umur = tahun_sekarang - tahunLahir
    
    print(f"Perkenalkan Nama Saya: {A}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : 2026")
    print(f"Asal Saya dari : {B}")

def main():
    tahunLahir = int(input())
    A = input().strip()
    B = input().strip()
    Biodata(tahunLahir, A, B)

if __name__ == "__main__":
    main()