import  stak_overflow_data as sod
import  pandas as pd

filt = sod.data_frame['Hobbyist'] == 'Yes'
filt_df = pd.DataFrame(filt)
#sod.data_frame(filt)
print(sod.data_frame.head())