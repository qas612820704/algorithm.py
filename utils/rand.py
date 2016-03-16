import random

def ran_list(size=10,start=1,end=100):
  data = []
  for i in range(0, size):
    data.append(random.randint(start, end))
  return data
