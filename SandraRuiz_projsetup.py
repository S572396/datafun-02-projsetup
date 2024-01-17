""" This module provides functions for creating a series of project folders."""
import math
import statistics
import pathlib


def create_project_directory (directory_name: str):"""
    Creates a prject sub-directory.
    :parm directory_name: "test"
    """
pathlib.Path('test').mkdir(exist_ok=True)

def main():
    """A Project for Directories."""
    create_project_directory(directory_name='test') #name the parameter
    create_project_directory(directory_name= 'docs') # name the parameter

#functions
def create_folders_for_range(start,end):
    start=2020
    end=2024    
     
    
    #call function 1 for range
    create_folders_for_range(start_year=2020, end_year=2023)
   
if __name__ == '_main_':
        main()
    




    
    
