import tkinter

root = tkinter.Tk()

frame = tkinter.Frame(root)

tkinter.Label(frame, text='Life couldn\'t be better').pack()

tkinter.Button(frame, text='B1').pack(side=tkinter.LEFT, fill=tkinter.Y)
tkinter.Button(frame, text='B2').pack(side=tkinter.TOP, fill=tkinter.X)
tkinter.Button(frame, text='B3').pack(side=tkinter.LEFT, fill=tkinter.X)
tkinter.Button(frame, text='B4').pack(side=tkinter.BOTTOM, fill=tkinter.X)


frame.pack()

root.mainloop()
