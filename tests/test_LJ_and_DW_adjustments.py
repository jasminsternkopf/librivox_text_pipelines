from english_text_normalization import \
    normalize_our_king_names as normalize_king_names_without_dot
from LJ_and_DW_adjustments import (
    geo_to_george, normalize_roman_numerals_in_chronicles_of_newgate,
    remove_indented_lines,
    remove_quotation_marks_as_itemization_in_other_cases)


def test_normalize_roman_numberals__in_chronicles_of_newgate():
  text = " i. The male debtors' side.   ii. The female debtors' side.   iii. The chapel yard.   iv. The middle yard.   v. The master felons' side.   vi. The female felons' side.   vii. The state side.   viii. The press yard."
  res = normalize_roman_numerals_in_chronicles_of_newgate(text)

  assert res == " one. The male debtors' side.   two. The female debtors' side.   three. The chapel yard.   four. The middle yard.   five. The master felons' side.   six. The female felons' side.   seven. The state side.   eight. The press yard."


def test_geo_to_george():
  text = "9th Geo. IV."
  res = geo_to_george(text)

  assert res == "9th George IV."


def test_geo_to_george_with_c_and_s():
  text = "9th Geo. III. c. 64, s. 5"
  res = geo_to_george(text)

  assert res == "9th George III. c 64, s 5"


def test_geo_to_george_with_c_no_s():
  text = "9th Geo. I. c. 64"
  res = geo_to_george(text)

  assert res == "9th George I. c 64"


def test_geo_to_george_with_cap_and_s():
  text = "9th Geo. IV. cap. 64, s. 45"
  res = geo_to_george(text)

  assert res == "9th George IV. cap 64, s 45"


def test_geo_to_george_with_cap_no_s():
  text = "9th Geo. IV. cap. 64"
  res = geo_to_george(text)

  assert res == "9th George IV. cap 64"


def test_remove_indented_lines():
  text = "  [11] Hartig finds the specific gravity of the wood in a tree is\n  increased from 0-60 to 0.74 when the surrounding wood has been\n  cut down.--_Bot. Central_, vol. xxx, p. 220.\n"
  res = remove_indented_lines(text)

  assert res == ""


def test_remove_quotation_marks_in_other_cases():
  text = "\"On Board the Schooner 'Sierra.'--\n  \"Off the City Front.\n    \"May 4, 1881.\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == "On Board the Schooner 'Sierra.'--\n  Off the City Front.\n    May 4, 1881.\n\n"


def test_remove_quotation_marks_in_other_cases_2():
  text = "\"CLIPPER SHIP, FLYING CLOUD,\n  \"January 4, 1857.\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == "CLIPPER SHIP, FLYING CLOUD,\n  January 4, 1857.\n\n"


def test_remove_remove_quotation_marks_in_other_cases_do_not_match_because_is_quotation():
  text = "\n\n\"Hello world!\" is what the computer said.\n\nI replied \"alright\".\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == text


def test_normalize_king_names_without_dot():
  text = "Charles III and James I, Henry V and Edward VI."
  res = normalize_king_names_without_dot(text)

  assert res == "Charles the third and James the first, Henry the fifth and Edward the sixth."
