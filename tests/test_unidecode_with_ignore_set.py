from text_pipeline.adjustments.unidecode_with_ignore_set import \
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
