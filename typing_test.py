import time
import random
sentences=[
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Typing tests are fun and challenging.",
    "Practice makes a man perfect.",]
def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words = sentence.split()
    word_count = len(words)
    correct_words = sum(1 for w in user_input.split() if w in words)
    accuracy = (correct_words / len(words)) * 100
    wpm = (len(user_input.split()) / elapsed_time) * 60
    print(f"Time: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {wpm:.2f}")
typing_test()