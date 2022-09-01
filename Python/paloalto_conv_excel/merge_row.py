import pandas as pd

file_path = 'D:/02_Programming/Python/paloalto_conv_excel/policy.xlsx'
df = pd.read_excel(file_path, na_filter=False)
