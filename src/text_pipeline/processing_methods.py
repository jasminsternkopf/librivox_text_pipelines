import pickle
import re
from pathlib import Path
from typing import Callable, List

from text_pipeline.adjustments.abbreviations import expand_abbreviations
from text_pipeline.adjustments.numbers import normalize_numbers
from text_pipeline.adjustments.LJ_and_DW_adjustments import *
from text_pipeline.txt_files_reading import get_text_files

from text_pipeline.additional_adjustments import (
    geo_to_george_general, replace_eg_with_for_example,
    replace_ie_with_that_is)


def create_pickle_containing_all_books(folder: Path):  # , normalizer: Callable[[str], str]):
  paths = get_text_files(folder)
  books: List[str] = []
  for path in paths:
    book = path.read_text()
    books.append(book)
    # normalized_text = normalizer(book)
  with open('all_books.pickle', 'wb') as file:
    pickle.dump(books, file)


# create_pickle_containing_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"))


def cut_off_beginning(text: str) -> str:
  pass


def cut_off_the_end_and_everything_after_it(text: str) -> str:
  THE_END = re.compile(r"\nthe end\.?(\n)*.{0,1000}$")


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


def extract_sentences_of_all_books(folder: Path, new_folder: Path) -> str:
  paths = get_text_files(folder)
  for path in paths:
    book = path.read_text()
    sentencewise_book = extract_sentences(book)
    new_path_with_txt_file = new_folder / path.relative_to(folder)
    new_path = new_path_with_txt_file.parent
    if not new_path.exists():
      new_path.mkdir(parents=True)
    new_path_with_txt_file.write_text(sentencewise_book, encoding="UTF-8")


def extract_sentences_old(text: str) -> str:
  text = remove_linebreaks(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  SENTENCE_ENDS = (".", "?", "!")
  SENTENCE_ENDS = (re.escape(x) for x in SENTENCE_ENDS)
  SENTENCE_ENDS_AND_CAPITAL_LETTER = (re.compile(rf"({end}\"?) ([A-Z])") for end in SENTENCE_ENDS)
  for sentence_end in SENTENCE_ENDS_AND_CAPITAL_LETTER:
    text = sentence_end.sub(r"\1\n\2", text)
  # text = text.replace(". ", ".\n")
  # text = text.replace("? ", "?\n")
  # text = text.replace("! ", "!\n")
  # text = text.replace(".\" ", ".\"\n")
  # text = text.replace("?\" ", "?\"\n")
  # text = text.replace("!\" ", "!\"\n")
  return text


def extract_sentences(text: str) -> str:
  text = remove_linebreaks(text)
  text = expand_abbreviations(text)
  text = remove_dot_after_single_capital_letters(text)
  text = remove_repeated_spaces(text)
  text = text.strip()
  SENTENCE_ENDS = (".", "?", "!")
  SENTENCE_ENDS = (re.escape(x) for x in SENTENCE_ENDS)
  SENTENCE_ENDS_AND_CAPITAL_LETTER = (re.compile(
    rf"({end}\"?)(?: |\-\-|\.\.\.)(\"?[A-Z])") for end in SENTENCE_ENDS)
  for sentence_end in SENTENCE_ENDS_AND_CAPITAL_LETTER:
    text = sentence_end.sub(r"\1\n\2", text)
  text = remove_quotation_marks_in_line_if_uneven_number_of_them(text)
  return text


def remove_quotation_marks_in_line_if_uneven_number_of_them(text: str) -> str:
  sentences = text.split("\n")
  new_sentences = []
  for sentence in sentences:
    if sentence.count("\"") % 2 == 1:
      sentence = sentence.replace("\"", "")
    new_sentences.append(sentence)
  new_sentences_single_string = "\n".join(new_sentences)
  return new_sentences_single_string


extract_sentences_of_all_books(Path("../DATA/data/librispeech-lm-corpus/corpus"),
                               ("../DATA/data/librispeech-lm-corpus/sentencewise_corpus"))

# def normalize_all_files_in_folder(folder: Path, new_folder: Path, normalizer: Callable[[str], str]):
#   paths = get_text_files(Path("data/librispeech-lm-corpus/corpus"))
#   for path in paths:
#     text = path.read_text()
#     normalized_text = normalizer(text)
#     new_path_with_txt_file = new_folder / path.relative_to(folder)
#     new_path = new_path_with_txt_file.parent
#     if not new_path.exists():
#       new_path.mkdir(parents=True)
#     new_path_with_txt_file.write_text(normalized_text, encoding="UTF-8")
