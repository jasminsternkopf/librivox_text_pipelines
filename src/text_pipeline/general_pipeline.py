import pickle
from pathlib import Path
from typing import Callable, List

from text_pipeline.adjustments.abbreviations import expand_abbreviations
from text_pipeline.adjustments.emails import normalize_emails_and_at
from text_pipeline.adjustments.king_names_normalization import \
    normalize_our_king_names
from text_pipeline.adjustments.LJ_and_DW_adjustments import *
from text_pipeline.adjustments.money_normalization import \
    normalize_pounds_shillings_and_pence
from text_pipeline.adjustments.normalize_degrees import (
    normalize_degrees_minutes_and_seconds, normalize_temperatures_general)
from text_pipeline.adjustments.numbers import normalize_numbers
from text_pipeline.adjustments.textcorpus_adjustments import (
    geo_to_george_general, normalize_percent, remove_equal_sign,
    replace_eg_with_for_example, replace_etc_with_et_cetera,
    replace_ie_with_that_is)
from text_pipeline.adjustments.unit_abbreviations_normalization import \
    normalize_all_units
from text_pipeline.auxiliary_methods.txt_files_reading import get_text_files
from text_pipeline.sentence_extraction import extract_sentences_of_all_books


def create_pickle_containing_all_books(folder: Path):
  paths = get_text_files(folder)
  books: List[str] = []
  for path in paths:
    book = path.read_text()
    books.append(book)
  with open('all_books.pickle', 'wb') as file:
    pickle.dump(books, file)


def general_pipeline(text: str) -> str:
  text = add_dot_after_headings(text)
  text = remove_quotation_marks_when_used_as_itemization(text)
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = normalize_emails_and_at(text)
  text = remove_underscore_characters(text)
  text = remove_equal_sign(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = replace_ie_with_that_is(text)
  text = replace_eg_with_for_example(text)
  text = replace_etc_with_et_cetera(text)  # untesrcheidund groß/kleinbuchstabe danach?
  text = replace_nos_with_numbers(text)
  text = replace_no_with_number(text)
  text = geo_to_george_general(text)
  text = write_out_month_abbreviations(text)
  text = normalize_today_and_tomorrow(text)
  text = normalize_our_king_names(text)
  text = normalize_am_and_pm(text)
  text = normalize_pounds_shillings_and_pence(text)
  text = normalize_temperatures_general(text)
  text = normalize_degrees_minutes_and_seconds(text)
  text = normalize_all_units(text)
  text = normalize_percent(text)
  text = expand_and_a_half(text)
  # text = normalize_fractions(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_second_and_third_when_abbr_with_d(text)  # abändern, allgemeiner machen
  # text = remove_colon_in_digital_time_format(text) ist oft bibelstelle
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = remove_dot_after_single_capital_letters(text)
  text = replace_and_sign_with_word_and(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = normalize_three_and_four_dots(text)
  text = replace_four_hyphens_by_two(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_sic(text)
  text = remove_stars(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text
# alles in [] wegcutten \[[^I\dFGS_g]


if __name__ == "__main__":
  # create_pickle_containing_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"))
  extract_sentences_of_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"),
                                 ("../DATA/data/librispeech-lm-corpus/sentencewise_corpus"))
