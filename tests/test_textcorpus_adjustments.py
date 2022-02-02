from text_pipeline.adjustments.textcorpus_adjustments import (
    normalize_king_names_general, normalize_our_king_names)


def test_normalize_king_names_general():
  text = "Charles II, Paul IVth and Henry III."
  res = normalize_king_names_general(text, {"Charles", "Henry"})

  assert res == "Charles the second, Paul IVth and Henry III."
