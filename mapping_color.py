import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

location = "10987"  # match request output
df = pd.read_csv(f"weather_info_{location}.csv")

temp_metric = "avg_temperatures_f"

# change to your color choices
colors = {
    "darkblue": "#00008B",  # Coldest - Dark Blue
    "blue": "#1E90FF",  # Dodger Blue
    "lightblue": "#87CEFA",  # Light Sky Blue
    "teal": "#20B2AA",  # Light Sea Green
    "lightgreen": "#98FB98",  # Pale Green
    "greenyellow": "#ADFF2F",  # Green Yellow
    "yellow": "#FFD700",  # Gold
    "orange": "#FFA500",  # Bright Orange
    "darkorange": "#FF8C00",  # Dark Orange
    "brightred": "#FF4500",  # Hottest - Orange Red
}

num_bins = len(colors)
hist_bins = np.histogram(df[temp_metric], bins=num_bins)[1]

list_color_keys = list(colors.keys())

for index, col in enumerate(list_color_keys):
    print(f"{col}: \t{np.round(hist_bins[index],3)}")


def map_temp_to_color_hist_with_name(temp, bins, color_keys, colors_dict):
    bin_index = np.digitize(temp, bins) - 1
    bin_index = min(bin_index, len(color_keys) - 1)
    color_key = color_keys[bin_index]
    return colors_dict[color_key], color_key


df["color_code"], df["color_name"] = zip(
    *df[temp_metric].apply(
        lambda x: map_temp_to_color_hist_with_name(
            x, hist_bins, list(list_color_keys), colors
        )
    )
)

fig, ax = plt.subplots(figsize=(len(colors), 2))

for i, color_key in enumerate(colors.keys()):
    ax.add_patch(mpatches.Rectangle((i, 0), 1, 1, color=colors[color_key]))

ax.set_xlim(0, len(colors))
ax.set_ylim(0, 1)

plt.savefig(f"./colors.png", bbox_inches="tight")

fig, ax = plt.subplots(
    figsize=(len(df), 20)
)  # Width is proportional to the number of days

for i, row in df.iterrows():
    ax.add_patch(mpatches.Rectangle((i, 0), 1, 20, color=row["color_code"]))

ax.set_xlim(0, len(df))
ax.set_ylim(0, 20)

plt.savefig(f"./daily_{location}_{temp_metric}.png", bbox_inches="tight")

df.to_csv(f"weather_info_{location}_colors.csv", index=False)
