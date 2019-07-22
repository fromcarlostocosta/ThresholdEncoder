# Packages
import pandas as pd
from tabulate import tabulate

# Simple encoder for limiting your categorical feature based on threshold %
# Arguments: dataframe, column, threshold
# Return: mapping with updated categories

def threshold_encoder(df, column, threshold = 0):
    perc = pd.DataFrame(df[column].value_counts(True)).reset_index()
    perc = perc.loc[perc[column]>=threshold,:]
    perc.columns=[column,'freq']
    # Optional
    # Printing values that will be kept
    print(tabulate(perc, headers=perc.columns, tablefmt='psql'))
    return dict(zip(perc[column], perc[column]))
