from tkinter import *

# Configuración de la raíz
root = Tk()

label1 = Label(root, text='Nombre muy largo')
label1.grid(row=0,column=0,sticky='e',padx=5,pady=5)

entry1 = Entry(root)
entry1.grid(row=0,column=1,padx=5,pady=5)
entry1.config(justify='right', state='disabled')



label2 = Label(root, text='Apellidos')
label2.grid(row=1,column=0,sticky='e',padx=5,pady=5)

entry2 = Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify='center')



label3 = Label(root, text='Contraseña')
label3.grid(row=2,column=0,sticky='e',padx=5,pady=5)

entry3 = Entry(root)
entry3.grid(row=2,column=1,padx=5,pady=5)
entry3.config(justify='center', show='*')



# Finalmente bucle de la aplicación
root.mainloop()