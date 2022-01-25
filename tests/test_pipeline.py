from text_pipeline.pipeline import normalize_chronicles_of_newgate
from text_pipeline.txt_files_reading import get_text_files

# region normalize_chronicles_of_newgate


def test_normalize_chronicles_of_newgate__text_is_empty():
  text = ""
  res = normalize_chronicles_of_newgate(text)

  assert res == ""


def xtest_normalize_chronicles_of_newgate():
  file = get_text_files("data/chronicles_of_newgate")
  path = file[5]
  text = path.read_text()
  res = normalize_chronicles_of_newgate(text)

  assert res == "Thus, amongst others, Thomas Blackburn had been committed on October fifteenth for a debt of one shilling five pence, The prison was always in \"the most filthy state imaginable.\" They were mainly members of the criminal classes; particularly to those who desire now to offer up their praises and thanksgivings for thy late mercies vouchsafed unto them.' belonging to the Reverend Doctor Griffiths of Rochester, to the value of twenty thousand pounds."

# endregion
