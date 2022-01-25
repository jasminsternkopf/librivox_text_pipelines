import re

from text_corpus_processing.search_pattern_in_books import \
    search_pattern_in_all_books


def test_search_pattern_in_all_books():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert res == "Abcdef\nabcdef"


def test_search_pattern_in_all_books__double_result_cut_out():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 1)

  assert res == "bcde"

def test_search_pattern_in_all_books__pattern_at_beginning_and_end():
  books = [
    "Abcdefg",
    "abcdef",
    "fg",
  ]
  pattern = "fg"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert res == "defg\nfg"

