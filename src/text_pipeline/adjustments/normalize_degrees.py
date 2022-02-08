import re

from text_pipeline.adjustments.unit_abbreviations_normalization import \
    POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION

CELSIUS = re.compile(rf"(\d) ?deg\.? ?C\.?({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")
#CENTIGRADE = re.compile(rf"(\d) ?deg\.? ?Cent({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")
FAHRENHEIT = re.compile(
  rf"(\d) ?deg\.? ?F(?:ahr)?\.?({POSSIBLE_FOLLOWING_CHARS_AFTER_ABBREVIATION})")


def normalize_temperatures_celsius(text: str) -> str:
  text = CELSIUS.sub(r"\1 degrees Celsius\2", text)
  return text


def normalize_temperatures_fahrenheit(text: str) -> str:
  text = FAHRENHEIT.sub(r"\1 degrees Fahrenheit\2", text)
  return text

# latitude and longitude
