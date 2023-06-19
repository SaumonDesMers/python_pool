import sys


def text_analyzer(txt=None):
    """This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text."""
    if txt is None:
        txt = input("What is the text to analyse?\n")
    print("The text contains", len(txt), "characters:")
    print(len(list(filter(lambda c: 'A' <= c <= 'Z', txt))), "upper letters")
    print(len(list(filter(lambda c: 'a' <= c <= 'z', txt))), "lower letters")
    print(len(list(filter(lambda c: c in ".,?:;!-'\"", txt))), "punctuations")
    print(len(list(filter(lambda c: c == ' ', txt))), "spaces")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('ERROR')
        exit()

    text_analyzer(sys.argv[1])
