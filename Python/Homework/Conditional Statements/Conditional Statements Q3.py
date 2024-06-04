# Question 3 :- printing the name of the day corresponding to the day number using match case:

def day_name(day):
  match day:
    case 1:
      return "Monday"
    case 2:
      return "Tuesday"
    case 3:
      return "Wednesday"
    case 4:
      return "Thursday"
    case 5:
      return "Friday"
    case 6:
      return "Saturday"
    case 7:
      return "Sunday"
    case default:
      print("Invalid day number")


day = int(input("Enter the day number :"))

result = day_name(day)
print(result)
