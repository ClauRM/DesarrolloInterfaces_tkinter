import tkinter as tk

ventana = tk.Tk()

tk.Scale(ventana,from_=0,to=100,orient=tk.HORIZONTAL).pack(padx=50,pady=50)

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
