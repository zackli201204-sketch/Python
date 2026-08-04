class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eyecolor=eye_color
        self.height=height_cm

    def show_traits(self):
        print("Eye Color:", self.eyecolor)
        print("Height (CM):", self.height_cm)

class Kid(FamilyMember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name=name
        self.age=age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)

child=Kid("Leo", 14, "brown", 110)

child.show_traits()
child.favorite_hobby("basketball")

print("Is kid a subclass of family member?", issubclass(Kid, FamilyMember))
        