import sys
from stats import get_num_words, get_character_count

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def convert_to_list(items):
  converted_list = []
  for key in items:
    converted_list.append({"char": key, "num": items[key] })
  return converted_list

def sort_on(items):
    return items["num"]

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file_path = sys.argv[1]
  file = get_book_text(file_path)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {get_num_words(file)} total words")
  print("--------- Character Count -------")
  character_list = convert_to_list(get_character_count(file))
  character_list.sort(reverse=True, key=sort_on)
  for data in character_list:
    print(f"{data["char"]}: {data["num"]}")
  print("============= END ===============")
main()