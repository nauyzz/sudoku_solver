from tkinter import *
import tkinter.messagebox
import simple_traceback

class MyUI():

    def __init__(self):
        self.data = []
        self.e = []
        self.l = []
        self.root = Tk()
        self.points = []
        self.text = []
        for i in range(81):
            self.text.append(StringVar())
            self.text[i].set('0')

    def doit(self):
        self.data = []
        for i in range(81):
            if self.e[i].get() == '':
                self.data.append(0)
            else:
                self.data.append(int(self.e[i].get()))
        #print(self.data)
        flag = True
        for i in range(9):
            for j in range(1, 10):
                if self.data[i * 9: i * 9 + 9].count(j) > 1:
                    tkinter.messagebox.showwarning('warn', 'no answer')
                    flag = False
                    break
            if not flag:
                break

        for i in range(9):
            if not flag:
                break
            column = []
            for j in range(9):
                column.append(self.data[j * 9 + i])
            for k in range(1, 10):
                if not flag:
                    break
                if column.count(k) > 1:
                    tkinter.messagebox.showwarning('warn', 'no answer')
                    flag = False
                    break
            if not flag:
                break

        for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
            if not flag:
                break
            block = []
            block.append(self.data[i])
            block.append(self.data[i+1])
            block.append(self.data[i+2])
            block.append(self.data[i+9])
            block.append(self.data[i+10])
            block.append(self.data[i+11])
            block.append(self.data[i+18])
            block.append(self.data[i+19])
            block.append(self.data[i+20])
            for j in range(1, 10):
                if block.count(j) > 1:
                    tkinter.messagebox.showwarning('warn', 'no answer')
                    flag = False
                    break

        for i in self.data:
            if not flag:
                break
            if i > 9:
                tkinter.messagebox.showwarning('warn', 'no answer')
                flag = False
                break

        if flag:
            simple_traceback.points = simple_traceback.pointsinfo(self.data)
            point = simple_traceback.points.pop()
            try:
                # trying(point, sudoku)
                simple_traceback.trying(point, self.data)
            except Exception:
                # printsudoku(answer)
                #print('a')
                #print(simple_traceback.answer)
                for i in range(81):
                    self.text[i].set(simple_traceback.answer[i])
            else:
                tkinter.messagebox.showwarning('warn', 'no answer')

    def initUI(self):
    #    root = Tk()
        self.root.title("sudoku solver")
        self.root.geometry("800x400")
       # e = []
        for i in range(9):
            for j in range(9):
                en = Entry(self.root, width=4)
                en.place(x=j * 30, y=i * 20)
                self.e.append(en)

       # l = []
        for i in range(9):
            for j in range(9):
                la = Entry(self.root, width=4, textvariable=self.text[i*9+j])
                la.place(x=500 + j * 30, y=i * 20)
                self.l.append(la)

        btn = Button(self.root, text='do it', command=self.doit, width=10, height=1)
        btn.place(x=350, y=100)
        #self.root.mainloop()


if __name__ == '__main__':
    ui = MyUI()
    ui.initUI()
    ui.root.mainloop()