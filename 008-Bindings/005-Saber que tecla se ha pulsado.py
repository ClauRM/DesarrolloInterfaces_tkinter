import tkinter as tk

def pulsaTecla(evento):
    print("Has pulsado la tecla:",evento.keysym)

ventana = tk.Tk()

lienzo=tk.Canvas(ventana)
lienzo.create_oval(20,20,50,50,outline="red",width=2)
lienzo.pack(padx=50,pady=50)

#escuchar teclado para moverlo
ventana.bind('<Key>',pulsaTecla)

ventana.mainloop() 
