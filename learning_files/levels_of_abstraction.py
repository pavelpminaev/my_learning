"""Конструктор make — принимает на вход числитель и знаменатель, возвращает дробь.
Селектор get_numer — возвращает числитель
Селектор get_denom — возвращает знаменатель
Сложение add — складывает переданные дроби
Вычитание sub — находит разность между двумя дробя"""

import math

def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
    "numer" : int(numer / gcd),
    "denom" : int(denom / gcd)
    }

def get_numer(rational):
    return rational['numer']

def get_denom(rational):
    return rational['denom']

def add(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )


rat1 = make(4, 3)
rat2 = make(3, 6)

print(add(rat1, rat2))

