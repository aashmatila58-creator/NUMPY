import numpy as np

# rng = np.random.default_rng(seed=1)

# print(rng.integers(low=1, high=88, size=(3, 2)))

# print(np.random.uniform(low=-1, high=1, size=3))

rng = np.random.default_rng()
# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)
# print(array)
fruits =np.array(["apple", "orange", "mango", "grapes"])
fruit = rng.choice(fruits, size=(3,3))
print(fruit)