import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["Chicago", "New York City", "Washington"]
    while True:
        city = input("\nEnter city name to filter by: (Chicago, New York City, Washington)\n")
        if city.title() not in cities:
            print("Please, enter one of the listed cities!\n")
            continue #to skip current invalid iteration
        else:
            break


    #get user input for month (all, january, february, ... , june)
    months = ["January","February","March","April","May","June"]
    while True:
        month = input("\nEnter month name to filter by: (January, February, March, April, May, June, all)\n")
        if month.title() not in months and month != "all":
            print("Please, enter one of the listed months!\n")
            continue #to skip current invalid iteration
        else:
            break


    #get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    while True:
        day = input("\nEnter day name to filter by: (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, all)\n")
        if day.title() not in days and day != "all":
            print("Please, enter one of the listed days!\n")
            continue #to skip current invalid iteration
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name(locale = 'English')
    
    
    # filter by month if applicable
    if month != 'all':
        #Convert month name to month number
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    most_common_month = df["month"].mode()[0]
    print("The most common month:",most_common_month)


    #display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("The most common day:",most_common_day)


    #display the most common start hour
    #Extract hour first
    df["hour"] = df["Start Time"].dt.hour
    most_common_hour = df["hour"].mode()[0]
    print("The most common hour:",most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    most_common_start = df["Start Station"].mode()[0]
    print("The most common start station:",most_common_start)


    #display most commonly used end station
    most_common_end = df["End Station"].mode()[0]
    print("The most common end station:",most_common_end)


    #display most frequent combination of start station and end station trip
    df["Combination Station"] = df["Start Station"] + " | " + df["End Station"]
    most_common_comb = df["Combination Station"].mode()[0]
    print("The most common combination station trip:",most_common_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("the total travel time in hours:", total_travel_time/3600)
    
    #display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("the mean travel time in hours:", mean_travel_time/3600)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics o
    n bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("the count of each user type:\n",user_type_count)
    
    #Check if city is not Washington
    #To avoid KeyError
    if city.title() != "Washington":
        #display counts of gender
        gender_count = df["Gender"].value_counts()
        print("the count of gender:\n",gender_count)

        #display earliest, most recent, and most common year of birth
        earliest_year = df["Birth Year"].min()
        print("The earliest birth year:",earliest_year)
        
        recent_year = df["Birth Year"].max()
        print("The most recent birth year:",recent_year)
        
        most_comm_year = df["Birth Year"].mode()[0]
        print("The most common birth year:",most_comm_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
