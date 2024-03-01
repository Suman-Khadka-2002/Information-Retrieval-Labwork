import re

class PorterStemmer:
    def __init__(self):
        self.step2list = {
            'ational': 'ate',
            'tional': 'tion',
            'enci': 'ence',
            'anci': 'ance',
            'izer': 'ize',
            'bli': 'ble',
            'alli': 'al',
            'entli': 'ent',
            'eli': 'e',
            'ousli': 'ous',
            'ization': 'ize',
            'ation': 'ate',
            'ator': 'ate',
            'alism': 'al',
            'iveness': 'ive',
            'fulness': 'ful',
            'ousness': 'ous',
            'aliti': 'al',
            'iviti': 'ive',
            'biliti': 'ble',
        }

        self.step3list = {
            'icate': 'ic',
            'ative': '',
            'alize': 'al',
            'iciti': 'ic',
            'ical': 'ic',
        }

    def stem(self, word):
        word = word.lower()
        word = re.sub(r"'s?$", "", word)
        word = re.sub(r"(ss|ies)$", r"\1", word)
        word = re.sub(r"(.*?[^aeiou])ies$", r"\1y", word)

        for suffix in self.step2list.keys():
            if word.endswith(suffix):
                stem = word[:-len(suffix)] + self.step2list[suffix]
                if self.m(stem) > 0:
                    return stem

        for suffix in self.step3list.keys():
            if word.endswith(suffix):
                stem = word[:-len(suffix)] + self.step3list[suffix]
                if self.m(stem) > 0:
                    return stem

        return word

    def m(self, word):
        return len(re.findall(r"[aeiou]", word))

# Example usage
stemmer = PorterStemmer()
words = ['rationalization', 'nationalization', 'catalyst', 'realization', 'sensational', 'ability', 'productivity', 'optimization']
print("\nAfter applying Porter Alogirithm: \n")
for word in words:
    print(f"{word}: {stemmer.stem(word)}")
