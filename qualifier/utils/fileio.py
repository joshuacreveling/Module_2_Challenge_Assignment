# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
#import sys
import sys


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csv_data, csvpath):
    """Takes a list of lists and exports to CSV file located in path provided.

    Args:
        csv data (List of Lists): Matrix of data to be exported to csv.

    Returns:
        Exports a CSV file to path indicated by user.

    """
    # Set the output header
    #header = ["Lender", "Max Loan", "Max LTV", "Max DTI", "Min Credit Score", "Interest_Rate"]

    # Set the output file path
    #csvpath = Path("qualifying_loans.csv")

    # Use the csv library and csv.writer to write the header row and each row of qualifying_loans[loan] from the qualifying_loans list.
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        #csvwriter.writerow(header)  
        for row in csv_data:  
            csvwriter.writerow(row) 
    #sys.exit(f"Your csv file has been created.  Thank you.")   
