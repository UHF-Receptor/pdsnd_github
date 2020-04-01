import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    cities = set(['chicago', 'new york city', 'washington'])
    city = 'no_city'
    while city not in cities:
        city = input('Which city would you check?                ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = set(['all', 'january', 'february','march','april','may','june'])
    month = 'not_all'
    while month not in months:
        month = input('Which month would you prefer?              ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = set(['monday','tuesday','wednesday','thursday','friday','saturday','sunday'])
    day = 'no day'
    while day not in days:
        day = input('Which day would you check?                 ').lower()
    print('-'*40)
    return city.lower(), month.lower() , day.lower()

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most active month is {}'.format(popular_month))
    # TO DO: display the most common day of week
    df['day_of_Week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('The most concurrous day is {}'.format(popular_day))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most active hour is {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    CommonStartStation = df['Start Station'].mode()[0]
    # TO DO: display most commonly used end station
    CommonEndStation = df['End Station'].mode()[0]
    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe Most Popular Station Trip is from {} to {}\n'.format(CommonStartStation,CommonEndStation))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    trip_count = df['End Station'].count()
    trip_time = df['Trip Duration'].sum()
    # TO DO: display mean travel time
    print('The mean of travels is {}.'.format(trip_time/trip_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    Type_count = df['User Type'].value_counts()
    print(Type_count)
    # TO DO: Display counts of gender
    try:
        Gender_count = df['Gender'].value_counts()
        print(Gender_count)
    except:
        print('There is not Gender info')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Younger=df['Birth Year'].max()
        Elder=df['Birth Year'].min()
        print('The youngest rider was born in {}, and the oldest was born in {}.'.format(Younger,Elder))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print('There is not birth info in this database')
    print('-'*40)

def display_raw_data(df):
    display = input('\nWould you like to see the first five rows? YES or NO?\n').lower()
    if display == 'yes':
        print(df.head(5))
    display = 'yes'
    count = 5
    print(len(df))
    while len(df) > count*5:
        display = input('Would you like to see the next five rows of the raw data? YES or NO?\n').lower()
        if display == 'yes':
            print(df.iloc[[count,count+1,count+2,count+3,count+4]])
            count=count+6
        else: break

def main():
    while True:
        city, month, day = get_filters()
        print('\nNow, we present you the desired DATA.\n')
        i = 'no'
        while i != 'ok':
            i = input('\nPress "OK" to continues or "NO" to exit.\n         ').lower()
            if i == 'no':
                exit()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\         n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
