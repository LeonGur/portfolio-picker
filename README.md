#Portfolio picker
This program enables the user to enter a risk level (1-10) and prints the tickers of those share that are most suitable.

#The logic
The program researches to historical data from the past 5 years of each ticker, via Yahoo-finance. In addition, it also creates a Dataframe only containing the data from the past year. It then proceeds to calculate the variance and average yearly return. This information is then, with the help of a formula combined into a single value, which can be sorted via a bubble sort function.

#Installation
In order to be able to meaningfully execute the code, various libraries are required.
•	quandl
•	Numpy
•	pandas
•	pandas_datareader
The easiest way to install those libraries is with pip:
1.	pip install quandl
2.	pip install numpy
3.	pip install pandas_datareader
