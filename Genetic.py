import numpy as np
import random
from Particle import *


class genetic:
    def __init__(self, variblesize, data):
        self.variblesize = variblesize
        self.data = data
        self.popsize = 200
        self.pop = []
        self.newgen = []
        self.maxcf = []
        self.mincf = []
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
        self.normalizecf()

    def normalizecf(self):
        fcount = len(self.pop[0].cf)
        for i in range(fcount):
            self.maxcf.append(self.pop[0].cf[i])
            self.mincf.append(self.pop[0].cf[i])
            for pt in self.pop:
                self.maxcf[i] = max(self.maxcf[i], pt.cf[i])
                self.mincf[i] = min(self.mincf[i], pt.cf[i])
            d = self.maxcf[i] - self.mincf[i]
            for j in range(self.popsize):
                self.pop[j].cf[i] = (self.pop[j].cf[i] - self.mincf[i]) / d

    def popDominatSort(self):
        for i in range(self.popsize):
            for j in range(i + 1, self.popsize):
                if self.pop[i].isDominanted(self.pop[j]):
                    self.pop[i].n += 1
        self.pop.sort(key=lambda x: x.n)

    def popDistense(self):
        n = [0]
        fcount = len(self.pop[0].cf)
        for i in range(self.popsize - 1):
            if self.pop[i].n != self.pop[i + 1].n:
                n.append(i + 1)
        n.append(self.popsize)

        for i in range(fcount):
            for j in range(len(n) - 1):
                if n[j + 1] - n[j] - 1 >= 3:
                    self.pop[n[j] : n[j + 1]] = sorted(
                        self.pop[n[j] : n[j + 1]], key=lambda x: x.cf[i]
                    )
                    for k in range(n[j], n[j + 1] - 1):
                        self.pop[k].crowd += self.pop[k + 1].cf[i] - self.pop[k].cf[i]
                    self.pop[n[j + 1] - 1].crowd = self.pop[n[j + 1] - 2].crowd
        for j in range(len(n) - 1):
            if n[j + 1] - n[j] - 1 >= 3:
                self.pop[n[j] : n[j + 1]] = reversed(
                    sorted(self.pop[n[j] : n[j + 1]], key=lambda x: x.crowd)
                )

    def generateNewpop(self):
        self.newgen = []
        parentsize = int(self.popsize * 0.5)
        div = int(parentsize * 0.5)
        parent1 = list(range(div))
        parent2 = list(range(div, div * 3))
        parent3 = list(range(div * 3, div * 4))
        random.shuffle(parent1)
        random.shuffle(parent2)
        random.shuffle(parent3)
        for i in range(div):
            pass

    def crossOpe(self, pt1, pt2):
        pass
