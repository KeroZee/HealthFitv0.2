class Condition:
    def __init__(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition

    def set_condition(self, condition):
        self.condition = condition


    def __str__(self):
        s = f'{self.get_condition()}'
        return s

class Recommend(Condition):
    def __init__(self, condition, recommend):
        super().__init__(condition)
        self.recommend = recommend

    def get_recommend(self):
        return self.recommend

    def set_recommend(self, recommend):
        self.recommend = recommend

    def __str__(self):
        s = super().__str__()
        s = f'{self.get_recommend()}'
        return s


