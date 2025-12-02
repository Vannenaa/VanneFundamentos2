# Librerías
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime

# Inventario Inicial inclye 10 productos
inventario = [
    {"id": "001", "modelo": "Guitarra", "marca": "Fender", "precio": 1800, "stock": 40,
     "descripción": "Instrumento de cuerdas metálicas, se adapta a estilos como el folk y el rock"},
    {"id": "002", "modelo": "Violín", "marca": "Gewa", "precio": 3500, "stock": 25,
     "descripción": "Instrumento de cuerda frotada con cuatro cuerdas afinadas en quinta"},
    {"id": "003", "modelo": "Flauta", "marca": "Yamaha", "precio": 250, "stock": 60,
     "descripción": "Instrumento de viento de forma tubular"},
    {"id": "004", "modelo": "Acordeón", "marca": "Roland", "precio": 16500, "stock": 15,
     "descripción": "inrumento de viento portatil de lengueta libre"},
    {"id": "005", "modelo": "Trompeta", "marca": "Yamaha", "precio": 5000, "stock": 20,
     "descripción": "Instrumento de viento metal, produce sonidos fuertes usando una"
     "boquilla y tres pistones"},
    {"id": "006", "modelo": "Saxofón", "marca": "Yamaha", "precio": 6000, "stock": 15,
      "descripción": "Instrumento de viento-madera de metal"},
    {"id": "007", "modelo": "Piano", "marca": "Yamaha", "precio": 50000, "stock": 5,
     "descripción": "Instrumento musical de teclado"},
    {"id": "008", "modelo": "Batería", "marca": "Yamaha", "precio": 15000, "stock": 10,
     "decripción": "Conjunto de instrumentos de perjución que incluye tambores"},
    {"id": "009", "modelo": "Guitarra eléctrica", "marca": "Fender", "precio": 14000, "stock": 15,
     "descripción": "Instrumento de cuerda que usa pastillas para transformar las vibraciones en sonido amplificado"},
    {"id": "010", "modelo": "Ukelele", "marca": "Fender", "precio": 2000, "stock": 20,
     "descripción": "Instrumento de cuerda pulsada de cuatro cuerdas"},
]

historial_ventas = []
STOCK_MINIMO = 3

# Funciones
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenids con estadísticas rápidas"""
    global boton_activo
    texto.delete(1.0, tk.END) 
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_instrumentos = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%H:%H").date())
    producto_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "¡Bienvenido a RockStar Music Shop!\n\n")

    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de Instrumentos en Stock: {total_instrumentos}\n")
    texto.insert(tk.END, F"Ventas Registradas (Hoy): {ventas_hoy}\n")

    if producto_stock_bajo > 0: 
        texto.insert (tk.END, f"¡ALERTA DE STOCK BAJO!: {producto_stock_bajo} productos necesitan reabastecimiento. \n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

#Botones
def activar_boton(boton):
    """Actualiza el color del botón activo."""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg= "#af7320")

    if boton:
        boton.config(bg= "#F9F7F7")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg= "#F9F7F7")

def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg= "#af7320")

#Parte gráfica
ventana = tk.Tk()
ventana.title("RockStar Music Shop")
ventana.geometry("1200x800")
ventana.configure(bg= "#150b01") 

boton_activo = None

titulo = tk.Label(ventana, text= "RockStar Music Shop",
                  font=("Helvetica", 32, "bold"), bg= "#150b01", fg= "#F8F3F3")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS)",
                     font=("Helvetica", 12), bg= "#150b01", fg= "#8B7E7E")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg= "#150b01") 
frame_botones.pack(pady=20)

btn_style = {"font": ("Calibrí Light", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# Botones del Menu
btn_home = tk.Button(frame_botones, text= "HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)
btn1 = tk.Button(frame_botones, text= "INVENTARIO", command=lambda: messagebox.showinfo("Info", "Función disponible"))
btn1.grid(row=0, column=1, padx=8)
btn2 = tk.Button(frame_botones, text= "AGREGAR", command=lambda: messagebox.showinfo("Info", "Función disponible"))
btn2.grid(row=0, column=2, padx=8)
btn3 = tk.Button(frame_botones, text= "VENDER", command=lambda: messagebox.showinfo("Info", "Función disponible"))
btn3.grid(row=0, column=3, padx=8)
btn4 = tk.Button(frame_botones, text="BUSCAR", command=lambda: messagebox.showinfo("Info", "Función disponible"))
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(ventana,
                                  font=("Open Sans", 11),
                                  bg= "#ffffff", fg= "#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground= "#000000")
texto.tag_config("alerta", background= "#ffe5e5", foreground= "#ff4500", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background= "#fddede", foreground= "#cc0000", font=("Open Sans", 11, "bold"))

footer = tk.Label(ventana, text= "RockStar Music Shop DÍA 1 (lUNES) - Interfaz Base y HOME",
                  font=("Helvetica", 10), bg= "#150b01", fg= "#E1E1E1")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()