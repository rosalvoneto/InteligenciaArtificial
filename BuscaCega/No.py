"""
Classe que representa a estrutura de dados de um No em uma árvore

Esta classe faz parte da implementação da Busca em árvore.

Author: Rosalvo Neto
https://www.researchgate.net/profile/Rosalvo_Neto
"""

class No:
    
    def __init__(self, state, NoPai, custo):
        self.estado = state
        self.NoPai  = NoPai
        self.custo  = custo
    
    def teste_objetivo(self):
        return self.estado.isObjetivo()
        
        
    def get_sucessores(self):
    	resultado = []
    	l_estados = self.estado.sucessor()
    	for s in l_estados:
    		no = No(s, self, 1)
    		resultado.append(no)
    	return resultado 
