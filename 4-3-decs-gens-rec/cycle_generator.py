def cycle(iterible):
    saved = []
    for element in iterible:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
