from Classes.DataLoader import DataJSONLoader, DataLoader, DataAPILoader

data_loader = DataLoader(DataJSONLoader("Data/short_cleaned_songs.json"))
print("Datos desde JSON:", data_loader.load())
