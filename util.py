import random


def sayHello():
    print("Hello!")


def genRandomIntList(length: int) -> list[int]:
    return random.sample(range(50), length)
