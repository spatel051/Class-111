import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
print("The mean is " + str(mean))
print("The standard deviation is " + str(standard_deviation))

def random_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_off_mean = random_mean(100)
    mean_list.append(set_off_mean)

sample_mean = statistics.mean(mean_list)
sample_std_deviation = statistics.stdev(mean_list)

print("The sample mean is " + str(sample_mean))
print("The sample standard deviation is " + str(sample_std_deviation))

fig = ff.create_distplot([mean_list], ["Math Scores"], show_hist = False)
fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 0.25],
    mode = "lines",
    name = "Mean"
))

fig.show()