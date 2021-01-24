# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# seed set
np.random.seed(123)

# Simulate random walk 10,000 times
all_walks = []
for i in range(10000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# clear plot
plt.clf()

# labels & titles
plt.xlabel("Step Reached")
plt.ylabel("Occurences")
plt.title("Reaching 60th step")

# Plot histogram of ends, display plot
plt.hist(ends, color='orange')
plt.show()

odds = ends >= 60
print(np.mean(odds))
