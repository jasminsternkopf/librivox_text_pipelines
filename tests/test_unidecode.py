from text_pipeline.adjustments.unidecode_with_ignoreset import \
    unidecode_with_ignore_set


def test_unidecode_with_ignore_set__no_ignore_set():
  text = "Κνωσός"
  res = unidecode_with_ignore_set(text)

  assert res == "Knosos"


def test_unidecode_with_ignore_set():
  text = "ÄbCdéèfGüÜ"
  ignore_set = {"ä", "ü", "é"}
  res = unidecode_with_ignore_set(text, ignore_set)

  assert res == "AbCdéefGüU"

# from text_pipeline.adjustments.unidecode_with_ignoreset import (unidecode,
#                                                  unidecode_expect_nonascii)


# def test_unidecode():
#   text = "Κνωσός"
#   res = unidecode(text)

#   assert res == ""


# def test_unidecode__2():
#   text = "ABCÜ"
#   res = unidecode(text)

#   assert res == "ABC"


# def test_unidecode_expect_nonascii():
#   text = "Κνωσός"
#   res = unidecode_expect_nonascii(text)

#   assert res == "Knosos"
