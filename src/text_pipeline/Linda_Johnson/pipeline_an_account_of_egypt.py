from english_text_normalization import (
    insert_space_before_and_after_double_hyphen,
    remove_double_hyphen_before_or_after_colon, remove_linebreaks,
    remove_repeated_spaces, remove_stars, remove_underscore_characters)


def normalize_account_of_egypt(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_underscore_characters(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
