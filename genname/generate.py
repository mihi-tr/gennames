
import random
import time
import re
import functools
from genname.words import adjectives, nouns

random.seed(time.time())

def plural(noun):
  sends=["s$","x$","sh$","ch$"]
  if functools.reduce(lambda x,y: x or re.search(y,noun),sends,False):
    return "%ses"%noun
  if re.search("[^ea]y$",noun):
    return "%sies"%noun[:-1]
  return "%ss"%noun

def generate_names(num,plural=False):
  a=random.sample(adjectives,num)
  n=random.sample(nouns,num)
  for (a,n) in zip(a,n):
    if plural:
        yield "The %s %s"%(a,plural(n))
    else:
        yield "%s %s"%(a,n)

def generate_name():
    return generate_names(1).next()

if __name__=="__main__":
  import sys
  try:
    num=int(sys.argv[1])
  except IndexError:
    num=5
  for i in generate_names(num,plural=True):
    print(i)
