# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:46:14 2016

@author: LunaFire
"""

from thinkbayes import Suite

class Bowl(object):   
    def __init__(self, num1, num2):
        self.mixes = {}
        self.mixes['vanilla'] = num1
        self.mixes['chocolate'] = num2
        
    def GetProb(self, kind):
        prob = 1.0 * self.mixes[kind] / (self.mixes['vanilla'] + self.mixes['chocolate'])
        if self.mixes[kind] > 0:
            self.mixes[kind] -= 1
        return prob
            
class Cookie(Suite):
    
    hypotheses = dict(B1=Bowl(75,25), B2=Bowl(50,50))
            
    def Likelihood(self, data, hypo):
        prob = 1.0
        for d in data:
            prob *= self.hypotheses[hypo].GetProb(d)
        return prob
        

pmf = Cookie(['B1', 'B2'])
pmf.Update(['vanilla', 'vanilla', 'vanilla', 'vanilla'])
pmf.Print()
