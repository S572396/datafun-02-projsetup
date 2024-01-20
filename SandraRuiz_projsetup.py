""" This module provides functions for creating a series of project folders."""
import math
import statistics
import SandraRuiz_utills
import pathlib  
import os
import time

pathlib.Path('test').mkdir(exist_ok=True)

print(f"Byline:{SandraRuiz_utills.byline}")

def main():
    '''
    A Project for Directories and module capabilities.
    '''
    create_project_directory(directory_name='test')
    create_project_directory(directory_name='docs')
    create_annual_data_directories(directory_name='dat', start_year=2000,end_year=2024)

    pipeline_folders= {'input', 'input_processed','output'}
    create_pipeline_folders(directory_name='pipeline', folder_list=pipeline_folders)

States=['Texas', 'Iowa', 'Kansas', 'Michigan'] # possible states for business
def create_folders_from_list(States):
     list= ['State 1', 'State 2','State 3','State 4']
     for itmes in list:
         pathlib.Path(str(itmes)).mkdir(exist_ok=True)


def create_folders_for_range(start_year,end_year):

 for year in range(start_year,end_year):
    folder_name="Year_"+str(year)
    pathlib.Path(str(year)).mkdir(exist_ok=True)
    

def create_prefixed_folders(folder_name= "regions", folder_list=["North America, South America, Europe"], prefix = 'R'):

#functions

 def create_folders_from_list(States):
     list= ['State 1', 'State 2','Sate 3','State 4']
     
     def create_prefixed_folders(regions):
      prefix = 'R-'

#function 4 While Loop
def create_folders_periodically(duration):
          duration_secs = 5
create_folders_periodically(duration_sec=5, folder_name= "New Callers", number_of_folders=2, Starting_number=1)


regions= ["North America, South America, Europe"]
create_folders_from_list(regions,to_lowercase=True,remove_spaces=True)
          
# create a path object
project_path = pathlib.Path.cwd

#define new sub folder path
data_path = project_path.joinpath ('data')

# create a new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#create anual directories
def create_annual_data_directories('data', start_year=2020, end_year=2024):
  create_annual_data_directories('data')
  for year in range(2020,2024+ 1):
      data = pathlib.Path().joinpath(str(year))
      print(f"data '{data}' created.")

  from pathlib import Path
  #list of weeday folder names
  day_list= ["01-Mon", "02-Tue","03-Wed", "04-Thu", "05-Fri", "06-Sat","07-Sun"]
  #iterate list and create folders
  for day in day_list:
     folder_name=f"data-{day}"
     Path(folder_name).mkdir(exist_ok=True)
     print(f" Folder '{folder_name}'created.")
     
   
if _name__ == '_main_':
        main()