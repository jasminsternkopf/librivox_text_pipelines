import re
from typing import List

# {chars_before_and_after}


def search_pattern_in_all_books(pattern: str, books: List[str], chars_before_and_after: int = 5):
  pattern = re.escape(pattern)
  pattern_and_span = re.compile(
    rf".{{0,{chars_before_and_after}}}{pattern}.{{0,{chars_before_and_after}}}")
  pattern_at_beginning = re.compile(rf"^{pattern}.{{0,{chars_before_and_after}}}", re.MULTILINE)
  pattern_at_end = re.compile(rf".{{0,{chars_before_and_after}}}{pattern}$", re.MULTILINE)
  all_patterns = [pattern_and_span, pattern_at_beginning, pattern_at_end]
  results = []
  for book in books:
    for pattern_to_search_for in all_patterns:
      matches = pattern_to_search_for.findall(book)
      results.extend(matches)
  results = list(set(results))
  results.sort()
  results_linewise = "\n".join(results)
  return results_linewise
