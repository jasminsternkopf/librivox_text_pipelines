# from text_pipeline.adjustments.abbreviations import expand_abbreviations
# from text_pipeline.adjustments.numbers import normalize_numbers
# from LJ_and_DW_adjustments import (
#     add_dot_after_headings, bible_verse, expand_and_a_half,
#     expand_latin_abbreviations, geo_to_george,
#     insert_space_before_and_after_double_hyphen, normalize_am_and_pm,
#     normalize_coordinates_in_in_the_footprints_of_the_padres,
#     normalize_degrees_and_latitudes, normalize_double_quotation_marks,
#     normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres,
#     normalize_king_names, normalize_king_names_without_dot,
#     normalize_point_before_numbers, normalize_pound,
#     normalize_roman_numerals_for_two_and_three,
#     normalize_roman_numerals_in_chronicles_of_newgate,
#     normalize_second_and_third_when_abbr_with_d,
#     normalize_shillings_and_pence_in_chronicles_of_newgate,
#     normalize_shillings_and_pence_in_haunted_london,
#     normalize_single_quotation_marks_and_apostrophes,
#     normalize_three_and_four_dots, normalize_today_and_tomorrow,
#     other_chronicles_of_newgate_adujstments, other_haunted_london_adjustments,
#     other_plant_life_adjustments, remove_colon_in_digital_time_format,
#     remove_dot_after_single_capital_letters, remove_dots_of_ie,
#     remove_double_hyphen_before_or_after_colon, remove_four_hyphens,
#     remove_illustrations, remove_indented_lines, remove_linebreaks,
#     remove_numbers_in_square_brackets,
#     remove_quotation_marks_as_itemization_in_other_cases,
#     remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
#     remove_sic, remove_stars, remove_stars_and_spaces,
#     remove_underscore_characters, replace_and_sign_with_word_and,
#     replace_four_hyphens_by_two, replace_hyphen_between_numbers_with_to,
#     replace_no_with_number, replace_nos_with_numbers,
#     square_brackets_to_round_brackets, write_out_month_abbreviations)
from english_text_normalization import (
    add_dot_after_headings, expand_abbreviations, expand_and_a_half,
    insert_space_before_and_after_double_hyphen, normalize_am_and_pm,
    normalize_numbers, normalize_our_king_names,
    normalize_point_before_numbers,
    normalize_second_and_third_when_abbr_with_d, normalize_three_and_four_dots,
    normalize_today_and_tomorrow, remove_dot_after_single_capital_letters,
    remove_double_hyphen_before_or_after_colon, remove_linebreaks,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_sic, remove_stars, remove_underscore_characters,
    replace_and_sign_with_word_and, replace_four_hyphens_by_two,
    replace_hyphen_between_numbers_with_to, replace_no_with_number,
    replace_nos_with_numbers, write_out_month_abbreviations)

# [^\w \.,\-"';():!?éèëæœöñôäüáàçâê]
# [^\w .,\-"';():“”’!?éèëæœ‘öñôäüáàçâê]
# [^\.]\.\.\.[^\. ]
# \.[^\.]\.\.\.[^\.]
# [A-Z]\.


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
