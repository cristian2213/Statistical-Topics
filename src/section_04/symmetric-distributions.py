from math import ceil, floor
import statistics

# steps of 10 units from 100 to 1000
data_set1 = range(100, 1001, 10)

mean = statistics.mean(data_set1)
stdev = statistics.stdev(data_set1)
x = -300
z_core = statistics.NormalDist(mean, stdev).zscore(x)
z_score = ceil(z_core) if z_core < 0 else floor(z_core)
print(f"z_score of {x} is {z_score}")
