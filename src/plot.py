'''
Created on 12 de nov de 2017

@author: Israël & Renan
'''
from tkinter import *
class Plot:
  def __init__(self,edges,pos):
    self.pos=[]
    self.pos=pos
    self.edges=[]
    self.edges=edges
  def plot(self,title):
    master=Tk()
    widget1 = Frame(master,width=600,height=500)
    widget1.pack()
    canvas=Canvas(widget1,width=500,height=500)
    canvas.pack(side=RIGHT)
    for p in self.edges:
      #criando linhas
      canvas.create_line(self.pos[p[0]][0],self.pos[p[0]][1],self.pos[p[1]][0],self.pos[p[1]][1])
      #primeiro vértice do par
      canvas.create_oval(self.pos[p[0]][0]-10,self.pos[p[0]][1]-10,self.pos[p[0]][0]+10,self.pos[p[0]][1]+10,fill="red")
      canvas.create_text(self.pos[p[0]][0],self.pos[p[0]][1],text=p[0],fill="yellow")
      #segundo vértice do par
      canvas.create_oval(self.pos[p[1]][0]-10,self.pos[p[1]][1]-10,self.pos[p[1]][0]+10,self.pos[p[1]][1]+10,fill="red")
      canvas.create_text(self.pos[p[1]][0],self.pos[p[1]][1],text=p[1],fill="yellow")
    master.title(title)
    master.mainloop()