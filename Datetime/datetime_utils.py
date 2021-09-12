import datetime


#dt_string = "2020-12-18 3:11:09"
#dt_string = "2020-12-18 00:00:00"
dt_string = "2020-12-18 00:00:00"
format = "%Y-%m-%d %H:%M:%S"

dt_object = datetime.datetime.strptime(dt_string, format)

print("Datetime: ", dt_object)
print("Minute: ", dt_object.minute)
print("Hour: ", dt_object.hour)
print("Second: ", dt_object.second)
