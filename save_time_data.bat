@echo off
setlocal ENABLEDELAYEDEXPANSION

REM class_token = inp1             =N3dwt5TableEd5acf8b1-3a6b-42fa-a35b-b52014ca6445 
REM time_bw_loops = inp2           =600
REM num_loops = inp3               =144
REM backup_freq = inp4             =6

set class=%1

set d=%date:~-4,4%%date:~-10,2%%date:~-7,2%
set d=%d: =_%

mkdir data
mkdir data\data_%d%
mkdir data\collected

Echo --------------------------------------------------------------------
Echo Starting extraction.
Echo [%date%]
Echo [%time%]

for /l %%n in (0,1,%3) do (
	Echo --------------------------------------------------------------------
	Echo [!time!]
	Echo --- Processing trial %%n.

	sysexp.exe /Title "Dev Plugin" /class %class% /Visible Yes /scomma "%HOMEPATH%\Desktop\DC-hack\Search_compilation\instant.csv"
	echo --- Search extracted.

	Time_extraction.py
	echo --- Time extracted.

	set z=%%n
	set /a y=!z! %% %4

	if %%n == %3 (
		Ren instant.csv msrch_%d%.csv
		Echo         msrch_%d%.csv added to archive.
		Copy msrch_%d%.csv data\data_%d% 1>NUL

		Ren time_data.csv mtime_%d%.csv
		Echo         mtime_%d%.csv added to archive. 
		Copy mtime_%d%.csv data\data_%d% 1>NUL

		Echo         msrch_%d%.csv added to collected.
		Move msrch_%d%.csv data\collected 1>NUL
		Echo         mtime_%d%.csv added to collected.
		Move mtime_%d%.csv data\collected 1>NUL

		Echo --- Trial %%n completed.
		Echo [!time!]
		Echo --------------------------------------------------------------------
		Echo Extraction completed.
		Echo [%date%]
		Echo [%time%]
		Echo --------------------------------------------------------------------
	) else (
		if !y! == 0 (
			set t1=!time:~0,2!
			set t2=!time:~3,2!
			set t3=!time:~6,2!
			set t1=!t1: =0!

			set t=!t1!!t2!!t3!

			Echo         srch_%d%_!t!.csv added to archive.
			Copy instant.csv srch_%d%_!t!.csv 1>NUL
			Move srch_%d%_!t!.csv data\data_%d% 1>NUL

			Echo         time_%d%_!t!.csv added to archive.
			Copy time_data.csv time_%d%_!t!.csv 1>NUL
			Move time_%d%_!t!.csv data\data_%d% 1>NUL

			Echo --- Trial %%n completed.
			Echo [!time!]
			Echo --------------------------------------------------------------------
			timeout /t %2 /nobreak
		) else ( 
			Echo --- Trial %%n completed.
			Echo [!time!]
			Echo --------------------------------------------------------------------
			timeout /t %2 /nobreak
		)
	)
)