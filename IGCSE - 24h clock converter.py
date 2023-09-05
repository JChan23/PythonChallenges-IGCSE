print("What's the time now? Please input the following information")
time = input("Is it now am or pm? ")
hour = int(input("What hour is it? "))
minute = int(input("What minute is it? "))

if time == "pm":
  hour = hour + 12
  if minute < 10:
    minute = str(minute) 
    minute = '0' + minute
  print("It is now", hour, ":", minute, "in terms of 24 hours")
elif time == "am":
  if minute < 10:
    minute = str(minute) 
    minute = '0' + minute
  print("It is now", hour, ":", minute, "in terms of 24 hours")
else:
  print('Error. Plese try again')
