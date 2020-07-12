import pandas as pd

dict_key_of_list = {
    'name': ['moshe', 'aharon', 'yoshef'],
    'profession': ['c#', 'java', 'python'],
    'experience_years': [5, 2, 12]
}
dict_key_of_list['name'][1:]
for l in dict_key_of_list.values():
    print([l])

dict_key_of_list_in_df = pd.DataFrame(dict_key_of_list)
dict_key_of_list_in_df

print(dict_key_of_list_in_df.iloc[[0, 2], [1, 2]])
type(dict_key_of_list_in_df)

print(dict_key_of_list_in_df.loc[0:2, ['name']])
type(dict_key_of_list_in_df.loc[[0, 2], ['name']])

print(dict_key_of_list_in_df.loc[0][1])

dict_key_of_list_in_df['name']

# define specific columns:
print(dict_key_of_list_in_df.loc[:, 'name':'experience_years'])
