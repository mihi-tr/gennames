
import random
import time
import re
import functools

f=open("adjectives.txt")
adjectives=[i.strip() for i in f]
f.close
f=open("nounlist.txt")
nouns=[i.strip() for i in f]
f.close()

random.seed(time.time())

def plural(noun):
  sends=["s$","x$","sh$","ch$"]
  if functools.reduce(lambda x,y: x or re.search(y,noun),sends,False):
    return "%ses"%noun
  if re.search("[^ea]y$",noun):
    return "%sies"%noun[:-1]
  return "%ss"%noun

def generate_names(num):
  a=random.sample(adjectives,num)
  n=random.sample(nouns,num)
  for (a,n) in zip(a,n):
    yield "The %s %s"%(a,plural(n))

if __name__=="__main__":
  import sys
  try:
    num=int(sys.argv[1])
  except IndexError:
    num=5
  for i in generate_names(num):
    print(i)
