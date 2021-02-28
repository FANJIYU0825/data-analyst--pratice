"""Date utilities."""
import datetime
import time


WEEKDAY_MAP = {
    0: 'Mon',
    1: 'Tue',
    2: 'Wed',
    3: 'Thu',
    4: 'Fri',
    5: 'Sat',
    6: 'Sun',
}


DAYS_IN_MONTH = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def prev_date(date):
    """Get the date for the previous day.

    Args:
      date: String.

    Returns:
      String.
    """
    today_date = str_to_date(date)
    yesterday_date = today_date - datetime.timedelta(days=1)
    return date_to_str(yesterday_date)


def days_in_month(year, month):
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    return DAYS_IN_MONTH[month]


def date_to_datetime(date):
    """Convert a date to a datetime.

    Args:
      date: datetime.date.

    Returns:
      datetime.datetime.
    """
    return datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day)


def date_time_to_date(date_time):
    return datetime.date(date_time.year, date_time.month, date_time.day)


def hour_start_end(date, hour):
    """Determine timestamps for hour start and end for filtering.

    Since we are taking the previous hour, if the hour is 7 then the start
    and end returned from this function will filter out everything in
      6pm <= x < 7pm

    Args:
      date: String of format "yyy-mm-dd".
      hour: Integer hour in 24 hour time.

    Returns:
      start: Integer timestamp.
      end: Integer timetamp.
    """
    date = date_to_datetime(str_to_date(date))
    start_date_time = date + datetime.timedelta(hours=hour-1)
    end_date_time = date + datetime.timedelta(hours=hour)
    start_timestamp = timestamp_from_date(start_date_time)
    end_timestamp = timestamp_from_date(end_date_time)
    return start_timestamp, end_timestamp


def date_start_end(date):
    """Convert UTC date into UTC start and end timestamps for Taiwan time.

    The intended usage is `start <= date < end`, noting the less than for end
    as it is defined to be 00:00 the next day.

    Args:
      date: datetime.date.

    Returns:
      start: integer timestamp.
      end: integer timestamp.
    """
    date_time = datetime.datetime.combine(date, datetime.datetime.min.time())
    a_day = datetime.timedelta(days=1)
    eight_hours = datetime.timedelta(hours=8)
    start = date_time - eight_hours
    end = date_time + a_day - eight_hours
    return timestamp_from_date(start), timestamp_from_date(end)


def week_start_end(date):
    """Get start and end timestamps for a week, mapping UTC to Taiwan time.

    Args:
      date: datetime.date.

    Returns:
      start: timestamp.
      end: timestamp.
    """
    days = days_for_week(date, False)
    start = date_start_end(days[0])[0]
    end = date_start_end(days[-1])[1]
    return start, end


def month_start_end(date):
    """Get start and end timestamps for a month, mapping UTC to Taiwan time.

    Args:
      date: datetime.date.

    Returns:
      start: timestamp.
      end: timestamp.
    """
    start = first_day_of_month(date)
    end = first_day_next_month(date) - datetime.timedelta(days=1)
    start = date_start_end(start)[0]
    end = date_start_end(end)[1]
    return start, end


def first_day_next_month(date):
    """Get the first day in the next month.

    Args:
      date: datetime.date.

    Returns:
      datetime.date.
    """
    if date.month == 12:
        return datetime.date(year=date.year+1, month=1, day=1)
    else:
        return datetime.date(year=date.year, month=date.month+1, day=1)


def date_from_timestamp(timestamp):
    """Convert a timestamp into a DateTime.

    The unusual thing here is dividing the timestamp by 1,000 to get rid of the
    extra three zeros at the end, motivating creating a function to do this
    conveniently. Timestamps should have 10 numbers. But the data has 13.

    Args:
      timestamp: Integer.

    Returns:
      datetime.datetime.
    """
    if timestamp > 1e11:
        timestamp /= 1e3
    return datetime.datetime.fromtimestamp(timestamp)


