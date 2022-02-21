from LJ_and_DW_adjustments import (
    L_into_Lew, footnote_normalization_in_south_sea_idyls,
    four_hyphens_followed_by_dot_into_blank,
    normalize_confessor_and_pere_fidelis, normalize_hell_and_damned,
    normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres,
    normalize_item_list, normalize_minute_colon_seconds,
    normalize_no_and_roman_numeral, normalize_roman_numerals_for_two_and_three,
    normalize_roman_numerals_in_chronicles_of_newgate, remove_dot_of_viz,
    remove_dots_of_ie, remove_indented_lines,
    remove_quotation_marks_as_itemization_in_other_cases,
    square_brackets_to_round_brackets)


def test_remove_quotation_marks_as_itemization_in_other_cases():
  # itfotp
  text = "\"On Board the Schooner 'Sierra.'--\n  \"Off the City Front.\n    \"May 4, 1881.\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == "On Board the Schooner 'Sierra.'--\n  Off the City Front.\n    May 4, 1881.\n\n"


def test_remove_dots_of_ie__in_in_the_footprints_of_the_padres():
  # itfotp, con
  text = "Life is a series of surprises; surprise No. 1, a brace of long, tapering javelins having villainous-looking heads, i.e., two marine rockets, with which to rend the heavens,..."
  res = remove_dots_of_ie(text)

  assert res == "Life is a series of surprises; surprise No. 1, a brace of long, tapering javelins having villainous-looking heads, i e, two marine rockets, with which to rend the heavens,..."


def test_remove_dots_of_ie__in_chronicles_of_newgate():
  # itfotp, con
  text = "As to the exclusion of strangers on these occasions, the experience I have had convinces me that one, and perhaps the only, good of an execution, _i. e._ the solemn admonition to the public, will thereby be lost."
  res = remove_dots_of_ie(text)

  assert res == "As to the exclusion of strangers on these occasions, the experience I have had convinces me that one, and perhaps the only, good of an execution, _i e_ the solemn admonition to the public, will thereby be lost."


def test_L_into_Lew():
  # ssi
  text = "especially as L---- was busy and could not talk much, and L----'s books were as old as the hills and a good deal drier."
  res = L_into_Lew(text)

  assert res == "especially as Lew was busy and could not talk much, and Lew's books were as old as the hills and a good deal drier."


def test_footnote_normalization_in_south_sea_idyls():
  # ssi
  text = "\"Haleakala!\"[A] cried he, triumphantly, for he saw he had resurrected my interest in life, and he felt that he had a thing or two worth showing, a glimpse of which might content me with this world, dull as I found it just then. \"Haleakala--the House of the Sun--up before us,\" said Kahéle.          [A] Haleakala, an extinct crater in the Sandwich Islands,             supposed to be the largest in the world."
  res = footnote_normalization_in_south_sea_idyls(text)

  assert res == "\"Haleakala!\" cried he, triumphantly, for he saw he had resurrected my interest in life, and he felt that he had a thing or two worth showing, a glimpse of which might content me with this world, dull as I found it just then. \"Haleakala--the House of the Sun--up before us,\" said Kahéle.          Footnote Haleakala, an extinct crater in the Sandwich Islands,             supposed to be the largest in the world."


def test_four_hyphens_followed_by_dot_into_blank():
  # ssi
  text = "ADMISSION, ----. CHILDREN, HALF PRICE."
  res = four_hyphens_followed_by_dot_into_blank(text)

  assert res == "ADMISSION, blank. CHILDREN, HALF PRICE."


def test_normalize_confessor_and_pere_fidelis():
  # ssi
  text = "_Conf._ \"Who is I?\"  _Père F._ \"Fidelis!\""
  res = normalize_confessor_and_pere_fidelis(text)

  assert res == "Confessor. \"Who is I?\"  Père Fidelis. \"Fidelis!\""


def test_normalize_hell_and_damned__hell():
  # roawm
  text = "Mr. Bliss thought fit to accompany his refusals by telling me to go to h--l,..."
  res = normalize_hell_and_damned(text)

  assert res == "Mr. Bliss thought fit to accompany his refusals by telling me to go to hell,..."


def test_normalize_hell_and_damned__damned():
  text = "What does this d----d fellow mean by calling me 'only a schoolmaster'?"
  res = normalize_hell_and_damned(text)

  assert res == "What does this damned fellow mean by calling me 'only a schoolmaster'?"


def test_normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres():
  # itfotp
  # normalerweise ersetzen wir Bindestrich zwischen Zahlen mit "to", aber David Wales hat an der Stelle "and" gesagt
  text = "...who spent the greater portion of two years--1834-35--on the coast of California..."
  res = normalize_inconsistent_year_span_in_in_the_footprints_of_the_padres(text)

  assert res == "...who spent the greater portion of two years--1834 and 35--on the coast of California..."


