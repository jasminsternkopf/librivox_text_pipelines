import re
from typing import List, Pattern, Tuple

NUMBERS_IN_SQUARE_BRACKETS = re.compile(r"\[\d+\]")  # egal ob r"..." oder nur "..."
ILLUSTRATION = re.compile(r"\[Illustration[^\]]*\]")
REPEATED_SPACES = re.compile(r" {2,}")

KING_NAMES = {"Henry", "Charles", "James", "George", "Edward",
              "Richard", "Ferdinand", "William", "Clement", "Louis", "Napoleon", "Philip", "Thibault"}

KING_NUMBER_MAPPINGS = [
  (r" I\.", " the first"),
  (r" II\.", " the second"),
  (r" III\.", " the third"),
  (r" IV\.", " the fourth"),
  (r" V\.", " the fifth"),
  (r" VI\.", " the sixth"),
  (r" VII\.", " the seventh"),
  (r" VIII\.", " the eighth"),
  (r" IX\.", " the ninth"),
  (r" X\.", " the tenth"),
  (r" XI\.", " the eleventh"),
  (r" XII\.", " the twelfth"),
  (r" XIII\.", " the thirteenth"),
  (r" XIV\.", " the fourteenth"),
  (r" XV\.", " the fifteenth")
]

KING_NUMBER_MAPPINGS_WITHOUT_DOT = [
  (r" I", " the first"),
  (r" II", " the second"),
  (r" III", " the third"),
  (r" IV", " the fourth"),
  (r" V", " the fifth"),
  (r" VI", " the sixth"),
  (r" VII", " the seventh"),
  (r" VIII", " the eighth"),
  (r" IX", " the ninth"),
  (r" X", " the tenth"),
  (r" XI", " the eleventh"),
  (r" XII", " the twelfth"),
  (r" XIII", " the thirteenth"),
  (r" XIV", " the fourteenth"),
  (r" XV", " the fifteenth")
]  # Achtung, muss andersrum durchgegangen werden!


def get_all_king_combinations():
  all_king_mappings = []
  for king_name in KING_NAMES:
    for king_number_mapping in KING_NUMBER_MAPPINGS:
      king_mapping = (re.compile(
        rf"{king_name}{king_number_mapping[0]}"), f"{king_name}{king_number_mapping[1]}")
      all_king_mappings.append(king_mapping)
  return all_king_mappings


def get_all_king_combinations_without_dot():
  all_king_mappings = []
  for king_name in KING_NAMES:
    for king_number_mapping in KING_NUMBER_MAPPINGS_WITHOUT_DOT[::-1]:
      king_mapping = (re.compile(
        rf"{king_name}{king_number_mapping[0]}"), f"{king_name}{king_number_mapping[1]}")
      all_king_mappings.append(king_mapping)
  return all_king_mappings


KING_COMBINATIONS = get_all_king_combinations()
KING_COMBINATIONS_WITHOUT_DOT = get_all_king_combinations_without_dot()

STARS = re.compile(r"( \*)+")

SHILLINGS_AND_PENCE = re.compile(r"(\d+)s\. (\d+)d\.")
SHILLINGS = re.compile(r"(\d+)s\.")

ROMAN_NUMERAL_MAPPINGS = [
  (re.compile(r" i\. The"), " one. The"),
  (re.compile(r" ii\. The"), " two. The"),
  (re.compile(r" iii\. The"), " three. The"),
  (re.compile(r" iv\. The"), " four. The"),
  (re.compile(r" v\. The"), " five. The"),
  (re.compile(r" vi\. The"), " six. The"),
  (re.compile(r" vii\. The"), " seven. The"),
  (re.compile(r" viii\. The"), " eight. The")
]

INDENTED_LINES = re.compile(r"  \[\d+\].+\n(  .+\n)*")

POINT_BEFORE_NUMBER = re.compile(r"·(\d+)")
POUND_AFTER_NUMBER = re.compile(r"(\d+) lb\.")

DOUBLE_HYPHEN_NOT_AFTER_CAPITAL_LETTER = re.compile(r"([^A-Z])--")

