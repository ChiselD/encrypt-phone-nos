# https://dev.to/devteam/daily-challenge-32-hide-phone-numbers-ham
# specs:
# - US phone no. as user input, allowing input variation
# - check validity of length/chars
# - print no. with last six digits anonymized

def encrypt():
  # Get and sanitize user input
  user_input = input("Enter phone number: ")
  num = sanitize(user_input)
  # Check US phone no. validity
  valid = validate(num)
  if valid:
    anonymized = anonymize(user_input)
    print(anonymized)
  else:
    invalid()

def invalid():
  raise TypeError("Invalid phone number")

def sanitize(user_input):
  # Returns input with all non-digits removed
  allowed = ['(', ')', '-', '+', ' ']
  arr = [] # the digits only, for validation purposes
  for i in user_input:
    # Check for disallowed characters
    if (i.isdigit() == False) and (i not in allowed):
      print("Invalid character present!")
      invalid()
    elif (i.isdigit()):
      arr.append(i)
    else:
      pass
  sanitized = ''.join(arr)
  print(f"Sanitization complete: {sanitized}")
  return sanitized

def validate(num):
  if (len(num) != 10):
    return False
  else:
    print(f"Validation complete: {num}")
    return True

def anonymize(phone_number):
  arr = list(phone_number)
  arr.reverse()
  result = []
  # Keep track of how many digits have been anonymized
  count = 1
  for i in arr:
    if count < 7 and i.isdigit():
      result.append('X')
      count += 1
    else:
      result.append(i)
  result.reverse()
  anonymized = ''.join(result)
  return anonymized

encrypt()