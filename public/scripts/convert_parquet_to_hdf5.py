import pandas as pd
import vaex

df = vaex.open("/home/ubuntu/clean_architecture/public/data/merged_output.hdf5")
print(df)
# df.export_hdf5("/home/ubuntu/clean_architecture/public/data/merged_output.hdf5")
# # Assuming 'id' is the common column in both CSV files
# df1 = pd.read_csv("/home/ubuntu/clean_architecture/public/data/Manzanas.csv", dtype={'Ubigeo_1': str})
# df2 = pd.read_csv("/home/ubuntu/clean_architecture/public/data/ubigueos_peru.csv", dtype={'Ubigeo_1': str})

# # Merge the CSV files based on the 'id' column
# merged_df = pd.merge(df1, df2, on='Ubigeo_1', how='inner')  # Change 'how' as needed (inner, outer, left, right)
# print(merged_df)
# # Save the merged data to a new CSV file
# merged_df.to_csv('/home/ubuntu/clean_architecture/public/data/merged_output.csv', index=False)

# print("CSV files merged and saved successfully.")