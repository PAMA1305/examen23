import requests

class _Registro:
    """Clase privada para manejar los registros desde la API."""
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

def obtener_registros():
    """Función pública para acceder a los registros."""
    registro = _Registro()  # Crear una instancia de _Registro
    return registro.obtener_registros()  # Llamar al método de instancia



