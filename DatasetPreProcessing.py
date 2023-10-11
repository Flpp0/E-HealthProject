import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/filippo/ScrivaniaLocale/E-HealthProject/originalDataset.csv")
print(df.shape)
df.drop_duplicates(inplace=True)
print(df.shape) # Dropped 10 duplicates

print(df.info())

print(df.isna().sum())

df_isNan = df.isna()
df.loc[56,'age'] = round(df['age'].mean())

df_education = df['education']
df_education.fillna(method='ffill',inplace=True)

df_phq_2 = df['phq_2']
df_phq_3 = df['phq_3']

df_phq_2.fillna(method='ffill',inplace=True)
df_phq_3.fillna(method='bfill',inplace=True)

df_phq_7 = df['phq_7']
df_phq_7.fillna(method='ffill',inplace=True)
df_phq_8 = df['phq_8']
df_phq_8.fillna(method='bfill',inplace=True)
df_phq_9 = df['phq_9']
df_phq_9.fillna(method='bfill',inplace=True)

df_gad_1 = df['gad_1']
df_gad_1.fillna(method='ffill',inplace=True)

df_gad_3 = df['gad_3']
df_gad_4 = df['gad_4']
df_gad_3.fillna(method='ffill',inplace=True)
df_gad_4.fillna(method='bfill',inplace=True)
df_gad_5 = df['gad_5']
df_gad_6 = df['gad_6']
df_gad_5.fillna(method='ffill',inplace=True)
df_gad_6.fillna(method='bfill',inplace=True)
df_gad_7 = df['gad_7']
df_gad_7.fillna(method='ffill',inplace=True)

df.drop(axis=1,labels=["ccs_1","ccs_2","ccs_3","ccs_4","ccs_5","ccs_6","ccs_7","ccs_8","ccs_9",
                       "ccs_10","ccs_11","ccs_12"],inplace=True)

# Removing questionnaire not used

values_eheals_1 = list(df.loc[:,'eheals_1'])

values_eheals_1, count = np.unique(values_eheals_1, return_counts=True)

print(values_eheals_1)
print(count)

df_eheals_1 = df['eheals_1']
df_eheals_1.fillna(method='ffill',inplace=True)
df_eheals_2 = df['eheals_2']
df_eheals_2.fillna(method='bfill',inplace=True)
df_eheals_3 = df['eheals_3']
df_eheals_3.fillna(method='ffill',inplace=True)
df_eheals_4 = df['eheals_4']
df_eheals_4.fillna(method='bfill',inplace=True)
df_eheals_5 = df['eheals_5']
df_eheals_5.fillna(method='ffill',inplace=True)
df_eheals_8 = df['eheals_8']
df_eheals_8.fillna(method='bfill',inplace=True)

df_heas_1 = df['heas_1']
df_heas_1.fillna(method='ffill',inplace=True)
df_heas_2 = df['heas_2']
df_heas_2.fillna(method='bfill',inplace=True)
df_heas_3 = df['heas_3']
df_heas_3.fillna(method='ffill',inplace=True)
df_heas_9 = df['heas_9']
df_heas_9.fillna(method='bfill',inplace=True)
df_heas_10 = df['heas_10']
df_heas_10.fillna(method='ffill',inplace=True)
df_heas_12 = df['heas_12']
df_heas_12.fillna(method='bfill',inplace=True)
df_heas_13 = df['heas_13']
df_heas_13.fillna(method='bfill',inplace=True)

df.drop(axis=1,labels=["heas_1","heas_2","heas_3","heas_4","heas_5","heas_6","heas_7","heas_8","heas_9",
                       "heas_10","heas_11","heas_12","heas_13"],inplace=True)

print(df.isna().sum())
print('Total numeber of missing values: ', df.isna().sum().sum())

df.to_csv("/Users/filippo/ScrivaniaLocale/E-HealthProject/dataset.csv")

