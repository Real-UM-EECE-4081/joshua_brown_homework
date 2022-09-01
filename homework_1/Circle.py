class Circle():

    def radius(self, radius):
        r = radius

    def area(self, r):

        area = r*r*3.14

        print("The area of the circle is: \n",area)

    def perimeter(self, r):

        perimeter = 2*r*3.14

        print("The perimeter of the circle is: \n",perimeter)

c = Circle()

radius = int(input("Please enter the radius of the circle: \n"))

c.area(radius)

c.perimeter(radius)
