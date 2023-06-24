try:
    while True:
        print("Istalgan son o'ylang")
        print("U songa 10 ni qo'shing")
        print("U songdan 4 ni ayiring")
        print("U songa 3 ni ko'paytiring")

        natija = int(input("Natija nechi chiqdi: "))

        x = natija / 3 + 4 - 10
        print(f"Siz o'ylagan son {x} ga teng")
        a = input("O'yindan chiqish uchun q ni bosing yoki davom ettiring")
        if a == 'b':
            break
except:
    print("Noto'g'ri belgi kirtildi")
