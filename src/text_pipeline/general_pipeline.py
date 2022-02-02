import pickle
from pathlib import Path
from typing import Callable, List

from text_pipeline.adjustments.abbreviations import expand_abbreviations
from text_pipeline.adjustments.LJ_and_DW_adjustments import *
from text_pipeline.adjustments.numbers import normalize_numbers
from text_pipeline.adjustments.textcorpus_adjustments import (
    geo_to_george_general, replace_eg_with_for_example,
    replace_ie_with_that_is)
from text_pipeline.sentence_extraction import extract_sentences_of_all_books
from text_pipeline.auxiliary_methods.txt_files_reading import get_text_files


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
  text = remove_linebreaks(text)
  text = remove_numbers_in_square_brackets(text)
  text = remove_illustrations(text)
  text = remove_underscore_characters(text)
  text = replace_ie_with_that_is(text)
  text = replace_eg_with_for_example(text)
  text = replace_nos_with_numbers(text)
  text = replace_no_with_number(text)
  text = geo_to_george_general(text)
  text = normalize_king_names(text)
  # text = remove_dot_after_single_capital_letters(text)
  # text = normalize_am_and_pm(text)
  text = replace_hyphen_between_numbers_with_to(text)
  text = normalize_numbers(text)
  text = expand_abbreviations(text)
  text = replace_and_sign_with_word_and(text)
  text = remove_double_hyphen_before_or_after_colon(text)
  text = normalize_three_and_four_dots(text)
  text = insert_space_before_and_after_double_hyphen(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  return text


if __name__ == "__main__":
  # create_pickle_containing_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"))
  extract_sentences_of_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"),
                                 ("../DATA/data/librispeech-lm-corpus/sentencewise_corpus"))
