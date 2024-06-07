"""
Q4:- code for multiple inheritance
"""

class Camera:
  def take_photo(self):
    return "Taking photo"

class Phone:
  def call(self):
    print("Calling from phone")

class SmartPhone(Camera, Phone):
  def play_game(self):
    return "Playing game"

  def call(self):
    super().call()
    print("Calling from smartphone")

smartphone = SmartPhone()
print(smartphone.take_photo())
smartphone.call()
print(smartphone.play_game())
