import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)


data = pd.DataFrame({'whoAmI': lst})

data['whoAmI'] = data['whoAmI'].astype('category').cat.codes

one_hot = pd.get_dummies(data, columns=['whoAmI'])

print(one_hot)