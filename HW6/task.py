class NumbersList:
    def __init__(self, frist: [int | float], second: [int | float]):
        self.frist = frist
        self.second = second

    def get_list(self) -> [float | float]:
        average1 = 0
        if self.frist:
            average1 = sum(self.frist) / len(self.frist)

        average2 = 0
        if self.second:
            average2 = sum(self.second) / len(self.second)

        return average1, average2

    def list_comparison(self):
        average1, average2 = self.get_list()
        if average1 > average2:
            print('Cписок 1 среднее значение больше')
        if average1 < average2:
            print('Cписок 2 среднее значение больше')
        else:
            print("Списки равное среднее значение")
