# GolfDiagnosis
- Go into your 'Garmin Connect' Scorecards:
	- Right click and 'Inspect'
	- Right above the below element right click <div> element and 'Copy-Copy outterHTML
			<div class='GolfList_divider__YBDg-'>2024</div>	
	- Save file to local drive and name 'source.html'..you'll need this path later.
- In 'get_Round_Numbers.py', copy path to the 'url' variable.
	- This will pull out the scorecard numbers into a python list.
	- Copy this list to 'create_scorecardCSV.py'..to the 'round_number' variable
		- This will cycle through each related round on the Garmin website and create a .CSV file, which you will have to change the path on the last line.
        - Change path in the "dfTotal.to_csv" to your path.
- Run 'Scores Diagnosis.py', changing the path to the .CSV file.
	- There are various queries commented out.




#####Things to look out for
# - Moon Lake Course could be named the following:
    - Moon Lake
          or
    - MoonLake
- Watch out for zeroed out rounds
    - I thought this code would remove 0 stroke holes, but it doesn't completely:
         'df = df[~(df[df.columns[3:3]]==0).any(axis=1)]'
- HPGC has 2 different type:
    - Executive
           and
    - Championship
- MoonLake has multiple types (Moors, Heather...)
- Whatch out for Moon Lake Heather(?), or wahtever that temp hole was as it will record as an Ace or Eagle (Par 5 instead of the temp Par 3)
York Lake is beneath me now
- I exluded 9 hole rounds, usually at HPGC...I think.
