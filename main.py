import string
from collections import Counter
import matplotlib.pyplot as plt

# Allows you to read the text in the other local file.
text = open('read.txt', encoding='utf-8').read()

# Converts text into lower case for sentimentality purposes
lower_case = text.lower()

# Convert lower case text into a cleaned version. The punctuation excludes special characters
# Str 1 ('') specifies list of characters that need to be replaced
# Str 2 ('') specifies list of characters with which the str 1 needs to be replaced with
# Str 3 (string.punctuation) specified the list of characters that needs to be deleted
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Breaks down a sentence and splits it into individual words into a list
tokenized_words = cleaned_text.split()

# Stop words are words that don't add anything to the analysis, this allows them to be excluded
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# The final list of words from the text that's being analyzed
final_words = []

# Excludes words that appear in the stop_words list, adding the rest to final_words list
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# The final list of emotions represented in final words will be stored here
emotion_list = []

# Saves all the text from emotions.txt as the variable file
with open('emotions.txt', 'r') as file:
    for line in file:
        # Replaces space between lines with nothing, removes quotation marks
        clear_line = line.replace("\n", '').replace(
            ',', '').replace("'", '').strip()

        # Splits words and emotions, everything before the colon is saved to word and after is saved to emotion
        word, emotion = clear_line.split(':')

        # If a word in the emotion list appears in the text analyzed, it adds it to the emotion list
        if word in final_words:
            emotion_list.append(emotion)

# Counts the occurances of each emotion in our emotions list
w = Counter(emotion_list)

print(w)

# Cleans up the graph, making the different bar annotations not overlap into eachother
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

# Saves everything to a picture
plt.savefig('FinalSotuTrump1Term.png')

# Displays the graph as a png
plt.show()
