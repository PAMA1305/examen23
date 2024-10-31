from registro import obtener_registros
from ventana import VentanaPrincipal

def main():
    registros = obtener_registros()
    print(registros)
    app = VentanaPrincipal()
    app.mainloop()

if __name__ == "__main__":
    main()
