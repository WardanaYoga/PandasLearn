import pandas as pd

print(pd.__version__)

s1 = pd.Series()
print(s1)

s2 = pd.Series([1,2,3,4,5])

print(s2)

print(s2.index)
print(s2.values)

s3 = pd.Series([1,2,3,4,5], index = [10,20,30,40,50])

print(s3)

score = pd.Series([3.2,4.5,2.6,5,3.8], index=["bob", "gorge", "alex", "fiona", "sarah"])
print(score)
print(score.index)
print(score.values)

d = {'bob' : 3.2, 'gorge': 4.5, 'alex': 2.6, 'Fiona': 5, 'Sarah':'3.8'}
s5 = pd.Series(d)

print(s5)
print(s5.values)
print(s5.index)




