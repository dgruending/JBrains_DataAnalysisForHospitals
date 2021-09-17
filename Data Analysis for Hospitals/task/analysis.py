import pandas as pd

import stage1

# call subroutine for current stage
if __name__ == "__main__":
    # As required for the tests
    pd.set_option('display.max_columns', 8)
    stage1.main()
