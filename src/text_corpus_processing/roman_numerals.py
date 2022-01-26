import pickle
import re
from typing import List

with open('all_books.pickle', 'rb') as f:
  books = pickle.load(f)

all_roman_numerals = re.compile(r"I?V?I{0,2}")


def roman_units() -> List[str]:
  all_roman_units = ["IV", "IX"]
  for no_of_ones in range(4):
    for no_of_fives in range(2):
      roman_numeral = "V" * no_of_fives + "I" * no_of_ones
      all_roman_units.append(roman_numeral)
  return all_roman_units
