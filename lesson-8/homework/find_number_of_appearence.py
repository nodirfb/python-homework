<<<<<<< HEAD

# task!!! -- you need find appearence of each word in text, you need create a dictionary like {"the":6,"Zen":1}

# reading file
path = r'D:\Python Files\python-homework\m1_homework-6_class_08_exception,file-handling\text.txt'

f = open(path,'r')
text = f.read().lower()

# cleaning text from punctuations
import string #importing all punctuation marks
punctuation_list = list(string.punctuation)

for i in punctuation_list:
    text = text.replace(i,'')
# print(text)
text = text.replace('\n', ' ')
list_of_words = text.split(' ')
# print(len(list_of_words))


# counting and storing in dictionary
d = {}
for i in list_of_words:
    if len(i) > 0:
        count = list_of_words.count(i)
        if i not in d:
            d[i] = count
print(d)
print(len(d))








['the', 'zen', 'of', 'python', 'by', 'tim', 'peters', '', 'beautiful', 'is', 'better', 'than', 'ugly', 'explicit', 'is', 'better', 'than', 'implicit', 'simple', 'is', 'better', 'than', 'complex', 'complex', 'is', 'better', 'than', 'complicated', 'flat', 'is', 'better', 'than', 'nested', 'sparse', 'is', 'better', 'than', 'dense', 'readability', 'counts', 'special', 'cases', 'arent', 'special', 'enough', 'to', 'break', 'the', 'rules', 'although', 'practicality', 'beats', 'purity', 'errors', 'should', 'never', 'pass', 'silently', 'unless', 'explicitly', 'silenced', 'in', 'the', 'face', 'of', 'ambiguity', 'refuse', 'the', 'temptation', 'to', 'guess', 'there', 'should', 'be', 'one', 'and', 'preferably', 'only', 'one', 'obvious', 'way', 'to', 'do', 'it', 'although', 'that', 'way', 'may', 'not', 'be', 'obvious', 'at', 'first', 'unless', 'youre', 'dutch', 'now', 'is', 'better', 'than', 'never', 'although', 'never', 'is', 'often', 'better', 'than', 'right', 'now', 'if', 'the', 'implementation', 'is', 'hard', 'to', 'explain', 'its', 'a', 'bad', 'idea', 'if', 'the', 'implementation', 'is', 'easy', 'to', 'explain', 'it', 'may', 'be', 'a', 'good', 'idea', 'namespaces', 'are', 'one', 'honking', 'great', 'idea', '', 'lets', 'do', 'more', 'of', 'those']

=======

# task!!! -- you need find appearence of each word in text, you need create a dictionary like {"the":6,"Zen":1}

# reading file
path = r'D:\Python Files\python-homework\m1_homework-6_class_08_exception,file-handling\text.txt'

f = open(path,'r')
text = f.read().lower()

# cleaning text from punctuations
import string #importing all punctuation marks
punctuation_list = list(string.punctuation)

for i in punctuation_list:
    text = text.replace(i,'')
# print(text)
text = text.replace('\n', ' ')
list_of_words = text.split(' ')
# print(len(list_of_words))


# counting and storing in dictionary
d = {}
for i in list_of_words:
    if len(i) > 0:
        count = list_of_words.count(i)
        if i not in d:
            d[i] = count
print(d)
print(len(d))








['the', 'zen', 'of', 'python', 'by', 'tim', 'peters', '', 'beautiful', 'is', 'better', 'than', 'ugly', 'explicit', 'is', 'better', 'than', 'implicit', 'simple', 'is', 'better', 'than', 'complex', 'complex', 'is', 'better', 'than', 'complicated', 'flat', 'is', 'better', 'than', 'nested', 'sparse', 'is', 'better', 'than', 'dense', 'readability', 'counts', 'special', 'cases', 'arent', 'special', 'enough', 'to', 'break', 'the', 'rules', 'although', 'practicality', 'beats', 'purity', 'errors', 'should', 'never', 'pass', 'silently', 'unless', 'explicitly', 'silenced', 'in', 'the', 'face', 'of', 'ambiguity', 'refuse', 'the', 'temptation', 'to', 'guess', 'there', 'should', 'be', 'one', 'and', 'preferably', 'only', 'one', 'obvious', 'way', 'to', 'do', 'it', 'although', 'that', 'way', 'may', 'not', 'be', 'obvious', 'at', 'first', 'unless', 'youre', 'dutch', 'now', 'is', 'better', 'than', 'never', 'although', 'never', 'is', 'often', 'better', 'than', 'right', 'now', 'if', 'the', 'implementation', 'is', 'hard', 'to', 'explain', 'its', 'a', 'bad', 'idea', 'if', 'the', 'implementation', 'is', 'easy', 'to', 'explain', 'it', 'may', 'be', 'a', 'good', 'idea', 'namespaces', 'are', 'one', 'honking', 'great', 'idea', '', 'lets', 'do', 'more', 'of', 'those']

>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
{'the': 6, 'zen': 1, 'of': 3, 'python': 1, 'by': 1, 'tim': 1, 'peters': 1, '': 2, 'beautiful': 1, 'is': 10, 'better': 8, 'than': 8, 'ugly': 1, 'explicit': 1, 'implicit': 1, 'simple': 1, 'complex': 2, 'complicated': 1, 'flat': 1, 'nested': 1, 'sparse': 1, 'dense': 1, 'readability': 1, 'counts': 1, 'special': 2, 'cases': 1, 'arent': 1, 'enough': 1, 'to': 5, 'break': 1, 'rules': 1, 'although': 3, 'practicality': 1, 'beats': 1, 'purity': 1, 'errors': 1, 'should': 2, 'never': 3, 'pass': 1, 'silently': 1, 'unless': 2, 'explicitly': 1, 'silenced': 1, 'in': 1, 'face': 1, 'ambiguity': 1, 'refuse': 1, 'temptation': 1, 'guess': 1, 'there': 1, 'be': 3, 'one': 3, 'and': 1, 'preferably': 1, 'only': 1, 'obvious': 2, 'way': 2, 'do': 2, 'it': 2, 'that': 1, 'may': 2, 'not': 1, 'at': 1, 'first': 1, 'youre': 1, 'dutch': 1, 'now': 2, 'often': 1, 'right': 1, 'if': 2, 'implementation': 2, 'hard': 1, 'explain': 2, 'its': 1, 'a': 2, 'bad': 1, 'idea': 3, 'easy': 1, 'good': 1, 'namespaces': 1, 'are': 1, 'honking': 1, 'great': 1, 'lets': 1, 'more': 1, 'those': 1}