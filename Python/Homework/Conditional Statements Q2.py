# to assign grade based on score (0-100) using nested if-else

score = int(input("Enter the score: "))

if score >= 90 :
  print("A")
else :
  if score >= 80 :
    print("B")
  else:
    if score >= 70 :
      print("C")
    else :
      if score >= 60 :
        print("D")
      else :
        print("F")
