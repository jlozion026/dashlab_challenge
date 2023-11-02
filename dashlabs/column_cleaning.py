import os
import pandas as pd
import json
import numpy as np
import shutil
import tkinter as tk
from .time_it import time_it

class ColumnCleaning:
    def __init__(self, target_folder, output_csv_folder, diagnostics_text):
        self.diagnostics_text = diagnostics_text
        self.target_folder = target_folder  # Modify to store the folder, not a list of folders
        self.output_csv_folder = output_csv_folder
    
    def update_diagnostics(self, message):
        self.diagnostics_text.config(state=tk.NORMAL)  # Set state to normal to edit
        self.diagnostics_text.insert(tk.END, message + "\n")
        self.diagnostics_text.see(tk.END)
        self.diagnostics_text.config(state=tk.DISABLED)  # Set state to disabled to make it uneditable
        self.diagnostics_text.update_idletasks()  # Refresh the GUI
    
    def apply_general_column_cleaning(self, df, column_mapping):
        if not column_mapping:
            return df

        new_column, column_dict = column_mapping.popitem()
        conditions = []
        values = []
        for column, value in column_dict.items():
            conditions.append(df[column] == 'selected')
            values.append(value)

        df[new_column] = np.select(conditions, values, default='unknown')
        return self.apply_general_column_cleaning(df, column_mapping)

    def apply_med_exam_column_cleaning(self, df, med_exam_column_cleaning):
        if not med_exam_column_cleaning:
            return df

        new_column, column = med_exam_column_cleaning.popitem()
        condition = pd.notna(df[column])
        value = df[column]

        df[new_column] = np.where(condition, value, 'Normal')
        return self.apply_med_exam_column_cleaning(df, med_exam_column_cleaning)    
        
    
    def create_new_column_dictionary(self, df, columns):
        general_column_cleaning = {}
        med_exam_column_cleaning = {}
        joiner = " "
        
        for column_name in columns:
            if '_' in column_name:
                if column_name.endswith('findings'):
                    split_column_name = column_name.split('_')
                    category = joiner.join(split_column_name[:-1])  
                    if category not in med_exam_column_cleaning:  
                        med_exam_column_cleaning[category] = {}
                    med_exam_column_cleaning[category] = column_name   
                else:
                        split_column_name = column_name.split('_')
                        category, option = joiner.join(split_column_name[:-1]), split_column_name[-1]
                        if category not in general_column_cleaning:
                            general_column_cleaning[category] = {}
                        general_column_cleaning[category][column_name] = option
            elif '-' in column_name:  
                split_column_name = column_name.split('-') 
                category, option = joiner.join(split_column_name[:-1]), split_column_name[-1]
                if category not in general_column_cleaning:
                    general_column_cleaning[category] = {}
                general_column_cleaning[category][column_name] = df[option]
        
        return general_column_cleaning, med_exam_column_cleaning

    def move_processed_json_files(self):
        processed_json_folder = os.path.join("processed_json", self.target_folder)

        if not os.path.exists(processed_json_folder):
            os.makedirs(processed_json_folder)

        folder_path = os.path.join("output_json", self.target_folder)
        json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

        for json_file in json_files:
            source_path = os.path.join(folder_path, json_file)
            dest_path = os.path.join(processed_json_folder, json_file)
            shutil.move(source_path, dest_path)

        print(f"Processed JSON files moved to {processed_json_folder}.")
       
    def combine_json_to_csv(self, column_order):
        dataframes = self.read_json_files()
        
        # Check if there are dataframes to concatenate
        if not dataframes:
            form_category = self.target_folder.replace("_json", " form")
            print(f"No dataframes to concatenate. Upload a {form_category}")
            
            self.update_diagnostics(f"No dataframes to concatenate. Upload a {form_category}")
            return
        
        
        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df = self.clean_columns(combined_df, column_order)

        self.insert_csv_to_main_by_category(combined_df)
        self.move_processed_json_files()

    def read_json_files(self):
        dataframes = []
        folder_path = os.path.join("output_json", self.target_folder)
        json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]
        
        for json_file in json_files:
            file_path = os.path.join(folder_path, json_file)
            with open(file_path, "r") as json_data:
                data = json.load(json_data)
                df = pd.DataFrame([data])
                dataframes.append(df)
        
        return dataframes

    def clean_columns(self, df, column_order):
        columns = df.columns.tolist()
        general_column_dict, med_exam_column_dict = self.create_new_column_dictionary(df, columns) 
        df = self.apply_general_column_cleaning(df, general_column_dict)
        df = self.apply_med_exam_column_cleaning(df, med_exam_column_dict)

        if self.target_folder == "psycho_eval_json":
            missing_columns = [col for col in column_order if col not in columns]
            if missing_columns:
                for col in missing_columns:
                    df[col] = None

        df = df[column_order]
        return df
    
    def insert_csv_to_main_by_category(self, combined_df):
        form_category = self.target_folder.replace("json", "")
        csv_filename = f"{form_category}db.csv"
        
        form_csv_path =   os.path.join(self.output_csv_folder, csv_filename)# Update this path to your main CSV file

        if not os.path.exists(self.output_csv_folder):
            os.makedirs(self.output_csv_folder)

        if not os.path.isfile(form_csv_path):
            # If the main CSV file doesn't exist, create it with the columns from combined_df
            combined_df.to_csv(form_csv_path, index=False)
            print(f"Main CSV file created at {form_csv_path}.")
        else:
            main_df = pd.read_csv(form_csv_path)
            main_df = pd.concat([main_df, combined_df], ignore_index=True)
            main_df.to_csv(form_csv_path, index=False)

        print(f"Data from {self.target_folder} inserted into the {csv_filename}.")
        self.update_diagnostics(f"Data from {self.target_folder} inserted into the {csv_filename}.")
