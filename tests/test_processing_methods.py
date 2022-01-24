from text_corpus_processing.processing_methods import extract_sentences


def test_extract_sentences__dot():
  text = "Hello World. It's a pleasure."
  res = extract_sentences(text)

  assert res == "Hello World.\nIt's a pleasure."


def test_extract_sentences__exclamation_mark():
  text = "Hello World! It's a pleasure."
  res = extract_sentences(text)

  assert res == "Hello World!\nIt's a pleasure."


def test_extract_sentences__question_mark():
  text = "Hello World? It's a pleasure."
  res = extract_sentences(text)

  assert res == "Hello World?\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_dot():
  text = "\"Hello World.\" she said. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World.\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_exclamation_mark():
  text = "\"Hello World!\" she said. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World!\" she said.\nIt's a pleasure."


def test_extract_sentences__quotation_marks_and_question_mark():
  text = "\"Hello World?\" she asked. It's a pleasure."
  res = extract_sentences(text)

  assert res == "\"Hello World?\" she asked.\nIt's a pleasure."
