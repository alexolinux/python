# This Pyscript provides current date.

from datetime import datetime
uptime = datetime.now()

print uptime

current_year = uptime.year
current_month = uptime.month
current_day = uptime.day

print "Current YEAR: ", current_year
print "Current MONTH: ", current_month
print "Current DAY: ", current_day