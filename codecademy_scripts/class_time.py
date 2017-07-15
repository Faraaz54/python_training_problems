def print_time(t):
    print "%2d : %2d : %2d" % (t.hour, t.minute, t.second)
	
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
	
def int_to_time(seconds):
    time = Time() 
    minutes, time.second = divmod(seconds, 60) 
    time.hour, time.minute = divmod(minutes, 60) 
    return time
    





class Time(object):
    """ this is a class which gives you the time
	    attributes: hours, minutes, seconds
    """
    def print_time(self):
        print "%2d : %2d : %2d" % (self.hour, self.minute, self.second)
		
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
	    
		
			
	
time = Time()
time.print_time()
t = Time()
t.hour = 5
t.minute = 10
t.second = 15
t.print_time()












