class Plant():
    class Stats():
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self):
            self._grow_calls += 1

        def record_age(self):
            self._age_calls += 1

        def record_show(self):
            self._show_calls += 1

        def display(self):
            print(
                f"Stats:  {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0)

    def grow(self, growth_rate):
        self._height = round(self._height + growth_rate, 1)
        self._stats.record_grow()

    def age_one_day(self):
        self._age += 1
        self._stats.record_age()

    def show(self):
        print(f"{self._name}:  {self._height}cm, {self._age} days old")
        self._stats.record_show()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color:  {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, height, age, color, num_seeds):
        super().__init__(name, height, age, color)
        self._num_seeds = num_seeds

    def show(self):
        super().show()
        if self._bloomed:
            print(f"Seeds:  {self._num_seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def record_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )
        self._stats.record_shade()

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
        print(f"Harvest season:  {self._season}")
        print(f"Nutritional value:  {self._nutritional_value}")


def display_stats(plant):
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year?  -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year?  -> {Plant.is_older_than_year(400)}")

    print()
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    display_stats(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow(8.0)
    flower.bloom()
    flower.show()
    display_stats(flower)

    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_stats(tree)

    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        vegetable.grow(2.1)
        vegetable.age_one_day()
    vegetable.show()