QUOTATION_MARK_AS_ITEMIZATION_OF_PARAGRAPH = re.compile(r"^\"([^\"]+)$\n\n", flags=re.MULTILINE)

################


def remove_linebreaks(text: str) -> str:
  text = text.replace("\n", " ")
  return text


def remove_numbers_in_square_brackets(text: str) -> str:
  text = NUMBERS_IN_SQUARE_BRACKETS.sub("", text)
  return text


def remove_illustrations(text: str) -> str:
  text = ILLUSTRATION.sub("", text)
  return text


def remove_repeated_spaces(text: str) -> str:
  text = REPEATED_SPACES.sub(" ", text)
  return text


def normalize_shillings_and_pence_in_chronicles_of_newgate(text: str) -> str:
  text = text.replace("1_s._", "one shilling")
  text = text.replace("_s._", " shillings")
  text = text.replace("_d._", " pence")
  return text


def normalize_shillings_and_pence_in_haunted_london(text: str) -> str:
  text = SHILLINGS_AND_PENCE.sub(r"\1 shillings \2 pence", text)
  text = SHILLINGS.sub(r"\1 shillings", text)
  return text


def remove_underscore_characters(text: str) -> str:
  text = text.replace("_", "")
  return text


def remove_double_hyphen_before_or_after_colon(text: str) -> str:
  text = text.replace(":--", ": ")
  text = text.replace("--:", ":")
  return text


def replace_no_with_number(text: str) -> str:
  text = text.replace("No. ", "number ")
  return text


def replace_nos_with_numbers(text: str) -> str:
  text = text.replace("Nos. ", "numbers ")
  return text


def geo_to_george(text: str) -> str:
  #text = text.replace("Geo.", "George")
  GEO_AND_C_OR_CAP = re.compile(r"Geo\. ([IVX]{1,3}\.) (c(ap)?)\. (\d)")
  text = GEO_AND_C_OR_CAP.sub(r"George \1 \2 \4", text)
  S_AFTER_GEO = re.compile(r", s. (\d)")
  text = S_AFTER_GEO.sub(r", s \1", text)
  GEO = re.compile(r"Geo\. ([IVX]{1,3}\.)")
  text = GEO.sub(r"George \1", text)
  return text


def normalize_king_names(text: str) -> str:
  for king_mapping in KING_COMBINATIONS:
    text = king_mapping[0].sub(king_mapping[1], text)
  return text


def normalize_king_names_without_dot(text: str) -> str:
  for king_mapping in KING_COMBINATIONS_WITHOUT_DOT:
    text = king_mapping[0].sub(king_mapping[1], text)
  return text


def normalize_roman_numerals_in_chronicles_of_newgate(text: str) -> str:
  for roman_numeral_mapping in ROMAN_NUMERAL_MAPPINGS:
    text = roman_numeral_mapping[0].sub(roman_numeral_mapping[1], text)
  return text


def other_chronicles_of_newgate_adujstments(text: str) -> str:
  text = text.replace("&c.", "et cetera")
  text = text.replace(" LL.", " LL ")
  text = text.replace("Schedule I", "Schedule one")
  text = text.replace("It was I", "It was I.")
  text = text.replace("Victoria, cap.", "Victoria, cap")
  return text


def replace_and_sign_with_word_and(text: str) -> str:
  text = text.replace(" & ", " and ")
  return text


def remove_stars_and_spaces(text: str) -> str:
  text = STARS.sub("", text)
  return text


def bible_verse(text: str) -> str:
  text = text.replace("Sam. iii.", "Samuel three")
  return text


def remove_indented_lines(text: str) -> str:
  text = INDENTED_LINES.sub("", text)
  return text


def remove_sic(text: str) -> str:
  text = text.replace(" [sic]", "")
  return text


def normalize_point_before_numbers(text: str) -> str:
  text = POINT_BEFORE_NUMBER.sub(r" point \1", text)
  return text


def normalize_pound(text: str) -> str:
  text = text.replace("1lb.", "one pound")
  text = text.replace("1/500 lb.", "one five hundredth pound")
  text = POUND_AFTER_NUMBER.sub(r"\1 pounds", text)
  text = text.replace("per lb.", "per pound.")
  return text


