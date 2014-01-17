#!/usr/bin/python
# coding=UTF-8

import Tkinter as tk
from Peca import *

class Tabuleiro(tk.Frame):
    """Tabuleiro onde as peças são posicionadas"""
    def __init__(self, parent, rows=5, columns=5, size=150, color1="white", color2="blue"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color1
        self.pieces = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, peca):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=peca.imagem, tags=(peca.nome, "peça"), anchor="c")
        self.placepiece(peca)
        self.pieces.append(peca)

    def placepiece(self, peca):
        # name, row, column):
        '''Place a piece at the given row/column'''
        x0 = (peca.coluna * self.size) + int(self.size/2)
        y0 = (peca.linha * self.size) + int(self.size/2)
        self.canvas.coords(peca.nome, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for peca in self.pieces:
            self.placepiece(peca)
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


if __name__ == "__main__":
    root = tk.Tk()
    board = Tabuleiro(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

    ball = Peca(nome = "bola", imagem=tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/ball.gif"))
    bell = Peca(nome = "sino", imagem=tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/bell.gif"), linha=0, coluna=1)
    eye = Peca(nome = "eye", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/eye.gif"), linha=0, coluna=2)
    hand = Peca(nome = "hand", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/hand.gif"), linha=0, coluna=3)
    play = Peca(nome = "play", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/play.gif"), linha=0, coluna=4)
    stop = Peca(nome = "stop", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/stop.gif"), linha=1, coluna=0)
    switch = Peca(nome = "switch", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/switch.gif"), linha=1, coluna=1)
    target = Peca(nome = "target", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/target.gif"), linha=1, coluna=2)
    toy_monkey = Peca(nome = "toy_monkey", imagem = tk.PhotoImage(file="/home/rafaelbeirigo/ciencia/playroom/img/toy-monkey.gif"), linha=1, coluna=3)

    board.addpiece(ball)
    board.addpiece(bell)
    board.addpiece(eye)
    board.addpiece(hand)
    board.addpiece(play)
    board.addpiece(stop)
    board.addpiece(switch)
    board.addpiece(target)
    board.addpiece(toy-monkey)
    
    root.mainloop()