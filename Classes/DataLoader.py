import json
import requests
import logging
from abc import ABC, abstractmethod


class DataLoaderStrategy(ABC):
    """
    Clase abstracta que define la interfaz para estrategias de carga de datos.
    """
    @abstractmethod
    def load_data(self):
        """
        Método abstracto para cargar datos. Debe ser implementado por subclases.
        """
        pass

class DataJSONLoader(DataLoaderStrategy):
    """
    Estrategia para cargar datos desde un archivo JSON.
    """
    def __init__(self, file_path):
        """
        Inicializa el loader con la ruta del archivo JSON.
        
        Args:
            file_path (str): Ruta del archivo JSON.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Carga datos desde el archivo JSON.

        Returns:
            dict: Datos cargados desde el archivo JSON.
        """
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            logging.info(f'Datos cargados exitosamente desde {self.file_path}.')
            return data
        except Exception as e:
            logging.critical(f'Error al cargar datos desde {self.file_path}: {e}')

class DataAPILoader(DataLoaderStrategy):
    """
    Estrategia para cargar datos desde una API.
    """
    def __init__(self, api_url):
        """
        Inicializa el loader con la URL de la API.
        
        Args:
            api_url (str): URL de la API.
        """
        self.api_url = api_url

    def load_data(self):
        """
        Carga datos desde la API.

        Returns:
            dict: Datos obtenidos de la API.
        """
        try:
            response = requests.get(self.api_url)
            logging.info(f'Datos obtenidos exitosamente desde la API: {self.api_url}.')
            return response.json()
        except Exception as e:
            logging.critcal(f'Error al obtener datos desde la API {self.api_url}: {e}')

class DataLoader:
    """
    Clase que utiliza una estrategia de carga de datos para cargar datos.
    """
    def __init__(self, strategy: DataLoaderStrategy):
        """
        Inicializa el DataLoader con una estrategia de carga de datos.

        Args:
            strategy (DataLoaderStrategy): Estrategia para cargar datos.
        """
        self.strategy = strategy

    def set_strategy(self, strategy: DataLoaderStrategy):
        """
        Configura una nueva estrategia de carga de datos.

        Args:
            strategy (DataLoaderStrategy): Nueva estrategia de carga de datos.
        """
        self.strategy = strategy
        logging.info(f'Strategia de carga de datos actualizada a {type(strategy).__name__}.')

    def load(self):
        """
        Carga los datos utilizando la estrategia actual.

        Returns:
            dict: Datos cargados.
        """
        logging.info('Cargando datos utilizando la estrategia actual.')
        return self.strategy.load_data()
