# Manual-natural-language-processing-of-text
Analyses sentiments of a full text stored locally, gives back a bar diagram of the different emotions highlighting the sentimentalities by taking emotinal words and processing them manually.

This function will:
1. Read text stored locally on your computer
2. Sets everything to lower case for readability
3. Cleans text to remove special characters
4. Tokenizes and splits the entire text into individual words in a list
5. Removes stop words (words that add no meaning to the text)
6. Stores words and compares them to different emotional weights from an emotion list
7. Counts the occurances of emotions appearing in text
8. Prints and saves the emotion occurances to a bar diagram for analysis

Store the text you want to analyse in the read.txt file, remember that if you intend to use a different emotion list you need to either store the emotions in the same format or change the formating for processing this list.

Only external package needed for this will be matplotlib. This can be installed using pip

Included are two analyses done on Barack Obama's final State of the Union speech (2016) as well as Trump's final State of the Union speech (2020) (at least for his first term)
