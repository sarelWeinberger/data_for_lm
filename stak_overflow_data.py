import pandas as pd

data_frame = pd.read_csv(r'C:\Users\User\Desktop\git_clone\survey_results_public.csv', index_col='UndergradMajor')
schema_df = pd.read_csv((r'C:\Users\User\Desktop\git_clone\survey_results_schema.csv'))
#print(data_frame.info())

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
print(schema_df)
#print(data_frame.head(2))

data_frame['Hobbyist'].value_counts()
data_frame.head()

data_frame.set_index('Student', inplace=True)
data_frame.sort_index(ascending=True)
data_frame.tail()

data_frame.loc['Yes, full-time'] #['Employed full-time']
# data_frame.sort_index(['Hobbyist'],inplace=True)
# df = data_frame.sort_index()
# df
# data_frame

#reset:
data_frame.reset_index()

