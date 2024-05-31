#Question 3:- Function to determine whether a date is valid or not:

def validate_date(day,month,year):
  if day < 1 or day > 31:
    return "Invalid day"
  else:
    if month < 1 or month > 12:
      return "Invalid month"
    else :
      if year <= 0 :
        return "Invalid year"
      else :
        isleapyear = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
        ajsn = (month == 4 or month == 6 or month == 9 or month == 11)
        f = (month == 2)
        if isleapyear:
          if ajsn:
            if day == 31:
              return "Invalid day"
            else :
              return "Valid date"
          elif f:
            if day == 30 or day == 31:
              return "Invalid day"
            else :
              return "Valid date"
          else :
            return "Valid date"
        else :
          if ajsn:
            if day == 31:
              return "Invalid day"
            else :
              return "Valid date"
          elif f:
            if day == 29 or day == 30 or day == 31:
              return "Invalid day"
            else:
              return "Valid date"
          else:
            return "Valid date"


day = int(input("Enter the day :"))
month = int(input("Enter the month :"))
year = int(input("Enter the year :"))

message = validate_date(day,month,year)
print(message)
