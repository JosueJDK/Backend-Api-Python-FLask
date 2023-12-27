# import vaex

# # Cargar el DataFrame desde el archivo HDF5
# df = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_DISTRITOS.hdf5")

# # Eliminar los espacios finales de la columna 'PROVINCIA'
# df['PROVINCIA'] = df['PROVINCIA'].str.rstrip()

# # Exportar el DataFrame modificado a un nuevo archivo HDF5
# df.export_hdf5("/home/ubuntu/clean_architecture/public/data/PERU_DISTRITOS_CORREGIDO.hdf5")


# def create_file_hdf5_address_street(file_parquet, file_hdf5_provincias):
#     # Leer un archivo Parquet
#     read_parquet = vaex.open(file_parquet, usecols=['OBJECTID', 'departamento', 'provincia', 'distrito', 'direcc', 'lat_y', 'lon_x', 'numpuerta'])
#     vaex_df = vaex.from_pandas(read_parquet)

#     # Cargar el archivo HDF5 con los departamentos y sus IDs correspondientes
#     departamentos_with_id = vaex.open("/home/ubuntu/clean_architecture/public/data/CALLES_PERU_DEPARTAMENTOS.hdf5")
#     provincias_with_id = vaex.open("/home/ubuntu/clean_architecture/public/data/CALLES_PERU_PROVINCIAS.hdf5")
#     distritos_with_id = vaex.open("/home/ubuntu/clean_architecture/public/data/CALLES_PERU_DISTRITOS.hdf5")

#     # Combinar la información de departamentos con IDs y provincias únicas
#     provincias_with_departamento = vaex_df.join(departamentos_with_id, 
#                         how='inner', 
#                         left_on='departamento',
#                         right_on='departamento')
    
    
#     # Rename the 'provincia' column in provincias_with_id dataframe
#     provincias_with_id.rename('provincia', 'provincia_provincias')
#     provincias_with_id.rename('id_departamento', 'id_departamento_provincias')


#     # Perform the join after renaming the column
#     provincias_with_provincia = provincias_with_departamento.join(provincias_with_id, 
#                         how='inner', 
#                         left_on='provincia',
#                         right_on='provincia_provincias')
    
#     # Rename the 'provincia' column in provincias_with_id dataframe
#     distritos_with_id.rename('distrito', 'distrito_distritos')
#     distritos_with_id.rename('id_departamento', 'id_departamento_distritos')
#     distritos_with_id.rename('id_provincia', 'id_provincia_distritos')
#     provincias_with_distrito = provincias_with_provincia.join(distritos_with_id, 
#                     how='inner', 
#                     left_on='distrito',
#                     right_on='distrito_distritos')

#     # Obtener distritos únicos
#     streets = provincias_with_distrito[['id_departamento', 'id_provincia', 'id_distrito', 'direcc', 'lat_y', 'lon_x', 'numpuerta']]
#     streets.export_hdf5(str(file_hdf5_provincias))
#     print(vaex.open(str(file_hdf5_provincias)).copy())
#     print("ARCHIVO HDF5 generado correctamente!")



# def create_file_hdf5_address_street(file_parquet, file_hdf5_provincias):
#     # Leer un archivo Parquet
#     read_parquet = vaex.open(file_parquet, usecols=['OBJECTID', 'departamento', 'provincia', 'distritos'])
#     vaex_df = vaex.from_pandas(read_parquet)

#     # Cargar el archivo HDF5 con los departamentos y sus IDs correspondientes
#     departamentos_with_id = vaex.open("/home/ubuntu/clean_architecture/public/data/CALLES_PERU_DEPARTAMENTOS.hdf5")
#     provincias_with_id = vaex.open("/home/ubuntu/clean_architecture/public/data/CALLES_PERU_PROVINCIAS.hdf5")

#     # Combinar la información de departamentos con IDs y provincias únicas
#     provincias_with_departamento = vaex_df.join(departamentos_with_id, 
#                         how='inner', 
#                         left_on='departamento',
#                         right_on='departamento')
    
    
#     # Rename the 'provincia' column in provincias_with_id dataframe
#     provincias_with_id.rename('provincia', 'provincia_provincias')
#     provincias_with_id.rename('id_departamento', 'id_departamento_provincias')


#     # Perform the join after renaming the column
#     provincias_with_provincia = provincias_with_departamento.join(provincias_with_id, 
#                         how='inner', 
#                         left_on='provincia',
#                         right_on='provincia_provincias')


#     # Obtener distritos únicos
#     distritos_unicos = provincias_with_provincia.groupby(by='distrito', agg={'id_departamento': 'first', "id_provincia":"first"}).sort(by='distrito')
#     # Crear un nuevo campo 'id_provincia' que combina 'id_departamento' con un número adicional
#     distritos_unicos['id_distrito'] = distritos_unicos['id_provincia'] * 10

#     # Convertir y guardar en HDF5
#     distritos_unicos.export_hdf5(str(file_hdf5_provincias))
#     print(vaex.open(str(file_hdf5_provincias)).copy())
#     print("ARCHIVO HDF5 generado correctamente!")


# import vaex

# # Leer un archivo Parquet
# read_parquet = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_CALLES.hdf5")

# # Obtener los valores únicos de la columna 'provincia'
# unique_provincias = read_parquet['provincia'].unique()

# # Crear un DataFrame con la columna 'provincia' que contiene valores únicos
# unique_provincias_df = vaex.from_arrays(provincia=unique_provincias)

# # # Convertir y guardar en HDF5
# # unique_provincias_df.export_hdf5("/home/ubuntu/clean_architecture/public/data/PERU_CALLES_VIAS.hdf5")
# # print(vaex.open(str(file_hdf5_provincias)).copy())
# print("ARCHIVO HDF5 generado correctamente!")



# def create_file_hdf5_address_street(file_parquet, file_hdf5_departamento):
#     # Leer un archivo Parquet
#     read_parquet = vaex.open(str(file_parquet), usecols=['OBJECTID', 'departamento'])

#     read_parquet = read_parquet[['departamento']]
#     vaex_df = vaex.from_pandas(read_parquet)

#     # Obtener valores únicos de la columna 'departamento'
#     unique_departamentos = vaex_df['departamento'].unique()

#     # Crear un DataFrame con los valores únicos de 'departamento' y asignar un ID único a cada uno
#     unique_departamentos_with_id = vaex.from_arrays(
#         id_departamento=range(len(unique_departamentos)),
#         departamento=unique_departamentos
#     )

#     # Convertir y guardar en HDF5
#     unique_departamentos_with_id.export_hdf5(str(file_hdf5_departamento))
#     print(vaex.open(str(file_hdf5_departamento)).copy())
#     print("ARCHIVO HDF5 generado correctamente!")


# def create_file_hdf5_address_streets(file_parquet, file_hdf5):
#     # Leer un archivo Parquet
#     read_parquet = vaex.open(str(file_parquet), usecols=['OBJECTID', 'departamento', 'provincia', 'distrito', 'direcc', 'lat_y', 'lon_x', 'geometry'])

#     read_parquet = read_parquet[['OBJECTID', 'departamento', 'provincia', 'distrito', 'direcc', 'numpuerta', 'lon_x', 'lat_y']]
#     vaex_df = vaex.from_pandas(read_parquet)

#     # Convert and save to HDF5
#     vaex_df.export_hdf5(str(file_hdf5))
#     print("ARCHIVO HDF5 generado correctamente!")
