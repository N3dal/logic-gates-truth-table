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


def start_app(root: tkinter.Tk):
    root.mainloop()


def main_window():
    pass


def main():
    main_window()


if __name__ == '__main__':
    main()
