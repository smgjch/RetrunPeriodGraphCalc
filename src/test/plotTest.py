import pandas as pd
import matplotlib.pyplot as plt
import os

from src.Directory import Directory

os.chdir("../../")
print(os.getcwd())

data_dir = "../../data"
origin_sheets = "cleaned_databases"
sliced_sheets = "sliced_data_sheets"
original_path = f'{data_dir}/{origin_sheets}'
sliced_path = f'{data_dir}/{sliced_sheets}'
original_folder = Directory(original_path)
countries = original_folder.get_directories()

def plot(df1, df2, country, event):
    ax = df1.plot()
    df2.plot(ax=ax)

def get_df(country, event):
    appendix = f"/{country}/{event}"
    ori_sheet_path = f"{original_path}{appendix}"
    sli_sheet_path = f"{sliced_path}{appendix}"
    ori_df = pd.read_csv(ori_sheet_path)
    sli_df = pd.read_csv(sli_sheet_path)
    ori_df = ori_df[['Year', ' DataCards']].set_index('Year')
    sli_df = sli_df[['Year', ' DataCards']].set_index('Year')
    return ori_df, sli_df

def main():
    count = 0
    for country in countries:
        events = country.get_files()
        for event in events:
            c, e = country.get_dirname(), event.get_filename()
            df1, df2 = get_df(c, e)
            total_datacards = df1[' DataCards'].sum()
            if total_datacards < 10000:
                continue
            plot(df1, df2, c, e)
            count += 1