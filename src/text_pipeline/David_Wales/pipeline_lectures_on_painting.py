from english_text_normalization import (
    expand_abbreviations, insert_space_before_and_after_double_hyphen,
    normalize_double_quotation_marks, normalize_numbers,
    normalize_king_name_followed_by_roman_numeral, normalize_second_and_third_when_abbr_with_d,
    normalize_single_quotation_marks_and_apostrophes,
    normalize_today_tomorrow_and_tonight,
    remove_dot_after_single_capital_letters, remove_dot_before_comma,
    remove_double_hyphen_before_or_after_colon,
    remove_everything_in_square_brackets, remove_linebreaks,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_stars, remove_underscore_characters, replace_etc_with_et_cetera,
    replace_nos_with_numbers)
from LJ_and_DW_adjustments import normalize_minute_colon_seconds


def normalize_lectures_on_painting(text: str) -> str:
  text = normalize_double_quotation_marks(text)
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_linebreaks(text)
  text = normalize_today_tomorrow_and_tonight(text)
  text = remove_underscore_characters(text)
  text = normalize_single_quotation_marks_and_apostrophes(text)
  text = remove_everything_in_square_brackets(text)
  text = replace_etc_with_et_cetera(text)
  text = replace_nos_with_numbers(text)
  text = expand_abbreviations(text)
  text = normalize_king_name_followed_by_roman_numeral(text)
  text = remove_dot_after_single_capital_letters(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = normalize_second_and_third_when_abbr_with_d(text)
  text = normalize_minute_colon_seconds(text)
  text = normalize_numbers(text)
  text = remove_dot_before_comma(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
