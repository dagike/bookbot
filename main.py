def words_count(text):
  words_counted = len(text.split())
  return words_counted

def characters_list_count(text):
  text = text.lower()
  characters_dic = {}
  for char in text:
    if(char not in characters_dic):
      characters_dic[char] = 0
    characters_dic[char] += 1
  return characters_dic

def main():
  with open("books/frankenstein.txt") as frankenstein_book:
    file_contents = frankenstein_book.read()
    words_counted = words_count(file_contents)
    characters_dic = characters_list_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_counted} words found in the document\n")
    for char in characters_dic:
      if(char.isalpha()):
        print(f"The '{char}' character was found {characters_dic[char]} times")


main()