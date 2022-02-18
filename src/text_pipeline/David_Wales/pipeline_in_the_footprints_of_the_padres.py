from english_text_normalization import (
    add_dot_after_headings, expand_abbreviations, expand_and_a_half,
    insert_space_before_and_after_double_hyphen, normalize_am_and_pm,
    normalize_degrees_minutes_and_seconds,
    normalize_king_name_followed_by_roman_numeral, normalize_numbers,
    normalize_second_and_third_when_abbr_with_d, normalize_three_and_four_dots,
    normalize_today_tomorrow_and_tonight,
    number_to_word_when_number_at_beginning_of_sentence,
    remove_colon_in_digital_time_format,
    remove_dot_after_single_capital_letters,
    remove_double_hyphen_before_or_after_colon, remove_four_hyphens,
    remove_illustrations, remove_linebreaks, remove_numbers_in_square_brackets,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_stars, remove_underscore_characters, replace_and_sign_with_word_and,
    replace_etc_with_et_cetera, replace_no_with_number,
    write_out_month_abbreviations)
from LJ_and_DW_adjustments import (
    normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres,
    normalize_roman_numerals_for_two_and_three, remove_dots_of_ie,
    remove_quotation_marks_as_itemization_in_other_cases,
    square_brackets_to_round_brackets)


def normalize_in_the_footprints_of_the_padres(text: str) -> str:
  text = add_dot_after_headings(text)
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_quotation_marks_as_itemization_in_other_cases(text)
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = replace_etc_with_et_cetera(text)
  text = normalize_king_name_followed_by_roman_numeral(text)
  text = write_out_month_abbreviations(text)
  text = normalize_roman_numerals_for_two_and_three(text)
  text = remove_dot_after_single_capital_letters(text)
  text = remove_dots_of_ie(text)
  text = normalize_am_and_pm(text)
  text = normalize_today_tomorrow_and_tonight(text)
  text = normalize_three_and_four_dots(text)
  text = replace_no_with_number(text)
  text = expand_abbreviations(text)
  text = remove_underscore_characters(text)
  text = remove_illustrations(text)
  text = square_brackets_to_round_brackets(text)
  text = remove_four_hyphens(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_colon_in_digital_time_format(text)
  text = normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text)
  text = normalize_degrees_minutes_and_seconds(text)
  text = expand_and_a_half(text)
  text = normalize_second_and_third_when_abbr_with_d(text)
  text = number_to_word_when_number_at_beginning_of_sentence(text)
  text = normalize_numbers(text)
  text = replace_and_sign_with_word_and(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
