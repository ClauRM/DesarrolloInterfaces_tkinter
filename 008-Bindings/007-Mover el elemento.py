import tkinter as tk

def pulsaTecla(evento):
    print("Has pulsado la tecla:",evento.keysym)
    if evento.keysym == 'a':
        print("izquierda")
        lienzo.move(elemento,-10,0)
    elif evento.keysym == 'd':
        print("derecha")
        lienzo.move(elemento,10,0)
    elif evento.keysym == 'w':
        print("arriba")
        lienzo.move(elemento,0,-10)
    elif evento.keysym == 's':
        print("abajo")
        lienzo.move(elemento,0,10)

ventana = tk.Tk()

lienzo=tk.Canvas(ventana)
elemento = lienzo.create_oval(20,20,50,50,outline="red",width=2)
lienzo.pack(padx=50,pady=50)

#escuchar teclado para moverlo
ventana.bind('<Key>',pulsaTecla)

ventana.mainloop() 
