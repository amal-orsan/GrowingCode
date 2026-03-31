class Plant():
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.height = starting_height
        self.age = starting_age

    def grow(self, growth_rate):
        self.height = round(self.height + growth_rate, 1)

    def age_one_day(self):
        self.age += 1

    def show(self):
        print(
            f"Created:  {self.name}:  {self.height}cm, {self.age} days old"
            )
    print("=== Plant Factory Output ===")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)

    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()
