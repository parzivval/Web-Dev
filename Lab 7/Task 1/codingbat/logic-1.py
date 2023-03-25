def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  return 40 <= cigars <= 60

def date_fashion(you, date):
      if (you <= 2 or date <= 2):
          return 0
      elif (you >= 8 or date >= 8):
          return 2
      else:
          return 1

def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  return 60 <= temp <= 90


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    if 60 < speed <= 80:
        return 1
    return 2

def sorta_sum(a, b):
  sum = a + b
  if(10 <= sum <= 19):
    return 20
  else:
    return sum


def alarm_clock(day, vacation):
    if not vacation:
        if 1 <= day <= 5:
            return '7:00'
        return '10:00'
    if 1 <= day <= 5:
        return '10:00'
    return 'off'

def love6(a, b):
  if(a == 6 or b == 6 or (a + b == 6) or (a - b == 6) or (b - a == 6)):
    return True
  else:
    return False


def in1to10(n, outside_mode):
  if not outside_mode:
    return n in range(1, 11)
  return n <= 1 or n >= 10

def near_ten(num):
  return num % 10 in [0,1,2,8,9,10]
