# DC-hack

These scripts can be used to used to monitor, analyse, and archive the traffic on your Apex DC++ client. They require you to install DevPlugin for Apex-DC++ : https://sourceforge.net/projects/dcplusplus/files/Plugins/DevPlugin/

To extract the raw data from the Dev-plugin we use sysexp.exe (https://www.nirsoft.net/utils/sysexp.html). This allows us to export the data as .txt and .csv files. These raw data files can then be cleaned and analysed using python scripts. 

We use a batch script(save_time_data.bat) to store and archive the data from DevPlugin and sysexp.exe, and a python script(Time_extraction.py) to save the local time with the stored data. This allows us to monitor the time at which a specific search-query was made.

We use search_compilation.ipynb to extract the user information behind a specific search-query. This information includes the user-nick, IP, hub and the specific search-query(see query_output.csv).

We can use nick_IP_extraction.ipynb to extract user IP and nick relations(see nick_backup_3.csv).

Overall, we can monitor all the searches that were made on the network, as well as determine the user-nick and IP that made the searches. We can also determine the time at which a search was made.  
