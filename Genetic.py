import numpy as np
import random
from Particle import *


class genetic:
    def __init__(self, variblesize, data):
        self.variblesize = variblesize
        self.data = data
        self.popsize = 1000
        self.pop = []
        self.randseed = 50
        self.gen = 0

    def popInit(self):
        random.seed(self.randseed)
        for i in range(self.popsize):
            x = np.arange(self.variblesize)
            np.random.shuffle(x)
            pt = particle(x)
            pt.computeCf(self.data)
            self.pop.append(pt)

    def popDominatSort(self):
        for i in range(self.popsize):
            for j in range(i + 1, self.popsize):
                if self.pop[i].isDominanted(self.pop[j]):
                    self.pop[i].n += 1
        self.pop.sort(key=lambda x: x.n)
        a = 1

    def computepop(self):
        pass
