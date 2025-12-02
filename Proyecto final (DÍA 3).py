# Librerías
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from datetime import datetime

# Inventario Inicial
inventario = [
    {"id": "001", "modelo": "Guitarra", "marca": "Fender", "precio": 1800, "stock": 40,
     "descripción": "Instrumento de cuerdas metálicas, se adapta a estilos como el folk y el rock"},
    {"id": "002", "modelo": "Violín", "marca": "Gewa", "precio": 3500, "stock": 25,
     "descripción": "Instrumento de cuerda frotada con cuatro cuerdas afinadas en quinta"},
    {"id": "003", "modelo": "Flauta", "marca": "Yamaha", "precio": 250, "stock": 60,
     "descripción": "Instrumento de viento de forma tubular"},
    {"id": "004", "modelo": "Acordeón", "marca": "Roland", "precio": 16500, "stock": 15,
     "descripción": "Instrumento de viento portátil de lengüeta libre"},
    {"id": "005", "modelo": "Trompeta", "marca": "Yamaha", "precio": 5000, "stock": 20,
     "descripción": "Instrumento de viento metal, produce sonidos fuertes usando una boquilla y tres pistones"},
    {"id": "006", "modelo": "Saxofón", "marca": "Yamaha", "precio": 6000, "stock": 15,
      "descripción": "Instrumento de viento-madera de metal"},
    {"id": "007", "modelo": "Piano", "marca": "Yamaha", "precio": 50000, "stock": 5,
     "descripción": "Instrumento musical de teclado"},
    {"id": "008", "modelo": "Batería", "marca": "Yamaha", "precio": 15000, "stock": 10,
     "descripción": "Conjunto de instrumentos de percusión que incluye tambores"},
    {"id": "009", "modelo": "Guitarra eléctrica", "marca": "Fender", "precio": 14000, "stock": 15,
     "descripción": "Instrumento de cuerda que usa pastillas para transformar vibraciones en sonido amplificado"},
    {"id": "010", "modelo": "Ukelele", "marca": "Fender", "precio": 2000, "stock": 20,
     "descripción": "Instrumento de cuerda pulsada de cuatro cuerdas"},
]

historial_ventas = []
STOCK_MINIMO = 3


# Funciones
def mostrar_bienvenida():
    texto.delete(1.0, tk.END) 
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_instrumentos = sum(t['stock'] for t in inventario)

    ventas_hoy = sum(
        1 for v in historial_ventas
        if datetime.strptime(v['fecha'], "%Y-%m-%d %H:%M:%S").date() == datetime.now().date()
    )

    producto_stock_bajo = sum(1 for t in inventario if 0 < t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "¡Bienvenido a RockStar Music Shop!\n\n")
    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de Instrumentos en Stock: {total_instrumentos}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")

    if producto_stock_bajo > 0:
        texto.insert(tk.END, f"¡ALERTA DE STOCK BAJO!: {producto_stock_bajo} productos necesitan reabastecimiento.\n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")


def validar_numero_positivo(valor, nombre_campo): 
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Error", f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error", f"'{nombre_campo}' debe ser un número válido.")
        return None


def generar_nuevo_id(): 
    if not inventario:
        return "001"
    max_id = max(int(prod["id"]) for prod in inventario)
    return str(max_id + 1).zfill(3)


def mostrar_inventario():
    texto.delete(1.0, tk.END)
    activar_boton(btn1)

    texto.insert(tk.END, "= INVENTARIO COMPLETO =\n\n")

    texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<20} | {'MARCA':<10} | {'PRECIO':<10} | {'STOCK':<5}\n")
    texto.insert(tk.END, "-" * 70 + "\n")

    for prod in inventario:
        linea = f"{prod['id']:<4} | {prod['modelo']:<20} | {prod['marca']:<10} | ${prod['precio']:<10} | {prod['stock']:<5}"
        texto.insert(tk.END, linea)

        if prod['stock'] == 0:
            texto.insert(tk.END, "  ← AGOTADO", "agotado")
        elif prod['stock'] <= STOCK_MINIMO:
            texto.insert(tk.END, "  ← STOCK BAJO", "alerta")

        texto.insert(tk.END, "\n")


