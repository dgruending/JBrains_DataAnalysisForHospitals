import pandas as pd

# Stage 1/5: Upload the data
# Requirements:
# 1.    After all the libraries imports write the following line of code:
#       pd.set_option('display.max_columns', 8)
#       It sets the number of columns, which pandas lets to display in the terminal.
#       Unfortunately, this number differs occasionally and causes problems in the tests, so we need to fix the number.
# 2.    Read 3 CSV files containing the datasets
# 3.    Print the first 20 rows of each data frame. Use the following order: 'general', 'prenatal', 'sports'


def main():
    # to match the example output, one should use index_col=0, but that doesn't pass the test
    general_df = pd.read_csv("test/general.csv")
    prenatal_df = pd.read_csv("test/prenatal.csv")
    sport_df = pd.read_csv("test/sports.csv")
    print(general_df.head(20))
    print(prenatal_df.head(20))
    print(sport_df.head(20))
