from abc import ABC, abstractmethod
import json
import requests

class DataLoaderStrategy(ABC):
    def load(self):
        pass

class DataJSONLoader():
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data

class DataAPILoader(DataLoaderStrategy):
    def __init__(self, api_url):
        self.api_url = api_url

    def load_data(self):
        response = requests.get(self.api_url)
        response.raise_for_status() 
        return response.json()

class DataLoader:
    def __init__(self, strategy: DataLoaderStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DataLoaderStrategy):
        self.strategy = strategy

    def load(self):
        return self.strategy.load_data()
