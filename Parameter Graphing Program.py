#PARAMETER GRAPHING PROGRAM
#This program takes water quality information from the CERP database and graphs it
#A program by Tyler Serio
#Python 3.7.4
#Circa Fall 2019

#IMPORT RELEVANT TOOLS
import os.path
from os import path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#DEFINE FUNCTIONS
#open the file, read it, and graph the information
def graph_param_file():
    opening = 1

    #open the database file
    while opening == 1:
        print("Which file would you like to graph?")
        print("Example: '2019-10-10_export_timeseries_station_1.txt'")
        print("Please type the name of the file exactly,")
        filename = input("or type [0] to return to the menu. ")
        print("")
        if filename == "0":
            break

        #check to see if the file exists
        path.exists(filename)

        #if the file exists, continue to the next step
        if path.exists(filename) == True:
            print("I will retrieve your file.")
            print("I have found your file.")
            print("")
            param_file = open(filename, "r")
            opening = 0
            break

        #if the file does not exist then ask the user for another one
        if path.exists(filename) == False:
            print ("I will retrieve your file.")
            print ("I cannot find this file. Make sure to type the file name exactly.")
            print ("Try again, or type [0] to return to the menu.")
            print ("")
            opening = 1

    print("We will now read the file for relevant information.")
    print("")
        
    #define important lists
    dates = []
    salinities = []
    pH = []

    #READ THE FILE
    #read the file and record information, handle errors arising from missing information
    for line in param_file:
        columns = line.split()
        try:
            date = columns[0]
        except IndexError:
            date = "null"
        try:
            SE = columns[5]
        except IndexError:
            SE = "null"
        try:
            bottom_temperature = columns[6]
        except IndexError:
            bottom_temperature = "null"
        try:
            bottom_oxygen = columns[7]
        except IndexError:
            bottom_oxygen = "null"
        try:
            bottom_salinity = columns[8]
        except IndexError:
            bottom_salinity = "null"
        try:
            bottom_ph = columns[9]
        except IndexError:
            bottom_ph = "null"

        dates.append(date)
        try:
            float(bottom_salinity)
        except ValueError:
            bottom_salinity = 0
        salinities.append(float(bottom_salinity))
        pH.append(bottom_ph)

    #delete unimportant labels in lists
    del dates[0]
    del salinities[0]

    #REFINE DATE INFORMATION
    #converting date information into proper format
    #producing a new list that can later be used to create x-axis ticks
    length = len(dates)
    simplifying = 1
    place = 0
    while simplifying == 1:
        new_date = str(dates[place]).split("/")
        if int(new_date[0]) <= 9:
            new_date[0] = "0" + str(new_date[0])
        if int(new_date[1]) <= 9:
            new_date[1] = "0" + str(new_date[1])
        dates[place] = str(new_date[2]) + "-" + str(new_date[0])
        place += 1
        if place >= length:
            simplifying = 0
            break
        
    #create a group of all dates between our starting date and our ending date     
    x = np.arange(dates[0], dates[len(dates) - 1], dtype = "datetime64[M]")
    
    #remove parts of string we don't need
    x = x.tolist()
    x.append(dates[len(dates) - 1])
    removing = 1
    place = 0

    #remove parts of the string that we don't need
    while removing == 1:
        x[place] = str(x[place]).replace("datetime.date(", "")
        x[place] = str(x[place]).replace(")", "")
        x[place] = str(x[place]).replace("/", "")
        place += 1
        if place >= len(x):
            removing = 0
            break

    #remove day part of date
    removing = 1
    place = 0
    while removing == 1:
        tx = x[place].split("-")
        x[place] = tx[0] + "-" + tx[1]
        place += 1
        if place >= len(x):
            removing = 0
            break

    #only plot to ticks in a list
    places = []
    ticking = 1
    place1 = 0
    place2 = -1
    while ticking == 1:
        place2 += 1
        if place2 >= len(x):
            ticking = 0
            break
        if str(x[place2]) == str(dates[place1]):
            places.append(place2)
            #print(places)
            place1 += 1
            place2 = 0
            if place1 >= len(dates):
                ticking = 0
                break  

    #This part of the program takes the numerical dates and converts them into a format
    #that is more easily read by people.
    recording = 1
    place = 0
    date_holder = ""
    while recording == 1:
        date_holder = dates[place]
        date_holder = date_holder.split("-")
        if str(date_holder[1]) == "01":
            date_holder[1] = "Jan. "
        if str(date_holder[1]) == "02":
            date_holder[1] = "Feb. "
        if str(date_holder[1]) == "03":
            date_holder[1] = "Mar. "
        if str(date_holder[1]) == "04":
            date_holder[1] = "Apr. "
        if str(date_holder[1]) == "05":
            date_holder[1] = "May "
        if str(date_holder[1]) == "06":
            date_holder[1] = "June "
        if str(date_holder[1]) == "07":
            date_holder[1] = "July "
        if str(date_holder[1]) == "08":
            date_holder[1] = "Aug. "
        if str(date_holder[1]) == "09":
            date_holder[1] = "Sept. "
        if str(date_holder[1]) == "10":
            date_holder[1] = "Oct. "
        if str(date_holder[1]) == "11":
            date_holder[1] = "Nov. "
        if str(date_holder[1]) == "12":
            date_holder[1] = "Dec. "

        date_holder = str(date_holder[1]) + str(date_holder[0])

        dates[place] = date_holder
        place += 1
        if place >= len(dates):
            recording = 0
            break


    #prepare to make labels
    labeling = 1
    place = 0
    labels = []
    while labeling == 1:
        labels.append("")
        place += 1
        if place >= len(x):
            labeling = 0
            break
       
    #create x-axis tick labels
    labeling = 1
    place = 0
    while labeling == 1:
        labels[places[place]] = str(dates[place])
        place += 1
        if place >= len(dates):
            labeling = 0
            break

    xi = list(range(len(x)))

    #print the lists to visualize the data
    print("Recorded dates: ")
    print(dates)
    print("")
    print("Recorded salinities: ")
    print(salinities)
    print("")

    #PLOT THE INFORMATION TO A GRAPH
    graphname = input("What would you like to name this graph? ")
    
    #create title and axis labels
    plt.ylabel("Salinity\n(ppt)", fontweight = "bold", fontsize = "16", rotation = "0", labelpad = 40)
    plt.xlabel("Date", fontweight = "bold", fontsize = "16", labelpad = -1)
    plt.title(graphname, fontweight = "bold", fontsize = "18", pad = "20")

    #define the axis ticks
    plt.tick_params(axis = "y", labelsize = "10")
    plt.tick_params(axis = "x", labelsize = "10")
    plt.xticks(xi, labels, rotation = "90")

    #define y-axis limits
    plt.ylim(0, 40)

    #plot the data
    plt.plot(places, salinities, "b")
    plt.plot(places, salinities, "bo")

    #create legend
    plt.legend(("Salinity",), loc = "upper right")

    #show the graph
    plt.show()

    #let the user know that the program has finished
    print("We have finished graphing.")
    print("")

#BEGIN THE PROGRAM
print("Hello, scientist. What would you like to do?")
menu = 1

#open the menu and ask the user what they would like to do
while menu == 1:
    print("Please choose an option to continue.")
    print("[1] - Graph salinity information.")
    print("[0] - Exit the program.")
    selection = input("Please choose: ")
    print("")

    #handle an improper selection
    if selection != "1" and selection != "0":
        print("That is not a proper selection.")
        print("Please chooes from the list of options.")
        print("")

    #graph the parameters
    if selection == "1":
        graph_param_file()

    #exit the program
    if selection == "0":
        exiting = 1

        #ask the user if they really want to exit the program
        while exiting == 1:
            print("Are you sure you want to exit?")
            print("[y] - Yes")
            print("[n] - No")
            exitv = input("Please choose: ")
            if exitv == "y":
                exit()
            if exitv == "n":
                print("Oh, nevermind then.")
                print("")
                exiting = 0
                menu = 1
                
