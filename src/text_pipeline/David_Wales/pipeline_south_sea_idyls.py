from english_text_normalization import (
    expand_abbreviations, insert_space_before_and_after_double_hyphen,
    normalize_numbers, normalize_three_and_four_dots,
    normalize_today_and_tomorrow, remove_dot_after_single_capital_letters,
    remove_double_hyphen_before_or_after_colon, remove_equal_sign,
    remove_everything_in_square_brackets, remove_four_hyphens,
    remove_linebreaks, remove_plus,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_stars, remove_tilde, remove_underscore_characters,
    replace_etc_with_et_cetera, write_out_month_abbreviations)
from LJ_and_DW_adjustments import (L_into_Lew,
                                   footnote_normalization_in_south_sea_idyls,
                                   four_hyphens_followed_by_dot_into_blank,
                                   normalize_confessor_and_pere_fidelis,
                                   normalize_item_list,
                                   normalize_no_and_roman_numeral,
                                   normalize_roman_numerals_for_two_and_three)


def normalize_south_sea_idyls(text: str) -> str:
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_linebreaks(text)
  text = write_out_month_abbreviations(text)
  text = normalize_no_and_roman_numeral(text)
  text = normalize_item_list(text)
  text = normalize_roman_numerals_for_two_and_three(text)
  text = normalize_confessor_and_pere_fidelis(text)
  text = footnote_normalization_in_south_sea_idyls(text)
  text = remove_everything_in_square_brackets(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_today_and_tomorrow(text)
  text = normalize_three_and_four_dots(text)
  text = replace_etc_with_et_cetera(text)
  text = expand_abbreviations(text)
  text = remove_underscore_characters(text)
  text = remove_equal_sign(text)
  text = remove_tilde(text)
  text = remove_plus(text)
  text = four_hyphens_followed_by_dot_into_blank(text)
  text = L_into_Lew(text)
  text = remove_four_hyphens(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = normalize_numbers(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
