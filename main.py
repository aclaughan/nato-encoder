import logging

from nato import NATO_ALPHABET

logging.basicConfig(level = logging.DEBUG)


def stretch_word(word):
    word_list = [char for char in word]
    return ' '.join(word_list)


def main():
    word = input("input a word to translate: \n   > ").upper()
    word_list = [char for char in word]
    print(f"\ninput:\n   {stretch_word(word)}\n\noutput:")

    for character in word_list:
        chr = NATO_ALPHABET[character]
        wrd = f"{chr['word']} ({chr['pronounced']}) "
        print(f"   {character} {wrd:<23} "
              f"{chr['morse']:<6}"
              f"{chr['file']}  "
              f"[{chr['tap code']}]"
              )


if __name__ == '__main__':
    main()

# logging.debug(stuff)
