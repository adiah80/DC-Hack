#Psedudocode for batch file

class_token = inp1            # =N3dwt5TableEd5acf8b1-3a6b-42fa-a35b-b52014ca6445 
time_bw_loops = inp2          # =600
num_loops = inp3              # =144
backup_freq = inp4            # =6

d = format(date)


mkdir "Data"
mkdir "Data/data_d"
mkdir "Data/collected"

for i in (1,1,inp3){
	print("Processing trial i...")

	sysexp.extract(saveto = "instant.csv" ,inp1)
	print("Temp data extracted.")

	run(Time_extraction.py)                                #Export outside to other batch file
	print("Time extracted.")

	print("Trial i completed.")

	if (i == inp3) {
		rename('instant.csv' to 'search_d.csv')
		copy('search_d.csv' to Data/data_d)

		rename('time_data.csv' to 'time_d.csv')
		copy('time_d.csv' to Data/data_d)

		move('search_d.csv' to Data/collected)
		move('time_d.csv' to Data/collected)

		print("Data collection completed.")

	} else if (i == [j*inp4 for j in range(inp3/inp4)]) {
		t = format(time)

		rename('instant.csv' to 'search_backup_d_t.csv')
		move('search_backup_d_t.csv' to Data/data_d/backup_d)

		rename('time_data.csv' to 'time_backup_d_t.csv')
		move('time_backup_d_t.csv' to Data/data_d/backup_d)
		
		print("Backup added to archive.")
		
		print("Waiting for next trial.")
		timeout(inp2)

	} else {
		print("Waiting for next trial.")
		timeout(inp2)
	}
}