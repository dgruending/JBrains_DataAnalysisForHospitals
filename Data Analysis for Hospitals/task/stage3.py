import pandas as pd
import numpy as np

from stage1 import read_all_test_files
from stage2 import merge_cleanup

# Stage 3/5: Improve your dataset
# Steps 1-5 are identical to stage 2
# Requirements:
# 1.    After all the libraries imports write the following line of code:
#       pd.set_option('display.max_columns', 8)
# 2.    Read the CSV files with datasets
# 3.    Change the column names. The column names of the sports
#       and the prenatal tables must match the column names of the general table
# 4.    Merge the data frames into one. Use the ignore_index = True parameter
#       and the following order: general, prenatal, sports
# 5.    Delete the Unnamed: 0 column
# 6.    Delete all the empty rows
# 7.    Correct all the gender column values to f and m respectively
# 8.    Replace the NaN values in the gender column of the prenatal hospital with f
# 9.    Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns
#       with zeros
# 10.   Print shape of the resulting data frame
# 11.   Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30


def improve_dataset(df):
    # Delete all rows considered by pandas empty
    df.dropna(how='all', axis=0, inplace=True)
    df['gender'] = df['gender'].replace(['female', 'woman', np.nan], 'f')
    df['gender'] = df['gender'].replace(['male', 'man'], 'm')
    df = df.fillna(0)
    return df


def main():
    # As required for the tests
    pd.set_option('display.max_columns', 8)
    general_df, prenatal_df, sports_df = read_all_test_files()
    merged_df = merge_cleanup(general_df, prenatal_df, sports_df)
    merged_df = improve_dataset(merged_df)
    print(merged_df.shape)
    print(merged_df.sample(n=20, random_state=30))
