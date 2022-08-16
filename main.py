#!/usr/bin/python3
# -----------------------------------------------------------------
# logic gate truth table.
#
#
#
# Author:N84.
#
# Create Date:Fri Feb 25 15:06:54 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import system
from os import name as OS_NAME
import tkinter


# TODO: highlight the table row on specific input, for example in the  "and" gate if the user turn on the sw1 and turn on the sw2,
# TODO: then you must highlight the table row that contain [1, 1, 1] that  means the input1=1, and input2=1, and the output=1,
# TODO: and hightlight that row in truth table for example with light-green color, and keep other columns with their default color.

def clear():
    """wipe the terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for all other os in the world.
        # system("your-command")
        pass

    return None


clear()


WIN_WIDTH = 400
WIN_HEIGHT = 500
WIN_BG = "gray75"


def start_app(root: tkinter.Tk):
    root.mainloop()

    return None


def load_image(img_name: str):
    """"""

    return tkinter.PhotoImage(
        file=f"./assets/{img_name}.png", name=img_name)


def create_component(root: tkinter.Tk, component_name: str, img: tkinter.PhotoImage):
    """this function will create the digital componet"""

    component = tkinter.Label(root, bd=0, image=img, bg=WIN_BG)

    return component


def create_vertical_line(root: tkinter.Tk, color: str, size: int):

    vertical_line = tkinter.Frame(root, bg=color, height=size, width=2)

    return vertical_line


def create_horizontal_line(root: tkinter.Tk, color: str, size: int):

    horizontal_line = tkinter.Frame(root, bg=color, height=2, width=size)

    return horizontal_line


def create_table(root: tkinter.Tk, color: str = "black",  gate_name: str = "not"):
    """"""

    vl, hl = create_vertical_line(
        root, color, 160), create_horizontal_line(root, color, 200)

    table_sizes = {
        "not": "2x2",
        "other_gates": "4x3"
    }

    width, height = map(lambda a: int(
        a)+1, table_sizes[gate_name if gate_name == "not" else "other_gates"].split('x'))

    print(width, height)  # DEBUG.

    # create logic gates tables.
    NOT_GATE = [1, 0, 0, 1]
    AND_GATE = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
    OR_GATE = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    NAND_GATE = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    NOR_GATE = [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0]
    XOR_GATE = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]

    # create the table lines.

    # first the horizontal lines.
    for w in range(width):
        create_horizontal_line(root, color, 200).place(x=110, y=350+30*w)

    # second create the vertical lines.
    for h in range(height):
        create_vertical_line(root, color, 120).place(x=110+66*h, y=350)

    return None


def main_window():

    root = tkinter.Tk()

    root.title("Logic Gates")

    root.resizable(False, False)

    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    root.configure(bg=WIN_BG)

    and_img = load_image("and")
    and_gate = create_component(root, "and", and_img)
    and_gate.place(x=180, y=180)

    create_table(root, gate_name="not")

    start_app(root)

    return None


def main():
    main_window()


if __name__ == '__main__':
    main()
