"""
Classe que representa a Borda

Esta classe faz parte da implementação da Busca em árvore.

Author: Rosalvo Neto
https://www.researchgate.net/profile/Rosalvo_Neto

"""

class Borda:
	
  elementos = []
  
  visitados = []

  def __init__(self, tipo):
    # tipo 0- em largura 1- profundidade 2- gulosa 3- A*
    self.tipo = tipo

  def inserir(self, item):
    id = item.estado.str_id()
    if not(id in self.visitados):
      self.elementos.append(item)
      self.visitados.append(id)
    
  def inserirTodos(self, L):
    for item in L:
      self.inserir(item)    

  def vazia(self):
    return (len(self.elementos)==0)

  def remover(self):        
    if self.tipo ==0:
      return self.elementos.pop(0)
    elif self.tipo ==1:
      return self.elementos.pop(-1)    
