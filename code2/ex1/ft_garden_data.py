class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name}:  {self.height}cm, {self.age} days old"
            )
    print("=== Garden Plant Registry ===")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()
