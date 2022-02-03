import re
from typing import Iterable

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
