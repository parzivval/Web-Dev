def hello_name(name):
  return ("Hello " + name + "!")

def make_abba(a, b):
  return (a + b + b + a)

def make_tags(tag, word):
  tagopen = "<" + tag + ">"
  tagclose = "</" + tag + ">"
  return tagopen + word + tagclose

def make_out_word(out, word):
  outfirst = out[:2]
  outlast = out[2:]
  return outfirst + word + outlast

def extra_end(str):
  str = str[len(str)-2:]
  return (str * 3)

def first_two(str):
  if (str <= 2):
    return str
  else:
    str = str[:2]
    return str

def first_half(str):
      str = str[:len(str) / 2]
      return str

def without_end(str):
  str = str[1:len(str)-1]
  return str
def combo_string(a, b):
  a_length = len(a)
  b_length = len(b)
  if(a_length > b_length):
    return b + a + b
  else:
    return a + b + a

def non_start(a, b):
  a = a[1:]
  b = b[1:]
  return a + b

def left2(str):
  if(len(str) <= 2):
    return str
  else:
    strfirst = str[:2]
    strend = str[2:]
    return strend + strfirst