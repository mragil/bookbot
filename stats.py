def get_num_words(text):
  num_words = len(text.split())
  return num_words

def get_character_count(text):
  word_arr = text.split()
  character_dict = {}
  for word in word_arr:
    for char in word:
      key = char.lower()
      if(key in character_dict):
        character_dict[key] = character_dict[key] + 1
      else:
        character_dict[key] = 1
  return character_dict