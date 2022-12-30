import timeit
import random
from tkinter import *
from pathlib import Path
from tkinter.font import BOLD

maxScore = 100
number = 10000000

def getTime():
    return timeit.default_timer()

def cpu():
    row = number//10000
    column = number//10000

    matrix1 = [[random.randint(0, 9) for j in range(column)]
               for i in range(row)]
    matrix2 = [[random.randint(0, 9) for j in range(column)]
               for i in range(row)]

    start = getTime()

    result = [[(m1+m2 for m1, m2 in zip(i, j))
               for j in zip(*matrix2)] for i in matrix1]
    
    stop = getTime()

    cpuScore = stop - start
    cpuPt = maxScore - cpuScore

    return cpuPt

# print(cpu())


def memory():
    start = getTime()

    list1 = [random.randint(0, number) for i in range(number)]
    for j in range(len(list1)):
        list1[j] = random.randint(0, number)

    stop = getTime()

    memoryScore = stop - start
    memoryPt = maxScore - memoryScore

    return memoryPt

# print(memory())


def disk():
    start = getTime()

    with open('text.txt', 'w') as file:
        for i in range(number):
            file.write(str(random.randint(0, number)))

    with open('text.txt', 'r') as file:
        line = file.readline()
        while line != '':
            line = file.readline()

    stop = getTime()

    diskScore = stop - start
    diskPt = maxScore - diskScore

    return diskPt

# print(disk())


def bench():
    labeltextR = Label(root, text="Result", font=(
        "Nico Moji", 64, "bold"), bg="Black", fg="White").pack(pady=55)

    # to min
    cpuScore = cpu()
    memoryScore = memory()
    diskScore = disk()
    totalScore = cpuScore + memoryScore + diskScore

    labelCpu = Label(root, text=f"CPU SCORES\t{cpuScore:.4f} point", font=(
        "Nico Moji", 32, "bold"), bg="#5C76FF", fg="White").pack(pady=9)

    labelMem = Label(root, text=f"MEMORY SCORES\t{memoryScore:.4f} point", font=(
        "Nico Moji", 32, "bold"), bg="#5C76FF", fg="White").pack(pady=21)

    labelDisk = Label(root, text=f"DISK SCORES\t{diskScore:.4f} point", font=(
        "Nico Moji", 32, "bold"), bg="#5C76FF", fg="White").pack(pady=14)

    labelTotal = Label(root, text=f"TOTAL SCORES\t{totalScore:.4f} point", font=(
        "Nico Moji", 32, "bold"), bg="Black", fg="White").pack(pady=60)

    frameBlue()


def exitProgram():
    root.destroy()


# set window
root = Tk()
root.title("Destroy Benchmark")
root.geometry("1000x720")
root.configure(bg="#000")


OUTPUT_PATH_H = Path("buildHome/guiH.py").parent
ASSETS_PATH_H = OUTPUT_PATH_H / Path("./assetsH")

def relative_to_assets_H(path: str) -> Path:
    return ASSETS_PATH_H / Path(path)

OUTPUT_PATH_R = Path("buildResult/guiR.py").parent
ASSETS_PATH_R = OUTPUT_PATH_R / Path("./assetsR")

def relative_to_assets_R(path: str) -> Path:
    return ASSETS_PATH_R / Path(path)


canvas = Canvas(
    root,
    bg="#000000",
    height=720,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1H = PhotoImage(
    file=relative_to_assets_H("image_1.png"))
image_1H = canvas.create_image(
    500.0,
    360.0,
    image=image_image_1H
)


labelText1 = Label(root, text="Destroy", font=(
    "Nico Moji", 64, BOLD), fg="White", bg="Black")
labelText1.pack(pady=20)
labelText2 = Label(root, text="Benchmark", font=(
    "Nico Moji", 64, BOLD), fg="White", bg="Black")
labelText2.pack(pady=0)


def clickToStart():
    labelText1.destroy()
    labelText2.destroy()
    button_1.destroy()
    bench()


# Start Button
button_image_1 = PhotoImage(
    file=relative_to_assets_H("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clickToStart
)
button_1.place(
    x=360.0,
    y=474.0,
    width=280.0,
    height=79.0
)

# Exit Button
button_image_2 = PhotoImage(
    file=relative_to_assets_R("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=exitProgram
)
button_2.place(
    x=455.0,
    y=604.0,
    width=90.0,
    height=37.0
)

OUTPUT_PATH = Path("build/assets").parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def frameBlue():
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = Label(image=image_image_2)
    image_2.image = image_image_2
    image_2 = canvas.create_image(
        500.0,
        393.2261657714844,
        image=image_image_2
    )

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = Label(image=image_image_3)
    image_3.image = image_image_3
    image_3 = canvas.create_image(
        500.0,
        313.1130676269531,
        image=image_image_3
    )

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = Label(image=image_image_4)
    image_4.image = image_image_4
    image_4 = canvas.create_image(
        500.0,
        233.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = Label(image=image_image_5)
    image_5.image = image_image_5
    image_5 = canvas.create_image(
        499.1405029296875,
        548.6445922851562,
        image=image_image_5
    )

root.resizable(False, False)
root.mainloop()