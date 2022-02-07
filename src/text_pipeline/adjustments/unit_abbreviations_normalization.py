import re
from typing import Iterable, Literal, Optional, Tuple

# \d[^ \w):;\.,\-/\d\?\]}!#%"'\[\+@=~\|]
UNIT_MAPPINGS_TIME_SINGULAR = [
  ('sec', 'second'),
  ('s', 'second'),
  ('min', 'minute'),
]

UNIT_MAPPINGS_LENGTH_SINGULAR = [
  ('mm', 'millimeter'),
  ('cm', 'centimeter'),
  ('m', 'meter'),
  ('km', 'kilometer')
]

UNIT_MAPPINGS_LENGTH_SINGULAR_AMERICAN = [
  #("″", "inch")
  #("′", "foot")
  ("in", "inch"),
  ("ft", "foot"),
  ("yd", "yard"),
  ("mi", "mile")
]

UNIT_MAPPINGS_LENGTH_AMERICAN = [
  ("in", "inches"),
  ("ft", "feet"),
  ("yd", "yards"),
  ("mi", "miles")
]

UNIT_MAPPINGS_WEIGHT_SINGULAR = [
  ('mg', 'milligram'),
  ('g', 'gram'),
  ('kg', 'kilogram'),
]

UNIT_MAPPINGS_WEIGHT_SINGULAR_AMERICAN = [
  ("gr", "grain"),
  ("dr", "dram"),
  ("oz", "ounce"),
  ("lb", "pound"),
]

POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION = r"[ ,:;)'\"]"


def normalize_abbreviated_units(text: str, abbr_from_to: Iterable[Tuple[str, str]]) -> str:
  unit_abbr = get_unit_abbreviations_as_regex(abbr_from_to)
  for unit_abbr_iterable in unit_abbr:
    for unit in unit_abbr_iterable:
      text = unit[0].sub(unit[1], text)
  return text


def get_unit_abbreviations_as_regex(abbr_from_to: Iterable[Tuple[str, str]], dot: Literal[Literal["always"], Literal["never"], Literal["optional"]] = "optional", abbr_from_to_plural: Optional[Iterable[Tuple[str, str]]] = None) -> Tuple[Iterable[Tuple[str, str]]]:
  dot_regex = get_dot_regex(dot)
  if abbr_from_to_plural is None:
    abbr_from_to_plural = get_plural_abbreviations(abbr_from_to)
  unit_abbreviations_singular = [
      (re.compile(rf" 1 ?{abbr}{dot_regex}({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})"), f" one {long_form}\1") for abbr, long_form in abbr_from_to]
  unit_abbreviations_plural = [
      (re.compile(rf"(\d) ?{abbr}s?{dot_regex}({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})"), f"\1 {long_form}\2") for abbr, long_form in abbr_from_to_plural]
  return unit_abbreviations_singular, unit_abbreviations_plural


def get_plural_abbreviations(abbr_from_to: Iterable[Tuple[str, str]]) -> Iterable[Tuple[str, str]]:
  abbr_from_to_plural = [(abbr, long_form + "s") for abbr, long_form in abbr_from_to]
  return abbr_from_to_plural


def get_dot_regex(dot: Literal[Literal["always"], Literal["never"], Literal["optional"]]) -> str:
  if dot == "always":
    return "\."
  if dot == "never":
    return ""
  return "\.?"
