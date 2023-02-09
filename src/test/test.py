__all__ = ["slicing"]

import os
from typing import Optional, List
import pandas as pd

from utils import Directory


class Slice:
    _SLICED_FOLDER_NAME = "sliced_data_sheets"
    _CLEANED_FOLDER_NAME = "cleaned_databases"

    def __init__(self):
        self.__data_folder: Optional[Directory] = None
        self.__cleaned_folder: Optional[Directory] = None
        self.__sliced_folder: Optional[Directory] = None
        self.__countries: Optional[List[Directory]] = None

    def __initialise(self):
        self.__cleaned_folder = \
            self.__data_folder.find_directory(
                Slice._CLEANED_FOLDER_NAME
            )
        self.__data_folder.create_subdirectory(
            Slice._SLICED_FOLDER_NAME
        )
        self.__sliced_folder = \
            self.__data_folder.find_directory(
                Slice._SLICED_FOLDER_NAME
            )
        self.__countries = self.__cleaned_folder.get_directories()

    @staticmethod
    def __get_data_quantity(target_year: int, df: pd.DataFrame):
        return df.loc[df['Year'] <= target_year, ' DataCards'].sum()

    def __save_dataframe(self, country, event, df):
        folder_path = self.__sliced_folder.get_path() + \
               f"/{country.get_dirname()}"
        os.makedirs(folder_path, exist_ok=True)
        filepath = folder_path + f"/{event.get_filename()}"
        df.to_csv(filepath)

    def start_slice(self, data_folder: Directory):
        self.__data_folder = data_folder
        self.__initialise()
        self.__slice_for_all_countries()

    def __slice_for_all_countries(self):
        for country in self.__countries:
            self.__slice_for_one_country(country)

    def __slice_for_one_country(self, country: Directory):
        events = country.get_files()
        for event in events:
            sliced_dataframe = \
                Slice.__slice_for_one_event(event.get_filepath())
            self.__save_dataframe(country, event, sliced_dataframe)

    @staticmethod
    def __slice_for_one_event(event_filepath: str):
        df = pd.read_csv(event_filepath)
        total_datacards = df[' DataCards'].sum()
        ratio = 0.05
        target_datacards = int(ratio * total_datacards)
        if 0 < total_datacards <= 20:
            return df
        start_year = int(df.iloc[0].at['Year'])
        end_year = int(df.iloc[-1].at['Year'])
        for slice_year in range(start_year + 1, end_year + 1):
            data_quantity = Slice.__get_data_quantity(slice_year, df)
            if data_quantity > target_datacards:
                return df[df['Year'] >= slice_year - 1]
        return df[df['Year'] == start_year]


slicing = Slice()
