import tkinter as tk
from tkinter import ttk
import requests

def obtener_registros():
    url = "https://671be6612c842d92c381b162.mockapi.io/test"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    return []

def mostrar_registros():
    for registro in tree.get_children():
        tree.delete(registro)
    for registro in obtener_registros():
        tree.insert("", tk.END, values=(
            registro.get('id', 'N/A'),
            registro.get('hack', 'N/A'),
            registro.get('nombre', 'N/A'),
            registro.get('horse', 'N/A'),
            registro.get('condado', 'N/A'),
            registro.get('color', 'N/A'),
            registro.get('insecto', 'N/A')
        ))

def buscar_registro():
    id_busqueda = entrada_busqueda.get()
    registros = obtener_registros()

    for registro in tree.get_children():
        tree.delete(registro)

    encontrado = False
    for registro in registros:
        if str(registro.get('id')) == id_busqueda:
            tree.insert("", tk.END, values=(
                registro.get('id', 'N/A'),
                registro.get('hack', 'N/A'),
                registro.get('nombre', 'N/A'),
                registro.get('horse', 'N/A'),
                registro.get('condado', 'N/A'),
                registro.get('color', 'N/A'),
                registro.get('insecto', 'N/A')
            ))
            encontrado = True
            break

    if not encontrado:
        tree.insert("", tk.END, values=("No encontrado",) * len(columnas))

def refrescar_registros():
    mostrar_registros()

def cerrar_aplicacion():
    ventana.destroy()  # Cierra la ventana y termina la aplicación

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gustos del Condado")
ventana.geometry("600x400")
ventana.resizable(False, False)  # Hacer que la ventana no sea dimensionable

# Configuración del Treeview y scrollbar
columnas = ("ID", "Hack", "Nombre", "Horse", "Condado", "Color", "Insecto")
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

tree = ttk.Treeview(frame, columns=columnas, show="headings")

# Establecer encabezados y ancho de columnas
tree.heading("ID", text="ID")
tree.heading("Hack", text="Hack")
tree.heading("Nombre", text="Nombre")
tree.heading("Horse", text="Horse")
tree.heading("Condado", text="Condado")
tree.heading("Color", text="Color")
tree.heading("Insecto", text="Insecto")

# Configurar el ancho de las columnas
ancho_columnas = 80  # Ancho de cada columna en píxeles
for col in columnas:
    tree.column(col, anchor="center", width=ancho_columnas)

# Scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Empaquetar Treeview y scrollbar
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Entrada para buscar un registro
entrada_busqueda = tk.Entry(ventana)
entrada_busqueda.pack(pady=10)

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones
boton_mostrar = tk.Button(frame_botones, text="Mostrar Registros", command=mostrar_registros)
boton_mostrar.pack(side=tk.LEFT, padx=5)

boton_buscar = tk.Button(frame_botones, text="Buscar Registro", command=buscar_registro)
boton_buscar.pack(side=tk.LEFT, padx=5)

boton_refrescar = tk.Button(frame_botones, text="Refrescar Registros", command=refrescar_registros)
boton_refrescar.pack(side=tk.LEFT, padx=5)

boton_cerrar = tk.Button(frame_botones, text="Cerrar", command=cerrar_aplicacion)
boton_cerrar.pack(side=tk.LEFT, padx=5)

# Ejecutar la aplicación
ventana.mainloop()
