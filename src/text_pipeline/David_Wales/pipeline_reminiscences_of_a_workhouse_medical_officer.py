from english_text_normalization import (
    expand_abbreviations, insert_space_before_and_after_double_hyphen,
    normalize_am_and_pm, normalize_numbers,
    remove_dot_after_single_capital_letters,
    remove_dot_after_word_not_followed_by_new_sentence,
    remove_everything_in_square_brackets, remove_linebreaks,
    remove_repeated_spaces, remove_underscore_characters,
    replace_and_char_c_dot_with_and_so_forth,
    replace_hyphen_between_numbers_with_to)
from LJ_and_DW_adjustments import normalize_hell_and_damned


def normalize_reminiscences_of_a_workhouse_medical_officer(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_underscore_characters(text)
  text = replace_and_char_c_dot_with_and_so_forth(text)
  text = normalize_hell_and_damned(text)
  text = remove_everything_in_square_brackets(text)
  text = expand_abbreviations(text)
  text = normalize_am_and_pm(text)
  text = remove_dot_after_single_capital_letters(text)
  text = remove_dot_after_word_not_followed_by_new_sentence(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = normalize_numbers(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
