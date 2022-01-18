from typing import Set

from unidecode import unidecode

#IGNORE_SET_ = set("âáàäæçêéèëñôöœü")
IGNORE_SET_A = set("Á")

print(IGNORE_SET_)


def unidecode_with_ignore_set(string: str, ignore_set: Set[str] = {}) -> str:
  unidecoded_chars = []
  for char in string:
    if char in ignore_set:
      unidecoded_chars.append(char)
    else:
      unidecoded_chars.append(unidecode(char))
  unidecoded_string = "".join(unidecoded_chars)
  return unidecoded_string
