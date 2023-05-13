"""Ignores case, punctuation, and white space. Treats hypenated words as a single word. Ignores stop words"""


from pprint import pprint

def strip_punct(text: str):
    """Strips punctuation from string. Useful for word frequency analysis. Requires import of string module"""
    from string import whitespace, punctuation
    text = text.replace("\n", " ")
    # Uncomment following line to count each part of a hyphenated word as a separate word. Otherwise, a hypenated word is considered a single word
    # text = text.replace("-", " ")
    processed_text = ""
    for char in text:
        if char.isalnum() or char in whitespace:
            processed_text += char   
    return processed_text

def word_counter(text: str):
    global word_count
    global set_count
    global word_list
    global word_set
    stripped_text = strip_punct(text)
    word_listi = stripped_text.split()
    word_list = [word.lower() for word in word_listi]
    word_set = set(word_list)
    word_count = len(word_list)
    set_count = len(word_set)
    scrubbed_list = []
    for word in word_set:
        if word not in stop_words:
            scrubbed_list.append(word)
    word_stats_raw = []
    for word in scrubbed_list:
        word_stats_raw.append((word, word_list.count(word)))
    word_stats = sorted(word_stats_raw, key=lambda x: x[1], reverse=True)
    return word_stats





    

text = """ """

results = word_counter(text)
for result in results:
    print(f"{result[1]:<5} {result[0]:<20} {(result[1] / word_count) * 100:.2f}% of text")

print(word_count)