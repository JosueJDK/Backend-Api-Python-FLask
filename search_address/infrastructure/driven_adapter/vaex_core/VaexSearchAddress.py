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
        self.urbanizacion = False
        self.manzana =False
        self.centropoblado = False
    
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
        if self.urbanizacion:
            data = self.urbanizacion 
        if self.manzana:
            data = self.manzana        
        if self.centropoblado:
            data = self.centropoblado
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
    
    def is_empty_dataframe(self, df, field):
        is_empty = (df[field]).sum().item()
        if is_empty == 0:
            return df
        else:
            return df

    def address_departamento(self):
        return self.df.copy()
    
    def address_provincia(self, id_departamento=False, provincia=False):
        self.provincia = provincia.upper()
        df = self.df.copy()
        if id_departamento:
            df = df[df.ID_DEPARTAMENTO == int(id_departamento)]
        df = self.return_dataframe(df, 'SIMILARITY_PROVINCIA', [df['PROVINCIA']])    
        is_empty = (df["SIMILARITY_PROVINCIA"]).sum().item()
        if is_empty == 0:
            return df
        return df.sort('SIMILARITY_PROVINCIA', ascending=False).head(10)
    
    def address_distrito(self, id_departamento=False, id_provincia=False, distrito=False):
        
        self.distrito = distrito.upper()
        df = self.df.copy()

        if id_departamento:
            df = df[df.ID_DEPARTAMENTO == int(id_departamento)]

        if id_provincia:
            df = df[df.ID_PROVINCIA == int(id_provincia)]
        
        df = self.return_dataframe(df, 'SIMILARITY_DISTRITO', [df['DISTRITO']])  
        is_empty = (df["SIMILARITY_DISTRITO"]).sum().item()
        if is_empty == 0:
            return df  
        return df.sort('SIMILARITY_DISTRITO', ascending=False).head(10)

    def address_urbanizacion(self, departamento=False, provincia=False, distrito=False, urbanizacion=False):
        df = self.df.copy()
        if departamento:
            departamento = "0"+str(departamento) if len(str(departamento)) == 1 else departamento
            df = df[df.UBI_DEPARTAMENTO== str(departamento)]

        if provincia:
            provincia = "0"+str(provincia) if len(str(provincia)) == 1 else provincia
            df = df[df.UBI_DEPARTAMENTO + df.UBI_PROVINCIA == str(provincia)]
        
        if distrito:
            distrito = "0"+str(distrito) if len(str(distrito)) == 1 else distrito
            df = df[df.UBI_DEPARTAMENTO + df.UBI_PROVINCIA + df.UBI_DISTRITO == str(distrito)]
        if urbanizacion:
            self.urbanizacion = urbanizacion.upper()
            df['SIMILARITY_URBANIZACION'] = df.apply(self.calculate_similarity_v2, arguments=[df['ROTULO']])
            df = df.sort('SIMILARITY_URBANIZACION', ascending=False)        
        is_empty = (df["SIMILARITY_URBANIZACION"]).sum().item()
        if is_empty == 0:
            return df
        return  df.head(10)
    
    def address_manzana(self, departamento=False, provincia=False, distrito=False, urbanizacion=False,manzana=False, lote=False):
        df = self.df.copy()
        if departamento:
            departamento = "0"+str(departamento) if len(str(departamento)) == 1 else departamento
            df = df[df.UBI_DEPARTAMENTO== str(departamento)]

        if provincia:
            provincia = "0"+str(provincia) if len(str(provincia)) == 1 else provincia
            df = df[df.UBI_DEPARTAMENTO + df.UBI_PROVINCIA == str(provincia)]
        
        if distrito:
            distrito = "0"+str(distrito) if len(str(distrito)) == 1 else distrito
            df = df[df.UBI_DEPARTAMENTO + df.UBI_PROVINCIA + df.UBI_DISTRITO == str(distrito)]
        
        if urbanizacion and manzana:
            self.manzana = manzana.upper()
            self.urbanizacion = urbanizacion.upper()
            
            df = df[df['ROTULO'] == self.urbanizacion]

            df['SIMILARITY_MANZANA'] = df.apply(self.calculate_similarity_v2, arguments=[df['MZ_1']])
            df = df.sort('SIMILARITY_MANZANA', ascending=False)
        is_empty = (df["SIMILARITY_MANZANA"]).sum().item()
        if is_empty == 0:
            return df
        # if manzana:
        #     self.manzana = manzana.upper()
        #     df['SIMILARITY_MANZANA'] = df.apply(self.calculate_similarity_v2, arguments=[df['MZ_1']])
        #     df = df.sort('SIMILARITY_MANZANA', ascending=False)        
        return  df.head(10)
    
    def address_centropoblado(self, departamento=False, provincia=False, distrito=False, centropoblado=False):
        df = self.df.copy()
        print(df)
        if departamento:
            print(departamento)
            departamento = "0"+str(departamento) if len(str(departamento)) == 1 else departamento
            df = df[df.UBI_DEPARTAMENTO== str(departamento)]

        if provincia:
            provincia = "0"+str(provincia) if len(str(provincia)) == 3 else provincia
            df = df[df.UBI_DEPARTAMENTO + df.UBI_PROVINCIA == str(provincia)]
        
        if distrito:
            distrito = "0"+str(distrito) if len(str(distrito)) == 5 else distrito
            print(distrito)
            df = df[df.UBI_DEPARTAMENTO+df.UBI_PROVINCIA+df.UBI_DISTRITO == str(distrito)]
        
        if centropoblado:
            print(df)
            self.centropoblado = centropoblado.upper()
            df['SIMILARITY_CENTRO_POBLADO'] = df.apply(self.calculate_similarity_v2, arguments=[df['NOM_CP']])
            print(df)
            df = df.sort('SIMILARITY_CENTRO_POBLADO', ascending=False)
        
        is_empty = (df["SIMILARITY_CENTRO_POBLADO"]).sum().item()
        if is_empty == 0:
            return df
        return  df.head(10)
    
    def address_street(self, departamento=False, provincia=False, distrito=False, direccion=False, numpuerta=False):
        df = self.df.copy()
        if departamento:
            df = df[df.DEPARTAMENTO == departamento.upper()]

        if provincia:
            df = df[df.PROVINCIA == provincia.upper()]

        if distrito:
            df = df[df.DISTRITO == distrito.upper()]
        if direccion and numpuerta:
            self.numpuerta = numpuerta
            self.direccion = direccion.upper()
            df['SIMILARITY_STREET'] = df.apply(self.calculate_similarity_v2, arguments=[df['VIA']])
            df = df.sort('SIMILARITY_STREET', ascending=False)

            df['SIMILARITY_NUMPUERTA'] = df.apply(self.find_closest_num_with_similarity, arguments=[df['NUM_PUERTA']])
            df['SIMILARITY_STREET_NUMPUERTA'] = df['SIMILARITY_NUMPUERTA'] + df['SIMILARITY_STREET']
            df = df.sort('SIMILARITY_STREET_NUMPUERTA', ascending=False)        
            # return self.is_empty_dataframe(df, "SIMILARITY_STREET_NUMPUERTA")

        if direccion:        
            self.direccion = direccion.upper()
            df['SIMILARITY_STREET'] = df.apply(self.calculate_similarity_v2, arguments=[df['VIA']])
            df = df.sort('SIMILARITY_STREET', ascending=False)        
            # return self.is_empty_dataframe(df, "SIMILARITY_STREET")
        
        is_empty = (df["SIMILARITY_STREET"]).sum().item()
        if is_empty == 0:
            return df
        return  df.head(10)