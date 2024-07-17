import random

# List of some common emojis
emojis = ["😀", "😂", "🥰", "😎", "🤔", "😜", "😢", "😡", "😱"]

# Number of emojis to print (up to 9)
num_emojis = random.randint(1, 9)

# Select random emojis and join them into a string
random_emojis = ''.join(random.choices(emojis, k=num_emojis))

print(random_emojis)
