import json

import numpy as np

data = np.loadtxt("dataset.csv", delimiter=", ")

json.dump(data.sum(), open("model.json", "w+"))

result = {"result": data.mean()}
json.dump(result, open("result.json", "w+"))
