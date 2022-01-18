from text_pipeline.adjustments.abbreviations import expand_abbreviations
from text_pipeline.adjustments.numbers import normalize_numbers
from text_pipeline.adjustments.other_adjustments import (
    add_dot_after_headings, bible_verse, expand_and_a_half,
    expand_latin_abbreviations, geo_to_george,
    insert_space_before_and_after_double_hyphen, normalize_am_and_pm,
    normalize_degrees_and_latitudes,
    normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres,
    normalize_king_names, normalize_king_names_without_dot,
    normalize_point_before_numbers, normalize_pound,
    normalize_roman_numerals_for_two_and_three,
    normalize_roman_numerals_in_chronicles_of_newgate,
    normalize_shillings_and_pence_in_chronicles_of_newgate,
    normalize_shillings_and_pence_in_haunted_london,
    normalize_three_and_four_dots, normalize_today_and_tomorrow,
    other_chronicles_of_newgate_adujstments, other_haunted_london_adjustments,
    other_plant_life_adjustments, remove_colon_in_digital_time_format,
    remove_dot_after_single_capital_letters, remove_dots_of_ie,
    remove_double_hyphen_after_colon, remove_four_hyphens,
    remove_illustrations, remove_indented_lines, remove_linebreaks,
    remove_numbers_in_square_brackets,
    remove_quotation_marks_as_itemization_in_other_cases,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_sic, remove_stars, remove_stars_and_spaces,
    remove_underscore_characters, replace_four_hyphens_by_two,
    replace_hyphen_between_numbers_with_to, replace_no_with_number,
    replace_nos_with_numbers, square_brackets_to_round_brackets,
    write_out_month_abbreviations)

# [^\w .,\-"';():“”’!?éèëæœ‘öñôäüáàçâê]
# [^\.]\.\.\.[^\. ]
# \.[^\.]\.\.\.[^\.]
# [A-Z]\.


def normalize_chronicles_of_newgate(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = normalize_shillings_and_pence_in_chronicles_of_newgate(text)
  text = remove_underscore_characters(text)
  text = replace_no_with_number(text)
  text = geo_to_george(text)
  text = normalize_king_names(text)
  text = normalize_roman_numerals_in_chronicles_of_newgate(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_am_and_pm(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = other_chronicles_of_newgate_adujstments(text)
  text = remove_double_hyphen_after_colon(text)
  text = normalize_three_and_four_dots(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


"""
1835-6  ... to six
1823-4 ... to four
"""


def normalize_haunted_london(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = normalize_shillings_and_pence_in_haunted_london(text)
  text = remove_underscore_characters(text)
  text = replace_no_with_number(text)
  text = replace_nos_with_numbers(text)
  text = normalize_king_names(text)
  text = other_haunted_london_adjustments(text)
  text = remove_dot_after_single_capital_letters(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = expand_latin_abbreviations(text)
  text = remove_stars_and_spaces(text)
  text = bible_verse(text)
  text = normalize_three_and_four_dots(text)
  text = remove_double_hyphen_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


"""
1721-4 ... to twenty-four
1753-4 ... to four
"""


def normalize_plant_life(text: str) -> str:
  text = remove_indented_lines(text)
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = remove_underscore_characters(text)
  text = normalize_three_and_four_dots(text)
  text = normalize_king_names_without_dot(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_pound(text)
  text = normalize_degrees_and_latitudes(text)
  text = normalize_point_before_numbers(text)
  text = expand_and_a_half(text)
  text = other_plant_life_adjustments(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = expand_latin_abbreviations(text)
  text = remove_sic(text)
  text = remove_double_hyphen_after_colon(text)
  text = replace_four_hyphens_by_two(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


def normalize_account_of_egypt(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_underscore_characters(text)
  text = remove_double_hyphen_after_colon(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text

# David Wales


def normalize_in_the_footprints_of_the_padres(text: str) -> str:
  text = add_dot_after_headings(text)
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_quotation_marks_as_itemization_in_other_cases(text)
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = normalize_king_names(text)
  text = write_out_month_abbreviations(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_roman_numerals_for_two_and_three(text)
  text = remove_dot_after_single_capital_letters(text)
  text = remove_dots_of_ie(text)
  text = normalize_am_and_pm(text)
  text = normalize_today_and_tomorrow(text)
  text = normalize_three_and_four_dots(text)
  text = replace_no_with_number(text)
  text = expand_abbreviations(text)
  text = remove_underscore_characters(text)
  text = remove_illustrations(text)
  text = square_brackets_to_round_brackets(text)
  text = remove_four_hyphens(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_colon_in_digital_time_format(text)
  text = normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text)
  text = normalize_numbers(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


def normalize_south_sea_idyls(text: str) -> str:
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_quotation_marks_as_itemization_in_other_cases(text)
  text = remove_linebreaks(text)
  # text = normalize_king_names(text)
  # text = write_out_month_abbreviations(text)
  # text = remove_dot_after_single_capital_letters(text)
  # text = normalize_roman_numerals_for_two_and_three(text)
  # text = remove_dot_after_single_capital_letters(text)
  # text = normalize_am_and_pm(text)
  # text = normalize_today_and_tomorrow(text)
  text = normalize_three_and_four_dots(text)
  # text = replace_no_with_number(text)
  # text = expand_abbreviations(text)
  # text = remove_underscore_characters(text)
  # text = remove_illustrations(text)
  # text = square_brackets_to_round_brackets(text)
  # text = remove_four_hyphens(text)
  # text = insert_space_before_and_after_double_hyphen(text)
  # text = remove_colon_in_digital_time_format(text)
  # text = normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text)
  text = normalize_numbers(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


# O pitiless Nature! thy irrevocable laws argue sore sacrifice in the
# waste places of God's universe!...
