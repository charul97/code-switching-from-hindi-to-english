This project uses NLTK in Python to translate the Hindi-English mixed sentences(with hindi words in romanized form) into English.
It does so by:
1.) First seperating the words in the sentence. The english words are kept as it is.
2.) Hindi words in the sentence are matched with their pure hindi translations in the Database of words used.
3.) The english words are then translated to their respective hindi words.
4.) After converting the entire sentence into hindi,it is translated to english using Google Translate API.
