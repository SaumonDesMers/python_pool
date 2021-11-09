def text_analyser(txt = None):
    if txt == None:
        txt = input("What is the text to analyse?\n")
    print("The text contains", len(txt), "characters:")
    print(len(list(filter(lambda c: 'A' <= c <= 'Z', txt))), "upper letters")
    print(len(list(filter(lambda c: 'a' <= c <= 'z', txt))), "lower letters")
    print(len(list(filter(lambda c: c in ".,?:;!-'\"", txt))), "punctuations")
    print(len(list(filter(lambda c: c == ' ', txt))), "spaces")
