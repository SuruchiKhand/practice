# 4. Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.


class Time(object):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes  = minutes

    def addTime(t1, t2):
        t3 = Time(0, 0)
        t3.hours = t1.hours + t2.hours
        t3.minutes = t3.minutes + t2.minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3
    
    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))

    def displayMinutes(self):
        print((self.hours * 60) +self.minutes, "minutes")

a = Time(2, 90)
b = Time(1, 90)
c = Time.addTime(a,b)

c.displayTime()
c.displayMinutes()

input()


