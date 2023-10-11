import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######LOAD DATA###########
df = pd.read_csv("/Users/filippo/ScrivaniaLocale/E-HealthProject/dataset.csv",index_col=0)
print(df.head(10))

#####DATA INSPECTION#########

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