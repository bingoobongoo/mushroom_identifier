import os
for mushroom in os.listdir("data/"):
    print(f"{mushroom}: {len(os.listdir('data/' + mushroom))}")