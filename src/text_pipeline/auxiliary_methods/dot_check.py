def dot_check_whole_text(text: str) -> str:
  sentences = text.split("\n")
  problematic_sentences = []
  for sentence in sentences:
    if not dot_check(sentence):
      problematic_sentences.append(sentence)
  return "\n".join(problematic_sentences)


def dot_check(sentence: str) -> str:
  no_of_dots = sentence.count(".")
  no_of_ex_marks = sentence.count("!")
  no_of_quest_marks = sentence.count("?")
  if no_of_dots + no_of_ex_marks + no_of_quest_marks != 1:
    return False
  return True
