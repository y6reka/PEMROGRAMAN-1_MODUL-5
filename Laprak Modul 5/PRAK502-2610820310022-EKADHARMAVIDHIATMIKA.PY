def hitung(nilai1, nilai2):
    return abs(nilai1 - nilai2)


x1, y1, x2, y2 = map(int, input().split())

jarak = hitung(x1, x2) + hitung(y1, y2)
print(jarak)