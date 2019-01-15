import random

class GibberishGenerator:

    text = ""
    sentences = []
    all_words = []
    probabilities = []

    def __init__(self, file):
        self.text = ""
        self.readText(file)

    def readText(self, file):
        f = open(file, "r", encoding="utf-8")
        for line in f:
            self.text += line.replace("\n", " ")

    def count(self, sentences, word1, word2):
        countw1 = 0
        countw1w2 = 0
        for sentence in sentences:
            old = "<s>"
            words = sentence.split(" ")
            for word in words:
                if old == word1:
                    countw1 += 1
                    if word == word2:
                        countw1w2 += 1
                old = word
            if old == word1:
                countw1 += 1
                if "</s>" == word2:
                    countw1w2 += 1
        return countw1, countw1w2

    def getAllWords(self, sentences):
        words = ["<s>", "</s>"]
        for sentence in sentences:
            for word in sentence.split(" "):
                if word not in words:
                    words.append(word)
        return words

    def learn(self):
        print("Learning ...")
        self.sentences = self.text[:-1].replace(". ", ".").split(".")
        self.all_words = self.getAllWords(self.sentences)
        probabilities = []
        for i in self.all_words:
            for j in self.all_words:
                if i == j:
                    continue
                cw1, cw12 = self.count(self.sentences, i, j)
                if cw1 != 0 and cw12 != 0:
                    probabilities.append((j + "|" + i, cw12 / cw1))
        self.probabilities = probabilities
        print("Learning completed!")

    def makeSentence(self, max_length = 50):
        sentence = ""
        word = "<s>"
        for i in range(max_length):
            prob = [p for p in self.probabilities if p[0].split("|")[1] == word]
            max_prob = max([p[1] for p in prob])
            prob = [p for p in prob if p[1] == max_prob]
            sentence += " " + word
            word = random.choice(prob)[0].split("|")[0]
            if word == "</s>":
                break
        sentence += "."
        return sentence.replace(" <s> ", "")

    def generateGibberish(self, number_of_sentences=10, mex_sentence_length=50):
        gibberish = ""
        for i in range(number_of_sentences):
            gibberish += self.makeSentence() + " "
        return gibberish


GG = GibberishGenerator("text.txt")
GG.learn()
print(GG.generateGibberish())



