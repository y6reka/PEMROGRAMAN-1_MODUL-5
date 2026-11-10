#include <stdio.h>

void Biodata(int tahunLahir, char A[], char B[]) {
    int tahun_sekarang = 2026;
    int umur = tahun_sekarang - tahunLahir;
    
    printf("Perkenalkan Nama Saya: %s\n", A);
    printf("Umur Saya : %d\n", umur);
    printf("Saya Adalah Angkatan : 2026\n");
    printf("Asal Saya dari : %s", B);
}

int main() {
    int tahunLahir;
    char A[20], B[15];
    scanf("%d", &tahunLahir);
    scanf(" %[^\n]%*c", A);
    scanf(" %[^\n]%*c", B);
    Biodata(tahunLahir, A, B);
    return 0;
}