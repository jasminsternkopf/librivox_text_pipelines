from text_pipeline.adjustments.LJ_and_DW_adjustments import (
    add_dot_after_headings, expand_and_a_half, geo_to_george,
    insert_space_before_and_after_double_hyphen,
    normalize_coordinates_in_in_the_footprints_of_the_padres,
    normalize_degrees_and_latitudes, normalize_double_quotation_marks,
    normalize_king_names, normalize_king_names_without_dot,
    normalize_point_before_numbers, normalize_pound,
    normalize_roman_numerals_in_chronicles_of_newgate,
    normalize_shillings_and_pence_in_chronicles_of_newgate,
    normalize_shillings_and_pence_in_haunted_london,
    normalize_single_quotation_marks_and_apostrophes,
    normalize_three_and_four_dots, normalize_year_span,
    remove_dot_after_single_capital_letters, remove_illustrations,
    remove_indented_lines, remove_linebreaks,
    remove_numbers_in_square_brackets,
    remove_quotation_marks_as_itemization_in_other_cases,
    remove_quotation_marks_when_used_as_itemization, remove_repeated_spaces,
    remove_stars_and_spaces, remove_underscore_characters,
    replace_hyphen_between_numbers_with_to, replace_no_with_number,
    write_out_month_abbreviations)


def test_remove_linebreaks():
  text = "Hello\nWorld"
  res = remove_linebreaks(text)

  assert res == "Hello World"

# region remove_numbers_in_square_brackets


def test_remove_numbers_in_square_brackets():
  text = "Hello World[123]"
  res = remove_numbers_in_square_brackets(text)

  assert res == "Hello World"


def test_remove_numbers_in_square_brackets__two_occurences():
  text = "Hello[1] World[2]"
  res = remove_numbers_in_square_brackets(text)

  assert res == "Hello World"


def test_remove_numbers_in_square_brackets__only_empty_square_brackets():
  text = "Hello[] World"
  res = remove_numbers_in_square_brackets(text)

  assert res == text

# endregion

# region remove_illustrations


def test_remove_illustrations():
  #text = "Hello World [Illustration: THE SAVOY FROM THE THAMES, 1650.]"
  text = "I was conducted by a  [Illustration: _Entrance to Mrs. Fry's Ward._]  decently-dressed person, the newly-appointed yards-woman, to the door of a ward where at the head of a long table sat a lady belonging to the Society of Friends."
  res = remove_illustrations(text)

  assert res == "I was conducted by a    decently-dressed person, the newly-appointed yards-woman, to the door of a ward where at the head of a long table sat a lady belonging to the Society of Friends."


def test_remove_illustrations__no_further_information_in_brackets():
  text = "They arrested all known offenders whom they met with,  [Illustration]  and were fully armed for their own and the public protection."
  res = remove_illustrations(text)

  assert res == "They arrested all known offenders whom they met with,    and were fully armed for their own and the public protection."

# endregion


def test_remove_repeated_spaces():
  text = " Hello   World  "
  res = remove_repeated_spaces(text)

  assert res == " Hello World "


def test_normalize_shillings_and_pence():
  text = "Thomas Blackburn had been committed on October 15th for a debt of 1_s._ 5_d._, for which the costs were 6_s._ 10_d._"
  res = normalize_shillings_and_pence_in_chronicles_of_newgate(text)

  assert res == "Thomas Blackburn had been committed on October 15th for a debt of one shilling 5 pence, for which the costs were 6 shillings 10 pence"


def test_remove_underscore_characters():
  text = "_Hello_ World"
  res = remove_underscore_characters(text)

  assert res == "Hello World"


def test_replace_no_with_number():
  text = "No. 1, Newgate Street"
  res = replace_no_with_number(text)

  assert res == "number 1, Newgate Street"


def test_replace_no_with_number__no_starting_with_small_letter():
  text = "I said no. "
  res = replace_no_with_number(text)

  assert res == text


def test_normalize_king_names():
  text = "Henry I. was the brother of Charles IV., who was William XIII.'s cousin and Abc IX.'s uncle."
  res = normalize_king_names(text)

  assert res == "Henry the first was the brother of Charles the fourth, who was William the thirteenth's cousin and Abc IX.'s uncle."


def test_normalize_roman_numberals__in_chronicles_of_newgate():
  text = " i. The male debtors' side.   ii. The female debtors' side.   iii. The chapel yard.   iv. The middle yard.   v. The master felons' side.   vi. The female felons' side.   vii. The state side.   viii. The press yard."
  res = normalize_roman_numerals_in_chronicles_of_newgate(text)

  assert res == " one. The male debtors' side.   two. The female debtors' side.   three. The chapel yard.   four. The middle yard.   five. The master felons' side.   six. The female felons' side.   seven. The state side.   eight. The press yard."


def test_remove_stars():
  text = "’Tis a brave cause of joy. * * Give me a deep-crowned bowl"
  res = remove_stars_and_spaces(text)

  assert res == "’Tis a brave cause of joy. Give me a deep-crowned bowl"


