import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#global variables - easier when using the same list in different funcionts ##
cities = ['chicago', 'new york city', 'washington'] ## List of cities allowed in this code ##
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june'] ## list for possible values ##
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True: ### While loop for city name OR USE TRY #####
        print('Which city? Chicago, New York City or Washington') #Message to the user#
        city = input().lower() #Receive the data from the user and keeping#
        if city in cities: ## checking if the typed data is allowed to be used, handling typing error###
          break
        print('{} is an invalid city...Try again'.format(city)) ## DIsplay to the user that he is trying to used an invalid city, echoing his choice
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: ## Loop to get the month or all ###
        print('Which month? Range: January to June or All')
        month = input().lower() ## Avoid case sensitivity
        if month in months:
            break;
        print('{} is an invalid month...Try again'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Which day? Range: Monday to Sunday or All')
        day = input().lower() ## Avoid case sensitivity##
        if day in days:
            break;
        print('{} is an invalid month...Try again'.format(day))

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
    ### Load datafile into a dataframe based on the city choosen
    df = pd.read_csv(CITY_DATA[city])

    #### convert column START TIME to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new column with month and day of the week to be used as filters
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name

    ## FILTERs for desired month and day ##

    if month != 'all': #month filter#
        df= df[df['month'] == months.index(month)]

    if day != 'all': #day filter#
        df = df[df['weekday'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    try:
        c_month = df['month'].value_counts() #count values in month column
        print("Most common month is {}, with {} travels".format(months[c_month.index[0]].title(),c_month.iloc[0]))
    except:
          print('no data to show for month')
    print("\n")
    # TO DO: display the most common day of week
    try:
        c_day = df['weekday'].value_counts()
        print("Most common day of the week is {}, with {} travels ".format(c_day.index[0], c_day.iloc[0])) #select the day with most travels
    except:
        print('no data to show fo weekday')

    # TO DO: display the most common start hour
    try:
        c_hour = df['Start Time'].dt.hour.value_counts() #selects only the hour from the Start Time columns
        print('\nMost common start hour is {}, with {} travels '.format(c_hour.index[0], c_hour.iloc[0]))
    except:
        print('no data to show for hour')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        c_start_station = df['Start Station'].value_counts()
        print('\n Most commonly used start station is {} with {} travels'.format(c_start_station.index[0], c_start_station.iloc[0]))
    except:
        print('no data to show for station')

    # TO DO: display most commonly used end station
    try:
        c_end_station = df['End Station'].value_counts()
        print('\n Most commonly used End station is {} with {} travels'.format(c_end_station.index[0], c_end_station.iloc[0]))
    except:
        print('no data to show for station')
    # TO DO: display most frequent combination of start station and end station trip
    try:
        c_both = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
        print("Most frequent travel starts at {} and ends at {} with {} travels".format(c_both.index[0] [0],c_both.index[0][1],c_both.max()))
    except:
        print('no data to show for comon travel')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        tr_time = df['Trip Duration'].sum()
        print("\n The total travel time is {} seconds".format(tr_time))
    except:
        print('no data for total travel time')
    # TO DO: display mean travel time
    try:
        m_time = df['Trip Duration'].mean()
        print("\n The mean travel time is {} seconds".format(m_time))
    except:
        print('no data for mean travel time')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        u_type = df['User Type'].value_counts()
        print('Count of user types: \n',u_type)
    except:
        print('no data for user types')
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nCount of gender: \n", gender)
    except:
        print('no data for gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_c = df['Birth Year'].value_counts()
        birth_e = df['Birth Year'].min()
        birth_r = df['Birth Year'].max()
        print("\nEarliest birth: ",int(birth_e))
        print("\nMost recent birth: ",int(birth_r))
        print("\nMost common year: ",int(birth_c.index[0]))
    except:
        print('no data for birth years')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def restart(): # defining restart function
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes': #checing if the user wants to restart
            return True
            break
        elif restart.lower() == 'no': #checking if the user do not want to restart
            return False
            break
        else :
            print('Invalid, try again') #handle invalid entries


def show_raw(df): #print five rows of data
    print('\n The first 5 rows of raw data is: \n')
    print(df.iloc[0:5]) #print the first five rows of data
    end = 5 #variable for the loop
    while True: #loop to check conditions (yes/no) and check for typing mistakes
        check = input('\n Would you like to see more data? Yes or No...\n')
        if check.lower() == 'no': #conditional if to check for entries and mistakes
            break
        elif check.lower() == 'yes': #condition to print the desired data
            start = end
            end = end + 5
            print(df.iloc[start:end])
        else:
            print('\n Invalid entry...try again:')
def main():
    loop = True

    while loop == True:
        city, month, day = get_filters() #Done
        df = load_data(city, month, day) #Done
        time_stats(df) #Done
        station_stats(df) #Done
        trip_duration_stats(df) #Done
        user_stats(df) #Done
        show_raw(df)

        loop = restart()


if __name__ == "__main__":
	main()
