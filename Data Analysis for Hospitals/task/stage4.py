import pandas as pd

from stage1 import read_all_test_files
from stage2 import merge_cleanup
from stage3 import improve_dataset

# Stage 4/5:
# Steps 1-8 are the same as steps 2-9 in the third stage.
# Requirements:
# 1.    Read the CSV files with datasets.
# 2.    Change the column names.
#       The column names of the sports and prenatal tables must match the column names of the general table.
# 3.    Merge the data frames into one. Use the ignore_index = True parameter
#       and the following order: general, prenatal, sports.
# 4.    Delete the Unnamed: 0 column.
# 5.    Delete all the empty rows.
# 6.    Correct all the gender column values to f and m respectively.
# 7.    Replace the NaN values in the gender column of the prenatal hospital with f.
# 8.    Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns
#       with zeros.
# 9.    Answer the 1-5 questions using the pandas library methods.
#       Output the answers on the separate lines in the format given in the Example section.
# Questions:
# 1.    Which hospital has the highest number of patients?
# 2.    What share of the patients in the general hospital suffers from stomach-related issues?
#       Round the result to the third decimal place.
# 3.    What share of the patients in the sports hospital suffers from dislocation-related issues?
#       Round the result to the third decimal place.
# 4.    What is the difference in the median ages of the patients in the general and sports hospitals?
# 5.    After data processing at the previous stages, the blood_test column has three values: t= a blood test was taken,
#       f= a blood test wasn't taken, and 0= there is no information.
#       In which hospital the blood test was taken the most often?
#       How many blood tests were taken?


def main():
    general_df, prenatal_df, sports_df = read_all_test_files()
    merged_df = merge_cleanup(general_df, prenatal_df, sports_df)
    merged_df = improve_dataset(merged_df)
    print("The answer to the 1st question is {}".format(merged_df['hospital'].value_counts().idxmax()))
