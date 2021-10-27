# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:22:54 2021

@author: 33781
"""


import random
import math

f=open(r'C:\Users\33781\Desktop\A3\A3 s6\DatA IA\algoG\temperature_sample.csv','r')
tabIT=[]
for ligne in f:
    ligne=ligne.replace('\n','')
    tabIT.append(ligne.split(';'))
del tabIT[0]
f.close()

class individu:
    def __init__(self,a=None,b=None,c=None):
        if b==None:
            self.b=random.randint(1,20)
        if c==None:
            self.c=random.randint(1,20)
        if a==None:
            self.a=round(random.random(),5)
        self.valsExp=tabIT
        self.valsTH=self.temptheorique
        self.qualite=self.fitness     
    def __str__(self):
        retour= "Votre individu est composé de " + str(self.a)+", " + str(self.b) +", "+ str(self.c) +", respectivement a b et c." 
        return retour
    def calcultemperature(self,i):
        temp=0.0
        for n in range(self.c+1):
            temp+=(self.a**float(n))*math.cos(float((self.b**n))*math.pi*float(i))
        return temp
    def temptheorique(self):
        tabtemp=[]
        for i in self.valsExp:
            tabtemp.append(self.calcultemperature(i[0]))
        return tabtemp
    def fitness(self):
        q=0.0        
        a=self.valsTH()
        b=self.valsExp
        for f, o in zip(a,b):
            q+= abs(f-float(o[1]))
        return q    
    
def create_rand_pop(count):
    lindiv=[]
    for i in range(count+1):
        lindiv.append(individu())        
    return lindiv

def evaluation(popindiv):
    popindiv = sorted(popindiv, key=lambda p: p.qualite())     
    return popindiv

def selection(pop, hcount, lcount):
    prem= pop[:hcount]
    prem +=pop[len(pop)-lcount:]
    return prem

def croisement(ind1,ind2):
    a=ind1.c
    b=ind2.c
    ind1.c=b
    ind2.c=a
    return (ind1,ind2) #tuple liste?
    
def mutation(ind):
    a=random.randint(1,3)
    if a==1:
        ind.a = round(random.random(),5)
    elif a==2:
        ind.b=random.randint(1,20)
    else:
        ind.c=random.randint(1,20)
    return ind        
                
def algoLoop(taillepop,iterationlim):
    popu =[]
    popu = create_rand_pop(taillepop)
    solutiontrouv= False
    nbiteration=0
    while not solutiontrouv and nbiteration<= iterationlim:
        print('iteration numéro : ', nbiteration )
        nbiteration +=1
        evalu = evaluation(popu)
        if evalu[0].qualite() == 0:
            solutiontrouv=True
        else:
            select = selection(evalu,10,4)
            croise=[]
            for i in range(0,len(select),2):
                croise+=croisement(select[i],select[i+1]) #tuple liste?
            mutes=[]
            for i in select:
                mutes.append(mutation(i))
            newalea= create_rand_pop(5)
            pop=select[:]+croise[:]+mutes[:]+newalea[:]
        print(evalu[0])
                
def algoLoop2(taillepop,iterationlim):
    popu =[]
    popu = create_rand_pop(taillepop)
    solutiontrouv= False
    nbiteration=0
    while not solutiontrouv and nbiteration<= iterationlim:
        print('iteration numéro : ', nbiteration )
        nbiteration +=1
        evalu = evaluation(popu)
        if evalu[0].qualite() == 0:
            solutiontrouv=True
        else:
            select = selection(evalu,10,4)
            croise=[]
            for i in range(0,len(select),2):
                croise+=croisement(select[i],select[i+1]) #tuple liste?
            mutes=[]
            for i in select:
                mutes.append(mutation(i))
            newalea= create_rand_pop(5)
            pop=select[:]+croise[:]+mutes[:]+newalea[:]
        print(evalu[0])



algoLoop(15,1000)