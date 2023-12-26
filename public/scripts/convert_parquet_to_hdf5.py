import vaex

def create_file_hdf5_address_street(file_parquet, file_hdf5):
    # Leer un archivo Parquet
    read_parquet = vaex.open(file_parquet, usecols=['departamento', 'provincia', 'distrito', 'direcc', 'lat_y', 'lon_x', 'geometry'])

    read_parquet = read_parquet[['departamento', 'provincia', 'distrito', 'direcc', 'numpuerta', 'lon_x', 'lat_y']]
    vaex_df = vaex.from_pandas(read_parquet)

    # Convert and save to HDF5
    vaex_df.export_hdf5(file_hdf5)
    print("ARCHIVO HDF5 generado correctamente!")
