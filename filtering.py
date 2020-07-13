import stak_overflow_data as sod
import pandas as pd

pd.set_option('display.max_columns',6)
filt = sod.data_frame['Hobbyist'] != 'Yes'
filt_df = pd.DataFrame(filt)
print(filt_df.head())
#or
df1 = sod.data_frame[filt]
print((df1.head()))
print(f"years code specelist {df1['YearsCode'].median()}")
#or
df2 = sod.data_frame[sod.data_frame['Hobbyist'] == 'Yes']
print((df2).head())
print(f"years code hobyst {df2['YearsCode'].median()}")

# compere two df
# if df1 & df2:
#     print('the same way of filtering')
#print(pd.data_frame(filt))

#print(sod.data_frame.head())