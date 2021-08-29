# Module 2 Challenge - Loan Qualifier Application with CSV Output

---

## Description

This code builds off of our existing Loan Qualifier Application by adding a new function, *'save_qualifying_loans()'*, directly to **app.py** as well as adding and utilizing a modularized funtion, *'csv_save()'*, to **fileio.py** that will save qualifying loans as a new CSV file.  This challenge builds on the skills that we have learned through Module 1 and Module 2 thus far.

This is a command-line interface application that prompts the user for their personal loan qualifying metrics and if they qualify for one or more loans, will prompt the user to save their loan options as a new .csv file.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```
---

## Usage
To use the loan qualifier application simply clone the repository and run the **app.py** file:

```python
python app.py
```

Upon launching the loan qualifier application you will be prompted with the following questions requesting personal finanical data.  In the example below, user text is colored "yellow".

![user_financial_data](./Images/user_financial_data.png)

If the user qualifies for one or more loans, the program will then ask the user if they would like to save a new .csv file.  Using the arrow key, the user will select 'yes' or 'no'.
The user will then be asked to confirm once more that they would like to save a new .csv file.  Using the arrow key, the user will select 'yes' or 'no'.
After recieving confirmation from the user, the program will prompt the user for a file path for their new .csv file.
The progarm will notify the user it is writing data to a CSV file and will output confirmation once completed.  
In the example below, user text is colored "yellow".  

![user_prompt](./Images/user_prompt.png)

---

## Contributors

Joshua Creveling

Email: josh.creveling22@gmail.com

GitHub: https://github.com/joshuacreveling

LinkedIn: https://www.linkedin.com/in/joshua-creveling/

*Starter code provided by Trilogy Education Services*

---

## License

MIT
