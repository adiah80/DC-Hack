'''
NAME    : Time_extraction 
PURPOSE : Extracts the last token number form 'instant.csv' and adds it to the file 'time_data.csv' 
			with the time at which the script is called. 
INPUT   : instant.csv
OUTPUT  : time_data.csv
'''

# Importing libraries
import pandas as pd
import numpy as np
import time
from pathlib import Path
pd.set_option('display.max_rows', None)



# Reading the instantanious log data into 'main' dataframe
main = pd.read_csv('instant.csv')
main.columns = ['Token', 'Dir', 'IP', 'Port', 'Peer info', 'Message']        # defining tokens
main = main.dropna(axis=0, how='any')                                        # removing 'bad' rows




# Checks if 'time_data.csv' exists
# Reads it to 'time_data' dataframe if it exists
# Creates 'time_data' dataframe and corresponding csv it if it doesn't exist
my_file = Path("time_data.csv")
if my_file.is_file():
	# Exists -> Read                                       
    print("Reading Time_data")
    time_data = pd.read_csv('time_data.csv')
    time_data
else:
	 # Does not exist -> Create
    print("Creating Time_data")                            
    time_data = pd.DataFrame({'Time' : [], 'Tokens' : []})
    time_data.columns = ['Time', 'Tokens']
    time_data.to_csv('time_data.csv', index=False)




# Creating an entry to add to the 'time_data' dataframe
import time
time = time.asctime(time.localtime(time.time()))                               # time = current time
token_upto = int(main.Token[len(main) - 1])                                    # token_upto = last token
entry = pd.DataFrame([[time,token_upto]], columns=['Time', 'Tokens'])




# Append the 'entry' to the 'time_data' dataframe
# Save the updated 'time_data' dataframe
time_data = time_data.append(entry)
time_data.to_csv('time_data.csv', index=False)

