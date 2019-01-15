class Ren:
    def __init__(self, name ,job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Ren):
    def giveRaise(self, percent, bonus = 0.10):
        Ren.giveRaise(self, percent + bonus)


if __name__ == '__main__':

    Yang = Ren('Yang', 'Dev', 8000)
    Zhang = Ren('Zhang')

    print(Yang.name, Yang.pay)
    print(Zhang.name, Zhang.pay)

    Huang = Manager('Huang', 'mgr', 5000)
    Huang.giveRaise(0.2)
    print(Huang.name, Huang.pay)