def timestamp_from_date(date_time):
    """Get a timestamp from a datetime.

    Args:
      date_time: datetime.datetime.

    Returns:
      Integer.

    Raises:
      ValueError: if not a datetime or a date.
    """
    if isinstance(date_time, datetime.datetime):
        return int(time.mktime(date_time.timetuple()) * 1000
                   + (date_time.microsecond / 1000))
    elif isinstance(date_time, datetime.date):
        return int(time.mktime(date_time.timetuple()) * 1000)
    else:
        raise ValueError('Unexpected type: %r' % type(date_time))


def convert_time(x, add_time=True):
    """Convert the DATE and TIME in a row to a single datetime object.

    Note: the TIME data originally comes as strings and includes some '-'
    entries.

    Args:
      x: Dictionary / JSON.
      add_time: Bool. If True the timedelta from TIME will be added to the DATE
        obtained from the timestamp. Default is True.

    Returns:
      datetime.datetime
    """
    t = date_from_timestamp(x['DATE'])
    if add_time \
            and 'TIME' in x.keys() \
            and x['TIME'] not in [0, '-']:
        t = t + datetime.timedelta(seconds=x['TIME'])
    return t


def date_range(start, end):
    """Get a  date range including from and including `start` to `end`.

    Args:
      start: datetime.date.
      end: datetime.date.

    Returns:
      List of datetime.date.
    """
    return [end - datetime.timedelta(days=x)
            for x in reversed(range(0, (end - start).days + 1))]


def days_for_week(date, to_date=True):
    """Gets a list of days up to `date` that belong to the same week.

    Args:
      date: datetime.date.
      to_date: Bool. If True the date range only goes up to date, as opposed to
        the end of the week.

    Returns:
      List of datetime.date.
    """
    weekday = date.weekday()
    start = date - datetime.timedelta(days=weekday)
    if to_date:
        return date_range(start, date)
    else:
        return date_range(start, start + datetime.timedelta(days=6))


def days_for_month(date, to_date=True):
    """Gets a list of days up to `date` that belong to the same month.

    Args:
      date: datetime.date.
      to_date: Bool. If True the date range only goes up to date, as opposed to
        the end of the month.

    Returns:
      List of datetime.date.
    """
    start = first_day_of_month(date)
    if to_date:
        return date_range(start, date)
    else:
        return date_range(start, last_day_of_month(date.year, date.month))


def first_day_of_month(date):
    """Get the first day of the month `date` falls in.

    Args:
      date: datetime.date.

    Returns:
      datetime.date.
    """
    return datetime.date(year=date.year, month=date.month, day=1)


def last_day_of_month(year, month):
    return datetime.date(year, month, days_in_month(year, month))


def str_to_date(date):
    """Convert the expected form of date string to date object.

    Args:
      date: String of form yyyy-mm-dd.

    Returns:
      datetime.date.
    """
    if 'T' in date:
        date = date.split('T')[0]
    return datetime.date(*(int(x) for x in date.split('-')))


def date_to_str(date):
    """Convert a date to a string of the expected form.

    Args:
      date: datetime.date.

    Returns:
      String of form yyyy-mm-dd.
    """
    def pad(i):
        s = str(i)
        if len(s) == 1:
            return '0' + s
        return s

    return '%s-%s-%s' % (date.year, pad(date.month), pad(date.day))


def check_date_format(date, logger):
    """"Validates a date parameter.

    Args:
      date: String. Should be in format yyyy-mm-dd.
      logger: logger.

    Raises:
      ValueError if date is not in the correct format.
    """
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        logger.error('Cannot parse date of format: %r' % date)
        raise e


def subtract_months(date, months):
    """Subtract months from a date.

    Can only handle up to 12 months.

    Args:
      date: datetime.date.
      months: integer.

    Returns:
      datetime.date.

    Raises:
      ValueError if months > 12.
    """
    if months > 12:
        raise ValueError('Can only handle up to 12 months.')
    new_year = date.year
    new_month = date.month - months
    new_day = date.day
    if new_month < 1:
        new_year -= 1
        new_month = 12 + new_month
    return datetime.date(new_year, new_month, new_day)
