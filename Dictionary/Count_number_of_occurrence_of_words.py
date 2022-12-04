def word_count(str):
    counts = dict()
    word_lower = str.lower()
    word_split = word_lower.split()

    for word in word_split:
        word_done = word.strip()
        if word_done in counts:
            counts[word_done] += 1
        else:
            counts[word_done] = 1
    return counts

print( word_count('the quick BROWN   Fox jumps over the lazY dog fox'))