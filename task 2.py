from math import ceil

def total_cost(calls_log:tuple) -> int:
    cost = 0
    dates = {}
    
    for call_log in calls_log:
        date_log, _, seconds_log = call_log.split(" ")
        if (date_log in dates):
            dates[date_log] += ceil(int(seconds_log) / 60)
        else:
            dates[date_log] = ceil(int(seconds_log) / 60)

    for minutes in dates.values():
        if minutes <= 100:
            cost += minutes
        else:
            cost += 100 + (minutes - 100) * 2
    
    return cost

if __name__ == "__main__": 
    assert total_cost(("2014-01-01 01:12:13 181",
    "2014-01-02 20:11:10 600",
    "2014-01-03 01:12:13 6009",
    "2014-01-03 12:13:55 200")) == 124