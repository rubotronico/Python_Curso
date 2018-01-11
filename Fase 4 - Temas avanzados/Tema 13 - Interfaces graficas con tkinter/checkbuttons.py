from tkinter import *


# Configuración de la raíz
root = Tk()
root.title('Cafetería')
root.config(bd=15)

leche = IntVar()	# 1 sí, 0 no
azucar = IntVar()	# 1 sí, 0 no

Label (root, text='¿Cómo quiere el café?').pack()
Checkbutton(root, text='Con leche', variable=leche).pack()
Checkbutton(root, text='Con azúcar', variable=azucar).pack()

# Finalmente bucle de la aplicación
root.mainloop()