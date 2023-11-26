import tkinter as tk

ventana = tk.Tk()

lienzo=tk.Canvas(ventana)
lienzo.create_oval(20,20,50,50,outline="red",width=2)
lienzo.pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
