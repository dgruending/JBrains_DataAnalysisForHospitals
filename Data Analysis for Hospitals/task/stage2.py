import pandas as pd

from stage1 import read_all_test_files

# Stage 2/5: Merge them
# Requirements:
# 1.    After all the libraries imports write the following line of code:
#       pd.set_option('display.max_columns', 8)
# 2.    Read 3 CSV files with datasets
# 3.    Change the column names. All column names in the sports and prenatal tables must match the column names
#       in the general table
# 4.    Merge the data frames into one. Use the ignore_index = True parameter and the following order:
#       general, prenatal, sports
# 5.    Delete the Unnamed: 0 column
# 6.    Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30


def merge_cleanup(general_df, prenatal_df, sports_df):
    # Equalize column names
    prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender', }, inplace=True)
    sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
    merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
    # First column needs to be deleted this time
    merged_df.drop(columns=['Unnamed: 0'], inplace=True)
    return merged_df


def main():
    general_df, prenatal_df, sports_df = read_all_test_files()
    general_df = merge_cleanup(general_df, prenatal_df, sports_df)
    print(general_df.sample(n=20, random_state=30))
