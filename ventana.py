import tkinter as tk
from tkinter import ttk
import requests

class VentanaPrincipal(tk.Tk):
    """Clase para la ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.title("Gustos del Condado")
        self.geometry("800x400")
        self.resizable(False, False)  # Hacer que la ventana no sea dimensionable

        self.crear_widgets()

    def crear_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        columnas = ("ID", "Hack", "Nombre", "Horse", "Condado", "Color", "Insecto")
        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame, columns=columnas, show="headings")

        # Establecer encabezados y ancho de columnas
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)  # Ancho de 80 píxeles

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Empaquetar Treeview y scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Entrada para buscar un registro
        self.entrada_busqueda = tk.Entry(self)
        self.entrada_busqueda.pack(pady=10)

        # Frame para los botones
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        # Botones
        tk.Button(frame_botones, text="Mostrar Registros", command=self.mostrar_registros).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Buscar Registro", command=self.buscar_registro).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Refrescar Registros", command=self.refrescar_registros).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Cerrar", command=self.cerrar_aplicacion).pack(side=tk.LEFT, padx=5)

    def obtener_registros(self):
        """Obtiene todos los registros desde la API."""
        url = "https://671be6612c842d92c381b162.mockapi.io/test"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
        return []

    def mostrar_registros(self):
        """Muestra todos los registros en el Treeview."""
        for registro in self.tree.get_children():
            self.tree.delete(registro)
        for registro in self.obtener_registros():
            self.tree.insert("", tk.END, values=(
                registro.get('id', 'N/A'),
                registro.get('hack', 'N/A'),
                registro.get('nombre', 'N/A'),
                registro.get('horse', 'N/A'),
                registro.get('condado', 'N/A'),
                registro.get('color', 'N/A'),
                registro.get('insecto', 'N/A')
            ))

    def buscar_registro(self):
        """Busca un registro específico por ID."""
        id_busqueda = self.entrada_busqueda.get()
        registros = self.obtener_registros()

        for registro in self.tree.get_children():
            self.tree.delete(registro)

        encontrado = False
        for registro in registros:
            if str(registro.get('id')) == id_busqueda:
                self.tree.insert("", tk.END, values=(
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
            self.tree.insert("", tk.END, values=("No encontrado",) * len(registros[0]))

    def refrescar_registros(self):
        """Refresca la lista de registros desde la API."""
        self.mostrar_registros()

    def cerrar_aplicacion(self):
        """Cierra la aplicación."""
        self.destroy()


