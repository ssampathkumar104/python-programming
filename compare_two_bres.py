"""
compare_two_bres.py

Compare two Excel workbooks cell-by-cell and produce a validation sheet.

This script expects two Excel files with the same columns and the same number
of rows. It normalizes values to strings (stripping whitespace and converting
NaN to an empty string) and compares corresponding cells row-by-row. The
output is an Excel file with one validation column per input column containing
the literal values "Match" or "Mismatch" for each row.

Usage:
    python compare_two_bres.py

Inputs (hard-coded filenames):
    - ADC_OLD_OG_v1.xlsx
    - ADC_NEW_OG_v1.xlsx

Output (hard-coded filename):
    - comparison_output_OG_v10.xlsx
"""

import pandas as pd

# Read the two input Excel files into pandas DataFrames
book1 = pd.read_excel("ADC_OLD_OG_v1.xlsx")
book2 = pd.read_excel("ADC_NEW_OG_v1.xlsx")

# Ensure each DataFrame has a clean, zero-based integer index for row-wise
# comparisons (drops any existing index column that may have been read).
book1 = book1.reset_index(drop=True)
book2 = book2.reset_index(drop=True)

# Prepare an empty DataFrame to collect per-column validation results
result = pd.DataFrame()

# Iterate over columns in the first workbook. For each column we will produce
# a new column in `result` named '<original_column>_Validation' that contains
# 'Match' when the two cells are equal and 'Mismatch' otherwise.
for col in book1.columns:

    # Normalize values from both DataFrames to comparable strings:
    #  - cast to str to avoid type-mismatch issues
    #  - strip surrounding whitespace
    #  - replace NaN with an empty string
    col1 = book1[col].astype(str).str.strip().fillna("").values
    col2 = book2[col].astype(str).str.strip().fillna("").values

    comparison = []

    # Compare corresponding cells row-by-row
    for v1, v2 in zip(col1, col2):
        comparison.append("Match" if v1 == v2 else "Mismatch")

    # Store the comparisons in the result DataFrame
    result[col + "_Validation"] = comparison

# Write the result to an Excel file without an index column
result.to_excel("comparison_output_OG_v10.xlsx", index=False)

print("Comparison completed")