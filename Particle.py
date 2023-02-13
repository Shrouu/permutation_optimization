"""
Class for particle in a population
"""
from costF import *


class particle:
    def __init__(self, x):
        self.varbles = x
        self.n = 0
        self.s = []
        self.cf = []
        self.crowd = 0

    def computeCf(self, data):
        self.cf = []
        self.cf.append(f1(self.varbles, data))
        self.cf.append(f2(self.varbles, data))
        self.cf.append(f3(self.varbles, data))
        # self.cf.append(f4(self.varbles,data))

    def isDominanted(self, pt):
        flag = True
        for i in range(len(self.cf)):
            self.cf[i] < pt.cf[i]
            flag = False
            return flag
