from english_text_normalization import (
    expand_abbreviations, insert_space_before_and_after_double_hyphen,
    normalize_double_quotation_marks, normalize_numbers,
    normalize_our_king_names, normalize_pounds_shillings_and_pence,
    normalize_second_and_third_when_abbr_with_d,
    normalize_single_quotation_marks_and_apostrophes,
    normalize_three_and_four_dots, remove_dot_after_single_capital_letters,
    remove_double_hyphen_before_or_after_colon, remove_illustrations,
    remove_linebreaks, remove_numbers_in_square_brackets,
    remove_repeated_spaces, remove_stars, remove_underscore_characters,
    replace_eg_with_for_example, replace_etc_with_et_cetera,
    replace_hyphen_between_numbers_with_to, replace_no_with_number,
    replace_nos_with_numbers)
from LJ_and_DW_adjustments import bible_verse, other_haunted_london_adjustments


def normalize_haunted_london(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = normalize_pounds_shillings_and_pence(text)
  text = remove_underscore_characters(text)
  text = replace_no_with_number(text)
  text = replace_nos_with_numbers(text)
  text = normalize_our_king_names(text)
  text = other_haunted_london_adjustments(text)
  text = normalize_double_quotation_marks(text)
  text = normalize_single_quotation_marks_and_apostrophes(text)
  text = replace_eg_with_for_example(text)
  text = replace_etc_with_et_cetera(text)
  text = remove_dot_after_single_capital_letters(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_second_and_third_when_abbr_with_d(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = remove_stars(text)
  text = bible_verse(text)
  text = normalize_three_and_four_dots(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
