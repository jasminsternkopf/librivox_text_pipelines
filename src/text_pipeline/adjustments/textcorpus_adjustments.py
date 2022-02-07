

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


# def remove_commas_in_numbers(text: str) -> str:
#   NUMBERS_WITH_COMMAS = re.compile(r"\d+(,\d{3})+")
# \d/\d+[^ ,\.\-\d/dt)_;'":lis%]
