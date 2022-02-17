from english_text_normalization import (
    expand_abbreviations, expand_and_a_half,
    insert_space_before_and_after_double_hyphen,
    normalize_degrees_minutes_and_seconds, normalize_latitude_and_longitude,
    normalize_length_units, normalize_numbers, normalize_our_king_names,
    normalize_per_cent_dot_if_not_end_of_sentence,
    normalize_point_before_numbers, normalize_pounds_shillings_and_pence,
    normalize_three_and_four_dots, normalize_today_tomorrow_and_tonight,
    normalize_weight_units,
    number_to_word_when_number_at_beginning_of_sentence,
    remove_dot_after_single_capital_letters,
    remove_double_hyphen_before_or_after_colon, remove_illustrations,
    remove_linebreaks, remove_numbers_in_square_brackets,
    remove_repeated_spaces, remove_sic, remove_underscore_characters,
    replace_eg_with_for_example, replace_etc_with_et_cetera,
    replace_four_hyphens_by_two, replace_hyphen_between_numbers_with_to)
from LJ_and_DW_adjustments import (normalize_pound,
                                   other_plant_life_adjustments,
                                   remove_dot_of_viz, remove_indented_lines)


def normalize_romance_of_plant_life(text: str) -> str:
  text = remove_indented_lines(text)
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = remove_underscore_characters(text)
  text = normalize_pounds_shillings_and_pence(text)
  text = normalize_three_and_four_dots(text)
  text = normalize_our_king_names(text)
  text = normalize_today_tomorrow_and_tonight(text)
  text = replace_etc_with_et_cetera(text)
  text = replace_eg_with_for_example(text)
  text = remove_dot_of_viz(text)
  text = normalize_per_cent_dot_if_not_end_of_sentence(text)
  text = remove_dot_after_single_capital_letters(text)
  text = normalize_pound(text)
  text = normalize_weight_units(text)
  text = normalize_length_units(text)
  text = normalize_latitude_and_longitude(text)
  text = normalize_degrees_minutes_and_seconds(text)
  text = normalize_point_before_numbers(text)
  text = expand_and_a_half(text)
  text = other_plant_life_adjustments(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = number_to_word_when_number_at_beginning_of_sentence(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = remove_sic(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = replace_four_hyphens_by_two(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
