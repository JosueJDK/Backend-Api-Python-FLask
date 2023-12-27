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
class SearchAddressStreet(object):
    def __init__(self, df):
        self.df = df.copy()
        self.departamento = False
        self.provincia = False
        self.distrito = False
        self.direccion = False
        self.numpuerta = False
    
    def calculate_similarity_v2(self, field):
        data = False
        if self.departamento:
            data = self.departamento
        if self.provincia:
            data = self.provincia
        if self.distrito:
            data = self.distrito
        if self.direccion:
            data = self.direccion        
        if not data:
            return 0.0
        return fuzz.ratio(field, data) / 100.0
    
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
    
    def return_dataframe(self, df, field, arguments):
        df[field] = df.apply(self.calculate_similarity_v2, arguments=arguments)

        df = df.sort(field, ascending=False)

        is_match = (df[field] == 1).sum().item()
        if is_match == 1:
            return  df.head(1)
        is_empty = (df[field]).sum().item()
        if is_empty == 0:
            return df
        return  df.head(10)

    def address_departamento(self, departamento):
        self.departamento = departamento.upper()
        df = self.df.copy()
        return self.return_dataframe(df, 'SIMILARITY_DEPARTAMENTO', [df['DEPARTAMENTO']])
    
    def address_provincia(self, departamento=False, provincia=False):
        self.provincia = provincia.upper()
        df = self.df.copy()
        if departamento:
            df = df[df.DEPARTAMENTO == departamento.upper()]
        return self.return_dataframe(df, 'SIMILARITY_PROVINCIA', [df['PROVINCIA']])
    
    def address_distrito(self, departamento=False, provincia=False, distrito=False):
        
        self.distrito = distrito.upper()
        df = self.df.copy()

        if departamento:
            df = df[df.DEPARTAMENTO == departamento.upper()]

        if provincia:
            df = df[df.PROVINCIA == provincia.upper()]
        
        return self.return_dataframe(df, 'SIMILARITY_DISTRITO', [df['DISTRITO']])

    
    def address_street(self, departamento=False, provincia=False, distrito=False, direccion=False, numpuerta=False):
        df = self.df.copy()
        if departamento:
            df = df[df.DEPARTAMENTO == departamento.upper()]

        if provincia:
            df = df[df.PROVINCIA == provincia.upper()]

        if distrito:
            print(df)
            df = df[df.DISTRITO == distrito.upper()]            
        if direccion:
            self.direccion = direccion.upper()
            df['SIMILARITY_STREET'] = df.apply(self.calculate_similarity_v2, arguments=[df['TIPO_VIA'] + ' ' + df['NOM_VIA']])
            df = df.sort('SIMILARITY_STREET', ascending=False)

        if numpuerta:
            self.numpuerta = numpuerta
            df['SIMILARITY_NUMPUERTA'] = df.apply(self.find_closest_num_with_similarity, arguments=[df['NUM_PUERTA']])
            df['SIMILARITY_STREET_NUMPUERTA'] = df['SIMILARITY_NUMPUERTA'] + df['SIMILARITY_STREET']
            df = df.sort('SIMILARITY_STREET_NUMPUERTA', ascending=False)
        return  df.head(10)