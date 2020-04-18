import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {'january': 1, 'february': 2, 'march': 3,
          'april': 4, 'may': 5, 'june': 6, 'all': 8}

days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
        'friday': 4, 'saturday': 5, 'sunday': 6, 'all': 13}

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
    while True:
        try:
            city = input('The name of the city to analyze (Chicago, New York City or Washington): ').lower()
            if city not in ['chicago', 'new york city', 'washington']:
                raise
            break
        except:
            print('Sorry, wrong city!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('The name of the month to filter by (January to June), or "all" to apply no month filter: ').lower()
            if month not in months:
                raise
            break
        except:
            print('Sorry, wrong month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('The name of the day of week to filter by, or "all" to apply no day filter: ').lower()
            if day not in days:
                raise
            break
        except:
            print('Sorry, wrong day!')

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
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday


    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months[month]
        df = df[df['Month'] == month]

    if day != 'all':
        # use the index of the days list to get the corresponding int
        day = days[day]
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month, day of week and start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    if month != 'all' and day != 'all':
        print("You only chose {} and {}, so these are the most common day and month!".format(day.title(), month.title()))
        print("The most common hour for {}s in {} is {}:00.".format(day.title(), month.title(), common_hour))
    elif month == 'all' and day != 'all':
        common_month = df['Month'].mode()
        for month_name, month_number in months.items():
            if month_number == common_month[0]:
                common_month_name = month_name
        print("You only chose {}, so that is the most common day of the week!".format(day.title()))
        print("The most common month for {}s is {} and".format(day.title(), common_month_name.title()))
        print("the most common hour for {}s is {}:00.".format(day.title(), common_hour))
    elif month != 'all' and day == 'all':
        common_day = df['Day of Week'].mode()
        for day_name, day_number in days.items():
            if day_number == common_day[0]:
                common_day_name = day_name
        print("You only chose {}, so that is the most common month!".format(month.title()))
        print("The most common day for {} is {} and".format(month.title(), common_day_name.title()))
        print("the most common hour for {} is {}:00.".format(month.title(), common_hour))
    else:
        common_month = df['Month'].mode()
        for month_name, month_number in months.items():
            if month_number == common_month[0]:
                common_month_name = month_name
        print("The most common month is {},".format(common_month_name.title()))
        common_day = df['Day of Week'].mode()
        for day_name, day_number in days.items():
            if day_number == common_day[0]:
                common_day_name = day_name
        print("the most common day is {} and".format(common_day_name.title()))
        print("the most common hour, regardless of month or day is {}:00.".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {},".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("the most common end station is {} and".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    trips = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("the most common trip is from {} to {}.".format(trips[0], trips[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    total_days_time = total_travel_time // 86400
    total_hours_time = (total_travel_time % 86400) // 3600
    total_mins_time = ((total_travel_time % 86400) % 3600) // 60
    total_secs_time = (((total_travel_time % 86400) % 3600) % 60) % 60
    print("The total travel time is {} seconds, or {} days, {} hours, {} minutes and {} seconds.".format(total_travel_time, total_days_time, total_hours_time,
                                                                                                total_mins_time, total_secs_time))

    # TO DO: display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    mean_hours_time = mean_travel_time // 3600
    mean_mins_time = (mean_travel_time % 3600) // 60
    mean_secs_time = (mean_travel_time % 3600) % 60
    print("The average trip is {} seconds, or {} hours, {} minutes and {} seconds.".format(mean_travel_time, mean_hours_time,
                                                                                            mean_mins_time, mean_secs_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    type_sum = df['User Type'].count()
    type_number = user_types.shape[0]
    if type_number == 0:
        print("There are no users for the selected day and month!\n")
    elif type_number == 1:
        print("There is only one type of user for the selected day and month,")
        print("{} {}s.\n".format(user_types.values[0], user_types.keys()[0].lower()))
    else:
        print("There are {} user types,".format(type_number))
        for i in range(type_number - 1):
            print("{} {}s,".format(user_types.values[i], user_types.keys()[i].lower()))
        if user_types.values[type_number - 1] == 1:
            print("and {} {}.\n".format(user_types.values[type_number - 1], user_types.keys()[type_number - 1].lower()))
        else:
            print("and {} {}s.\n".format(user_types.values[type_number - 1], user_types.keys()[type_number - 1].lower()))

    # TO DO: Display counts of gender
    if city == 'washington':
        print("Unfortunately, we have no data about gender or age for the users in Washington!")
    else:
        gender_types = df['Gender'].value_counts()
        gender_number = gender_types.shape[0]
        gender_sum = df['Gender'].count()
        if gender_sum == 0:
            print("We have no information for the users' gender regarding the selected day and month!\n")
        elif gender_number == 1:
            print("Of the {} total users,".format(type_sum))
            print("we know about {} {}s.\n".format(gender_types.values[0], gender_types.keys()[0].lower()))
        else:
            print("Of the {} total users, we know about".format(type_sum))
            for i in range(gender_number - 1):
                print("{} {}s,".format(gender_types.values[i], gender_types.keys()[i].lower()))
            print("and {} {}s.\n".format(gender_types.values[gender_number - 1], gender_types.keys()[gender_number - 1].lower()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        birth_year = df['Birth Year']
        oldest_birth = birth_year.min()
        oldest_age = time.gmtime()[0] - oldest_birth
        print("The oldest user was born in {}, so he is {} years old,".format(int(oldest_birth), int(oldest_age)))
        youngest_birth = birth_year.max()
        youngest_age = time.gmtime()[0] - youngest_birth
        print("the youngest user was born in {}, so he is {} years old and".format(int(youngest_birth), int(youngest_age)))
        common_birth = birth_year.mode()
        if common_birth.size == 1:
            common_age = time.gmtime()[0] - common_birth
            print("most of the users were born in {}, so they are {} years old.".format(int(common_birth), int(common_age)))
        else:
            common_age = time.gmtime()[0] - common_birth[0]
            print("most of the users were born either in {}, so they are {} years old".format(int(common_birth[0]), int(common_age)))
            for i in range(1, common_birth.size - 1):
                common_age = time.gmtime()[0] - common_birth[i]
                print("or where born in {}, so they are {} years old,".format(int(common_birth[i]), int(common_age)))
            common_age = time.gmtime()[0] - common_birth[common_birth.size - 1]
            print("or where born in {}, so they are {} years old.".format(int(common_birth[common_birth.size - 1]), int(common_age)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data on bikeshare users."""
    data_req = input('Would you like display the raw data for the first five users? Enter yes or no: ').lower()
    count = 0
    while data_req == 'yes':
        print(df[count: count + 5])
        count += 5
        data_req = input('Would you like display the raw data for another five users? Enter yes or no: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
