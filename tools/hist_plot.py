import matplotlib.pyplot as plt
from eaxtension import jsonE

noise = jsonE.load("../noise_data.json")
noise = noise["noise_list"]

plt.xlim(0, 1000)
plt.hist(noise, bins=1000)
plt.show()