def normalize_degrees_and_latitudes(text: str) -> str:
  text = text.replace("°", " degrees")
  text = text.replace("N. lat.", "north latitude")
  return text


def expand_latin_abbreviations(text: str) -> str:
  text = text.replace("e.g.", "for example")
  text = text.replace("etc.", "et cetera")
  return text


def expand_and_a_half(text: str) -> str:
  text = text.replace("-1/2", " and a half")
  return text


# def roman_to_arabic_numbers(roman_number: str):
#   arabic_number = 0
#   while "x" in roman_number:
#     arabic_number += 10

def replace_hyphen_between_numbers_with_to(text):
  HYPHEN_BETWEEN_NUMBERS = re.compile("(\d+)-(\d+)")
  text = HYPHEN_BETWEEN_NUMBERS.sub(r"\1 to \2", text)
  # plant lifes hat nicht dieses komische 1841-9 oder so
  return text


def normalize_year_span(text):
  YEAR_SPAN = re.compile(r"(\d\d)(\d)(\d)-(\d)(\D)")
  text = YEAR_SPAN.sub(r"\1\2\3 to \2\4\5", text)
  return text


def other_plant_life_adjustments(text: str) -> str:
  text = text.replace("(see Chap. XXVIII.)", "")  # file 11, ca 13:29
  text = text.replace("xiv.", "14")  # file 10, ca 16:37
  text = text.replace("xxxvii.", "37")
  text = text.replace("E v. Proskowetz", "E v Proskowetz")
  text = text.replace("^15", " to the fifteenth power")
  text = text.replace("to the £", "to the pound")
  text = text.replace(" p. 47", "")
  text = text.replace(" (see p. 304)", "")
  return text


def other_haunted_london_adjustments(text: str) -> str:
  text = text.replace("M. Mallet", "Mister Mallet")
  text = text.replace("MSS.", "M S S")
  text = text. replace("c. 25", "c 25")
  text = text.replace("£9: 2: 3", "£9 2 and 3")
  return text


def remove_stars(text: str) -> str:
  text = text.replace("*", "")
  return text


def insert_space_before_and_after_double_hyphen(text: str) -> str:
  # exception: after capital letter
  text = DOUBLE_HYPHEN_NOT_AFTER_CAPITAL_LETTER.sub(r"\1 -- ", text)
  return text


def replace_four_hyphens_by_two(text: str) -> str:
  text = text.replace("----", "--")
  return text


def remove_quotation_marks_when_used_as_itemization(text: str) -> str:
  text = QUOTATION_MARK_AS_ITEMIZATION_OF_PARAGRAPH.sub(r"\1\n\n", text)
  return text


def remove_quotation_marks_as_itemization_in_other_cases(text: str) -> str:
  """
  Examples:
  "On Board the Schooner 'Sierra.'--
    "Off the City Front.
      "May 4, 1881.

  "CLIPPER SHIP, FLYING CLOUD,
    "January 4, 1857.

  """
  QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES = re.compile(
    r"^( *)\"([^\"\n]+)(\n\n|\n  +)", flags=re.MULTILINE)
  # two times, otherwise every second line is not subbed
  text = QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES.sub(r"\1\2\3", text)
  text = QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES.sub(r"\1\2\3", text)
  return text


def normalize_today_and_tomorrow(text: str) -> str:
  text = text.replace("To-day", "Today")
  text = text.replace("to-day", "today")
  text = text.replace("To-morrow", "Tomorrow")
  text = text.replace("to-morrow", "tomorrow")
  return text


def normalize_three_and_four_dots(text: str) -> str:
  text = text.replace("....", ".")
  THREE_POINTS_BETWEEN_SENTENCES = re.compile(r"(\.\"| )\.\.\. (\"{0,1}[A-Z])")
  THREE_POINTS_MID_SENTENCE = re.compile(r"\.\.\. ([^A-Z])")
  text = THREE_POINTS_BETWEEN_SENTENCES.sub(r"\1 \2", text)
  text = THREE_POINTS_MID_SENTENCE.sub(r"\1", text)
  text = text.replace("...", ".")
  return text


