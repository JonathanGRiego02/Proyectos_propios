import tkinter as tk

def cerrar_ventana(event):
  ventana.destroy()

def mover_snake():
    global direccion_x, direccion_y

    # Mueve la serpiente en la dirección actual
    canvas.move(snake, direccion_x, direccion_y)

    # Llama a mover_snake después de 50 milisegundos
    ventana.after(50, mover_snake)

def cambiar_direccion(event):
    global direccion_x, direccion_y
    if event.keysym == 'Up':
      direccion_x, direccion_y = 0, -5  # Mueve hacia arriba
    elif event.keysym == 'Down':
      direccion_x, direccion_y = 0, 5   # Mueve hacia abajo
    elif event.keysym == 'Left':
      direccion_x, direccion_y = -5, 0  # Mueve hacia la izquierda
    elif event.keysym == 'Right':
      direccion_x, direccion_y = 5, 0   # Mueve hacia la derecha

ventana = tk.Tk()
ventana.title("snake")
ventana.geometry("1920x1080")

# Asociar la función cerrar_ventana con el evento de cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Asociar la función cerrar_ventana con el evento de presionar la tecla "Escape"
ventana.bind("<Escape>", cerrar_ventana)

canvas = tk.Canvas(ventana, width=1920, height=1080)
canvas.pack()

# Crear un óvalo como snake que se moverá
snake = canvas.create_rectangle(50, 50, 100, 100, fill="green")

# Inicializar la dirección del movimiento
direccion_x, direccion_y = 5, 0

# Asociar la función cambiar_direccion con el evento de presionar una tecla
ventana.bind("<KeyPress>", cambiar_direccion)

# Iniciar el movimiento constante
mover_snake()

# Mostrar la ventana
ventana.mainloop()
