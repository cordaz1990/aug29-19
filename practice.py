class Time:
  """ Represent the time of day """

def print_time(time):
    print('%.2d: %.2d:%.2d' % (time.hour, time.minute, time.second))
    
start = Time()
start.hour = 9
start. minute = 45
start.second = 00
print_time(start)
09:45:00
