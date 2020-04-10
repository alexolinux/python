"""Basic example of function usage"""

def shut_down(s):
  if (s.lower() == "yes"):
    return "Shutting down"
  elif (s.lower() == "not" or s.lower() == "no"):
    return "Shutdown aborted"
  else:
    return "Input is wrong bastard!"

message = input("Yes or Not: ")
print(shut_down(message))