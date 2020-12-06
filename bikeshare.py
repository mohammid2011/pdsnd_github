import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

names_of_months = ['january', 'february', 'march', 'april', 'may', 'june']
names_of_days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    validation = False
    while not validation:
        city = str(input("Please enter the the city's name to analise it. The cities are: \n (chicago, new york city, washington)"))
        for key in CITY_DATA:
            if city.lower() == key:
                validation = True
        if validation == False:
            print("You've entered invalid value. \n Please try again")
        continue 

    validation = False
    while not validation:
        month = str(input("wright the name of the month to filter by, or type \"all\" to apply no month filter. \n The months are: \n  (january, february, ... , june)"))
        for name_of_month in names_of_months:
            if month.lower() == name_of_month or month.lower() == 'all':
                validation = True
                break
            else:
                validation = False
        if validation == False:
            print("You've entered invalid value. \n Please try again")
        continue

    validation = False
    while not validation:
        day = str(input("name of the day of week to filter by, or \"all\" to apply no day filter. \n The days are: \n (monday, tuesday, ... sunday)"))
        for name_of_day in names_of_days:
            if day.lower() == name_of_day or day.lower() == 'all':
                validation = True
                break
            else:
                validation = False
        if validation == False:
            print("You've entered invalid value. \n Please try again")
        continue

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    print("The most common month is: \n {} \n"
    "the most common day of week is: \n {} \n"
    "the most common start hour is:\n  {} \n"
    .format(df['month'].mode()[0], df['day_of_week'].mode()[0], df['hour'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most start station is \n', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most end station is \n', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['trip station'] = df['Start Station'] + ' ' + df['End Station']
    print("The most frequent combination of start station and end station trip is: \n", df['trip station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: \n', df['Trip Duration'].sum(0))

    # TO DO: display mean travel time
    print('The mean travel time is: \n', df['Trip Duration'].mean(0))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print('The user typs are: \n', user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
    except:
        print("The gender data is not available in your selected city")
    else:
        print("The genders are: \n", genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min(0)

        most_recent = df['Birth Year'].max(0)

        common = df['Birth Year'].mode()[0]
    except:
        print("The birth year data is not available in your selected city")
    else:
        print('the earliest, most recent, and most common year of birth are: \n {} \n {} \n {} \n'
    .format(earliest, most_recent, common))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def several_data(df):
    validation = False
    while not validation:
        row_data = str(input("Befor moving to Displays statistics of the data, \n do you would  to display rows from the data? \n Please type yes or no"))
        if row_data.lower() == 'yes' or row_data.lower() == 'no':
            validation = True
    start_point = 0
    end_point = 5
    while row_data.lower() == 'yes':
        print(df[start_point:end_point])
        start_point += 5
        end_point +=5
        row_data = str(input('Type yes to view more rows of the data, or press enter to move to the Statistics'))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)        


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
