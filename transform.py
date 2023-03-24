#### Packages ####

import pandas as pd

import numpy as np


#### Extract ####

df = pd.read_csv("data/diabetic_data_modified.csv")





#### Transform ####

## standardization ##

# let's remove duplicate data

df = df.drop_duplicates()


# let's replace all question marks with a blank space to avoid confusion
df = df.replace('?', '')



## race ##

# assign the elements in the "race" column with a corresponding number

race_to_number = {'AfricanAmerican': 1, 
                  'Asian': 2, 
                  'Caucasian': 3, 
                  'Hispanic': 4, 
                  'Other': 5}

df['race'] = df['race'].replace(race_to_number)

print(df)


## gender ##

# similar deal as race with far fewer elements

gender_to_number = {'Male': 0, 
                    'Female': 1}

df['gender'] = df['gender'].replace(gender_to_number)

print(df)


## age ##

# taking a number from the age interval randomly with np

age_to_number = {'[0-10)': np.random.randint(0, 10),
                 '[10-20)': np.random.randint(10, 20),
                 '[20-30)': np.random.randint(20, 30),
                 '[30-40)': np.random.randint(30, 40),
                 '[40-50)': np.random.randint(40, 50),
                 '[50-60)': np.random.randint(50, 60),
                 '[60-70)': np.random.randint(60, 70),
                 '[70-80)': np.random.randint(70, 80),
                 '[80-90)': np.random.randint(80, 90),
                 '[90-100)': np.random.randint(90, 100)
                 }

df['age'] = df['age'].replace(age_to_number)

print(df['age'])


## payer code ## 

# let's drop it.

df = df.drop('payer_code', axis=1)

df.columns

# rest of the columns seem to check out. when in doubt, we inquire to get more info. last order of business is readmitted.


## readmitted

readmitted_corrected = {'>30': 'NO', 
                    '<30': 'YES'}

df['readmitted'] = df['readmitted'].replace(readmitted_corrected)

print(df)




#### LOAD ####

df.to_csv('data/diabetic_data_modified_final.csv')