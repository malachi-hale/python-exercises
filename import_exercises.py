from function_exercises1 import calculate_tip
print(calculate_tip(0.2, 100))

import itertools
print(list(itertools.product("abc", [1,2,3])))
print(len(list(itertools.product("abc", [1,2,3]))))

print(list(itertools.combinations("abcd",2)))
print(len(list(itertools.combinations("abcd",2))))

print(list(itertools.permutations("abcd",2)))
print(len(list(itertools.permutations("abcd",2))))
