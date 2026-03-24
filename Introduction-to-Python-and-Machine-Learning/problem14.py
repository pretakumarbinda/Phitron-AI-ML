# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/ai-mood-detector

sentence = input()

if "happy" in sentence or "joy" in sentence or "smile" in sentence:
    print("Happy Mood")
elif "sad" in sentence or "cry" in sentence or "angry" in sentence:
    print("Sad Mood")
else:
    print("Neutral Mood")
