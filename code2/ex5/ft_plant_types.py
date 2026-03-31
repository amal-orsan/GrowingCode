class Plant():
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(
            f"{self._name}:  {self._height}cm, {self._age} days old"
        )

    def age_one_day(self):
        self._age += 1

    def grow(self, growth_rate):
        self._height = round(self._height + growth_rate, 1)

    def lower(self):
        if self._name >= "A" and self._name <= "Z":
            self._name = self._name + 32


class Flower(Plant):
    def __init__(self, name, height, age, color, bloomed=False):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = bloomed

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter:  {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, season):
        super().__init__(name, height, age)
        self._season = season
        self._nutritional_value = 0

    def grow(self, growth_rate):
        super().grow(growth_rate)
        self._nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest Season:  {self._season}")
        print(f"Nutritional Value:  {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print(f"[asking the {flower._name.lower()} to bloom]")
    flower.bloom()
    flower.show()

    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print(f"[asking the {tree._name.lower()} to produce shade]")
    tree.produce_shade()

    print()
    print("=== Vegetable")
    vegetable = Vegetable("Carrot", 5.0, 10, "April")
    vegetable.show()
    print(f"[make {vegetable._name.lower()} grow and age for 20 days]")
    for i in range(20):
        vegetable.grow(2.1)
        vegetable.age_one_day()
    vegetable.show()
