Teemu Saravirta - teemu.saravirta@gmail.com

Commands tested on a Windows OS.

To run the program in command line:
Navigate to the folder "Wolt Coding Task 2019 - Pickup times"

To run the program we need pandas, numpy and click. These are provided with the venv in the folder.
virtualenv venv
venv/scripts/activate
pip install --editable . __OR__ python setup.py develop

Then you can run the program by:
delivery --date YYYY-MM-DD --time HH-HH --city STRING

with --date being within the dates in the data provided

with --city STRING being optional, with Helsinki set as default. If the name of the city has multiple words,
please provide it in the form of "Rio de Janeiro". Please note that the default data is still from Helsinki,
and has to be changed in CSVreformatter.py if you wish to save some other city's data. This can also be achieved by
just replacing the locations.csv and pickup_times.csv files in the folder.

Output is printed out as well as saved in mediantimes.csv


Find out more:
delivery --help
