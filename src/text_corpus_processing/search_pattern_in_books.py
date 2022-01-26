import re
from pathlib import Path
from typing import Iterable, Iterator, List

# {chars_before_and_after}


def search_pattern_in_all_books2(pattern: str, books: Iterable[str], chars_before_and_after: int = 5):
  pattern = re.escape(pattern)
  pattern_and_span = re.compile(
    rf".{{1,{chars_before_and_after}}}{pattern}.{{1,{chars_before_and_after}}}")
  pattern_at_beginning = re.compile(rf"^{pattern}.{{0,{chars_before_and_after}}}", re.MULTILINE)
  pattern_at_end = re.compile(rf".{{0,{chars_before_and_after}}}{pattern}$", re.MULTILINE)
  all_patterns = [pattern_and_span, pattern_at_beginning, pattern_at_end]
  for book in books:
    for pattern_to_search_for in all_patterns:
      matches = pattern_to_search_for.findall(book)
      for match in matches:
        yield match
  #results = list(set(results))
  # results.sort()
  #results_linewise = "\n".join(results)
  # return results_linewise


def search_pattern_in_all_books(pattern: str, books: Iterable[str], chars_before_and_after: int = 5):
  #pattern = re.escape(pattern)
  pattern_and_span = re.compile(
    rf".{{0,{chars_before_and_after}}}{pattern}.{{0,{chars_before_and_after}}}")
  for book in books:
    matches = pattern_and_span.findall(book)
    for match in matches:
      yield match


def search_pattern_in_all_books_and_word_before_and_after(pattern: str, books: Iterable[str]):
  #pattern = re.escape(pattern)
  pattern_and_word_before_and_after = re.compile(
    rf"(?:\w+ |^){pattern}(?: \w+|$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      yield match


def search_pattern_in_all_books_and_word_before(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?:\w+ ){pattern}(?: |$)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      yield match


def search_pattern_in_all_books_and_word_after(pattern: str, books: Iterable[str]):
  pattern_and_word_before_and_after = re.compile(
    rf"(?: |^){pattern}(?: \w+)", re.MULTILINE)
  for book in books:
    matches = pattern_and_word_before_and_after.findall(book)
    for match in matches:
      yield match


def process_matches(matches: Iterator):
  matches = sorted(set(matches))
  matches_linewise = "\n".join(matches)
  return matches_linewise


def write_in_txt_file(text: str, path: Path):
  path.parent.mkdir(parents=True, exist_ok=True)
  path.write_text(text, encoding="UTF-8")
