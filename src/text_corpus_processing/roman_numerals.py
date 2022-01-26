import pickle
import re
from typing import List

# with open('all_books.pickle', 'rb') as f:
#   books = pickle.load(f)

# all_roman_numerals = re.compile(r"I?V?I{0,2}")


# def roman_numerals_for_a_certain_power_of_ten(power_of_ten: str, five_times_power_of_ten: str, next_power_of_ten) -> List[str]:
#   all_numerals = [power_of_ten + five_times_power_of_ten, power_of_ten + next_power_of_ten]
#   for no_of_power_of_ten in range(4):
#     for no_of_five_times_power_of_ten in range(2):
#       roman_numeral = five_times_power_of_ten * \
#         no_of_five_times_power_of_ten + power_of_ten * no_of_power_of_ten
#       all_numerals.append(roman_numeral)
#   return all_numerals

def roman_numerals_for_a_certain_power_of_ten(power_of_ten: str, five_times_power_of_ten: str, next_power_of_ten: str, max_number: int) -> List[str]:
  max_number = max_number % 10
  all_numerals = [power_of_ten + five_times_power_of_ten, power_of_ten + next_power_of_ten]
  for no_of_power_of_ten in range(4):
    for no_of_five_times_power_of_ten in range(2):
      roman_numeral = five_times_power_of_ten * \
        no_of_five_times_power_of_ten + power_of_ten * no_of_power_of_ten
      all_numerals.append(roman_numeral)
  return all_numerals


def roman_units() -> List[str]:
  return roman_numerals_for_a_certain_power_of_ten("I", "V", "X")


def roman_tens() -> List[str]:
  return roman_numerals_for_a_certain_power_of_ten("X", "L", "C")


def get_all_roman_numerals_up_to_N(N: int) -> List[str]:
  assert N > 0
  if N < 9:

    # def roman_units() -> List[str]:
    #   all_roman_units = ["IV", "IX"]
    #   for no_of_ones in range(4):
    #     for no_of_fives in range(2):
    #       roman_numeral = "V" * no_of_fives + "I" * no_of_ones
    #       all_roman_units.append(roman_numeral)
    #   return all_roman_units

    # def roman_tens() -> List[str]:
    #   all_roman_units = ["IV", "IX"]
    #   for no_of_ones in range(4):
    #     for no_of_fives in range(2):
    #       roman_numeral = "V" * no_of_fives + "X" * no_of_ones
    #       all_roman_units.append(roman_numeral)
    #   return all_roman_units
