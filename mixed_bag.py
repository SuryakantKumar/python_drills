import random
import os


def unique(items):
    return set(items)


def shuffle(items):
    return random.shuffle(items)


def getcwd():
    return os.getcwd()


def mkdir(name):
    return os.mkdir(name)
