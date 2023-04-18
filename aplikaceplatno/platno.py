from tkinter import *
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import io

class main:
    def __init__(self,master):
        self.master = master
        self.barva_pera = 'black'
        self.barva_pozadi = 'white'
        self.stare_x = None
        self.stare_y = None
        self.sirka_pera = 30
        self.platno()
        self.c.bind('<B1-Motion>',self.malovat)
        self.c.bind('<ButtonRelease-1>',self.reset)

    def malovat(self,e):
        if self.stare_x and self.stare_y:
            self.c.create_line(self.stare_x,self.stare_y,e.x,e.y,width=self.sirka_pera,fill=self.barva_pera,capstyle=ROUND,smooth=False)
        self.stare_x = e.x
        self.stare_y = e.y

    def reset(self,e):
        self.stare_x = None
        self.stare_y = None

    def vymazat(self):
        self.c.delete(ALL)

    def vyhodnoceni(self):
        ps = self.c.postscript(colormode='color')
        jmeno_jpg = 'cislice.jpg'
        obraz = Image.open(io.BytesIO(ps.encode('utf-8')))
        obraz.save(jmeno_jpg)
        obraz = cv2.imread(jmeno_jpg,cv2.IMREAD_GRAYSCALE)
        obraz = cv2.resize(obraz, (28,28), interpolation = cv2.INTER_AREA)
        obraz = cv2.bitwise_not(obraz)
        
        vstup = obraz.reshape((784,1)) / 255
        self.test_samostatne(vstup, obraz)
        
    def test_samostatne(self, vstup, obraz):
        A3 = self.dopredna_propagace(vstup)
        odhad = self.odhady(A3)
        A3 = A3*100
        
        odhad = int(str(odhad).replace(' [', '').replace('[', '').replace(']', ''))
        jistota = A3[odhad]
        jistota = round(float(str(jistota).replace(' [', '').replace('[', '').replace(']', '')), 2)
        
        plt.title(f'Odhadnutá číslice: {odhad}')
        plt.gray()
        plt.imshow(obraz)
        plt.show()
        
    def ReLU(self, X, derivace = False):
        return np.maximum(0, X)

    def softmax(self, X):
        return np.exp(X) / sum(np.exp(X))

    def nacist_parametry(self):
        W1 = np.load(r'parametry-939\W1.npy')
        W2 = np.load(r'parametry-939\W2.npy')
        W3 = np.load(r'parametry-939\W3.npy')
        b1 = np.load(r'parametry-939\b1.npy')
        b2 = np.load(r'parametry-939\b2.npy')
        b3 = np.load(r'parametry-939\b3.npy')
        return W1, b1, W2, b2, W3, b3

    def dopredna_propagace(self, X):
        W1, b1, W2, b2, W3, b3 = self.nacist_parametry()
        Z1 = W1.dot(X) + b1
        A1 = self.ReLU(Z1)
        Z2 = W2.dot(A1) + b2
        A2 = self.ReLU(Z2)
        Z3 = W3.dot(A2) + b3
        A3 = self.softmax(Z3)
        return A3
    
    def odhady(self, A):
        odhady = np.argmax(A, axis=0)
        return odhady
        
    def platno(self):
        self.c = Canvas(self.master,width=400,height=400,bg=self.barva_pozadi,)
        self.c.pack(fill=BOTH,expand=True)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        menu.add_command(label='Konec',command=self.master.destroy)
        vyhodnotit_btn = Button(root, text ="VYHODNOTIT", command = self.vyhodnoceni)
        vyhodnotit_btn.pack(side=RIGHT, pady = 5, padx = 5)
        vymazat_btn = Button(root, text ="VYMAZAT", command = self.vymazat)
        vymazat_btn.pack(side=RIGHT, pady = 5, padx = 5)
        
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Zadejte číslici')
    root.minsize(400,440)
    root.maxsize(400,440)
    root.mainloop()
