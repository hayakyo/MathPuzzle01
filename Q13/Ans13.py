import itertools
import re

# expression = 'WE*LOVE==CODEIQ'
expression = 'READ+WRITE+TALK==SKILL'
nums = list(re.split(r"[^a-zA-Z]", expression))
chars = list(set(list("".join(nums))))
head = [num[0] for num in nums if num != ""]

count = 0
for seq in itertools.permutations(list(range(10)), len(chars)):
    is_zero_first = False
    if 0 in seq:
        is_zero_first = True if chars[seq.index(0)] in head else False
    if not is_zero_first:
        formula = expression.translate(str.maketrans(
            dict(zip(chars, list(map(str, seq))))))
        if eval(formula):
            print(formula)
            count += 1
print(count)
