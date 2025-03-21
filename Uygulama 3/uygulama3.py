def multiplication_table():
    num = int(input("Bir sayı giriniz: "))
    for i in range(1, 11):
        print(num * i, end=" ")
    print()

def digit_count():
    num = int(input("Bir sayı giriniz: "))
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("Basamak sayısı:", count)

def divisible_by_five():
    numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for num in numbers:
        if num > 150:
            break
        if num % 5 == 0:
            print(num, end=", ")
    print()

def count_divisibles():
    start = int(input("Başlangıç değerini giriniz: "))
    end = int(input("Bitiş değerini giriniz: "))
    divisor = int(input("Bölünecek sayıyı giriniz: "))
    count = sum(1 for i in range(start, end + 1) if i % divisor == 0)
    print("Bölünebilen sayı adedi:", count)

def even_number_output():
    for i in range(1, 100):
        print(f"{i} - {100 - i}")

def increment_ip_address():
    ip = list(map(int, input("IP adresini giriniz (boşluk ile ayırarak): ").split()))
    for _ in range(5):
        ip[3] += 1
        for i in range(3, -1, -1):
            if ip[i] > 255:
                ip[i] = 0
                if i > 0:
                    ip[i-1] += 1
        print(" ".join(map(str, ip)))

options = {
    "1": multiplication_table,
    "2": digit_count,
    "3": divisible_by_five,
    "4": count_divisibles,
    "5": even_number_output,
    "6": increment_ip_address
}

choice = input("Çalıştırmak istediğiniz ödevin numarasını giriniz (1-6): ")
if choice in options:
    options[choice]()
else:
    print("Geçersiz seçim!")
