import re
from typing import Iterable, Literate

from text_pipeline.adjustments.abbreviations import _unit_mappings
from text_pipeline.auxiliary_methods.txt_files_reading import \
    get_list_out_of_txt_file


def replace_ie_with_that_is(text: str) -> str:
  text = text.replace("i.e.", "that is")
  text = text.replace("I.e.", "That is")
  return text


def replace_eg_with_for_example(text: str) -> str:
  text = text.replace("e.g.", "for example")
  text = text.replace("E.g.", "For example")
  return text


def geo_to_george_general(text: str) -> str:
  text = text.replace(" Geo. ", " George ")
  return text


ONE_POUND_EXPECT_SHILLINGS_AFTERWARDS = re.compile(r" L\.? ?1,?( \d)")
ONE_POUND = re.compile(r" L\.? ?1(\W\W)")
POUNDS_WITH_DOT_AFTER_NUMBER = re.compile(r" L\.? ?(\d+[\d\.,]*)\.(\W)")
POUNDS_WITH_COMMA_AFTER_NUMBER = re.compile(r" L\.? ?(\d+[\d\.,]*)\,(\W)")
POUNDS = re.compile(r" L\.? ?(\d+[\d\.,]*)(\W)")

SHILLINGS_AND_PENCE_WITHOUT_DOT = re.compile(r" (\d{1,2}) ?s,? (\d{1,6}) ?d(\W)")
#SHILLINGS_AND_PENCE_WITHOUT_DOT = re.compile(r" (\d{1,2}) ?s,? ([\d\-/]{1,6}) ?d(\W)")
#SHILLINGS_AND_PENCE_WITH_DOT = re.compile(r" (\d{1,2}) ?s\.,? ?([\d\-/]{1,6}) ?d\.(\W)")
SHILLINGS_AND_PENCE_WITH_DOT = re.compile(r" (\d{1,2}) ?s\.,? ?(\d{1,6}) ?d\.(\W)")

ONE_SHILLING = re.compile(r" 1 ?s[\., ]{1,3}")
SHILLINGS = re.compile(r" (\d{1,2}) ?s[\., ]{1,3}")


ONE_PENNY = re.compile(r" 1 ?d\.?(\W)")
AND_A_HALF_PENCE = re.compile(r"\-?1/2 ?d\.?(\W)")
MORE_THAN_FOUR_PENCE = re.compile(r"([04-9]) ?d\.?(\W)")
# 2d and 3d often stand for second and third, with dot after them when at the end of a sentence.


def normalize_pounds(text: str) -> str:
  text = ONE_POUND_EXPECT_SHILLINGS_AFTERWARDS.sub(r" one pound\1", text)
  text = ONE_POUND.sub(r" one pound\1", text)
  text = POUNDS_WITH_DOT_AFTER_NUMBER.sub(r" \1 pounds\2", text)
  text = POUNDS_WITH_COMMA_AFTER_NUMBER.sub(r" \1 pounds\2", text)
  text = POUNDS.sub(r" \1 pounds\2", text)
  return text


def normalize_shillings_and_pounds_without_dots(text: str) -> str:
  text = SHILLINGS_AND_PENCE_WITHOUT_DOT.sub(r" \1 shillings and \2 pence\3", text)
  return text


def normalize_shillings_and_pounds_with_dots(text: str) -> str:
  text = SHILLINGS_AND_PENCE_WITH_DOT.sub(r" \1 shillings and \2 pence\3", text)
  return text


def normalize_shillings(text: str) -> str:
  text = ONE_SHILLING.sub(r" one shilling ", text)
  text = SHILLINGS.sub(r" \1 shillings ", text)
  return text


def normalize_pence(text: str) -> str:
  text = ONE_PENNY.sub(r" one penny\1", text)
  text = AND_A_HALF_PENCE.sub(r" and a half pence\1", text)
  text = MORE_THAN_FOUR_PENCE.sub(r"\1 pence\2", text)
  return text


