import re

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


def bible_verse(text: str) -> str:
  text = text.replace("Sam. iii.", "Samuel three")
  return text


INDENTED_LINES = re.compile(r"  \[\d+\].+\n(  .+\n)*")


def remove_indented_lines(text: str) -> str:
  text = INDENTED_LINES.sub("", text)
  return text


def normalize_pound(text: str) -> str:
  text = text.replace("1lb.", "one pound")
  text = text.replace("1/500 lb.", "one five hundredth pound")
  text = text.replace("per lb.", "per pound.")
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


QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES = re.compile(
    r"^( *)\"([^\"\n]+)(\n\n|\n  +)", flags=re.MULTILINE)

"""
Examples:
"On Board the Schooner 'Sierra.'--
  "Off the City Front.
    "May 4, 1881.

"CLIPPER SHIP, FLYING CLOUD,
  "January 4, 1857.

"""


def remove_quotation_marks_as_itemization_in_other_cases(text: str) -> str:
  # two times, otherwise every second line is not subbed
  text = QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES.sub(r"\1\2\3", text)
  text = QUOTATION_MARK_AS_ITEMIZATION_OTHER_CASES.sub(r"\1\2\3", text)
  return text


def square_brackets_to_round_brackets(text: str) -> str:
  text = text.replace("[", "(")
  text = text.replace("]", ")")
  return text


def normalize_roman_numerals_for_two_and_three(text: str) -> str:
  text = text.replace(" II. ", " Two. ")
  text = text.replace(" III. ", " Three. ")
  return text


def remove_dots_of_ie(text: str) -> str:
  text = text.replace("i.e.,", "i e,")
  text = text.replace("i. e.", "i e")
  return text


def normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text: str) -> str:
  text = text.replace("1834-35", "1834 and 35")
  return text


ROMAN_NUMERALS_TILL_SIX = ["I", "II", "III", "IV", "V", "VI"]
NO_AND_ROMAN_NUMERAL = [re.compile(rf" No\. {num}\.") for num in ROMAN_NUMERALS_TILL_SIX]


def normalize_no_and_roman_numeral(text: str) -> str:
  # only I to V appear in south sea idyls
  for number in range(1, 6):
    text = NO_AND_ROMAN_NUMERAL[number - 1].sub(f" number {number}", text)
  return text


def normalize_confessor_and_pere_fidelis(text: str) -> str:
  text = text.replace("_Conf._", "Confessor.")
  text = text.replace("_Père F._", "Père Fidelis.")
  return text


ITEM_PLUS_NUMERAL = [re.compile(rf"\"\s+{numeral}\.") for numeral in ROMAN_NUMERALS_TILL_SIX[1:]]


def normalize_item_list(text: str) -> str:
  for number in range(2, 7):
    text = ITEM_PLUS_NUMERAL[number - 2].sub(f"Item {number}", text)
  return text


def four_hyphens_followed_by_dot_into_blank(text: str) -> str:
  text = text.replace(" ----.", " blank.")
  return text


def footnote_normalization_in_south_sea_idyls(text: str) -> str:
  text = text.replace("[A] Haleakala", "Footnote Haleakala")
  text = text.replace("[A]", "")
  return text


def L_into_Lew(text: str) -> str:
  text = text.replace("L----", "Lew")
  return text


MINUTE_COLON_SECONDS = re.compile(r"(\d):(\d)")


def normalize_minute_colon_seconds(text: str) -> str:
  text = MINUTE_COLON_SECONDS.sub(r"\1 and \2", text)
  return text
