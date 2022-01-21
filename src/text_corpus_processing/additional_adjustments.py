import re


def replace_ie_with_that_is(text: str) -> str:
  text = text.replace("i.e.", "that is")
  text = text.replace("I.e.", "That is")
  return text


def replace_eg_with_for_example(text: str) -> str:
  text = text.replace("e.g.", "for example")
  text = text.replace("E.g.", "For example")
  return text


def geo_to_george_general(text: str) -> str:
  text = text.replace(" Geo. ", " George ")
  return text


#POUNDS_AND_SHILLINGS_AND_PENCE = re.compile(r"L(\d+)\.? (\d+)s\. (\d+)d\.")
L_NUMBER_AND_SHILLINGS = re.compile(r"L(\d+[\d\.,]*)[\.,]? \d+s\.")
SHILLINGS_AND_PENCE = re.compile(r"(\d+)s\. (\d+)d\.")
SHILLINGS = re.compile(r"(\d+)s\.")


def normalize_pounds_shillings_and_pence(text: str) -> str:
  text = SHILLINGS_AND_PENCE.sub(r"\1 shillings \2 pence", text)
  text = SHILLINGS.sub(r"\1 shillings", text)
  return text