def normalize_pounds_shillings_and_pence(text: str) -> str:
  text = normalize_pounds(text)
  text = normalize_shillings_and_pounds_with_dots(text)
  text = normalize_shillings_and_pounds_without_dots(text)
  text = normalize_shillings(text)
  text = normalize_pence(text)
  return text


# def remove_commas_in_numbers(text: str) -> str:
#   NUMBERS_WITH_COMMAS = re.compile(r"\d+(,\d{3})+")

# \d/\d+[^ ,\.\-\d/dt)_;'":lis%]

"""
Space, Komma, Punkt klar,
Klammer zu und Semikolon kommen vor,
' und " werden als Maßeinheiten (Inch?) genutzt,
ebenso lb, inch und s (seconds),
% kommt vor

Nicht dabei sein darf/Sonderbehandlung bedarf d (abgedeckt durch pence, zumindest für 2 (todo für 4), vorher behandeln) und th (getrennt behandeln)
"""

CHARS_ALLOWED_AFTER_FRACTION = r"[ ,\.\-);'\":lis%]"

ONE_HALF = re.compile(rf"1/2({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_ONE_IN_NUMERATOR = re.compile(rf"1/(\d+)({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_DENOMINATOR_EQUALS_TWO = re.compile(rf"(\d)/2({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_DENOMINATOR_EQUALS_THREE = re.compile(rf"(\d)/3({CHARS_ALLOWED_AFTER_FRACTION})")
FRACTION_WITH_NUMERATOR_NOT_ONE = re.compile(rf"(\d)/(\d+)({CHARS_ALLOWED_AFTER_FRACTION})")


def normalize_fractions(text: str) -> str:
  text = ONE_HALF.sub(r"one half\1", text)
  #text = text.replace("1/2 ", "one half ")
  text = text.replace("1/3 ", "one third ")
  text = FRACTION_WITH_ONE_IN_NUMERATOR.sub(r"one \1th\2", text)
  text = FRACTION_WITH_DENOMINATOR_EQUALS_TWO.sub(r"\1 halves\2", text)
  text = FRACTION_WITH_DENOMINATOR_EQUALS_THREE.sub(r"\1 thirds\2", text)
  return text


KING_NUMBER_MAPPINGS_WITHOUT_DOT = [
  # (re.compile(r" the I[\.st]?(\W)"), " the first"),
  (re.compile(r" the II[\.nd]{0,3}(\W)"), r" the second\1"),
  (re.compile(r" the III[\.rd]{0,3}(\W)"), r" the third\1"),
  (re.compile(r" the IV[\.th]{0,3}(\W)"), r" the fourth\1"),
  (re.compile(r" the V[\.th]{0,3}(\W)"), r" the fifth\1"),
  (re.compile(r" the VI[\.th]{0,3}(\W)"), r" the sixth\1"),
  (re.compile(r" the VII[\.th]{0,3}(\W)"), r" the seventh\1"),
  (re.compile(r" the VIII[\.th]{0,3}(\W)"), r" the eighth\1"),
  (re.compile(r" the IX[\.th]{0,3}(\W)"), r" the ninth\1"),
  (re.compile(r" the X[\.th]{0,3}(\W)"), r" the tenth\1"),
  (re.compile(r" the XI[\.th]{0,3}(\W)"), r" the eleventh\1"),
  (re.compile(r" the XII[\.th]{0,3}(\W)"), r" the twelfth\1"),
  (re.compile(r" the XIII[\.th]{0,3}(\W)"), r" the thirteenth\1"),
  (re.compile(r" the XIV[\.th]{0,3}(\W)"), r" the fourteenth\1"),
  (re.compile(r" the XV[\.th]{0,3}(\W)"), r" the fifteenth\1"),
  (re.compile(r" the XVI[\.th]{0,3}(\W)"), r" the sixteenth\1"),
  (re.compile(r" the XVII[\.th]{0,3}(\W)"), r" the seventeenth\1"),
  (re.compile(r" the XVIII[\.th]{0,3}(\W)"), r" the eighteenth\1"),
  (re.compile(r" the XIX[\.th]{0,3}(\W)"), r" the nineteenth\1"),
  (re.compile(r" the XX[\.th]{0,3}(\W)"), r" the twentieth\1")
]


def normalize_king_names_general(text: str, king_names: Iterable[str], max_number: int = 20) -> str:
  text = add_the_between_king_name_and_roman_numeral(text, king_names)
  for roman_numeral in KING_NUMBER_MAPPINGS_WITHOUT_DOT[::-1]:
    text = roman_numeral[0].sub(roman_numeral[1], text)
  return text


def add_the_between_king_name_and_roman_numeral(text: str, king_names: Iterable[str]) -> str:
  king_names_conc_with_or = "|".join(king_names)
  king_name_plus_roman_numeral = re.compile(rf"({king_names_conc_with_or}) ([XVI]{{2,5}})\.?")
  text = king_name_plus_roman_numeral.sub(rf"\1 the \2", text)
  return text


def normalize_our_king_names(text: str) -> str:
  king_names = get_list_out_of_txt_file("data/name_corpus.txt")
  text = normalize_king_names_general(text, king_names)
  return text


#\d[^ \w):;\.,\-/\d\?\]}!#%"'\[\+@=~\|]

UNIT_MAPPINGS_TIME_SINGULAR = [
  ('sec', 'second'),
  ('s', 'second'),
  ('min', 'minute'),
]

UNIT_MAPPINGS_TIME = [
  ('sec', 'seconds'),
  ('s', 'seconds'),
  ('min', 'minutes'),
]

UNIT_MAPPINGS_LENGTH_SINGULAR = [
  ('mm', 'millimeter'),
  ('cm', 'centimeter'),
  ('m', 'meter')
  ('km', 'kilometer')
]

UNIT_MAPPINGS_LENGTH = [
  ('mm', 'millimeters'),
  ('cm', 'centimeters'),
  ('m', 'meters'),
  ('km', 'kilometers')
]

UNIT_MAPPINGS_LENGTH_SINGULAR_AMERICAN = [
  #("″", "inch")
  #("′", "foot")
  ("in", "inch"),
  ("ft", "foot"),
  ("yd", "yard"),
  ("mi", "mile")

]

UNIT_MAPPINGS_LENGTH_AMERICAN = [
  ("in", "inches"),
  ("ins", "inches"),
  ("ft", "feet"),
  ("fts", "feet"),
  ("yd", "yards"),
  ("yds", "yards"),
  ("mi", "miles")

]

UNIT_MAPPINGS_WEIGHT_SINGULAR = [
  ('mg', 'milligram'),
  ('g', 'gram'),
  ('kg', 'kilogram'),
]

UNIT_MAPPINGS_WEIGHT = [
  ('g', 'grams'),
  ('kg', 'kilograms'),
]

UNIT_MAPPINGS_WEIGHT_SINGULAR_AMERICAN = [
  ("gr", "grain"),
  ("dr", "dram"),
  ("oz", "ounce")
  ("lb", "pound"),
]

_unit_abbreviations_singular = [
  (re.compile(rf" 1 ?{abbr}\b"), f" {long_form}") for abbr, long_form in UNIT_MAPPINGS_TIME]

_unit_abbreviations = [(re.compile(rf"(\d) ?{abbr}\b"), f" {long_form}")
                       for abbr, long_form in _unit_mappings]


def get_unit_abbrevaitions_as_regex(abbr_from_to: Iterable[Tuple[str, str]], dot: Literal[Literal["always"], Literal["never"], Literal["optional"]] = "optional"):
  dot_regex = get_dot_regex(dot)

def get_dot_regex(dot: str):
  if dot == "always":
    return "\."
  if dot == "never":
    return ""
  return "\.?"

def unit_mappings(text: str) -> str:
  pass
