import pickle
from pathlib import Path
from typing import Callable, List

from text_pipeline.txt_files_reading import get_text_files


def create_pickle_containing_all_books(folder: Path):  # , normalizer: Callable[[str], str]):
  paths = get_text_files(folder)
  books: List[str] = []
  for path in paths:
    book = path.read_text()
    books.append(book)
    #normalized_text = normalizer(book)
  with open('data/all_books.pickle', 'wb') as file:
    pickle.dump(books, file)


create_pickle_containing_all_books(Path("data/librispeech-lm-corpus/corpus"))
