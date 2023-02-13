import numpy as np
import random
from Particle import *


class genetic:
    def __init__(self, variblesize, data):
        self.variblesize = variblesize
        self.data = data
        self.popsize = 400
        self.pop = []
        self.newgen = []
        self.maxcf = [-1, -1, -1]
        self.mincf = [10, 10, 10]
        self.randseed = 50
        self.mutationProbability = 0.5
        self.gen = 0
        self.bestGeneration = []

    def popInit(self):
        random.seed(self.randseed)
        for i in range(self.popsize):
            x = np.arange(self.variblesize)
            np.random.shuffle(x)
            pt = particle(x)
            self.pop.append(pt)

    def normalizecf(self):
        fcount = len(self.pop[0].cf)
        for i in range(fcount):
            for pt in self.pop:
                self.maxcf[i] = max(self.maxcf[i], pt.cf[i])
                self.mincf[i] = min(self.mincf[i], pt.cf[i])
            d = self.maxcf[i] - self.mincf[i]
            for j in range(self.popsize):
                self.pop[j].cf[i] = (self.pop[j].cf[i] - self.mincf[i]) / d

    def computeCostfunction(self):
        for particle in self.pop:
            particle.computeCf(self.data)
        self.normalizecf()

    # def newGenNormalizecf(self):
    #     fcount = len(self.newgen[0].cf)
    #     for i in range(fcount):
    #         for pt in self.newgen:
    #             self.maxcf[i] = max(self.maxcf[i], pt.cf[i])
    #             self.mincf[i] = min(self.mincf[i], pt.cf[i])
    #         d = self.maxcf[i] - self.mincf[i]
    #         for j in range(self.popsize):
    #             self.pop[j].cf[i] = (self.pop[j].cf[i] - self.mincf[i]) / d

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
            self.crossOpe(self.pop[parent1[i]].varbles, self.pop[parent2[i]].varbles)
            self.crossOpe(
                self.pop[parent2[i + 25]].varbles, self.pop[parent3[i]].varbles
            )
        for particle in self.newgen:
            particle.varbles = self.mutation(particle.varbles)
        self.pop = self.pop[0:parentsize] + self.newgen

    def crossOpe(self, pt1, pt2):
        l = len(pt1)
        start1 = random.randint(0, l - 1)
        end1 = random.randint(start1 + 1, l)
        start2 = random.randint(0, l - 1)
        end2 = random.randint(start2 + 1, l)
        factor1 = pt1[start1:end1]
        factor2 = pt2[start2:end2]
        flag1 = np.ones(l, dtype=int)
        flag2 = np.ones(l, dtype=int)
        flag1[factor1] = 0
        flag2[factor2] = 0
        remain1 = []
        remain2 = []
        for i in range(end2, l):
            if flag1[pt2[i]] == 1:
                remain1.append(pt2[i])
        for i in range(end2):
            if flag1[pt2[i]] == 1:
                remain1.append(pt2[i])
        for i in range(end1, l):
            if flag2[pt1[i]] == 1:
                remain2.append(pt1[i])
        for i in range(end1):
            if flag2[pt1[i]] == 1:
                remain2.append(pt1[i])

        remain1 = np.array(remain1)
        remain2 = np.array(remain2)
        child1 = np.concatenate([remain1[l - end1 :], factor1, remain1[0 : l - end1]])
        child2 = np.concatenate([remain2[l - end2 :], factor2, remain2[0 : l - end2]])
        self.newgen.append(particle(child1))
        self.newgen.append(particle(child2))

    def mutation(self, sequence):
        sequenceLength = len(sequence)
        ismutation = random.random()
        if ismutation < self.mutationProbability:
            mutationPointA = random.randint(0, sequenceLength - 1)
            mutationPointB = random.randint(0, sequenceLength - 1)
            while mutationPointA == mutationPointB:
                mutationPointB = random.randint(0, sequenceLength - 1)
            sequence[mutationPointA], sequence[mutationPointB] = (
                sequence[mutationPointB],
                sequence[mutationPointA],
            )
            return sequence
        return sequence

    def evalution(self, endGeneration):
        self.gen = 0
        self.popInit()
        while self.gen < endGeneration:
            self.computeCostfunction()
            self.popDominatSort()
            self.popDistense()
            self.generateNewpop()
            self.gen += 1
            print("Processing genetation " + str(self.gen) + "...")
            print("Maxcf: " + str(self.maxcf) + "Mincf: " + str(self.mincf))
