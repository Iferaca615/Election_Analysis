# Election_Analysis
written in python

# Overview of the Project:

In this module we successfully helped Seth and Tom create a program that reads and manipulates a large data set and produces the result of an election along with data regarding voter turnout, percentage of votes from each county out of the total amount of votes.  We were asked to create a code and then print the results of the code onto another text file that would be very readable to the average eye. 

- Using for loops, decision statements, dependencies and many other tools; we created a code that would organize the required data very efficiently.
- In the end we were able to print out the results to another text file to make the findings as readable as possible.

## Snapshot of the text file with final results of the election:
1) ![election-results](election-results.png)

# Election Audit Results:

* There were a total of 369,711 votes cast:

	- Jefferson held: 10.5% (38,855) votes
	- Denver held: 82.6% (306,055) votes
	- Arapahoe held: 6.7% (24,801) votes

* Largest county Turnout:
	- Denver

* Candidate Results (percentage of votes / votes):
	- Charles Casper Stockham: 23.0% (85,213) votes
	- Diana DeGette: 73.8% (272,8920 votes
	- Raymon Anthony Doane: 3.1% (11,606)

* Winner of the Election:
	- Diana DeGette:
		- Winning Vote count: 272,892
		- Winning percentage: 73.8%

# Election Audit Summary:
The winner of the Election is Diana DeGette, who totaled 272,892 votes in the election and had a winning percentage of 73.8%.  Because of the way this script is written, it can be reused to account for more candidates, counties and can even be adjusted to explore more into other statistics.

## Modifications to the code:
As mentioned previously, this code is very versatile.  By first assigning an empty list and dictionary in the code, changes can be made to the csv sheet and be processed within the code.  This flexibility allows for increased functionality in processing more data.  

If needed you can also import another csv file with additional data by using the import csv and os path functions.  By doing this the code will be adjusted to pull from those data sets and will be processed in the written code.
- add for loop statements to loop through new data sets and make new calculations for additional statistics.
