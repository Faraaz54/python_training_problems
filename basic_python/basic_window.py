from Tkinter import *

class window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('GUI')
        self.pack(fill = BOTH, expand = 1)
        #quitbutton = Button(self, text = 'quit', command = self.client_exit)
        #quitbutton.place(x=0, y=0)
        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = 'exit', command = self.client_exit)
        menu.add_cascade(label = 'file', menu = file)

        edit = Menu(menu)
        edit.add_command(label = 'undo')
        menu.add_cascade(label = 'edit', menu = edit)
        



    def client_exit(self):
        exit()

root = Tk()
root.geometry('400x300')

app = window(root)

root.mainloop()



