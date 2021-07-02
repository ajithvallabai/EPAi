import random
from decimal import *


class Qualean:
    def __init__(self, num=random.choice([1, 0, -1])):
        if num not in [-1, 0, 1]:
            raise ValueError("Please enter one of value [-1,0,1]")
        self.org_num = num
        self.number = round(random.uniform(-1, 1) * self.org_num, 10)
        self.return_qualean = self.__qnumber__

    def __call__(self):
        return self.number

    def __qnumber__(self):
        return self.number

    def __and__(self, q2):
        return bool(self.number and q2)

    def __or__(self, q2):
        if q2 == None:
            return True
        return bool(self.number or q2)

    def __add__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() + q2
        return self.return_qualean() + q2.return_qualean()

    def __mul__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() * q2
        return self.return_qualean() * q2.return_qualean()

    def __bool__(self):
        return bool(self.return_qualean())

    def __float__(self):
        return float(self.return_qualean())

    def __invertsign__(self):
        return -1 * (self.return_qualean())

    def __sqrt__(self):
        if self.return_qualean() < 0:
            return str(round(Decimal(self.__invertsign__()).sqrt(), 10)) + 'i'
        else:
            return round(Decimal(self.return_qualean()).sqrt(), 10)

    def __ge__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() >= q2
        return self.return_qualean() >= q2.return_qualean()

    def __gt__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() > q2
        return self.return_qualean() > q2.return_qualean()

    def __le__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() <= q2
        return self.return_qualean() <= q2.return_qualean()

    def __lt__(self, q2):
        if not isinstance(q2, Qualean):
            return self.return_qualean() < q2
        return self.return_qualean() < q2.return_qualean()

    def __eq__(self, q2):
        if isinstance(q2, str):
            raise TypeError
        if not isinstance(q2, Qualean):
            return self.return_qualean() == q2
        return self.return_qualean() == q2.return_qualean()

    def __repr__(self):
        return 'Qualean Class Instance'

    def __str__(self):
        return str(self.return_qualean())