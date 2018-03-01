class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # Getter
    # allows reference to individual fields
    @property
    def height(self):
        print("Retrieving the Height")

        # use __ to show that information is private
        return self.__height

    # Setter
    # protect form putting in bad data
    @height.setter
    def height(self, value):

        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the Width")

        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        self.__width = int(self.__width) * (int(self.__height))
        return int(self.__width) * (int(self.__height))

def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    # because we use @property and @height.setter, don't need height()
    aSquare.height = height
    aSquare.width = width

    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)
    print(aSquare.width)
    aSquare.width = str(aSquare.getArea())
    print(aSquare.width)


main()