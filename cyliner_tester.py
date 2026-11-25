#Testing the functions of the cylinder class
from cylinder import Cylinder
def main():
        cyl = Cylinder(5, 6)
        print(cyl.volume())
        print(cyl.surface_area())



if __name__ == "__main__":
    main()