def test_normalize_shillings_and_pence_in_haunted_london():
  text = "2s. 10d."
  res = normalize_shillings_and_pence_in_haunted_london(text)

  assert res == "2 shillings 10 pence"


def test_normalize_shillings_and_pence_in_haunted_london__only_shillings():
  text = "15s. per day"
  res = normalize_shillings_and_pence_in_haunted_london(text)

  assert res == "15 shillings per day"


def test_geo_to_george():
  text = "9th Geo. IV."
  res = geo_to_george(text)

  assert res == "9th George IV."


def test_geo_to_george_with_c_and_s():
  text = "9th Geo. III. c. 64, s. 5"
  res = geo_to_george(text)

  assert res == "9th George III. c 64, s 5"


def test_geo_to_george_with_c_no_s():
  text = "9th Geo. I. c. 64"
  res = geo_to_george(text)

  assert res == "9th George I. c 64"


def test_geo_to_george_with_cap_and_s():
  text = "9th Geo. IV. cap. 64, s. 45"
  res = geo_to_george(text)

  assert res == "9th George IV. cap 64, s 45"


def test_geo_to_george_with_cap_no_s():
  text = "9th Geo. IV. cap. 64"
  res = geo_to_george(text)

  assert res == "9th George IV. cap 64"


def test_remove_indented_lines():
  text = "  [11] Hartig finds the specific gravity of the wood in a tree is\n  increased from 0-60 to 0.74 when the surrounding wood has been\n  cut down.--_Bot. Central_, vol. xxx, p. 220.\n"
  res = remove_indented_lines(text)

  assert res == ""


def test_normalize_point_before_numbers():
  text = "and carbo-hydrates 66·5 per cent"
  res = normalize_point_before_numbers(text)

  assert res == "and carbo-hydrates 66 point 5 per cent"


def test_normalize_pound():
  text = "2000 lb., 1lb. and 1/500 lb. per lb."
  res = normalize_pound(text)

  assert res == "2000 pounds, one pound and one five hundredth pound per pound."


def test_normalize_degrees_and_latitudes():
  text = "69.50° N. lat."
  res = normalize_degrees_and_latitudes(text)

  assert res == "69.50 degrees north latitude"


def test_expand_and_a_half():
  text = "11-1/2 per cent"
  res = expand_and_a_half(text)

  assert res == "11 and a half per cent"


def test_replace_hyphen_between_numbers_with_to():
  text = "38-41"
  res = replace_hyphen_between_numbers_with_to(text)

  assert res == "38 to 41"


def test_normalize_year_span__do_not_normalize():
  text = "1792-95"
  res = normalize_year_span(text)

  assert res == text


def test_normalize_year_span__do_not_normalize():
  text = "1753-4."
  res = normalize_year_span(text)

  assert res == "1753 to 54."


def test_insert_space_before_and_after_double_hyphen():
  text = "It was not likely that a system which left innocent men--for the great bulk of new arrivals were still untried--to be pitchforked by chance anywhere"
  res = insert_space_before_and_after_double_hyphen(text)

  assert res == "It was not likely that a system which left innocent men -- for the great bulk of new arrivals were still untried -- to be pitchforked by chance anywhere"


def test_insert_space_before_and_after_double_hyphen__do_not_replace_as_capital_letter_for_double_hyphen():
  text = "D--n seize you all."
  res = insert_space_before_and_after_double_hyphen(text)

  assert res == text


def test_remove_quotation_marks_when_used_as_itemization():
  text = "\"The arrival of the English in California being soon known through the\ncountry, two persons in the character of ambassadors came to the Admiral\nand informed him, in the best manner they were able, that the king would\nvisit him, if he might be assured of coming in safety. Being satisfied\non this point, a numerous company soon appeared, in front of which was a\nvery comely person bearing a kind of sceptre, on which hung two crowns,\nand three chains of great length. The chains were of bones, and the\ncrowns of network, curiously wrought with feathers of many colors.\n\n\"Next to sceptre-bearer came the king, a handsome, majestic person,\nsurrounded by a number of tall men dressed in skins, who were followed\nby the common people, who, to make the grander appearance, had painted\ntheir faces of various colors; and all of them, even the children, being\nloaded with presents.\n\n"
  res = remove_quotation_marks_when_used_as_itemization(text)

  assert res == "The arrival of the English in California being soon known through the\ncountry, two persons in the character of ambassadors came to the Admiral\nand informed him, in the best manner they were able, that the king would\nvisit him, if he might be assured of coming in safety. Being satisfied\non this point, a numerous company soon appeared, in front of which was a\nvery comely person bearing a kind of sceptre, on which hung two crowns,\nand three chains of great length. The chains were of bones, and the\ncrowns of network, curiously wrought with feathers of many colors.\n\nNext to sceptre-bearer came the king, a handsome, majestic person,\nsurrounded by a number of tall men dressed in skins, who were followed\nby the common people, who, to make the grander appearance, had painted\ntheir faces of various colors; and all of them, even the children, being\nloaded with presents.\n\n"


