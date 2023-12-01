"""
Really simple script to calculate precision, recall, and f1 from a list of true positives, false positives, true negatives, and false negatives.
Simply step through each detection image and type in the result. Type 'undo' to undo the last result. Type nothing to finish.
"""

import pyperclip

scene = input("Scene: ")
inp = 0
results = []
while inp != "":
    inp = input("tp, fp, tn, fn: ")
    if inp == "":
        break
    else:
        try:
            if inp in ['tp', 'fp', 'tn', 'fn']:
                results.append(inp)
            elif inp == 'undo':
                results.pop()
        except ValueError:
            print("Invalid input") 
    print(len(results))

# get frequencies of each result
tp = results.count("tp")
fp = results.count("fp")
tn = results.count("tn")
fn = results.count("fn")

# calculate precision, recall, and f1
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * ((precision * recall) / (precision + recall))

# print results
print("tp:", tp)
print("fp:", fp)
print("tn:", tn)
print("fn:", fn)

# print results
print("Precision: " + str(precision))
print("Recall: " + str(recall))
print("F1: " + str(f1))

# copy output to clipboard
pyperclip.copy(f"```\nscene {scene}\ntp: {tp}\nfp: {fp}\ntn: {tn}\nfn: {fn}\nPrecision: " + str(precision) + "\nRecall: " + str(recall) + "\nF1: " + str(f1) + "\n```")
