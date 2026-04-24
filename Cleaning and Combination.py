import pandas as pd
import glob

files = glob.glob('*.csv')

df_list = []

for file in files:
    print("Reading:", file)

    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    header_row = None
    for i, line in enumerate(lines):
        if 'state_name' in line.lower() and 'county_name' in line.lower():
            header_row = i
            break

    print("Header row:", header_row)

    df = pd.read_csv(
        file,
        skiprows=header_row,
        sep=',',
        engine='python',
        on_bad_lines='skip'
    )

    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)


combined_df['state_name'] = combined_df['state_name'].astype(str).str.strip()

# Filter only New York
ny_df = combined_df[
    combined_df['state_name'].str.upper() == 'NEW YORK'
]


ny_df.to_csv('NewYork_SAHIE_Combined.csv', index=False)

print(ny_df.head())
print("Total New York Rows:", len(ny_df))