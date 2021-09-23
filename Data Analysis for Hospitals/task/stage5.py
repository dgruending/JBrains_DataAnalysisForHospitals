import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from stage1 import read_all_test_files
from stage2 import merge_cleanup
from stage3 import improve_dataset

# Stage 5/5: Visualize it!
# Steps 1-8 are the same as in the previous stage.
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
# 9.    Answer questions 1-3. Output the answers in the specified format.
#       The answers to the first two questions should be formatted as in the examples.
#       No special form is required to answer the third question
# Questions:
# 1.    What is the most common age of a patient among all hospitals?
#       Plot a histogram and choose one of the following age ranges: 0 - 15, 15 - 35, 35 - 55, 55 - 70, or 70 - 80
# 2.    What is the most common diagnosis among patients in all hospitals? Create a pie chart
# 3.    Build a violin plot of height distribution by hospitals. Try to answer the questions.
#       What is the main reason for the gap in values? Why there are two peaks,
#       which correspond to the relatively small and big values? No special form is required to answer this question.
# Example:
# >The answer to the 1st question: 0 - 15
# >The answer to the 2nd question: flu
# >The answer to the 3rd question: It's because...


def question_1(df):
    df.plot(y="age", kind="hist", bins=[0, 15, 35, 55, 70, 80])
    plt.savefig('question_1.jpg', bbox_inches='tight')
    plt.clf()

    # Answer could be read from histogram (15 - 35) and hardcoded, but a different approach is used
    # Create a new Dataframe with the age bins and their corresponding count
    age_bins_df = pd.DataFrame([df.loc[(df.age >= 0) & (df.age < 15), "age"].count(),
                                df.loc[(df.age >= 15) & (df.age < 35), "age"].count(),
                                df.loc[(df.age >= 35) & (df.age < 55), "age"].count(),
                                df.loc[(df.age >= 55) & (df.age < 70), "age"].count(),
                                df.loc[(df.age >= 70) & (df.age < 80), "age"].count()],
                               index=["0 - 15", "15 - 35", "35 - 55", "55 - 70", "70 - 80"], columns=["count"])

    print(f"The answer to the 1st question: {age_bins_df['count'].idxmax()}")


def question_2(df):
    df.groupby("diagnosis").size().plot(kind="pie")
    plt.savefig('question_2.jpg', bbox_inches='tight')
    plt.clf()

    # Pie chart shows pregnancy as most common diagnosis
    print(f"The answer to the 2nd question: {df['diagnosis'].value_counts().idxmax()}")


def question_3(df):
    fig, axes = plt.subplots()
    sns.violinplot(y="height", data=df, axes=axes)
    plt.savefig('question_3.jpg', bbox_inches='tight')
    plt.clf()

    print("The answer to the 3rd question: It's because the height is measured in meter for general and prenatal, "
          "but in feet for sports.")


def main():
    general_df, prenatal_df, sports_df = read_all_test_files()
    merged_df = merge_cleanup(general_df, prenatal_df, sports_df)
    df = improve_dataset(merged_df)
    question_1(df)
    question_2(df)
    question_3(df)
