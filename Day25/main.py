import pandas
import numpy
data = pandas.read_csv("Squirrel_Data.csv")


fur_color = data["PrimaryFurColor"].tolist()
color_list = pandas.value_counts(numpy.array(fur_color).tolist())

df = pandas.DataFrame(color_list)
df.to_csv("squirellcount.csv")

