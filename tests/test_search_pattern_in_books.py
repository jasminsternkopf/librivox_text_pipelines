import re

from text_corpus_processing.search_pattern_in_books import (
    process_matches, search_pattern_in_all_books)


def test_search_pattern_in_all_books():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert list(res) == ["Abcdef", "abcdef"]


def test_search_pattern_in_all_books__double_result_cut_out():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 1)

  assert list(res) == ["bcde", "bcde"]


def test_search_pattern_in_all_books__pattern_at_beginning_and_end():
  books = [
    "Abcdefg",
    "abcdef",
    "fg",
  ]
  pattern = "fg"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 2)

  assert list(res) == ["defg", "fg"]


def test_search_pattern_in_all_books__with_new_lines_in_book():
  books = [
    "Abc\ndefg",
    "abcd\nef",
    "ab\ncdefg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  res = search_pattern_in_all_books(pattern, books, 3)

  assert list(res) == ["abcd", "cdefg"]


def test_process_matches__cut_out_duplicates():
  books = [
    "Abcdefg",
    "abcdef",
    "ABCDEfg",
  ]
  pattern = "cd"  # re.compile(r"cd")
  matches = search_pattern_in_all_books(pattern, books, 1)
  res = process_matches(matches)

  assert res == "bcde"


def test_process_matches__sort_alphabetically():
  books = [
    "Abc\ndefg",
    "ab\ncdefg",
    "abcd\nef",
  ]
  pattern = "cd"  # re.compile(r"cd")
  matches = search_pattern_in_all_books(pattern, books, 3)
  res = process_matches(matches)

  assert res == "abcd\ncdefg"
