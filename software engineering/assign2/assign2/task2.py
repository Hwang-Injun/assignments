import pandas as pd

df = pd.read_pickle("d30c14b3-4039-3ad8-9cc3-025485863b7c-61939.pickle")
df = df[["type"]]

#task 2.a
wificount = df[(df['type'] == "WiFi")].count().values[0]
print("wificount: " + str(wificount))

mobilecount = df[(df['type'] == "Mobile")].count().values[0]
print("mobilecount: " + str(mobilecount))

#task 2.b

df['subgroup'] = (df['type'] != df['type'].shift(1)).cumsum()

grouped_df = df.groupby('subgroup', as_index=False).apply(lambda x: (x['type'].head(1), x.shape[0]))

maximum_wifi = 0
maximum_mobile = 0
for i in range(297):
    if grouped_df.values[i][1] > maximum_wifi and grouped_df.values[i][0].values[0] == "WiFi":
        maximum_wifi = grouped_df.values[i][1]
    if grouped_df.values[i][1] > maximum_mobile and grouped_df.values[i][0].values[0] == "Mobile":
        maximum_mobile = grouped_df.values[i][1]

print("consecutive maximum wifi: " + str(maximum_wifi))
print("consecutive maximum mobile: " + str(maximum_mobile))



