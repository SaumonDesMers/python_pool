languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

txt = "{} was created by {}"
for key in languages:
    print(txt.format(key, languages[key]))
