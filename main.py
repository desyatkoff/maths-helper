import os
import time


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
        print(f"{ASCII_LOGO}\nMathsHelper by Serriox\n\n\n")

        input("Press <Enter> to open menu...\n")

        os.system(CLEAR_CMD)

        self.menu()


    def menu(self):
        print(
"""
You want to find a ...?

0. Exit

1. Area
1.1. Area of rectangle
1.2. Area of circle
1.3. Area of rhombus
1.4. Area of ellipse

2. Perimeter
2.1. Perimeter of rectangle
2.2. Perimeter of circle
2.3. Perimeter of rhombus

3. Other
3.1. Hypotenuse
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
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

            self.menu()


    def area_of_rectangle(self):
        self.rect_side_a = input("First rectangle side\n: ")
        self.rect_side_b = input("Second rectangle side\n: ")

        try:
            print(f"Result\n: {float(self.rect_side_a) * float(self.rect_side_b)}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_circle(self):
        self.radius = input("Radius\n: ")

        try:
            print(f"Result\n: {3.14 * (float(self.radius) ** 2)}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_rhombus(self):
        self.diagonal_a = input("First diagonal\n: ")
        self.diagonal_b = input("Second diagonal\n: ")

        try:
            print(f"Result\n: {(float(self.diagonal_a) * float(self.diagonal_b)) / 2}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def area_of_ellipse(self):
        self.diagonal_a = input("First diagonal\n: ")
        self.diagonal_b = input("Second diagonal\n: ")

        try:
            print(f"Result\n: {3.14 * float(self.diagonal_a) * float(self.diagonal_b)}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


    def perimeter_of_rectangle(self):
        self.rect_side_a = input("First rectangle side\n: ")
        self.rect_side_b = input("Second rectangle side\n: ")

        try:
            print(f"Result\n: {(float(self.rect_side_a) + float(self.rect_side_b)) * 2}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def perimeter_of_circle(self):
        self.radius = input("Radius\n: ")

        try:
            print(f"Result\n: {2 * 3.14 * float(self.radius)}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()

    def perimeter_of_rhombus(self):
        self.side = input("Rhombus side\n: ")

        try:
            print(f"Result\n: {float(self.side) * 4}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


    def hypotenuse(self):
        self.cathetus_a = input("Cathetus A\n: ")
        self.cathetus_b = input("Cathetus B\n: ")

        try:
            print(f"Result\n: {((float(self.cathetus_a) ** 2) + (float(self.cathetus_b) ** 2)) ** 0.5}\n")
        except BaseException:
            print("Incorrect value!")

            time.sleep(1)

            os.system(CLEAR_CMD)

        input("Press <Enter> to continue...\n")

        os.system(CLEAR_CMD)

        self.menu()


def main():
    MathsHelper()


if __name__ == "__main__":
    main()
