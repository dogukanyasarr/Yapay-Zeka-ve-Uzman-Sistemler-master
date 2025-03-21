num = float(input("Bir sayı giriniz: "))

if num > 0:
    print("Girilen sayı pozitiftir.")

if num % 2 == 0:
    print("Girilen sayı çifttir.")
else:
    print("Girilen sayı tektir.")

if num < 0:
    print("Girilen sayı negatiftir.")
elif num == 0:
    print("Girilen sayı sıfırdır.")
else:
    print("Girilen sayı pozitiftir.")

weight = float(input("Bagajınızın ağırlığını giriniz: "))

if weight > 50:
    print("Bu ağırlıktaki bir çanta için ek ücret ödemeniz gerekmektedir.")
else:
    print("Bagajınızın ağırlığı uygundur.")
