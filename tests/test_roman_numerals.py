from text_corpus_processing.roman_numerals import roman_units


def test_roman_units():
  units = roman_units()

  assert units == ["IV", "IX", "", "V", "I", "VI", "II", "VII", "III", "VIII"]
