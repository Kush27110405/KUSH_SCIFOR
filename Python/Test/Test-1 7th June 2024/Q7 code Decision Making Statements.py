"""
Q7:- code for decision making statements (using switch case)
"""
def day_to_activity(day):
  match day:
    case "Monday":
      return "Cook at home"
    case "Tuesday":
      return "Go to gym"
    case "Wednesday":
      return "read a book"
    case "Thursday":
      return "Play games"
    case "Friday":
      return "Party"
    case "Saturday":
      return "Watch a movie"
    case "Sunday":
      return "Sleep"
    case _:
      return "Invalid day"

day = input("Enter a day: ")
print(day_to_activity(day))
