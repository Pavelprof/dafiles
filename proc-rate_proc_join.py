import pandas as pd
from fuzzywuzzy import fuzz

# Чтение данных из файлов
output_all_data = pd.read_excel(r'C:\Users\Павел\Desktop\output_all.xlsx')
rate_proc_data = pd.read_excel(r'C:\Users\Павел\Desktop\rate_proc.xlsx')

# Объединение данных по условию
merged_data = pd.DataFrame(columns=output_all_data.columns)  # Создаем пустой DataFrame для объединенных данных

for _, row in output_all_data.iterrows():
    model = row['model']
    matching_rows = rate_proc_data[rate_proc_data['Model_full'].str.contains(model, case=False)]

    if not matching_rows.empty:
        best_match_row = matching_rows.iloc[0]  # Берем первую найденную строку
        merged_row = pd.concat([row, best_match_row], axis=0)
        merged_data = merged_data._append(merged_row, ignore_index=True)

# Сохранение результата в новый файл
merged_data.to_excel(r'C:\Users\Павел\Desktop\output_merged.xlsx', index=False)
