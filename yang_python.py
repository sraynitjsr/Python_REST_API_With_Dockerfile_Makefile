def yangify_sentence(sentence):
    yangified_sentence = sentence.replace("hello", "Hello")
    yangified_sentence = yangified_sentence.replace("world", "World")
    return yangified_sentence

def start():
    print('Inside Yangify Module')
    original_sentence = input("Enter a sentence: ")
    yangified_sentence = yangify_sentence(original_sentence)
    print("Yangified sentence:", yangified_sentence, "of type", type(yangified_sentence))
