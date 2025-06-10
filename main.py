def classify_age(age):
  if age < 0:
    return "Invalid age"
  elif age <= 13:
    return "Child"
  elif age <= 19:
    return "Teenager"
  elif age <= 60:
    return "Adult"
  else:
    return "Senior"


try:
  age = int(input("Enter your age: "))
  group = classify_age(age)
  print(f"You are a {group}.")
except ValueError:
  print("Invalid input. Please enter a valid age.")
