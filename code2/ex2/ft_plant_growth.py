class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth_rate):
        self.height = round(self.height + growth_rate, 1)

    def age_every_one_day(self):
        self.age += 1

    def show(self):
        print(
            f"{self.name}:  {self.height}cm, {self.age} days old"
            )


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30)
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant1.show()
        plant1.grow(0.8)
        plant1.age_every_one_day()
    total_growth = round(0.8 * 7)
    print(f"Growth this week:  {total_growth}cm")
