# Q9: Circle class with area and perimeter methods.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius


def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric radius.")
        return

    circle = Circle(radius)
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")


if __name__ == "__main__":
    main()
