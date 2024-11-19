import os
import time


ascii_logo = """
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


class MathsHelper:
    def __init__(self):
        print(f"{ascii_logo}\n\n")

        self.menu()


    def menu(self):
        print(
"""
You want to find a ...?

1. Area of square
2. Area of circle
3. Perimeter of square
4. Hypotenuse
5. Circle length

0. Exit
\n
"""
        )


        self.option = input("Choose [0-5]: ")
        print("\n\n")


        if self.option == "1":
            self.area_of_square()
        elif self.option == "2":
            self.area_of_circle()
        elif self.option == "3":
            self.perimeter_of_square()
        elif self.option == "4":
            self.hypotenuse()
        elif self.option == "5":
            self.circle_length()
        elif self.option == "0":
            self.are_you_sure = input("Are you sure? [Y/n] ")

            if self.are_you_sure.lower() == "y" or len(self.are_you_sure) < 1:
                quit(0)
            else:
                self.menu()
        else:
            print("Incorrect value!")

            self.menu()


    def area_of_square(self):
        self.square_side = input("Square side: ")

        try:
            print(f"Result: {float(self.square_side) ** 2}\n\n")
        except BaseException:
            print("Incorrect value!\n\n")

            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        self.menu()

    def area_of_circle(self):
        self.radius = input("Radius: ")

        try:
            print(f"Result: {3.14 * (float(self.radius) ** 2)}\n\n")
        except BaseException:
            print("Incorrect value!\n\n")

            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        self.menu()

    def perimeter_of_square(self):
        self.square_side = input("Square side: ")

        try:
            print(f"Result: {float(self.square_side) * 4}\n\n")
        except BaseException:
            print("Incorrect value!\n\n")

            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        self.menu()

    def hypotenuse(self):
        self.cathetus_a = input("Cathetus A: ")
        self.cathetus_b = input("Cathetus B: ")

        try:
            print(f"Result: {((float(self.cathetus_a) ** 2) + (float(self.cathetus_b) ** 2)) ** 0.5}\n\n")
        except BaseException:
            print("Incorrect value!\n\n")

            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        self.menu()

    def circle_length(self):
        self.radius = input("Radius: ")

        try:
            print(f"Result: {2 * 3.14 * float(self.radius)}\n\n")
        except BaseException:
            print("Incorrect value!\n\n")

            time.sleep(1)

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        self.menu()


def main():
    MathsHelper()


if __name__ == "__main__":
    main()
