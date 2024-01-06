import random

def tebak_angka():
    acak = random.randint(1, 50)
    print("Selamat datang di game tebak angka!")
    print("Tebak angka antara 1 sampai 50!")
    while True:
        percobaan = input("Tebak angkamu: ")
        if not percobaan.isdigit():
            print("Harus angka! Coba lagi.")
        else:
            percobaan = int(percobaan)
            if percobaan == acak:
                print("Selamat! Angka yang tebakanmu adalah", acak)
                break
            elif percobaan < acak:
                print("Angka terlalu kecil! Coba lagi.")
            else:
                print("Angka terlalu besar! Coba lagi.")

if __name__ == "__main__":
    tebak_angka()