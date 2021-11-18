class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter the string: ")

    def print_String(self):
        print(self.str1.upper())


if __name__ == '__main__':
    str1 = IOString()
    str1.get_String()
    str1.print_String()