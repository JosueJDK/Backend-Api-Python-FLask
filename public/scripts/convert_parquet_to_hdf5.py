import vaex
# df["data"] = df['UBI_DEPARTAMENTO_PPROVINCIA_DISTRITO']  + "="+  df['ROTULO']   + "="+    df['UBI_DEPARTAMENTO']  + "="+  df['UBI_PROVINCIA'] + "="+  df['UBI_DISTRITO']  + "="+  df['UBI_DEPARTAMENTO_PROVINCIA']
# data_unique = df["data"].unique()
# vaex_column = vaex.from_arrays(data=data_unique)
print(vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_CENTROS_POBLADOS.hdf5"))

# import pandas as pd
# import vaex
# import unidecode

# def clean_text(text):
#     # Quitar tildes y caracteres especiales y convertir a mayúsculas
#     cleaned_text = unidecode.unidecode(text).upper()
#     # Eliminar espacios en blanco al final de la cadena
#     cleaned_text = cleaned_text.rstrip()
#     return cleaned_text

# df = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_DISTRITOS.hdf5")
# df["DISTRITO"] = df["DISTRITO"].apply(clean_text)
# df["PROVINCIA"] = df["PROVINCIA"].apply(clean_text)
# df["DEPARTAMENTO"] = df["DEPARTAMENTO"].apply(clean_text)
# print(df.export_hdf5("/home/ubuntu/clean_architecture/public/data/PERU_DISTRITOS_.hdf5"))
# def ubigueos_peru_dep(codigo):
#     ubi = str(codigo)
#     if len(ubi) >= 2:  # Verificar que hay al menos dos caracteres
#         return str(ubi[0:2])  # Obtener los primeros dos caracteres
#     else:
#         print("false")

# def ubigueos_peru_prov(codigo):
#     ubi = str(codigo)
#     if len(ubi) >= 2:  # Verificar que hay al menos dos caracteres
#         return str(ubi[2:4])  # Obtener los primeros dos caracteres
#     else:
#         print("false")

# def ubigueos_peru_dist(codigo):
#     ubi = str(codigo)
#     if len(ubi) >= 2:
#         return str(ubi[4:6])
#     else:
#         print("false")



# # df.rename("ubigeo", "UBIGEO_DISTRITO")
# # df.rename("distrito", "DISTRITO")
# # df.rename("provincia", "PROVINCIA")
# # df.rename("departamen", "DEPARTAMENTO")
# # df.rename("geometry", "GEOMETRY_DISTRITO")

# # # print(df[['UBIGEO_DISTRITO', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO', 'GEOMETRY_DISTRITO', 'UBI_DEPARTAMENTO', 'UBI_PROVINCIA', 'UBI_DISTRITO', 'UBI_DEPARTAMENTO_PROVINCIA']])

# # df_distrito = df[['UBIGEO_DISTRITO', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO', 'UBI_DEPARTAMENTO', 'UBI_PROVINCIA', 'UBI_DISTRITO', 'UBI_DEPARTAMENTO_PROVINCIA']]
# # df_distrito.export_hdf5("public/data/PERU_DISTRITOS.hdf5")
# # print(df_distrito)

# # def convert_int(integer):
# #     if integer is None or integer in 'None':
# #         return None  # O cualquier otro valor predeterminado que desees

# #     try:
# #         return int(integer)
# #     except (ValueError, TypeError):
# #         return integer  # Devuelve el mismo valor si no se puede convertir a entero

# # df = vaex.open("/home/ubuntu/clean_architecture/public/data/PERU_CENTROS_POBLADOS.hdf5")
# # print(df)