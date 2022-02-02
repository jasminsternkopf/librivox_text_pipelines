import os
from collections import OrderedDict
from pathlib import Path
from typing import Generator, List
from typing import OrderedDict as OrderedDictType
from typing import Set

TXT_FILE_TYPE = ".txt"


def get_text_files(folder: Path) -> Generator[Path, None, None]:
  return get_files_dict(folder, filetypes={TXT_FILE_TYPE})


def get_files_dict(folder: Path, filetypes: Set[str]) -> Generator[Path, None, None]:
  filetypes_lower = {ft.lower() for ft in filetypes}
  all_files = get_all_files_in_all_subfolders(folder)
  resulting_files = (file
                     for file in all_files if file.suffix.lower() in filetypes_lower
                     )
  return resulting_files


def get_all_files_in_all_subfolders(dir: Path) -> Generator[Path, None, None]:
  for root, _, files in os.walk(dir):
    for name in files:
      file_path = Path(root) / name
      yield file_path
