def disemvowel(word):
  words = list(word)
  new_letters = []
  for i in words:
    if i.upper() == "A" or i.upper() == "E" or i.upper() == "I" or i.upper() == "O" or i.upper() == "U":
        pass
    else:
      new_letters.append(i)
  return(''.join(new_letters))