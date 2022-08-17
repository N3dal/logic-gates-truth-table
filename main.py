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
from tkinter import ttk


# TODO: highlight the table row on specific input, for example in the  "and" gate if the user turn on the sw1 and turn on the sw2,
# TODO: then you must highlight the table row that contain [1, 1, 1] that  means the input1=1, and input2=1, and the output=1,
# TODO: and hightlight that row in truth table for example with light-green color, and keep other columns with their default color.


# defaults vars.
GATE_NAMES = (
    "NOT",
    "AND",
    "OR",
    "NAND",
    "NOR",
    "XOR"

)
WIN_WIDTH = 400
WIN_HEIGHT = 500
WIN_BG = "gray75"
TITLE = "Logic Gates"


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


def start_app(root: tkinter.Tk):
    root.mainloop()

    return None


def load_image(root: tkinter.Tk, img_name: str):
    """"""

    return tkinter.PhotoImage(master=root,
                              file=f"./assets/{img_name}.png", name=f"image_{img_name}")


def create_component(root: tkinter.Tk, component_name: str, img: tkinter.PhotoImage):
    """this function will create the digital componet"""

    component = tkinter.Label(root, bd=0, image=img, bg=WIN_BG)

    return component


def create_vertical_line(root: tkinter.Tk, color: str, size: int):
    """"""
    vertical_line = tkinter.Frame(root, bg=color, height=size, width=2)

    return vertical_line


def create_horizontal_line(root: tkinter.Tk, color: str, size: int):
    """"""
    horizontal_line = tkinter.Frame(root, bg=color, height=2, width=size)

    return horizontal_line


def create_logic_value_label(root: tkinter.Tk, value: bool, name: str):
    """create a cell value for the table.
    for show either '1' or '0'."""

    label = tkinter.Label(root, bd=0, text=str(value), bg=WIN_BG, name=name)

    return label


def create_table(root: tkinter.Tk, color: str = "black",  gate_name: str = "not"):
    """"""

    # todo : add guard conditions.

    vl, hl = create_vertical_line(
        root, color, 160), create_horizontal_line(root, color, 200)

    table_sizes = {
        "not": "2x1",
        "other_gates": "4x2"
    }

    lines_size = {
        "not": (134, 60),
        "other_gates": (200, 122)
    }

    lines_x_coordinates = {
        "not": 143,
        "other_gates": 110
    }

    width, height = map(lambda a: int(
        a)+1, table_sizes[gate_name if gate_name == "not" else "other_gates"].split('x'))

    line_width, line_height = lines_size[gate_name if gate_name ==
                                         "not" else "other_gates"]

    x_coordinates = lines_x_coordinates[gate_name if gate_name ==
                                        "not" else "other_gates"]

    print(width, height)  # DEBUG.

    # create logic gates tables.
    NOT_GATE = [1, 0, 0, 1]
    AND_GATE = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
    OR_GATE = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    NAND_GATE = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    NOR_GATE = [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0]
    XOR_GATE = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]

    gates_values = {
        "not": NOT_GATE,
        "and": AND_GATE,
        "or": OR_GATE,
        "nand": NAND_GATE,
        "nor": NOR_GATE,
        "xor": XOR_GATE
    }

    # create the table lines.

    # first the horizontal lines.
    for w in range(width):
        create_horizontal_line(
            root, color, line_width).place(x=x_coordinates, y=350+30*w)

    # second create the vertical lines.
    for h in range(height + 1):
        create_vertical_line(root, color, line_height).place(
            x=x_coordinates+66*h, y=350)

    # create cell values.
    # x, y = 172, 357; index = 1; for not gate

    cell_values = [create_logic_value_label(
        root, value, name=f"cell{index}") for index, value in enumerate(gates_values[gate_name])]

    # x for the gates cell values.
    x_cell_coordinates = 172 if gate_name == "not" else 140

    # align - check.

    align_check = 2 if gate_name == "not" else 3

    # for align the cell values.
    i, j = 0, 0

    for index, cell_value in enumerate(cell_values, 1):
        cell_value.place(x=x_cell_coordinates+i, y=357+j)

        i += 65

        if index % align_check == 0:
            i = 0
            j += 30

    return None


def combobox_select_event(root: tkinter.Tk, combobox: ttk.Combobox, images: dict):
    """callback for the combobox"""

    value = combobox.get()

    create_gate(root, value.lower(), images)

    return None


def create_gate(root: tkinter.Tk, gate_name: str, images: dict):
    """create both the table and the gate picture and placing them."""

    clear_main_window(root)

    if gate_name == "and":
        and_img = images["and"]
        and_gate = create_component(root, "and", and_img)
        and_gate.place(x=180, y=180)
        create_table(root, gate_name="and")

    elif gate_name == "or":
        or_img = images["or"]
        or_gate = create_component(root, "or", or_img)
        or_gate.place(x=180, y=180)

        create_table(root, gate_name="or")

    elif gate_name == "nand":
        nand_img = images["nand"]
        nand_gate = create_component(root, "nand", nand_img)
        nand_gate.place(x=180, y=180)

        create_table(root, gate_name="nand")

    elif gate_name == "nor":
        nor_img = images["nor"]
        nor_gate = create_component(root, "nor", nor_img)
        nor_gate.place(x=180, y=180)

        create_table(root, gate_name="nor")

    elif gate_name == "xor":
        xor_img = images["xor"]
        xor_gate = create_component(root, "xor", xor_img)
        xor_gate.place(x=180, y=180)

        create_table(root, gate_name="xor")

    else:
        not_img = images["not"]
        not_gate = create_component(root, "not", not_img)
        not_gate.place(x=180, y=180)

        create_table(root, gate_name="not")

    return None


def clear_main_window(root: tkinter.Tk):
    """remove all widgets from the main window except the combo-box"""

    widgets = root.winfo_children()

    for widget in widgets:
        if "combobox" not in widget.__repr__():
            widget.destroy()


def main_window():

    root = tkinter.Tk()

    root.title(TITLE)

    root.resizable(False, False)

    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    root.configure(bg=WIN_BG)

    # load all needed images for gates.
    gates_images = {gate.lower(): load_image(root, gate.lower())
                    for gate in GATE_NAMES}

    gates_select_box = ttk.Combobox(root, values=GATE_NAMES)
    gates_select_box.set("Pick any Gate".center(37))
    gates_select_box.bind("<<ComboboxSelected>>",
                          lambda e: combobox_select_event(root, gates_select_box, images=gates_images))

    # prevent the users from enter new values.
    gates_select_box["state"] = "readonly"

    gates_select_box.place(x=110, y=40)

    start_app(root)

    return None


def main():
    main_window()


if __name__ == '__main__':
    main()