def test_remove_quotation_marks_when_used_as_itemization_do_not_match_because_is_quotation():
  text = "\n\n\"Hello world!\" is what the computer said.\n\nI replied \"alright\".\n\n"
  res = remove_quotation_marks_when_used_as_itemization(text)

  assert res == text


def test_remove_quotation_marks_in_other_cases():
  text = "\"On Board the Schooner 'Sierra.'--\n  \"Off the City Front.\n    \"May 4, 1881.\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == "On Board the Schooner 'Sierra.'--\n  Off the City Front.\n    May 4, 1881.\n\n"


def test_remove_quotation_marks_in_other_cases_2():
  text = "\"CLIPPER SHIP, FLYING CLOUD,\n  \"January 4, 1857.\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == "CLIPPER SHIP, FLYING CLOUD,\n  January 4, 1857.\n\n"


def test_remove_remove_quotation_marks_in_other_cases_do_not_match_because_is_quotation():
  text = "\n\n\"Hello world!\" is what the computer said.\n\nI replied \"alright\".\n\n"
  res = remove_quotation_marks_as_itemization_in_other_cases(text)

  assert res == text


def test_remove_dot_after_single_capital_letters():
  text = "Mrs. L.A.C. Clapp."
  res = remove_dot_after_single_capital_letters(text)

  assert res == "Mrs. L A C Clapp."


def test_remove_dot_after_single_capital_letters__do_not_remove():
  text = "JAN. WASHINGTON'S BIRTHDAY. MARCUS AURELIUS."
  res = remove_dot_after_single_capital_letters(text)

  assert res == text


def test_remove_dot_after_single_capital_letters__do_not_remove():
  text = "\"N.B.--Front seats reserved for ladies!\""
  res = remove_dot_after_single_capital_letters(text)

  assert res == "\"N B--Front seats reserved for ladies!\""


def test_write_out_month_abbreviations():
  text = "JAN. Feb. mar."
  res = write_out_month_abbreviations(text)

  assert res == "January February March"


def test_write_out_month_abbreviations__nothing_changes():
  text = "October NOVEMBER december"
  res = write_out_month_abbreviations(text)

  assert res == text


def test_write_out_month_abbreviations__jan_several_times():
  text = "JAN. JAN. JAN."
  res = write_out_month_abbreviations(text)

  assert res == "January January January"


def test_normalize_king_names_without_dot():
  text = "Charles III and James I, Henry V and Edward VI."
  res = normalize_king_names_without_dot(text)

  assert res == "Charles the third and James the first, Henry the fifth and Edward the sixth."


def test_normalize_three_and_four_dots__between_two_sentences__no_quotation_marks():
  text = "Hello. ... World."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello. World."


def test_normalize_three_and_four_dots__between_two_sentences__quotation_mark_on_left_side():
  text = "\"Hello.\"... World."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "\"Hello.\" World."


def test_normalize_three_and_four_dots__between_two_sentences__quotation_mark_on_right_side():
  text = "Hello. ... \"World.\""
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello. \"World.\""


def test_normalize_three_and_four_dots__between_two_sentences__quotation_marks_on_both_sides():
  text = "\"Hello.\"... \"World.\""
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "\"Hello.\" \"World.\""


def test_normalize_three_and_four_dots__mid_sentence():
  text = "Hello ... world."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."


def test_normalize_three_and_four_dots__end_of_sentence__three_dots():
  text = "Hello world..."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."


def test_normalize_three_and_four_dots__end_of_sentence__four_dots():
  text = "Hello world...."
  res = normalize_three_and_four_dots(text)

  assert remove_repeated_spaces(res) == "Hello world."


def test_normalize_double_quotation_marks():
  text = "“The Royal Diversion.”"
  res = normalize_double_quotation_marks(text)

  assert res == "\"The Royal Diversion.\""


def test_normalize_single_quotation_marks_and_apostrophes():
  text = "‘poor little chuck!’"
  res = normalize_single_quotation_marks_and_apostrophes(text)

  assert res == "\"poor little chuck!\""


def test_normalize_single_quotation_marks_and_apostrophes__apostrophes_not_quotation_marks():
  text = "William III.’s reign"
  res = normalize_single_quotation_marks_and_apostrophes(text)

  assert res == "William III.'s reign"


def test_normalize_coordinates_in_in_the_footprints_of_the_padres():
  text = "latitude 37° 59' 5\"; longitude 122° 57-1/2'."
  res = normalize_coordinates_in_in_the_footprints_of_the_padres(text)

  assert res == "latitude 37 degrees 59 minutes 5 seconds; longitude 122 degrees 57-1/2 minutes."


def test_add_dot_after_headings():
  text = "\nCROSSING THE ISTHMUS\n"
  res = add_dot_after_headings(text)

  assert res == "\nCROSSING THE ISTHMUS.\n"


def test_add_dot_after_headings__dot_already_there_not_added():
  text = "\nCROSSING THE ISTHMUS.\n"
  res = add_dot_after_headings(text)

  assert res == text
