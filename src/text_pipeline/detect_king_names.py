from typing import List, Tuple

from nltk.corpus import words


def get_name_variants(names: List[str]) -> List[Tuple[str]]:
  all_name_variants = []
  for name in names:
    if name[-1] == "\n":
      name = name[:-1]
    name_variants = (name, name.lower(), name.lower() + "s")
    all_name_variants.append(name_variants)
  return all_name_variants


def find_names_in_wordcorpus(names: List[Tuple[str]]) -> Tuple[List[str], List[str]]:
  words_in_corpus = []
  words_not_in_corpus = []
  for variants_of_a_name in names:
    name_appended = False
    for name_variante in variants_of_a_name:
      if name_variante in words.words():
        words_in_corpus.append(name_variante)
        name_appended = True
        break
    if not name_appended:
      words_not_in_corpus.append(variants_of_a_name[0])
  return words_in_corpus, words_not_in_corpus
