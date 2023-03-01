from random import *
while True:
    try:
        player = int(input("Mời bạn chơi (1:Kéo 2:Búa 3:Bao): "))
        if player not in [1, 2, 3]:
            print("Lựa chọn không hợp lệ, mời bạn chọn lại!")
        computer = randrange(0,2)
        if computer == 0:
            print("Máy chọn Kéo")
        if computer == 1:
            print("Máy chọn Búa")
        if computer == 2:
            print("Máy chọn Bao")
        if player == 1:
            print("Bạn chọn kéo")
            if computer == 0:
                print("Hòa")
            if computer == 1:
                print("Thua")
            if computer == 2:
                print("Win")
        if player == 2:
            print("Bạn chọn búa")
            if computer == 1:
                print("Hòa")
            if computer == 2:
                print("Thua")
            if computer == 0:
                print("Win")
        if player == 3:
            print("Bạn chọn bao")
            if computer == 2:
                print("Hòa")
            if computer == 0:
                print("Thua")
            if computer == 1:
                print("Win")
    except:
        print("Nhập 1 2 hoặc 3 thôi thằng ngu")
    a = input("Muốn tiếp ko? Y/N: ")
    if a == "N":
        break
print("Cút")