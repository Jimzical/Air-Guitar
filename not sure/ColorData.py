import pandas


# read the csv file
# df = pandas.read_csv("colorfinger.csv")
# df = pandas.read_csv("colorlist.csv")
df = pandas.read_csv("colornew.csv")

# print df stats
print(df.describe())
print(type(df.describe()))