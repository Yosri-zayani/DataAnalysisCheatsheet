## required Libraries 
import requests # you need this module to make an API call
import pandas as pd
api_url = "http://api.open-notify.org/astros.json" 

response = requests.get(api_url) # Call the API using the get method and store the
                                # output of the API call in a variable called response.

if response.ok:             # if all is well() no errors, no network timeouts)
    data = response.json()  # store the result in json format in a variable called data
                            # the variable data is of type dictionary.


print(data)   # print the data just to check the output or for debugging


export dataframe into excel sheet 
from openpyxl import Workbook        # import Workbook class from module openpyxl
wb=Workbook()                        # create a workbook object
ws=wb.active                         # use the active worksheet
ws.append(['Country','Continent'])   # add a row with two columns 'Country' and 'Continent'
ws.append(['Eygpt','Africa'])        # add a row with two columns 'Egypt' and 'Africa'
ws.append(['India','Asia'])          # add another row
ws.append(['France','Europe'])       # add another row
wb.save("countries.xlsx")            # save the workbook into a file called countries.xlsx
