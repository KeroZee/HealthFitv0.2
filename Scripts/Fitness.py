# import personalDetails (weight, height)

def bmi():
    bodyMassIndex = weight / (height ** 2)
    return bodyMassIndex

# in webapp, nChoice not available. Definition will be available through hover


def category():
    print("(Bulk, Body Recomposition, Cut)")

    while True:

        nChoice = input("View or choose: ")

        if nChoice.lower() == "view":
            definition = input("View which category?:")
            if definition.lower() == "bulk":
                print("Providing your body excess calories to gain weight.")
            elif definition.lower() == "body recomposition":
                print("Focuses on body composition rather than weight.")
            elif definition.lower() == "cut":
                print("Uses fat burning and healthy diet to lose weight.")

        elif nChoice.lower() == "choose":
            types = input("Choose a nutrition plan:")
            if types.lower() == "bulk":
                nutritionPlan = types
                print("Nutrition plan for " + nutritionPlan + " confirmed.")
                break
            elif types.lower() == "body recomposition":
                nutritionPlan = types
                print("Nutrition plan for " + nutritionPlan + " confirmed.")
                break
            elif types.lower() == "cut":
                nutritionPlan = types
                print("Nutrition plan for " + nutritionPlan + " confirmed.")
                break
            else:
                print("An error occured, please put in the right plan.")

# store nutritionPlan in database


def macronutrient_measured_per_gram():
    protein = 4
    protein_intake = weight * 1.4
    carb = 4
    fat = 9


def maintenanceNutrition():
    # https://jcdfitness.com/calorie-intake-calculator/#calculator
    calories = int(input("Input the calculated calories"))

# def bulk():
#     35% of calories from protein, 45% of calories from carb, 20% of calories from fat

# def recomp():
#     cutting diet but high protein, down kcal but maintain protein_intake

# def cut():
#     maintenanceNutrition()* 80%


class YourPlan:
    def __init__(self, maintenance, diet):
        self.__maintenance = maintenance
        self.__diet = diet

    def get_diet(self):
        return self.__diet

    def get_maintenance(self):
        return self.__maintenance

    def set_diet(self, diet):
        self.__diet = diet

    def set_maintenance(self, maintenance):
        self.__maintenance = maintenance


class Record:
    def __init__(self, record):
        self.__record = record

    def get_record(self):
        return self.__record

    def set_record(self, record):
        self.__record = record


# get all info with this class and store into database
