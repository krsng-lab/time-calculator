def add_time(start, duration, day=None): 
    
    # handle start
    start_time, start_period = start.split()
    start_hours, start_minutes = start_time.split(":")
    
    # handle duration
    duration_hours, duration_minutes = duration.split(":")

    # handle days
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # handle calculation
    new_time_hours = int(start_hours) + int(duration_hours)
    new_day = 0
    while new_time_hours > 12:
        new_time_hours -= 12
        if start_period == "PM":
            start_period = "AM"
            new_day += 1
        elif start_period == "AM":
            start_period = "PM"
    if new_time_hours == 12:
        if start_period == "PM":
            start_period = "AM"
            new_day += 1
        elif start_period == "AM":
            start_period = "PM"
    
    new_time_minutes = int(start_minutes) + int(duration_minutes)

    # When minutes exceed 59
    if new_time_minutes > 59:
        new_time_minutes = int(new_time_minutes) - 60
        new_time_hours += 1
        if new_time_hours == 12: 
            if start_period == "PM":
                start_period = "AM"
                new_day += 1
            elif start_period == "AM":
                start_period = "PM"

    # handle day
    if day:
        start_day_index = days.index(day.capitalize())
        end_day_index = (start_day_index + new_day) % 7 
        end_day = days[end_day_index]

    
    new_time_minutes = f'{new_time_minutes:02}'
    if new_day == 1:
        if day:
            return(f'{new_time_hours}:{new_time_minutes} {start_period}, {end_day} (next day)')

        else:
            return(f'{new_time_hours}:{new_time_minutes} {start_period} (next day)')

    elif new_day == 0:
        if day:
            return(f'{new_time_hours}:{new_time_minutes} {start_period}, {end_day}')
        
        else:
            return(f'{new_time_hours}:{new_time_minutes} {start_period}')

    else:
        if day:
            return(f'{new_time_hours}:{new_time_minutes} {start_period}, {end_day} ({new_day} days later)')
        
        else:
            return(f'{new_time_hours}:{new_time_minutes} {start_period} ({new_day} days later)')
