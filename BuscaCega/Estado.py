"""
Classe que representa o Estado (Fotografia do ambiente para o Quebra cabeça de oito peças)

Esta classe faz parte da implementação da Busca em árvore.

Author: Rosalvo Neto
https://www.researchgate.net/profile/Rosalvo_Neto
"""

import numpy as np

class Estado:
    
    def __init__(self, l1, l2, l3):
        self.matrix = np.array([l1, l2, l3])
        
    def str_id(self):
        resultado = str(self.matrix[0, 0]) + str(self.matrix[0, 1]) + str(self.matrix[0, 2]) + str(self.matrix[1, 0]) + str(self.matrix[1, 1]) + str(self.matrix[1, 2]) + str(self.matrix[2, 0]) + str(self.matrix[2, 1]) + str(self.matrix[2, 2])
        return resultado
    
    def imprimir(self):
        for l in range(3):
            print("-"*10)
            line = ""
            for c in range(3):
                line = line + str(self.matrix[l, c]) + " | "
            print(line[:-2])
            
    def findZero(self):
        indices = np.where(self.matrix==0)
        l = indices[0][0]
        c = indices[1][0]
        return l, c
        
    def isObjetivo(self):    
        return (self.str_id() == '012345678')
    
    def sucessor(self):
        resultado = []
        
        l, c = self.findZero()

        if (l == 0) & (c==0):
            resultado = self.sucessor_00()
        elif (l == 0) & (c==1):
            resultado = self.sucessor_01()
        elif (l == 0) & (c==2):
            resultado = self.sucessor_02()
        elif (l == 1) & (c==0):
            resultado = self.sucessor_10()
        elif (l == 1) & (c==1):
            resultado = self.sucessor_11()
        elif (l == 1) & (c==2):
            resultado = self.sucessor_12()
        elif (l == 2) & (c==0):
            resultado = self.sucessor_20()
        elif (l == 2) & (c==1):
            resultado = self.sucessor_21()
        elif (l == 2) & (c==2):
            resultado = self.sucessor_22()
        else:
            raise NameError("Configuração não encontrada!")
        return resultado
    
    def sucessor_00(self):
        resultado = []
        # Mov 1
        l1 = [self.matrix[0, 1], self.matrix[0, 0], self.matrix[0, 2]]
        l2 = self.matrix[1, :]
        l3 = self.matrix[2, :]
        new_s1 = Estado(l1, l2, l3)
        resultado.append(new_s1)
        # Mov 2
        l1 = [self.matrix[1, 0]] + list(self.matrix[0, 1:])
        l2 = [self.matrix[0, 0]] + list(self.matrix[1, 1:])
        l3 = self.matrix[2, :]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)

        return resultado
    
    def sucessor_01(self):
        resultado = []
        # Mov 1
        l1 = [self.matrix[0, 0], self.matrix[1, 1]  ,self.matrix[0, 2]]
        l2 = [self.matrix[1, 0], self.matrix[0, 1]  ,self.matrix[1, 2]]
        l3 = self.matrix[2, :]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = [self.matrix[0, 1], self.matrix[0, 0], self.matrix[0, 2]]
        l2 = self.matrix[1, :]
        l3 = self.matrix[2, :]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)
        # Mov 3
        l1 = [self.matrix[0, 0], self.matrix[0, 2], self.matrix[0, 1]]
        l2 = self.matrix[1, :]
        l3 = self.matrix[2, :]
        new_s3 = Estado(l1, l2, l3)
        resultado.append(new_s3)
        
        return resultado
    
    def sucessor_02(self):
        resultado = []
        # Mov 1
        l1 = [self.matrix[0, 0], self.matrix[0, 2]  ,self.matrix[0, 1]]
        l2 = self.matrix[1, :]
        l3 = self.matrix[2, :]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = [self.matrix[0, 0], self.matrix[0, 1]  ,self.matrix[1, 2]]
        l2 = [self.matrix[1, 0], self.matrix[1, 1]  ,self.matrix[0, 2]]
        l3 = self.matrix[2, :]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)
        
        return resultado
        
    def sucessor_10(self):
        resultado = []
        # Mov 1
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 1], self.matrix[1, 0]  ,self.matrix[1, 2]]
        l3 = self.matrix[2, :]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = [self.matrix[2, 0], self.matrix[1, 1]  ,self.matrix[1, 2]]
        l3 = [self.matrix[1, 0], self.matrix[2, 1]  ,self.matrix[2, 2]]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)        
        # Mov 3
        l1 = [self.matrix[1, 0], self.matrix[0, 1], self.matrix[0, 2]]
        l2 = [self.matrix[0, 0], self.matrix[1, 1], self.matrix[1, 2]]
        l3 = self.matrix[2, :]
        new_s3 = Estado(l1, l2, l3)
        resultado.append(new_s3)

        return resultado    
    
    def sucessor_11(self):
        resultado = []
        # Mov 1
        l1 = [self.matrix[0, 0], self.matrix[1, 1]  ,self.matrix[0, 2]]
        l2 = [self.matrix[1, 0], self.matrix[0, 1]  ,self.matrix[1, 2]]
        l3 = self.matrix[2, :]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[1, 2]  ,self.matrix[1, 1]]
        l3 = self.matrix[2, :]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)        
        # Mov 3
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[2, 1], self.matrix[1, 2]]
        l3 = [self.matrix[2, 0], self.matrix[1, 1], self.matrix[2, 2]]        
        new_s3 = Estado(l1, l2, l3)
        resultado.append(new_s3)        
        # Mov 4
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 1], self.matrix[1, 0], self.matrix[1, 2]]
        l3 = self.matrix[2, :]        
        new_s4 = Estado(l1, l2, l3)
        resultado.append(new_s4)

        return resultado
    
    def sucessor_12(self):
        resultado = []
        # Mov 1
        l1 = [self.matrix[0, 0], self.matrix[0, 1]  ,self.matrix[1, 2]]
        l2 = [self.matrix[1, 0], self.matrix[1, 1]  ,self.matrix[0, 2]]
        l3 = self.matrix[2, :]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[1, 1]  ,self.matrix[2, 2]]
        l3 = [self.matrix[2, 0], self.matrix[2, 1]  ,self.matrix[1, 2]]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)        
        # Mov 3
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[1, 2], self.matrix[1, 1]]
        l3 = self.matrix[2, :]
        new_s3 = Estado(l1, l2, l3)
        resultado.append(new_s3)        

        return resultado
    
    def sucessor_20(self):
        resultado = []
        # Mov 1
        l1 = self.matrix[0, :]
        l2 = [self.matrix[2, 0], self.matrix[1, 1]  ,self.matrix[1, 2]]
        l3 = [self.matrix[1, 0], self.matrix[2, 1]  ,self.matrix[2, 2]]        
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = self.matrix[1, :]
        l3 = [self.matrix[2, 1], self.matrix[2, 0]  ,self.matrix[2, 2]]        
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)                

        return resultado    
    
    def sucessor_21(self):
        resultado = []
        
        # Mov 1
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[2, 1]  ,self.matrix[1, 2]]
        l3 = [self.matrix[2, 0], self.matrix[1, 1]  ,self.matrix[2, 2]]
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = self.matrix[1, :]
        l3 = [self.matrix[2, 0], self.matrix[2, 2]  ,self.matrix[2, 1]]
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)                
        # Mov 3
        l1 = self.matrix[0, :]
        l2 = self.matrix[1, :]
        l3 = [self.matrix[2, 1], self.matrix[2, 0]  ,self.matrix[2, 2]]
        new_s3 = Estado(l1, l2, l3)
        resultado.append(new_s3) 
        
        return resultado    
    
    def sucessor_22(self):
        resultado = []
        # Mov 1
        l1 = self.matrix[0, :]
        l2 = [self.matrix[1, 0], self.matrix[1, 1]  ,self.matrix[2, 2]]
        l3 = [self.matrix[2, 0], self.matrix[2, 1]  ,self.matrix[1, 2]]        
        new_self = Estado(l1, l2, l3)
        resultado.append(new_self)
        # Mov 2
        l1 = self.matrix[0, :]
        l2 = self.matrix[1, :]
        l3 = [self.matrix[2, 0], self.matrix[2, 2], self.matrix[2, 1]]        
        new_s2 = Estado(l1, l2, l3)
        resultado.append(new_s2)                
                
        return resultado
