import pandas as pd

pd.set_option('display.max_columns',14)
# data from kaggle url: https://www.kaggle.com/nareshbhat/health-care-data-set-on-heart-attack-possibility
heart_data = pd.read_csv(r'C:\Users\User\Desktop\git_clone\heart.csv')
print(heart_data.head())
# data explain form the same place
with open(r"C:\Users\User\Desktop\git_clone\heart_dec.txt", 'r+', encoding='utf=8') as file:
    description = file.readlines()
print(description[:])

# use specific data:
heart_data.drop(columns=['restecg'], inplace=True)

# calc new val for, to diffrent column for prediction:
heart_data['full chances'] = heart_data['age'].apply(float) - (heart_data['exang'].apply(float) * 20)
print(heart_data.head())

#full sum:
print(heart_data['full chances'].sum())

# change_specific column name:
heart_data.rename(columns={'fbs' : 'fasting_blood_sugar' },inplace=True)
print(heart_data.head())

# get sum of  chances for the targeted people:
filt = heart_data['target'] == 1
heart_data[filt]
print(heart_data[filt]['full chances'].sum())

# get sum of  chances for the untargeted people:
filt = heart_data['target'] != 1
heart_data[filt]
print(heart_data[filt]['full chances'].sum())
