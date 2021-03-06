########################################
# E3 Countdown
# Countdown to next E3 Event
# Python 3
# Mindi - contact@mindinet.org
# Best way to watch: http://twitch.tv/totalbiscuit
########################################

from datetime import datetime, time

# Coundown to given date
def CountdownToDate(Date="0", Event="none"):
    timedelta = Date - datetime.now()
    seconds = timedelta.days * 24 * 3600 + timedelta.seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
	
    if Event == "none":
        return "Set event name please."

# Lets show only what needed
    elif days == 0:
        if hours == 0:
            return "%s: %dmin %dsec" %(Event, minutes, seconds)
        else:
            return "%s: %dh %dmin %dsec" %(Event, hours, minutes, seconds)
    elif days > 1:
        return "%s: %ddays %dh %dmin %dsec" %(Event, days, hours, minutes, seconds)
    else:
        return "%s: %dday %dh %dmin %dsec" %(Event, days, hours, minutes, seconds)

def NextE3():
# Time list if you add others remember add also event name on other list (These times are in UTC + 3, change if needed)
    TimeList = [
    '2017-06-10 21:45:00', 
    '2017-06-11 23:45:00',
    '2017-06-12 06:45:00',
    '2017-06-12 22:45:00',
    '2017-06-13 03:45:00',
    '2017-06-13 19:00:00',
    '2017-06-13 21:00:00'
    ];
	
# Event name list
    EventList  = [
    'EA Conference', 
    'MS Conference',
    'Bethesda Conference',
    'UBI Conference',
    'Sony Conference',
    'Nintendo Spotlight',
    'Elite Dangerous E3 Live'
    ];
	
# Let's check if and when there is next event
    count = 0
    while (count < len(TimeList)):
        Date = datetime.strptime(TimeList[count], '%Y-%m-%d %H:%M:%S')
        TimeCheck = (Date - datetime.now()).days * 24 * 3600 + (Date - datetime.now()).seconds
        if TimeCheck > 0:
            return(CountdownToDate(Date, EventList[count]))
            sys.exit()
        count = count + 1

# And now just print if there is event
if NextE3() != None:
    print(NextE3())
else:
    print("E3 is over")
