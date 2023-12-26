import vaex
from fuzzywuzzy import fuzz

import os
import multiprocessing

# Obtener el número de núcleos de CPU disponibles
num_cpus = multiprocessing.cpu_count()

# Establecer el número de procesos para multiprocesamiento (e.g., apply)
vaex.settings.main.process_count = num_cpus

# Establecer el número de subprocesos para cálculos
vaex.settings.main.thread_count = os.cpu_count()

@vaex.register_dataframe_accessor('search', override=True)
class SearchAddress(object):
    def __init__(self, df):
        self.df = df.copy()
        self.direccion = False
        self.numpuerta = False

    def calculate_similarity(self, direcc, numpuerta):
        sim_direcc = fuzz.ratio(direcc, self.direccion) / 100.0
        sim_numpuerta = 0.0
        if self.numpuerta:
            sim_numpuerta = self.find_closest_num_with_similarity(numpuerta)
        return sim_direcc + sim_numpuerta
    
    def find_closest_num_with_similarity(self, numpuerta):
        num1 = int(numpuerta)
        num2 = int(self.numpuerta)
        # Obtiene el valor absoluto de las diferencias entre los dos números
        diff_num1 = abs(num1)
        diff_num2 = abs(num2)
        
        # Calcula el número más cercano entre num1 y num2
        closest_num = num1 if diff_num1 < diff_num2 else num2
        
        # Calcula el porcentaje de similitud basado en la diferencia relativa
        similarity_percentage = 1 - ((abs(num1 - num2)) / closest_num)
        
        return similarity_percentage
    
    def address_street(self, departamento, provincia, distrito, direccion, numpuerta):
        df = self.df.copy()
        if departamento:
            df = df[df.departamento == departamento]

        if provincia:
            df = df[df.provincia == provincia]

        if distrito:
            df = df[df.distrito == distrito]
        if direccion and numpuerta and len(direccion) != 0 and len(numpuerta) != 0:
            self.direccion = direccion + ' ' + numpuerta
            self.numpuerta = numpuerta
            return self.similarity_address_street(df)
        if direccion and len(direccion) != 0:
            self.direccion = direccion
            return self.similarity_address_street(df)
        return df.head(10)

    def similarity_address_street(self, dataframe):        
        df = dataframe.copy()

        # Calcular la similitud exacta
        df['similarity_direccion'] = df.apply(self.calculate_similarity, arguments=[df['direcc'], df['numpuerta']])

        # # Ordenar de mayor a menor
        df = df.sort('similarity_direccion', ascending=False)
        
        # Seleccionar campos especificos
        filtering_data = df[['departamento', 'provincia', 'distrito', 'direcc', 'lon_x', 'lat_y', 'similarity_direccion']]
        is_empty = (df['similarity_direccion']).sum().item()

        if is_empty == 0:
            return df

        return  filtering_data.head(10)