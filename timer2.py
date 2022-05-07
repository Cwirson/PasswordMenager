def timer(seconds):
    if seconds == 0:
        return "now"
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    
    seconds = seconds - (minutes * 60)
    minutes = minutes - (hours * 60)
    hours = hours - (days * 24)
    days = days - (years * 365)
    years = years
    
    timedict = {"year":years, "day":days, "hour":hours, "minute":minutes, "second":seconds}
    
    list_of_values = []
    list_of_formats = []
    for timevalue in timedict:
        if timedict[timevalue] == 1:
            list_of_values.append(timedict[timevalue])
            list_of_formats.append(timevalue)
        elif timedict[timevalue] > 1:
            list_of_values.append(timedict[timevalue])
            timevalue += "s"
            list_of_formats.append(timevalue)
    if len(list_of_formats) == 1:
        return f"{list_of_values[0]} {list_of_formats[0]}"
    elif len(list_of_formats) == 2:
        return f"{list_of_values[0]} {list_of_formats[0]} and {list_of_values[1]} {list_of_formats[1]}"
    elif len(list_of_formats) == 3:
        return f"{list_of_values[0]} {list_of_formats[0]}, {list_of_values[1]} {list_of_formats[1]} and {list_of_values[2]} {list_of_formats[2]}"
    elif len(list_of_formats) == 4:
        return f"{list_of_values[0]} {list_of_formats[0]}, {list_of_values[1]} {list_of_formats[1]}, {list_of_values[2]} {list_of_formats[2]} and {list_of_values[3]} {list_of_formats[3]}"
    elif len(list_of_formats) == 5:
        return f"{list_of_values[0]} {list_of_formats[0]}, {list_of_values[1]} {list_of_formats[1]}, {list_of_values[2]} {list_of_formats[2]}, {list_of_values[3]} {list_of_formats[3]} and {list_of_values[4]} {list_of_formats[4]}"

