class Plant():
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(
            f"{self._name}:  {self._height}cm, {self._age} days old\n"
        )

    def set_age(self, new_age):
        if self.check_validity(new_age, "age"):
            print("Age updated rejected")
        else:
            self._age = new_age
            print(f"Age updated:  {self._age} days\n")

    def set_height(self, new_height):
        if self.check_validity(new_height, "height"):
            print("Height updated rejected")
        else:
            self._height = new_height
            print(f"Height updated:  {self._height}cm")

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def check_validity(self, value, name):
        if value < 0:
            print(f"{self._name}:  Error, {name} can't be negative")
            return True
        return False


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)
    print(
        f"Plant created:  {plant1._name}: "
        f"{plant1.get_height()}cm, {plant1.get_age()} days old\n"
    )
    plant1.set_height(25.0)
    plant1.set_age(30)
    plant1.set_height(-10.0)
    plant1.set_age(-5)
    print()
    print(
        f"Current state:  {plant1._name}: "
        f"{plant1.get_height()}cm, {plant1.get_age()} days old\n"
        )
