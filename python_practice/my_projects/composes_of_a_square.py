def square (side):
    """Принимает сторону квадрата и выводит обьём куба, площадь и т.д."""
    side = float(side)
    perimeter = side * 4 # Периметр одной стороны куба.
    area = side ** 2 # площадь одной стороны куба.
    diogonal_square = (side ** 2) + (side ** 2)
    diogonal_square = diogonal_square ** 0.5 # диогональ стороны куба.
    volume_cube = side ** 3 # объём куба
    diogonal_cube = (diogonal_square ** 2) + (side ** 2)
    diogonal_cube **= 0.5 # диогональ куба.
    perimeter_cube = perimeter * 6 # Периметр куба.
    area_cube = area * 6 # Площадь куба.

    print("perimeter: " + str(perimeter) + "cm;\n"
    	"area: " + str(area) + "cm^2;\n"
        "diogonal_square: " + str(diogonal_square) + "cm;\n"
    	"volume_cube: " + str(volume_cube) + "cm^3;\n"
        "diogonal_cube: " + str(diogonal_cube) + "cm;\n"
        "perimeter_cube: " + str(perimeter_cube) + "cm;\n"
        "area_cube: " + str(area_cube) + "cm^2;\n")

value = input("Enter value square (cm):")
square(value)
