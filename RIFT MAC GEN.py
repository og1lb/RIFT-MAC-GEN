import os
import random


os.system("cls" if os.name == "nt" else "clear")


logo = r"""
  ___ ___ ___ _____   __  __   _   ___    ___ ___ _  _
 | _ \_ _| __|_   _| |  \/  | /_\ / __|  / __| __| \| |
 |   /| || _|  | |   | |\/| |/ _ \ (__  | (_ | _|| .` |
 |_|_\___|_|   |_|   |_|  |_/_/ \_\___|  \___|___|_|\_|

                    MAC ADDRESS GENERATOR
"""


print(logo)


def generate_mac():

    mac = [
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    ]

    return ":".join(
        f"{x:02X}" for x in mac
    )


def create_box(title, lines):

    longest = max(
        len(title),
        *(len(line) for line in lines)
    )

    padding = 2
    width = longest + padding * 2


    def box_line(line=""):

        return (
            "│"
            + " " * padding
            + line.ljust(longest)
            + " " * padding
            + "│"
        )


    print()

    print(
        "┌"
        + "─" * width
        + "┐"
    )


    print(
        box_line(
            title.center(longest)
        )
    )


    print(
        "├"
        + "─" * width
        + "┤"
    )


    for line in lines:

        print(
            box_line(line)
        )


    print(
        "└"
        + "─" * width
        + "┘"
    )



try:

    amount = int(
        input("Generate Amount > ")
    )


    mac_addresses = []


    for i in range(amount):

        mac_addresses.append(
            f"{i+1}. {generate_mac()}"
        )


    create_box(
        f"GENERATED {amount} MAC ADDRESSES",
        mac_addresses
    )


except ValueError:

    print(
        "\n[-] Invalid input."
    )


input(
    "\nPress ENTER to exit..."
)