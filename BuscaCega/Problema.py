"""
Classe que representa a abstração do Problema (Quebra cabeça de oito peças)

Esta classe faz parte da implementação da Busca em árvore.

Author: Rosalvo Neto
https://www.researchgate.net/profile/Rosalvo_Neto
"""

from Estado import Estado
from No import No
import random as rnd

class Problema:
    
    def get_inicio_aleatorio(self):
        l = list(range(9))
        rnd.shuffle(l)
        L1 = l[:3]
        L2 = l[3:6]
        L3 = l[6:]
        s = Estado(L1, L2, L3)
        no = No(s, None, 0)
        return no
    
    def get_inicio(self, l1, l2, l3):
        s = Estado(l1, l2, l3)
        no = No(s, None, 0)
        return no
