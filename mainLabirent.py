import time
import os
from tkinter import *

labirent1 = [
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

labirent2 = [
    [1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],

]

labirent3 = [
    [1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],

]

labirent4 = [
    [1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],

]
labirent5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
labirent = labirent5
sY = 30  # 30
sX = 1  # 1

fY = 0  # 0
fX = 14  # 14

# sY = 8  #30
# sX = 6   #1
#
# fY = 0   #0
# fX = 2  #14

labirent[sY][sX] = 2

hedef_yon = "+x"
guncel_yon = "+x"

rota = []
tum_rotalar = []
gidilen_her_nokta = []

secenekli_yol = []
tum_secenekli_yollar = []
sayac = 0

time1 = 0


def reverse1(Y, X):
    rota_reverse = rota
    global rota_original
    global sayac
    rota_original = rota
    rota_reverse.reverse()

    for z in rota_reverse:
        sayac += 1
        # os.system("cls")

        # print(z)
        # print(secenekli_yol[-1])
        # print(z == secenekli_yol[-1])
        # print(f"reverse rota : {rota_reverse}")

        labirent[Y][X] = 0
        Y = z[0]
        X = z[1]
        labirent[Y][X] = 2

        # for i in labirent:
        #     print(i)
        # print("\n\n")

        time.sleep(time1)
        if z == secenekli_yol[-1]:
            global cc
            cc = z
            # print("burası")
            secenekli_yol.pop(-1)
            break


while True:
    # os.system("cls")
    # print(gidilen_her_nokta)
    # print(f"rota : {rota}")
    # print(f"tüm secenekliler {tum_secenekli_yollar}")
    # print(f"secenekliler {secenekli_yol}")

    # for x in labirent:
    #     print(x)
    # print("\n\n")

    time.sleep(time1)
    controlX = sX
    controlY = sY

    if sX == fX and sY == fY:

        for i in rota:
            labirent[i[0]][i[1]] = 2
        for x in labirent:
            print(x)
        print("\n\n")
        print(f"Rota : {rota}")
        print("LABİRENT BİTTİ")

        break

    if guncel_yon == "+x":
        yol_sayisi = 0
        if labirent[controlY][controlX + 1] != 1:  ### Yol sayısı bulmak için 3 ihtimal işlem yapılmadan kontrol edilir.
            yol_sayisi += 1
        if labirent[controlY - 1][controlX] != 1:
            yol_sayisi += 1
        if labirent[controlY][controlX - 1] != 1:
            yol_sayisi += 1
        if labirent[controlY + 1][controlX] != 1:
            yol_sayisi += 1
        if yol_sayisi >= 3:
            if ([controlY, controlX] in tum_secenekli_yollar) == False:
                secenekli_yol.append([controlY, controlX])
                tum_secenekli_yollar.append([controlY, controlX])

        if labirent[controlY][controlX + 1] != 1 and ([controlY, controlX + 1] in gidilen_her_nokta) != True:
            # print("1")

            labirent[sY][sX] = 0
            sX += 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlX = sX
        elif labirent[controlY - 1][controlX] != 1 and ([controlY - 1, controlX] in gidilen_her_nokta) != True:
            # print("2")
            labirent[sY][sX] = 0
            sY -= 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlY = sY
        elif labirent[controlY][controlX - 1] != 1 and ([controlY, controlX - 1] in gidilen_her_nokta) != True:
            # print("3")
            labirent[sY][sX] = 0
            sX -= 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlX = sX
        elif labirent[controlY + 1][controlX] != 1 and ([controlY + 1, controlX] in gidilen_her_nokta) != True:
            # print("4")
            labirent[sY][sX] = 0
            sY += 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlY = sY

        else:
            reverse1(sY, sX)
            rota.reverse()
            for i in range(sayac):
                try:
                    rota.pop(-1)
                except:
                    pass
            sayac = 0
            sY = cc[0]
            sX = cc[1]
            if ([sY, sX] in tum_secenekli_yollar) == False:
                rota.append([sY, sX])
            else:
                rota.append([sY, sX])

    if guncel_yon == "-x":
        yol_sayisi = 0
        if labirent[controlY][controlX + 1] != 1:  ### Yol sayısı bulmak için 3 ihtimal işlem yapılmadan kontrol edilir.
            yol_sayisi += 1
        if labirent[controlY - 1][controlX] != 1:
            yol_sayisi += 1
        if labirent[controlY][controlX - 1] != 1:
            yol_sayisi += 1
        if labirent[controlY + 1][controlX] != 1:
            yol_sayisi += 1
        if yol_sayisi >= 3:
            if ([controlY, controlX] in tum_secenekli_yollar) == False:
                secenekli_yol.append([controlY, controlX])
                tum_secenekli_yollar.append([controlY, controlX])

        if labirent[controlY][controlX - 1] != 1 and ([controlY, controlX - 1] in gidilen_her_nokta) != True:
            # print("3")
            labirent[sY][sX] = 0
            sX -= 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlX = sX
        elif labirent[controlY - 1][controlX] != 1 and ([controlY - 1, controlX] in gidilen_her_nokta) != True:
            # print("2")
            labirent[sY][sX] = 0
            sY -= 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlY = sY
        elif labirent[controlY][controlX + 1] != 1 and ([controlY, controlX + 1] in gidilen_her_nokta) != True:
            # print("1")

            labirent[sY][sX] = 0
            sX += 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlX = sX


        elif labirent[controlY + 1][controlX] != 1 and ([controlY + 1, controlX] in gidilen_her_nokta) != True:
            # print("4")
            labirent[sY][sX] = 0
            sY += 1
            labirent[sY][sX] = 2
            gidilen_her_nokta.append([sY, sX])
            rota.append([sY, sX])
            controlY = sY

        else:
            reverse1(sY, sX)
            rota.reverse()
            for i in range(sayac):
                try:
                    rota.pop(-1)
                except:
                    pass
            sayac = 0
            sY = cc[0]
            sX = cc[1]
            if ([sY, sX] in tum_secenekli_yollar) == False:
                rota.append([sY, sX])
            else:
                rota.append([sY, sX])

ws = Tk()
ws.title('PythonGuides')
ws.geometry('1000x1000')
ws.config(bg='#345')

canvas = Canvas(
    ws,
    height=1000,
    width=1000,
    bg="#345"
)
canvas.pack()

x1 = 0
y1 = 0

x2 = 32
y2 = 32
for i in labirent:
    for z in i:
        if z == 1:
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="#000",
                fill="#000", )
        elif z == 0:
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="#fff",
                fill="#fff", )
        elif z == 2:
            canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="#900",
                fill="#900", )
        x1 += 32
        x2 += 32
    x1 = 0
    x2 = 32

    y1 += 32
    y2 += 32

y1 = 0
y2 = 32

ws.mainloop()
