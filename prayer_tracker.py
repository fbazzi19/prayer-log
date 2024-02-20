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




def main():

    #Boolean indicating
    cycle=False #menstruation status
    #new_user=True #if the user is new

    #ask if new user
    is_new=input("Welcome! Is this your first time logging? (y/n)")
    if is_new=="n":
        new_user=False #temp
        #to do: ask for the users file of previous tracking and read (read csv function)
    elif is_new=="y":
        #to do: create a new csv file to start tracking
        a=0 #temp
        with open('my_prayer_data.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            #writer.writerow([0,1,2])
            f.close()

    #array containing prayer status: 0=not completed, 1=completed, 2=menstruating
    prayer=np.empty([1,5]) #will likely have to read and write to a csv to monitor data values

if __name__ == '__main__':
    main()
