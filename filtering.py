import stak_overflow_data as sod
import pandas as pd

filt = sod.data_frame['Hobbyist'] == 'Yes'
filt_df = pd.DataFrame(filt)
#or
df1 = sod.data_frame[filt]
print(type(df1))
#or
df2 = sod.data_frame[sod.data_frame['Hobbyist'] == 'Yes']
print(type(df2))
# compere two df
# if df1 & df2:
#     print('the same way of filtering')
#print(pd.data_frame(filt))

#print(sod.data_frame.head())