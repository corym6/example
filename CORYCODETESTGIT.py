import random

name = input("Hello, what is your name? ")

print("Hello " + name)

feeling = input("How are you today? ")

if "good" in feeling.lower() or "great" in feeling.lower() or "awesome" in feeling.lower() or "ok" in feeling.lower() or "okay" in feeling.lower():
    print("I'm feeling " + feeling + " too!")
elif "bad" in feeling.lower() or "not good" in feeling.lower() or "unhappy" in feeling.lower() or "tired" in feeling.lower() or "horrible" in feeling.lower():
    print("I'm sorry to hear that")
else:
    print("I am here to help!")

answer = input("I am a music assistant, would you like me find you something to listen to? ")

if "yes" in answer.lower() or "ok" in answer.lower() or "okay" in answer.lower() or "yeah" in answer.lower():
    print("Great, I will do my best")
    genres = ["rap", "hip-hop", "rock", "jazz", "pop", "country", "classical"]
    favgenre = input("What is you favorite genre: ")
    if favgenre.lower() in genres:
        print("Cool, my favorite is " + random.choice(genres))
    else:
        print("I'm sorry but I do not know that genre")
else:
    print("Unfortunately, I can't help then. My apologies.")