def agregar_producto():
    activar_boton(btn2)
    nuevo_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Producto", "Modelo (obligatorio):", parent=ventana)
    if not modelo: return

    marca = simpledialog.askstring("Agregar Producto", "Marca (obligatorio):", parent=ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Producto", "Precio unitario:", parent=ventana)
    if not precio_str: return

    precio = validar_numero_positivo(precio_str, "Precio")
    if precio is None: return

    stock_str = simpledialog.askstring("Agregar Producto", "Stock inicial:", parent=ventana)
    if not stock_str: return

    stock = validar_numero_positivo(stock_str, "Stock")
    if stock is None: return

    descripcion = simpledialog.askstring("Agregar Producto", "Descripción (opcional):", parent=ventana)

    nuevo_producto = {
        "id": nuevo_id,
        "modelo": modelo,
        "marca": marca,
        "precio": float(precio),
        "stock": int(stock),
        "descripción": descripcion if descripcion else "Sin descripción"
    }

    inventario.append(nuevo_producto)
    messagebox.showinfo("Éxito", f"'{modelo}' agregado con ID {nuevo_id}.")
    mostrar_inventario()


def buscar_instrumentos():
    activar_boton(btn4)

    criterio_busqueda = simpledialog.askstring("Buscar", "Buscar por modelo o marca:", parent=ventana)
    if not criterio_busqueda:
        return

    criterio = criterio_busqueda.lower()

    resultados = [
        prod for prod in inventario
        if criterio in prod["modelo"].lower() or criterio in prod["marca"].lower()
    ]

    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"RESULTADOS DE BÚSQUEDA: '{criterio_busqueda}'\n\n")

    if not resultados:
        texto.insert(tk.END, "Sin resultados.\n")
        return

    texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<10} | {'MARCA':<10} | {'STOCK':<5}\n")
    texto.insert(tk.END, "-"*70 + "\n")

    for prod in resultados:
        linea = (
            f"{prod['id']:<4} | "
            f"{prod['modelo']:<25} | "
            f"${prod['precio']:<10} | "
            f"{prod['marca']:<10} | "
            f"{prod['stock']:<5}\n"
        )
        texto.insert(tk.END, linea)



def vender_instrumentos():
    activar_boton(btn3)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles.")
        return

    opciones = "\n".join([
        f"{i+1}. ID:{prod['id']} - {prod['modelo']} (Stock: {prod['stock']})"
        for i, prod in enumerate(inventario)
    ])

    seleccion = simpledialog.askinteger(
        "Vender", f"Seleccione un producto:\n\n{opciones}", parent=ventana
    )

    if not seleccion or seleccion < 1 or seleccion > len(inventario):
        return

    prod = inventario[seleccion - 1]

    if prod["stock"] <= 0:
        messagebox.showwarning("Agotado", "Este producto no tiene stock.")
        return

    cant_str = simpledialog.askstring(
        "Cantidad", f"¿Cuántas unidades deseas vender de '{prod['modelo']}'?",
        parent=ventana
    )

    if not cant_str:
        return

    cant_valida = validar_numero_positivo(cant_str, "Cantidad")
    if cant_valida is None:
        return

    cantidad = int(cant_valida)

    if cantidad > prod["stock"]:
        messagebox.showerror("Error", f"Hay solo {prod['stock']} unidades disponibles.")
        return

    monto = cantidad * prod["precio"]
    prod["stock"] -= cantidad

    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id_producto": prod["id"],
        "modelo": prod["modelo"],
        "cantidad": cantidad,
        "precio_unitario": prod["precio"],
        "monto_total": monto
    }

    historial_ventas.append(registro)

    messagebox.showinfo("Venta realizada",
        f"Venta de {cantidad} unidades de '{prod['modelo']}' por ${monto:.2f}.")

    mostrar_resumen_venta(registro)


def mostrar_resumen_venta(venta):
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= VENTA REGISTRADA =\n\n")

    texto.insert(tk.END, f"Fecha y Hora: {venta['fecha']}\n")
    texto.insert(tk.END, f"ID Producto: {venta['id_producto']}\n")
    texto.insert(tk.END, f"Modelo: {venta['modelo']}\n")
    texto.insert(tk.END, f"Cantidad: {venta['cantidad']}\n")
    texto.insert(tk.END, f"Precio Unitario: ${venta['precio_unitario']:.2f}\n")
    texto.insert(tk.END, f"Monto Total: ${venta['monto_total']:.2f}\n")


# Botones
ventana = tk.Tk()
ventana.title("RockStar Music Shop")
ventana.geometry("1200x800")
ventana.configure(bg="#150b01") 

boton_activo = None

def activar_boton(boton):
    global boton_activo
    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#af7320")
    boton.config(bg="#F9F7F7")
    boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo: boton.config(bg="#F9F7F7")

def on_leave(e, boton):
    if boton != boton_activo: boton.config(bg="#af7320")


titulo = tk.Label(ventana, text="RockStar Music Shop",
                  font=("Helvetica", 32, "bold"), bg="#150b01", fg="#F8F3F3")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS",
                     font=("Helvetica", 12), bg="#150b01", fg="#8B7E7E")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#150b01") 
frame_botones.pack(pady=20)

btn_style = {"font": ("Calibri", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_producto, **btn_style)
btn3 = tk.Button(frame_botones, text="VENDER", command=vender_instrumentos, **btn_style)
btn4 = tk.Button(frame_botones, text="BUSCAR", command=buscar_instrumentos, **btn_style)

btn_home.grid(row=0, column=0, padx=8)
btn1.grid(row=0, column=1, padx=8)
btn2.grid(row=0, column=2, padx=8)
btn3.grid(row=0, column=3, padx=8)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(
    ventana, font=("Open Sans", 11), bg="#ffffff", fg="#000000",
    height=18, padx=20, pady=20, relief=tk.SOLID, bd=1
)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"))
texto.tag_config("alerta", background="#ffe5e5", foreground="#ff4500", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#fddede", foreground="#cc0000", font=("Open Sans", 11, "bold"))

footer = tk.Label(ventana, text="RockStar Music Shop - Gestión completa",
                  font=("Helvetica", 10), bg="#150b01", fg="#E1E1E1")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()