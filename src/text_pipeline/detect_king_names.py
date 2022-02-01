from typing import List, Optional, Tuple

from nltk.corpus import names, words

# def get_word_variants(names_or_words: List[str]) -> List[Tuple[str]]:
#   all_word_variants = []
#   for word in names_or_words:
#     word_lower = word.lower()
#     word_plural = get_plural_of_word(word_lower)
#     word_variants = (word, word_lower, word_plural)
#     all_word_variants.append(word_variants)
#   return all_word_variants


# def get_plural_of_word(word: str) -> str:
#   word_plural = word + "s" if word[-1] != "y" else word[:-1] + "ies"
#   return word_plural

def get_word_variants(names_or_words: List[str]) -> List[Tuple[str]]:
  all_word_variants = []
  for word in names_or_words:
    word_lower = word.lower()
    word_singular = get_singular_of_word(word_lower)
    if word_singular:
      word_variants = (word, word_lower, word_singular)
    else:
      word_variants = (word, word_lower)
    all_word_variants.append(word_variants)
  return all_word_variants


def get_singular_of_word(word: str) -> Optional[str]:
  if word[-1] != "s":
    return None
  if word[-3:-1] == "ie":
    return word[:-3] + "y"
  return word[:-1]


def find_words_in_wordcorpus(names_or_words: List[Tuple[str]]) -> Tuple[List[str], List[str]]:
  words_in_corpus = []
  words_not_in_corpus = []
  for variants_of_a_name in names_or_words:
    name_appended = False
    for name_variante in variants_of_a_name:
      if name_variante in words.words():
        words_in_corpus.append(name_variante)
        name_appended = True
        break
    if not name_appended:
      words_not_in_corpus.append(variants_of_a_name[0])
  return words_in_corpus, words_not_in_corpus


def find_names_in_namecorpus(names_or_words: List[str]) -> Tuple[List[str], List[str]]:
  words_in_corpus = []
  words_not_in_corpus = []
  for name in names_or_words:
    if name in names.words():
      words_in_corpus.append(name)
    else:
      words_not_in_corpus.append(name)
  return words_in_corpus, words_not_in_corpus
