import parse

morpheme_data = parse.get_morpheme_from_neko()

print(parse.get_counter_from_words(parse.flatten(morpheme_data)))
