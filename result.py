import pandas as pd

get_info = input('Ievadiet reģiona nosaukumu: ').strip()

df = pd.read_excel("description.xlsx", sheet_name="LookupAREA")

area_value = df.loc[df['Description'] == get_info, 'Area'].values

if len(area_value) == 0:
    print("Reģions netika atrasts.")
else:
    print("Reģiona kods/area:")
    print(area_value)
    area_value = area_value[0] 

    area_value = str(area_value) 

    df_data = pd.read_csv("data.csv")

    geo_count_sum = df_data.loc[df_data['Area'] == area_value, 'geo_count'].sum()

    print("Savākta informācija par geo_count vērtībām no data.csv un to summa:")
    print(geo_count_sum) 
