from english_text_normalization import (
    expand_abbreviations, geo_to_george,
    insert_space_before_and_after_double_hyphen, normalize_am_and_pm,
    normalize_king_name_followed_by_roman_numeral, normalize_numbers,
    normalize_per_cent_dot, normalize_pounds_shillings_and_pence,
    normalize_three_and_four_dots,
    number_to_word_when_number_at_beginning_of_sentence,
    remove_dot_after_single_capital_letters,
    remove_dot_after_single_small_letters, remove_dot_between_word_and_number,
    remove_double_hyphen_before_or_after_colon,
    remove_everything_in_square_brackets, remove_linebreaks,
    remove_repeated_spaces, remove_underscore_characters,
    replace_and_sign_with_word_and, replace_hyphen_between_numbers_with_to,
    replace_no_with_number)
from LJ_and_DW_adjustments import (
    normalize_roman_numerals_in_chronicles_of_newgate,
    other_chronicles_of_newgate_adjustments, remove_dot_of_viz,
    remove_dots_of_ie)


def normalize_chronicles_of_newgate(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_everything_in_square_brackets(text)
  text = remove_underscore_characters(text)
  text = normalize_pounds_shillings_and_pence(text)
  text = remove_dots_of_ie(text)
  text = remove_dot_of_viz(text)
  text = normalize_per_cent_dot(text)
  text = replace_no_with_number(text)
  text = geo_to_george(text)
  text = normalize_king_name_followed_by_roman_numeral(text)
  text = normalize_roman_numerals_in_chronicles_of_newgate(text)
  text = expand_abbreviations(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_am_and_pm(text)
  text = remove_dot_after_single_small_letters(text)
  text = remove_dot_between_word_and_number(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = number_to_word_when_number_at_beginning_of_sentence(text)
  text = normalize_numbers(text)
  text = other_chronicles_of_newgate_adjustments(text)
  text = replace_and_sign_with_word_and(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = normalize_three_and_four_dots(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
