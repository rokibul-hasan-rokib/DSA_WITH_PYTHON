import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2020, 5, 17)
print(y.strftime("%A"))
print(y.strftime("%B"))