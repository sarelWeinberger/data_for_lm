import csv
import pandas as pd
survey_res_lines = []

data_frame = pd.read_csv(r'C:\Users\User\Desktop\git_clone\survey_results_public.csv')
schema_df = pd.read_csv((r'C:\Users\User\Desktop\git_clone\survey_results_schema.csv'))
print(data_frame.info())
print(schema_df.info())
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(data_frame.head(2))

