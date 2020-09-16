from tkinter import *

class testOverlap(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root


        self.topButtons()

        self.pageOne()
        self.pageTwo()
        self.pageThree()

    def topButtons(self):

        self.firstPage = Button(self.root, text="Go to Page 1", background="WHITE", height = 2, width = 16, command= self.pageOne())
        self.firstPage.place(x=0, y=0)

        self.secondPage = Button(self.root, text="Go to Page 2", background="WHITE",height = 2, width = 16, command= self.pageTwo())
        self.secondPage.place(x=121, y=0)

        self.thirdPage = Button(self.root, text="Go to Page 3", background="WHITE",height = 2, width = 17, command= self.pageThree())
        self.thirdPage.place(x=242, y=0)

#class mainPage(Frame):
    def pageOne(self):
        self.Label1 = Label(self.root, text=" First Page ", height = 20, width = 52, background="Green")
        self.Label1.place(x=0, y=40)

#class middlePage(Frame):
    def pageTwo(self):
        self.Label2 = Label(self.root, text=" Second Page ", height = 20, width = 52, background="Blue")
        self.Label2.place(x=0, y=40)

#class finalPage(Frame):
    def pageThree(self):
        self.Label3 = Label(self.root, text=" Third Page ", height = 20, width = 52, background="Red")
        self.Label3.place(x=0, y=40)

def main():
    root = Tk()
    root.title('Sheikh test')
    root.geometry('500x700')
    app = testOverlap(root)
    root.mainloop()


if __name__ == '__main__':
    main()
