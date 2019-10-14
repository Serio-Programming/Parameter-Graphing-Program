# Parameter-Graphing-Program
# A Program by Tyler Serio

# What is it?
The Parameter Graphing Program

# What does it do?
This program takes information from the CERP (Comprehensive Evergladres Restoration Project) database and graphs it.

# How does it do it?
Information downloaded from the CERP database comes in an easily manipulated tabular format. The program reads every line of a station's downloaded water quality parameters for the dates and corresponding measurements, makes lists of them, and then plots them to a graph using matplotlib in Python. 

# Why was it made?
There is more than 15 years worth of water quality data spread across many different stations along the Indian River Lagoon and other bodies of water. It is useful to look at this data and to find general trends that might effect species diversity and organism populations in these areas. 

# Limitations
Right now This program only graphs salinity measurements, though other measurements such as pH and temperature will be added later. Also, the program makes lists of measurements depending on the positions of the tabular columns in the downloaded file. If a different number of parameters are downloaded in a single file, the program will now work properly. Right now the program is only coded to use download files that have the bottom temperature, bottom oxygen, bottom salinity, and bottom pH parameters selected. Adding other measurements, like surface temperature or surface salinity, will most likely produce erroneous graphs.
