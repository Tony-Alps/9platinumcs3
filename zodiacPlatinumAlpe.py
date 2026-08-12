year=int(input("Enter your birth year: "))
if year<1900:
    print("Invalid year, it should not be earlier than 1900.")
if year>=1900:
    zodiac = (year - 1900) % 12
    if zodiac == 0:
        print("Your Chinese Zodiac sign is: Monkey (猴 / Hóu)")
    elif zodiac == 1:
        print("Your Chinese Zodiac sign is: Ox (牛 / Niú)")
    elif zodiac == 2:
        print("Your Chinese Zodiac sign is: Tiger (虎 / Hǔ)")
    elif zodiac == 3:
        print("Your Chinese Zodiac sign is: Rabbit (兔 / Tù)")
    elif zodiac == 4:
        print("Your Chinese Zodiac sign is: Dragon (龙 / Lóng)")
    elif zodiac == 5:
        print("Your Chinese Zodiac sign is: Snake (蛇 / Shé)")
    elif zodiac == 6:
        print("Your Chinese Zodiac sign is: Horse (马 / Mǎ)")
    elif zodiac == 7:
        print("Your Chinese Zodiac sign is: Goat (羊 / Yáng)")
    elif zodiac == 8:
        print("Your Chinese Zodiac sign is: Rooster (鸡 / Jī")
    elif zodiac == 9:
        print("Your Chinese Zodiac sign is: Dog (狗 / Gǒu)")
    elif zodiac == 10:
        print("Your Chinese Zodiac sign is: Pig (猪 / Zhū)")
    elif zodiac == 11:
        print("Your Chinese Zodiac sign is: Rat (鼠 / Shǔ)")
