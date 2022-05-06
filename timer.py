def timer(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    if seconds == 1:
        return "1 second"
    
    elif seconds < 60:
        return f"{seconds} seconds"
    
    elif seconds == 60:
        return "1 minute" 

    elif seconds == 61:
        return "1 minute and 1 second"

    elif seconds > 60 and hours == 0:
        seconds = seconds - (minutes * 60)
        return f"{minutes} minutes and {seconds} seconds"
    
    elif seconds == 3600:
        return "1 hour"
    
    elif seconds == 3601:
        return "1 hour and 1 second"
    
    elif seconds == 3660:
        return "1 hour and 1 minute"
    
    elif seconds == 3661:
        return "1 hour, 1 minute, and 1 second"
    
    elif seconds < 86400:
        seconds = seconds - (minutes * 60)
        minutes = minutes - (hours * 60)
        return f"{hours} hours, {minutes} minutes and {seconds} seconds"
    
    elif seconds == 31536000:
        return "1 year"
    
    elif seconds > 31536000:
        seconds = seconds - (minutes * 60)
        minutes = minutes - (hours * 60)
        hours = hours - (days * 24)
        days = days - (years * 365)
        return f"{years} years, {hours} hours, {minutes} minutes and {seconds} seconds"
        
        
def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        return timer(seconds)
        
print(format_duration(31536362))

# nie dziala jesli jest dokladnie jeden rok i wiecej niz 1 wartosc z kazdego rodzaju