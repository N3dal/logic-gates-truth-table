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
from os import name as os_name
import tkinter


def clear():
    """wipe the terminal screen."""
    if os_name == "posix":
        # *nix machines.
        system("clear")
    else:
        # window macines.
        system("cls")


clear()


WIN_WIDTH = 400
WIN_HEIGHT = 500
WIN_BG = "gray75"


def start_app(root: tkinter.Tk):
    root.mainloop()


def load_image(img_name: str):
    """"""

    return tkinter.PhotoImage(
        file=f"./assets/{img_name}.png", name=img_name)


def create_component(root: tkinter.Tk, component_name: str, img: tkinter.PhotoImage):
    """this function will create the digital componet"""

    component = tkinter.Label(root, bd=0, image=img, bg=WIN_BG)

    return component


def main_window():

    root = tkinter.Tk()

    root.title("Logic Gates")

    root.resizable(False, False)

    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    root.configure(bg=WIN_BG)

    and_img = load_image("and")
    and_gate = create_component(root, "and", and_img)
    and_gate.place(x=180, y=180)

    start_app(root)


def main():
    main_window()


if __name__ == '__main__':
    main()
