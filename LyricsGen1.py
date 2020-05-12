import requests
import numpy as np
data = requests.get("https://raw.githubusercontent.com/coding-blocks-archives/ML-Noida-2019-June-Two/master/datasets/speeches/speech.txt")
data = data.text

def generateTable(data, k=4):
    T = {}

    for i in range(len(data) - k):
        X = data[i: i + k]
        y = data[i + k]

        if T.get(X) is None:
            T[X] = {}
            T[X][y] = 1
        else:
            if T[X].get(y) is None:
                T[X][y] = 1
            else:
                T[X][y] += 1
    return T
T=generateTable(data.lower())

def generate_new_text(seed, k=4, maxlen=10000):
    generated_text = seed
    seed = seed[-k:]

    for i in range(maxlen):
        seed = generated_text[-k:]
        possible_chars = list(T[seed].keys())
        possible_freq = list(T[seed].values())
        possible_probab = [ele / sum(possible_freq) for ele in possible_freq]
        pred_char = np.random.choice(possible_chars, p=possible_probab)
        generated_text = generated_text + pred_char
    return generated_text

output=generate_new_text("country")
print(output)