def test_normalize_item_list():
  # ssi
  """
         OBJECTS OF INTEREST RELATING TO CAPTAIN COOK.

      Item   I. The tree where Cook was struck.
        "   II. The rock where Cook fell.
        "  III. The altar on the hill-top.
        "   IV. The riven palms.
        "    V. The sole survivor,--the boy that ran.
        "   VI. A specimen sepulchre in the cliff.
  """
  text = "       OBJECTS OF INTEREST RELATING TO CAPTAIN COOK.        Item   I. The tree where Cook was struck.         \"   II. The rock where Cook fell.         \"  III. The altar on the hill-top.         \"   IV. The riven palms.         \"    V. The sole survivor,--the boy that ran.         \"   VI. A specimen sepulchre in the cliff."
  res = normalize_item_list(text)

  assert res == "       OBJECTS OF INTEREST RELATING TO CAPTAIN COOK.        Item   I. The tree where Cook was struck.         Item 2 The rock where Cook fell.         Item 3 The altar on the hill-top.         Item 4 The riven palms.         Item 5 The sole survivor,--the boy that ran.         Item 6 A specimen sepulchre in the cliff."


def test_normalize_minute_colon_seconds():
  # lop
  text = "The 1:40 gait translated into English means that Sally Gardner was going at the rate of a mile in one minute forty seconds, which certainly is a great pace even for a Derby winner."
  res = normalize_minute_colon_seconds(text)

  assert res == "The 1 and 40 gait translated into English means that Sally Gardner was going at the rate of a mile in one minute forty seconds, which certainly is a great pace even for a Derby winner."


def test_normalize_no_and_roman_numeral():
  # ssi
  text = "We come first upon No. II. in the list of historic haunts."
  res = normalize_no_and_roman_numeral(text)

  assert res == "We come first upon number 2 in the list of historic haunts."


def test_normalize_roman_numerals_for_two_and_three():
  # itfotp, ssi
  text = "...I may add, not unprofitable.   II.  Some months of mellow and beautiful weather..."
  res = normalize_roman_numerals_for_two_and_three(text)

  assert res == "...I may add, not unprofitable.   Two.  Some months of mellow and beautiful weather..."


def test_normalize_roman_numerals_in_chronicles_of_newgate():
  # con
  """
  These were--

  i. The male debtors' side.
  ii. The female debtors' side.
  iii. The chapel yard.
  iv. The middle yard.
  v. The master felons' side.
  vi. The female felons' side.
  vii. The state side.
  viii. The press yard.
  """
  text = "These were--    i. The male debtors' side.   ii. The female debtors' side.   iii. The chapel yard.   iv. The middle yard.   v. The master felons' side.   vi. The female felons' side.   vii. The state side.   viii. The press yard."
  res = normalize_roman_numerals_in_chronicles_of_newgate(text)

  assert res == "These were--    One. The male debtors' side.   Two. The female debtors' side.   Three. The chapel yard.   Four. The middle yard.   Five. The master felons' side.   Six. The female felons' side.   Seven. The state side.   Eight. The press yard."


def test_remove_dot_of_viz():
  # con, ropl
  text = "We will suppose what is quite as likely as any other theory, viz. that man as a gardening creature first settled somewhere in the Euphrates or Caucasian valleys."
  res = remove_dot_of_viz(text)

  assert res == "We will suppose what is quite as likely as any other theory, viz that man as a gardening creature first settled somewhere in the Euphrates or Caucasian valleys."


def test_remove_indented_lines():
  # ropl
  """
  Very little
light is lost by escaping between the leaves, and very few of the
leaves are overshaded by their neighbours on the same branch.

  [1] Kerner, _Natural History of Plants_; also Scott Elliot,
  _Nature Studies--Plant Life_.

Thus all co-operate in sunlight-catching.
  """
  text = "Very little\nlight is lost by escaping between the leaves, and very few of the\nleaves are overshaded by their neighbours on the same branch.\n\n  [1] Kerner, _Natural History of Plants_; also Scott Elliot,\n  _Nature Studies--Plant Life_.\n\nThus all co-operate in sunlight-catching."
  res = remove_indented_lines(text)

  assert res == "Very little\nlight is lost by escaping between the leaves, and very few of the\nleaves are overshaded by their neighbours on the same branch.\n\n\nThus all co-operate in sunlight-catching."


def test_square_brackets_to_round_brackets():
  # itfotp
  text = "These people bringing the Admiral [Captain Drake] a present of feathers..."
  res = square_brackets_to_round_brackets(text)

  assert res == "These people bringing the Admiral (Captain Drake) a present of feathers..."


"""
Weitere Anmerkungen:
normalize_pound normalisiert lb. in romance of plant life dort, wo normale weight unit normalization nicht greifen würde bzw. wo noch Extra-Normalisierungen realisiert werden können

Dann gibt es noch extra Funktionen die Kleinigkeiten in den einzelnen Büchern normalisieren und entsprechend benannt sind, ergibt sich eigentlich durch Anschauen der Funktion was sie macht
"""
