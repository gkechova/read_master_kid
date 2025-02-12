# from os import listdir, curdir
# from words.words_dictionary import words


# Step 1 - from filenames, get names and construct new dict words
# for file in listdir(curdir):
#     filename_only = file.replace('.png', '')
#     dictionary_word = f'    "{filename_only}": [[0, ""], [1, ""], [2, ""], [3, ""], [4, ""], [5, ""]],'
#     print(dictionary_word)

# Step 2 - Add results to word_dictionary
#
# Step 3 - After filling the dict, remove empty syllables and print the new dictionary sorted
# for word, syllables in words.items():
#     for i in range(len(syllables) - 1, -1, -1):
#         if syllables[i][1] == "":
#             syllables.remove(syllables[i])
#             words[word] = syllables
#         else:
#             break
#     words[word] = syllables
# for word, syllables in sorted(words.items()):
#     print(f'    "{word}": {syllables},')

# Step 4 - Copy and replace the dict values








