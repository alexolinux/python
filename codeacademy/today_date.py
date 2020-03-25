from datetime import datetime
now = datetime.now()

print("Current Month: \t%02d" % now.month)
print("Current Day: \t%02d" % now.day)
print("Current Year: \t%04d" % now.year)

print(("Formated Date: \t%02d/%02d/%04d") % (now.month, now.day, now.year))