def square_brackets_to_round_brackets(text: str) -> str:
  text = text.replace("[", "(")
  text = text.replace("]", ")")
  return text


def normalize_roman_numerals_for_two_and_three(text: str) -> str:
  text = text.replace(" II. ", " Two. ")
  text = text.replace(" III. ", " Three. ")
  return text


def remove_four_hyphens(text: str) -> str:  # _when_used_directly_after_single_letter
  text = text.replace("----", "")
  return text


def remove_colon_in_digital_time_format(text: str) -> str:
  DIGITAL_TIME = re.compile(r"(\d):(\d\d)")
  text = DIGITAL_TIME.sub(r"\1 \2", text)
  return text


def add_dot_after_headings(text: str) -> str:
  HEADING = re.compile(r"\n([A-Z \"]+)\n")
  text = HEADING.sub(r"\n\1.\n", text)
  return text


def remove_dot_after_single_capital_letters(text: str) -> str:
  CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS = re.compile(r"([^A-Z])([A-Z])\.(\w)")
  while text != CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS.sub(r"\1\2 \3", text):
    text = CAPITAL_LETTERS_WITH_DOT_AND_ALPHANUM_AFTERWARDS.sub(r"\1\2 \3", text)

  CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS = re.compile(r"([^A-Z])([A-Z])\.(\W)")
  while text != CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS.sub(r"\1\2\3", text):
    text = CAPITAL_LETTERS_WITH_DOT_AND_NOT_ALPHANUM_AFTERWARDS.sub(r"\1\2\3", text)
  return text


def remove_dots_of_ie(text: str) -> str:
  text = text.replace("i.e.,", "i e,")
  text = text.replace("i. e.", "i e")
  return text


def normalize_am_and_pm(text: str) -> str:
  text = text.replace("p.m.", "p m")
  text = text.replace("a.m.", "a m")
  return text


def normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text: str) -> str:
  text = text.replace("1834-35", "1834 and 35")
  return text


MONTH_MAPPINGS: List[Tuple[Pattern, str]] = [
  (re.compile("jan\.", re.IGNORECASE), "January"),
  (re.compile("feb\.", re.IGNORECASE), "February"),
  (re.compile("mar\.", re.IGNORECASE), "March"),
  (re.compile("apr\.", re.IGNORECASE), "April"),
  (re.compile("aug\.", re.IGNORECASE), "August"),
  (re.compile("sept\.", re.IGNORECASE), "September"),
  (re.compile("oct\.", re.IGNORECASE), "October"),
  (re.compile("nov\.", re.IGNORECASE), "November"),
  (re.compile("dec\.", re.IGNORECASE), "December")
]


def write_out_month_abbreviations(text: str) -> str:
  for month in MONTH_MAPPINGS:
    text = month[0].sub(month[1], text)
  return text


def normalize_double_quotation_marks(text: str) -> str:
  text = text.replace("“", "\"")
  text = text.replace("”", "\"")
  return text


def normalize_single_quotation_marks_and_apostrophes(text: str) -> str:
  UNUSUAL_QUOTATION_MARKS = re.compile(r"‘([^’]{2,2000})’")
  text = UNUSUAL_QUOTATION_MARKS.sub(r'"\1"', text)
  text = text.replace("’", "'")
  return text


def normalize_coordinates_in_in_the_footprints_of_the_padres(text: str) -> str:
  SECONDS = re.compile(r"(\d{1,3}° \d{1,3}(-1/2)?' \d)\"")
  MINUTES = re.compile(r" (\d{1,3}° \d{1,3}(-1/2)?)'")
  DEGREES = re.compile(r"(\d{1,3})°")
  text = SECONDS.sub(r"\1 seconds", text)
  text = MINUTES.sub(r" \1 minutes", text)
  text = DEGREES.sub(r"\1 degrees", text)
  return text


def normalize_second_and_third_when_abbr_with_d(text: str) -> str:
  text = text.replace("22d", "twenty-second")
  text = text.replace("2d", "second")
  text = text.replace("3d", "third")

  return text
