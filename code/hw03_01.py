# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:07:19 2016

@author: LunaFire
"""

from thinkbayes import Suite

class Train(Suite):
     
     def Likelihood(self, data, hypo):
        if data in range(hypo[0], hypo[1] + 1):
            return 1.0 / (hypo[1] - hypo[0] + 1)
        else:
            return 0
            

suite = Train([(1, 1000), (50, 70), (80, 100), (2, 65)])
suite.Update(60)
suite.Print()