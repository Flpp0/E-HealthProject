import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
directory = r'C:\Users\Utente\Desktop\E-health project\dataset_project_eHealth20232024.csv'

######LOAD DATA###########
df = pd.read_csv(directory)
print(df.head(10)) #all the questions are mandatory so there are no null values

#####DATA INSPECTION#########

#Since the answers about climate change questionnaires aren't useful for our analysis we can drop them from df
df = df.drop(['ccs_1','ccs_2','ccs_3','ccs_4','ccs_5','ccs_6','ccs_7','ccs_8','ccs_9','ccs_10','ccs_11','ccs_12'], axis=1)
df = df.drop(['heas_1','heas_2','heas_3','heas_4','heas_5','heas_6','heas_7','heas_8','heas_9','heas_10','heas_11','heas_12','heas_13'], axis=1)
print(df.head())
#Dimensions
print('Dimensions: ', df.shape) #160x29
#Statistics
print(df.info)


#Age distribution to find a serious game suitable for our population
plt.hist(df.age, bins=25) #--> la popolazione si concentra tra i 18 e i 55
plt.title('Age')
plt.show()

### PHQ questionnaire
# List of questionnaire column names
questionnaire_columns_phq = ['phq_1', 'phq_2', 'phq_3', 'phq_4', 'phq_5', 'phq_6', 'phq_7', 'phq_8', 'phq_9']

# Create subplots for the histograms
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(9, 9))
axes = axes.flatten()
x_val = [0, 1, 2, 3]

# Create histograms for each column and plot them in subplots
for i, column_name in enumerate(questionnaire_columns_phq):
    ax = axes[i]

    ax.hist(df[column_name], bins=4, rwidth=0.8)
    ax.set_xlabel('Responses')
    ax.set_ylabel('Frequency')
    ax.set_title(column_name)
    ax.set_xticks(x_val)
    ax.set_xticklabels(x_val)

plt.suptitle('PHQ Questionnaire')
plt.tight_layout()
plt.show()


###gad questionnaire
# List of questionnaire column names
questionnaire_columns_gad = ['gad_1', 'gad_2', 'gad_3', 'gad_4', 'gad_5', 'gad_6', 'gad_7']

# Create subplots for the histograms
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(9, 9))
axes = axes.flatten()
x_val = [0, 1, 2, 3]

# Create histograms for each column and plot them in subplots
for i, column_name in enumerate(questionnaire_columns_gad):
    ax = axes[i]
    ax.hist(df[column_name], bins=4, rwidth=0.8)
    ax.set_xlabel('Responses')
    ax.set_ylabel('Frequency')
    ax.set_title(column_name)
    ax.set_xticks(x_val)
    ax.set_xticklabels(x_val)

plt.suptitle('GAD Questionnaire')
plt.tight_layout()
plt.show()


###eheals questionnaire
# List of questionnaire column names
questionnaire_columns_eheals = ['eheals_1', 'eheals_2', 'eheals_3', 'eheals_4', 'eheals_5', 'eheals_6', 'eheals_7', 'eheals_8']

# Create subplots for the histograms
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(9, 9))
axes = axes.flatten()
x_val = [1, 2, 3, 4, 5]

# Create histograms for each column and plot them in subplots
for i, column_name in enumerate(questionnaire_columns_eheals):
    ax = axes[i]
    ax.hist(df[column_name], bins=5, rwidth=0.8)
    ax.set_xlabel('Responses')
    ax.set_ylabel('Frequency')
    ax.set_title(column_name)
    ax.set_xticks(x_val)
    ax.set_xticklabels(x_val)

plt.suptitle('EHEALS Questionnaire')
plt.tight_layout()
plt.show()