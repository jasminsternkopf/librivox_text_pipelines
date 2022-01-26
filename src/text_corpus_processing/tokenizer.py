from nltk import sent_tokenize

#text = "On the day in which I visited the ship (the fourteenth), Wyatt and a party were also to visit it--so the captain informed me--and I waited on board an hour longer than I had designed, in hope of being presented to the bride; but then an apology came. \"Mr. W. was a little indisposed, and would decline coming on board until to-morrow, at the hour of sailing.\""

#text = "Pursuing the track of the naturalist, I have learned to distinguish the animal, the vegetable, and the mineral kingdoms, and to divide these into their distinct tribes and families;--but can I tell, after all this toil, whence a single blade of grass derives its vitality?--Could the most minute researches enable me to discover the exquisite pencil that paints the flower of the field? and have I ever detected the secret that gives their brilliant dye to the ruby and the emerald, or the art that enamels the delicate shell?--I observe the sagacity of animals--I call it instinct, and speculate upon its various degrees of approximation to the reason of man; but, after all, I know as little of the cogitations of the brute as he does of mine."

text = "The procession of her wooers files before our wondering eyes, and each the likeness of a kingly crown has on: Louis himself, her bright possibility of twenty years, till he takes her at her own estimate and prefers the Infanta,--Monsieur, his younger brother, Philip IV. of Spain, Charles II. of England, the Emperor of Germany, the Archduke Leopold of Austria,--prospective king of Holland,--the King of Portugal, the Prince of Denmark, the Elector of Bavaria, the Duke of Savoy, Conde's son, and Conde himself."

#text = text.replace("--", " ")

t_text = sent_tokenize(text)
print(len(t_text))
for sent in t_text:
  print(sent)
  print("---------------")
