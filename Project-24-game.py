'''Project  MARK-II'''
import sys
from Tkinter import *
import tkMessageBox
lv1 = [['1', '2', '3', '4'], ['4', '4', '4', '4'], ['2', '2', '3', '3'], ['5', '5', '5', '5'], ['1', '2', '3', '9']]
lv2 = [['2', '1', '7', '7'], ['1', '1', '8', '1'], ['2', '7', '7', '1'], ['3', '6', '1', '4'], ['5', '6', '4', '1']]
lv3 = [['3', '3', '6', '6'], ['3', '3', '5', '5'], ['3', '3', '7', '7'], ['3', '3', '8', '8'], ['3', '3', '3', '3']]
lv4 = [['4', '4', '4', '5'], ['4', '5', '5', '7'], ['4', '5', '5', '8'], ['4', '5', '9', '9'], ['4', '7', '7', '7']]    
lv5 = [['5', '5', '8', '8'], ['5', '5', '9', '9'], ['5', '6', '6', '6'], ['5', '6', '7', '7'], ['9', '8', '5', '2']]
lv6 = [['1', '3', '6', '9'], ['2', '8', '8', '9'], ['7', '8', '3', '5'], ['1', '6', '2', '1'], ['4', '9', '5', '7']]
lv7 = [['8', '8', '5', '4'], ['7', '1', '2', '7'], ['1', '1', '8', '5'], ['5', '6', '2', '4'], ['6', '5', '3', '4']]
lv8 = [['8', '2', '7', '8'], ['2', '2', '6', '9'], ['9', '7', '3', '3'], ['7', '8', '2', '4'], ['7', '6', '3', '6']]
lv9 = [['1', '7', '9', '2'], ['9', '8', '6', '2'], ['5', '5', '5', '1'], ['1', '3', '4', '6'], ['5', '4', '2', '6']]
lv10 = [['9', '8', '5', '4'], ['6', '3', '1', '3'], ['6', '7', '4', '3'], ['8', '8', '8', '3'], ['7', '5', '2', '4']]
lis = [lv1, lv2, lv3, lv4, lv5, lv6, lv7, lv8, lv9, lv10]
check = ['+', '-', '*', '/', '(', ')']
class menuinterface(object):
    '''main method'''
    def __init__(self):
        '''
        menu interface
        '''
        self.root = Tk()
        self.root.geometry('450x450+200+200')
        self.root.config(bg = 'black')
        self.root.title('GAME-24-FOR-FUN')
        #--Button and Label--
        mlabel = Label(self.root,text = 'GAME-24-FOR-FUN', fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 45, y = 50)
        self.button = Button(self.root, text = 'Play', command = lambda:self.root.destroy()&self.game24(0, 0, 0),bg = 'white', fg = 'black', font = ('purisa', 20)).place(x = 185, y = 200)
        self.button = Button(self.root, text = 'Quit', command = self.quit24,bg = 'white', fg = 'black', font = ('purisa', 12)).place(x = 400, y = 400)
        #--menubar--
        menubar = Menu(self.root)
        filemenu = Menu(menubar,tearoff = 0)
        filemenu.add_command(label = 'Play', command = lambda:self.root.destroy()&self.game24(0, 0, 0))
        menubar.add_cascade(label = 'Game',menu = filemenu)
        helpmenu = Menu(menubar,tearoff = 0)
        helpmenu.add_command(label = 'About us', command = self.aboutus)
        helpmenu.add_command(label = 'How to play', command = self.howtoplay)
        helpmenu.add_command(label = 'Credit',command = self.credit)
        menubar.add_cascade(label = 'Help',menu = helpmenu)
        self.root.config(menu = menubar)
        self.root.mainloop()
    def game24(self, j, lv,lv_game):
        '''
        game interface
        '''
        self.game = Tk()
        self.game.geometry('450x450+200+200')
        self.game.config(bg = 'black')
        self.game.title('GAME-24-FOR-FUN')
        #--menubar--
        menubar = Menu(self.game)
        filemenu = Menu(menubar,tearoff = 0)
        filemenu.add_command(label = 'Menu', command = lambda:self.game.destroy()&self.__init__())
        menubar.add_cascade(label = 'Game',menu = filemenu)
        helpmenu = Menu(menubar,tearoff = 0)
        helpmenu.add_command(label = 'About us', command = self.aboutus)
        helpmenu.add_command(label = 'How to play', command = self.howtoplay)
        helpmenu.add_command(label = 'Credit',command = self.credit)
        menubar.add_cascade(label = 'Help',menu = helpmenu)
        display = StringVar()
        mlabel = Label(self.game,text = 'LV.'+str(lv_game) , fg = 'white', font = ('purisa', 12),bg = 'black').place(x = 10, y = 10)
        mlabel = Label(self.game,text = (lis[lv][j][0], lis[lv][j][1], lis[lv][j][2], lis[lv][j][3]) , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 155, y = 50)
        gentry = Entry(self.game,textvariable = display).place(x = 160, y = 150)
        gbutton = Button(self.game,text = 'OK', command = lambda:self.calculate(display.get(), j, lv,lv_game), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 205, y = 200)
        self.game.config(menu = menubar)
        self.game.mainloop()     
    def quit24(self):
        '''
        quiet function
        '''
        self.root.destroy()
    #--MessageBox--
    def howtoplay(self):
        '''
        how to play message
        '''
        tkMessageBox.showinfo(title='How to play',message='1.There are only four numbers.\n'
+                              '2.Think of the factors of 24: 1x24, 2x12, 3x8, and 4x6. Try to make factors if it is what you are can do with your numbers.\n'
+                              '3.Make factors with the four numbers shown in the first step.\n'
+                              '4.Solve the problem. 2x4=8, now when you have used 2 and 4, you may not use them again. \n'
+                              'Now multiply your numbers together. 8x3=24. You may not repeat ANY numbers. You may only use each number once.\n')
        return
    def aboutus(self):
        '''
        about this project message
        '''
        tkMessageBox.showinfo(title='About us',message='This is project by freshy college IT@KMITL')
        return
    def credit(self):
        '''
        credit message
        '''
        tkMessageBox.showinfo(title='CREDIT',message='\n MR.Phossawat Pruekphanasant IT57070077 Sec2 \n MR.Apchai Tuntasirin IT57070142 Sec3')
        return
    def calculate(self,display, j, lv,lv_game):
        '''
        calculate the entry of input and check it equal 24 or not
        '''
        ans = str(display)
        lis_ans = []
        num_check = 0
        for k in display:
            if k not in lis[lv][j]:
                if k not in check:
                    self.cannot(j, lv, lv_game,k)
            elif k in lis[lv][j]:
                k = str(float(k))
                num_check += 1
            lis_ans.append(k)
            if k not in check:
                if lis_ans.count(k) > lis[lv][j].count(k[0]):
                    self.counterror(j, lv, lv_game,k)
        if num_check != 4:
            self.numerror(j, lv, lv_game,k)
        ans = eval(str(''.join(lis_ans)))
        if ans == 24:
            j += 1
            lv_game += 1
            if j == 5:
                j = 0
                lv += 1
            if lv == 50:
                self.win_game(j, lv, lv_game)
            else:
                self.win_f(j, lv, lv_game)
        else:
            self.lose(j, lv, lv_game)
    def win_f(self, j, lv, lv_game):
        '''
        game win display
        '''
        self.game.destroy()
        self.win = Tk()
        self.win.geometry('450x450+200+200')
        self.win.config(bg = 'black')
        self.win.title('GAME-24-FOR-FUN')
        mlabel = Label(self.win,text = 'CORRECT' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 120, y = 50)
        mlabel = Label(self.win,text = 'You LV.'+str(lv_game) , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 130, y = 100) 
        gbutton = Button(self.win,text = 'NEXT', command = lambda:self.win.destroy()&self.game24(j, lv,lv_game), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.win.mainloop()
    def win_game(self, j, lv, lv_game):
        '''
        player clear the game
        '''
        self.game.destroy()
        self.wing = Tk()
        self.wing.geometry('450x450+200+200')
        self.wing.config(bg = 'black')
        self.wing.title('GAME-24-FOR-FUN')
        mlabel = Label(self.wing,text = 'YOU WIN' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 115, y = 50)
        mlabel = Label(self.wing,text = 'You LV.'+str(lv_game) , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 130, y = 100)
        gbutton = Button(self.wing,text = 'Menu', command = lambda:self.wing.destroy()&self.__init__(), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.wing.mainloop()
    def lose(self, j, lv, lv_game):
        '''
        game lose display
        '''
        self.game.destroy()
        self.lose = Tk()
        self.lose.geometry('450x450+200+200')
        self.lose.config(bg = 'black')
        self.lose.title('GAME-24-FOR-FUN')
        mlabel = Label(self.lose,text = 'GAME OVER' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 110, y = 50)
        mlabel = Label(self.lose,text = 'You LV.'+str(lv_game) , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 130, y = 100)
        gbutton = Button(self.lose,text = 'Menu', command = lambda:self.lose.destroy()&self.__init__(), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.lose.mainloop()
    def cannot(self, j, lv, lv_game,k):
        '''
        error cannot use some thing that player input
        '''
        self.game.destroy()
        self.cannot_gui = Tk()
        self.cannot_gui.geometry('450x450+200+200')
        self.cannot_gui.config(bg = 'black')
        self.cannot_gui.title('GAME-24-FOR-FUN')
        mlabel = Label(self.cannot_gui,text = 'ERROR' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 140, y = 50)
        mlabel = Label(self.cannot_gui,text = 'Cannot use '+str(k) , fg = 'white', font = ('purisa', 20),bg = 'black').place(x = 120, y = 100)
        gbutton = Button(self.cannot_gui,text = 'Try Again', command = lambda:self.cannot_gui.destroy()&self.game24(j, lv, lv_game), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.cannot_gui.mainloop()
    def counterror(self, j, lv, lv_game,k):
        '''
        error count if player write some number more than quize have
        '''
        self.game.destroy()
        self.counterror_gui = Tk()
        self.counterror_gui.geometry('450x450+200+200')
        self.counterror_gui.config(bg = 'black')
        self.counterror_gui.title('GAME-24-FOR-FUN')
        mlabel = Label(self.counterror_gui,text = 'ERROR' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 140, y = 50)
        mlabel = Label(self.counterror_gui,text = 'You use '+str(k)+' over the limit' , fg = 'white', font = ('purisa', 20),bg = 'black').place(x = 90, y = 100)
        gbutton = Button(self.counterror_gui,text = 'Try Again', command = lambda:self.counterror_gui.destroy()&self.game24(j, lv, lv_game), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.counterror_gui.mainloop()
    def numerror(self, j, lv, lv_game,k):
        '''
        error player use number less than 4
        '''
        self.game.destroy()
        self.num = Tk()
        self.num.geometry('450x450+200+200')
        self.num.config(bg = 'black')
        self.num.title('GAME-24-FOR-FUN')
        mlabel = Label(self.num,text = 'ERROR' , fg = 'white', font = ('purisa', 30),bg = 'black').place(x = 140, y = 50)
        mlabel = Label(self.num,text = 'You use incomplete number' , fg = 'white', font = ('purisa', 20),bg = 'black').place(x = 70, y = 100)
        gbutton = Button(self.num,text = 'Try Again', command = lambda:self.num.destroy()&self.game24(j, lv, lv_game), font = ('purisa', 10), bg = 'white', fg = 'black').place(x = 195, y = 200)
        self.num.mainloop()
menuinterface()
