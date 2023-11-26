import tkinter as tk

ventana = tk.Tk()

frutas=["manzana","pera","platano","fresa"]
listado=tk.Listbox(ventana)

for fruta in frutas:
    listado.insert(tk.END,fruta)

listado.pack(padx=50,pady=50)#se da el paxk despues de rellenar el listado

ventana.mainloop() #para que se ejecute la ventana ejecutando el archivo
