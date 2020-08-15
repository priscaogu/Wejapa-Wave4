
def readable_timedelta(days):

    '''Takes in a number of days, returns the days in weeks and remaining number of days '''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

print(readable_timedelta .__doc__ )