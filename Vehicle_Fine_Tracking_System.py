# Program to read input text file and return the vehicle numbers whose fine is at least 50 Euros i decreasing order
# Written By: Shivam Kislay
# Date: 07/01/2020

import datetime


# Function Name: list_toll_dodgers()
# input: input file name
# output: to return vehicles with atleast 50 Euros fine in decreasing order
def list_toll_dodgers(tfile):
    # open the text file
    fname = open(tfile, 'r')

    # dictionary that stores the vehicle registration number and fine against it.
    car_dict = {}
    # list that holds the fines
    fine_list = []
    # final dictionary with fines and vehicles numbers in decreasing order
    final_dict = {}

    # loop to read each entry in the text file and add the fines against each car as mentioned in the rules
    for line in fname:
        line_entities = line.split()
        car_number = line_entities[0]
        date = line_entities[1]
        date_entity_list = date.split('/')
        dd = int(date_entity_list[0])
        mm = int(date_entity_list[1])
        yy = int(date_entity_list[2])
        time = line_entities[2]
        time_entity_list = time.split(":")
        hh = int(time_entity_list[0])
        ms = int(time_entity_list[1])
        ss = int(time_entity_list[2])
        time_high = datetime.time(19, 0, 0)
        time_low = datetime.time(7, 0, 0)
        time_recorded = datetime.time(hh, ms, ss)
        if car_number not in car_dict:
            car_dict[car_number] = 0

        if time_high > time_recorded > time_low and dd != 1:
            car_dict[car_number] += 2.50
        elif (time_recorded > time_high or time_recorded < time_low) and dd != 1:
            car_dict[car_number] += 1

    # store the vehicle number and its fine in its respective list greater than 50 Euros
    for i in car_dict:
        if car_dict[i] >= 50:
            fine_list.append(car_dict[i])

    # sort the fine list in decreasing order
    sorted_fines = sorted(fine_list, reverse=True)

    # match the sorted fine list to car dictionary and prepare the final dictionary to be returned
    for i in sorted_fines:
        for j in car_dict:
            if car_dict[j] == i and j not in final_dict:
                final_dict[j] = i

    return final_dict
