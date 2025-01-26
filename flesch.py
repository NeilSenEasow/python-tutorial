def count_syllables(word):
    vowels = "aeiouy"
    word = word.lower()
    count = sum(1 for i in range(1, len(word)) if word[i] in vowels and word[i-1] not in vowels)
    count = max(count, 1)
    if word.endswith("e"):
        count -= 1
    return max(count, 1)

def calculate_flesch_index(text):
    words = text.split()
    sentences = text.split(".")
    
    total_syllables = sum(count_syllables(word) for word in words)
    total_words = len(words)
    total_sentences = max(len(sentences), 1)

    avg_syllables_per_word = total_syllables / total_words
    avg_words_per_sentence = total_words / total_sentences

    flesch_index = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    grade_level = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59

    return round(flesch_index, 2), round(grade_level, 2)

with open("flesch.txt", "r") as file:
    text = file.read()

flesch_index, grade_level = calculate_flesch_index(text)

print(f"Flesch Index: {flesch_index}")
print(f"Grade Level: {grade_level}")
