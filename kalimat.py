import demoji  # for removing emoji


class Kalimat:
    def __init__(self, sentence):
        self.sentence = sentence

    def getSentence(self):
        text = self.removeWords()
        return text

    def removeWords(self):
        self.sentence = demoji.replace(self.sentence)
        finalText = ''
        excludedChars = [',', '.', '!', '?', '&', '-', '"']
        excludedWords = ['2beer!', 'mksfess',
                         '[askmf]', '[cm]', '[gmf]', '[tanyarl]', '/wal', '/rlt/']
        words = [i for j in self.sentence.split() for i in (j, ' ')][:-1]
        for word in words:
            # bt = 0
            # if word == u"\u2800":
            #     bt += 1
            #     print(bt)
            word = word.lower()
            if word[0] == '@' or word[0] == '#' or word[0:4] == 'http':
                word = word.replace(word, '')

            for ew in excludedWords:  # remove unnecassary words
                word = word.replace(ew, '')
            for char in word:
                if char == u"\u2800":  # remove BRAILLE PATTERN BLANK char
                    char = char.replace(char, '')
                for ec in excludedChars:  # remove unnecessary char
                    char = char.replace(ec, '')
                finalText += char
        self.sentence = finalText
        return self.sentence

    def transform(self):
        finalText = ''
        text = self.removeWords()
        for i, char in enumerate(text):
            if i % 2 != 0:
                char = char.replace(char, char.upper())
                finalText += char
            else:
                finalText += char
        self.sentence = finalText
        return self.sentence

    def trinsfirm(self):
        finalText = ''
        text = self.removeWords()
        consonant = ['a', 'u', 'e', 'o']
        for char in text:
            if char in consonant:
                char = char.replace(char, 'i')
                finalText += char
            else:
                finalText += char
        self.sentence = finalText
        return self.sentence

    def transformoji(self, emoji_type):
        finalText = ''
        text = self.removeWords()
        if emoji_type == "laugh":
            for char in text:
                if char == ' ':
                    char = char.replace(char, "😂")
                    finalText += char
                else:
                    finalText += char
            self.sentence = finalText
            return self.sentence

        elif emoji_type == "clap":
            for char in text:
                if char == ' ':
                    char = char.replace(char, "👏")
                    finalText += char
                else:
                    finalText += char
            self.sentence = finalText
            return self.sentence

# CHANGE HOW transformoji WORK

# Testing purpose
# k = Kalimat("coba coba coba coba test test test")
# k.removeWords()
# kalimat = k.getSentence()
# print(k.sentence)
# k.transformoji("clap")
# print(k.sentence)
