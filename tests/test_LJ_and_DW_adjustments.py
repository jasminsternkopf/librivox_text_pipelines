from LJ_and_DW_adjustments import (
    normalize_item_list, normalize_no_and_roman_numeral,
    normalize_roman_numerals_in_chronicles_of_newgate, remove_indented_lines,
    remove_quotation_marks_as_itemization_in_other_cases)


def test_normalize_roman_numberals__in_chronicles_of_newgate():
  text = " i. The male debtors' side.   ii. The female debtors' side.   iii. The chapel yard.   iv. The middle yard.   v. The master felons' side.   vi. The female felons' side.   vii. The state side.   viii. The press yard."
  res = normalize_roman_numerals_in_chronicles_of_newgate(text)

  assert res == " one. The male debtors' side.   two. The female debtors' side.   three. The chapel yard.   four. The middle yard.   five. The master felons' side.   six. The female felons' side.   seven. The state side.   eight. The press yard."


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


def test_normalize_no_and_roman_numeral():
  text = "I found No. II., you found No. V.!"
  res = normalize_no_and_roman_numeral(text)

  assert res == "I found number 2, you found number 5!"


def test_normalize_item_list():
  text = "      Item   I. The tree where Cook was struck.\n        \"   II. The rock where Cook fell.\n        \"  III. The altar on the hill-top.\n        \"   IV. The riven palms.\n        \"    V. The sole survivor,--the boy that ran.\n        \"   VI. A specimen sepulchre in the cliff."
  res = normalize_item_list(text)

  assert res == "      Item   I. The tree where Cook was struck.\n        Item 2 The rock where Cook fell.\n        Item 3 The altar on the hill-top.\n        Item 4 The riven palms.\n        Item 5 The sole survivor,--the boy that ran.\n        Item 6 A specimen sepulchre in the cliff."
