

import re


def replace_ie_with_that_is(text: str) -> str:
  text = text.replace("i.e.", "that is")
  text = text.replace("I.e.", "That is")
  return text


def replace_eg_with_for_example(text: str) -> str:
  text = text.replace("e.g.", "for example")
  text = text.replace("E.g.", "For example")
  return text


def replace_etc_with_et_cetera(text: str) -> str:
  text = text.replace("etc.", "et cetera")
  text = text.replace("Etc.", "Et cetera")
  return text


def geo_to_george_general(text: str) -> str:
  text = text.replace(" Geo. ", " George ")
  return text


# def remove_commas_in_numbers(text: str) -> str:
#   NUMBERS_WITH_COMMAS = re.compile(r"\d+(,\d{3})+")
# \d/\d+[^ ,\.\-\d/dt)_;'":lis%]

PERCENT = re.compile(r"(\d) ?%")


def normalize_percent(text: str) -> str:
  text = PERCENT.sub(r"\1 percent", text)
  return text


def remove_equal_sign(text: str) -> str:
  # is very rarely used as actual equal sign, much more often in headings or accentuation
  text = text.replace("=", "")
  return text
