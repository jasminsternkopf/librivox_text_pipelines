from text_pipeline.adjustments.normalize_degrees import (
    normalize_temperatures_celsius, normalize_temperatures_fahrenheit)

# region normalize_temperatures_celsius


def test_normalize_temperatures_celsius():
  text = "It was 30 deg.C. outside today."
  res = normalize_temperatures_celsius(text)

  assert res == "It was 30 degrees Celsius outside today."


def test_normalize_temperatures_celsius__2():
  text = "Today it was 30 deg C!"
  res = normalize_temperatures_celsius(text)

  assert res == "Today it was 30 degrees Celsius!"

# endregion

# region normalize_temperatures_fahrenheit


def test_normalize_temperatures_fahrenheit__f_not_fahr():
  text = "It was 30 deg.F. outside today."
  res = normalize_temperatures_fahrenheit(text)

  assert res == "It was 30 degrees Fahrenheit outside today."


def test_normalize_temperatures_fahrenheit__f_not_fahr__2():
  text = "Today it was 30 deg F!"
  res = normalize_temperatures_fahrenheit(text)

  assert res == "Today it was 30 degrees Fahrenheit!"


def test_normalize_temperatures_fahrenheit__fahr_not_f():
  text = "It was 30 deg.Fahr. outside today."
  res = normalize_temperatures_fahrenheit(text)

  assert res == "It was 30 degrees Fahrenheit outside today."


def test_normalize_temperatures_fahrenheit__fahr_not_f__2():
  text = "Today it was 30 deg Fahr!"
  res = normalize_temperatures_fahrenheit(text)

  assert res == "Today it was 30 degrees Fahrenheit!"

# endregion
