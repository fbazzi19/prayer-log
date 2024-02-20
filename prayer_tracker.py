#potential future development: add date and time tracker to allow user to log multiple times a day for different prayers within one day
import numpy as np
import csv

def streak_counter():
    #variables to keep track of streaks
    fajr_streak=0
    duhr_streak=0
    asr_streak=0
    maghrib_streak=0
    ishaa_streak=0
    day_streak=0
    #streak calculation: difference in array position between the current entry (today) and the last day with a recorded zero

def log_today(file_name):
    a=0 #temp
    #to do: ask about today


def main():

    #Boolean indicating
    cycle=False #menstruation status
    #new_user=True #if the user is new
    
    file_name="" #name of the file containing log

    #ask if new user
    is_new=input("Welcome! Is this your first time logging? (y/n) ")
    if is_new=="n":
        file_name=input("What is your log's name? ")
        #to do: add something to check if the file name is valid
        log_today(file_name)
    elif is_new=="y":
        file_name=input("What would you like to name your log? (No spaces or special characters) ")
        #to do: add something to check if the file name is valid
        with open(file_name+'.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            f.close()
        log_today(file_name)

    #array containing prayer status: 0=not completed, 1=completed, 2=menstruating
    prayer=np.empty([1,5]) #will likely have to read and write to a csv to monitor data values

if __name__ == '__main__':
    main()
