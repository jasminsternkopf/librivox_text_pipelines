import re


def geo_to_george(text: str) -> str:
  #text = text.replace("Geo.", "George")
  GEO_AND_C_OR_CAP = re.compile(r"Geo\. ([IVX]{1,3}\.) (c(ap)?)\. (\d)")
  text = GEO_AND_C_OR_CAP.sub(r"George \1 \2 \4", text)
  S_AFTER_GEO = re.compile(r", s. (\d)")
  text = S_AFTER_GEO.sub(r", s \1", text)
  GEO = re.compile(r"Geo\. ([IVX]{1,3}\.)")
  text = GEO.sub(r"George \1", text)
  return text


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
