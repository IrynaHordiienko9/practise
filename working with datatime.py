from datetime import timedelta
from datetime import date

def checkio(start_date, end_date):
    weekends = 0
    current_date = start_date
    while current_date <= end_date:
        day = current_date.weekday()
        if day == 5 or day == 6: 
            weekends += 1
        current_date += timedelta(days=1)
    return weekends 


if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"