import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    city=input("please enter the name of city: ").lower()
    while (city not in CITY_DATA):
        city=input("Wrong city. please enter the name of city: ").lower()   
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("please enter the month (january to june or all): ").lower()
    while (month not in list('all')+months):
        month=input("Wrong month. please enter another month: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednsday','thursday','friday','saturday','sunday','all']
    day=input("please enter the day: ").lower()
    while (day not in days):
        day=input("Wrong input. please enter the day: ").lower()
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
    df = pd.read_csv(CITY_DATA[city])   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    if df.empty:
        print('DataFrame is empty!')
    else:
        df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
        df['month'] = df['Start Time'].dt.month

    # find the most popular month
        popular_month = df['month'].mode()[0]
        print('Most Popular Start month:', popular_month)
    
    # TO DO: display the most common day of week
        df['day'] = df['Start Time'].dt.weekday_name
        popular_day = df['day'].mode()[0]
        print('Most Popular Start day:', popular_day)
    # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    if df.empty:
        print('DataFrame is empty!')
    else:
        popular_Start_Station = df['Start Station'].mode()[0]
        print('Most Popular Start Station:', popular_Start_Station)

    # TO DO: display most commonly used end station
        popular_End_Station = df['End Station'].mode()[0]
        print('Most Popular End Station:', popular_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
        df['combination'] = df['Start Station']+ ',' + df['End Station']
    
        popular_StartEnd_Station = df['combination'].mode()[0]
        print('Most Popular Start & END Station:', popular_StartEnd_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration= df['Trip Duration'].sum()
    print('total travel time: ', total_duration)

    # TO DO: display mean travel time
    mean_duration= df['Trip Duration'].mean()
    print('mean travel time: ',mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_gender=df['Gender'].value_counts()
        print(user_gender)
    else:
        print('There is not any Gender column.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if df.empty:
        print('DataFrame is empty!')
    else:
        if 'Birth Year' in df:
            print('earliest year of birth: ', min(df['Birth Year']))
            print('most recent year of birth: ', max(df['Birth Year']))
            print('most common year of birth: ', df['Birth Year'].mode()[0])
        else:
            print('There is not any Birth Year column.') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        num_rows= df.shape [0]
        while (view_data.lower() == 'yes' and num_rows-start_loc>=0 ):
            if num_rows-start_loc<5:
               print(df.iloc[start_loc : num_rows])
            else:
                print(df.iloc[start_loc : start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
