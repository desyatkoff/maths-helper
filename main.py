import os
import time

import rich


ASCII_LOGO = """
███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗    
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝    
██╔████╔██║███████║   ██║   ███████║███████╗    
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚════██║    
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████║    
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝    

██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
"""

if os.name == "nt":
    CLEAR_CMD = "cls"
else:
    CLEAR_CMD = "clear"


class MathsHelper:
    def __init__(self):
        rich.print(f"{ASCII_LOGO}\nMathsHelper by [blue]Serriox[/blue]\n\n\n")

        input("Press <Enter> to open menu...")

        os.system(CLEAR_CMD)

        self.menu()


    def menu(self):
        rich.print(
"""
You want to find a ...?

[bold red]0.[/bold red] [red]Exit[/red]

[bold green]1.[/bold green] [green]Area[/green]
[bold green]1.1.[/bold green] [green]Area of rectangle[/green]
[bold green]1.2.[/bold green] [green]Area of circle[/green]
[bold green]1.3.[/bold green] [green]Area of rhombus[/green]
[bold green]1.4.[/bold green] [green]Area of ellipse[/green]

[bold blue]2.[/bold blue] [blue]Perimeter[/blue]
[bold blue]2.1.[/bold blue] [blue]Perimeter of rectangle[/blue]
[bold blue]2.2.[/bold blue] [blue]Perimeter of circle[/blue]
[bold blue]2.3.[/bold blue] [blue]Perimeter of rhombus[/blue]

[bold yellow]3.[/bold yellow] [yellow]Other[/yellow]
[bold yellow]3.1.[/bold yellow] [yellow]Hypotenuse[/yellow]
"""
        )


        self.option = input("Choose\n: ")


        print("\n")


        if self.option == "0":
            self.are_you_sure = input("Are you sure? [Y/n]\n: ")

            if self.are_you_sure.lower() == "y" or len(self.are_you_sure) < 1:
                quit(0)
            else:
                os.system(CLEAR_CMD)

                self.menu()
        elif self.option == "1.1":
            self.area_of_rectangle()
        elif self.option == "1.2":
            self.area_of_circle()
        elif self.option == "1.3":
            self.area_of_rhombus()
        elif self.option == "1.4":
            self.area_of_ellipse()
        elif self.option == "2.1":
            self.perimeter_of_rectangle()
        elif self.option == "2.2":
            self.perimeter_of_circle()
        elif self.option == "2.3":
            self.perimeter_of_rhombus()
        elif self.option == "3.1":
            self.hypotenuse()
        else:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

            self.menu()


    def area_of_rectangle(self):
        self.rect_side_a = input("First rectangle side\n: ")
        self.rect_side_b = input("Second rectangle side\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {float(self.rect_side_a) * float(self.rect_side_b)}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_circle(self):
        self.radius = input("Radius\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {3.14 * (float(self.radius) ** 2)}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_rhombus(self):
        self.diagonal_a = input("First diagonal\n: ")
        self.diagonal_b = input("Second diagonal\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {(float(self.diagonal_a) * float(self.diagonal_b)) / 2}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_ellipse(self):
        self.diagonal_a = input("First diagonal\n: ")
        self.diagonal_b = input("Second diagonal\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {3.14 * float(self.diagonal_a) * float(self.diagonal_b)}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


    def perimeter_of_rectangle(self):
        self.rect_side_a = input("First rectangle side\n: ")
        self.rect_side_b = input("Second rectangle side\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {(float(self.rect_side_a) + float(self.rect_side_b)) * 2}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def perimeter_of_circle(self):
        self.radius = input("Radius\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {2 * 3.14 * float(self.radius)}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def perimeter_of_rhombus(self):
        self.side = input("Rhombus side\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {float(self.side) * 4}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


    def hypotenuse(self):
        self.cathetus_a = input("Cathetus A\n: ")
        self.cathetus_b = input("Cathetus B\n: ")

        try:
            rich.print(f"[green]Result\n:[/green] {((float(self.cathetus_a) ** 2) + (float(self.cathetus_b) ** 2)) ** 0.5}\n")
        except BaseException:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


def main():
    MathsHelper()


if __name__ == "__main__":
    main()
