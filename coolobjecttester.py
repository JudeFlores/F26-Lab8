#testing topspinner class
from FavoriteObject import topspinner
def main():
    spinner = topspinner("Red", "Titanium", 80)
    spinner.describe()
    spinner.spin(200)

if __name__ == "__main__":
    main()