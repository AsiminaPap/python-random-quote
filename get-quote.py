import random

def main():
  
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 13
  rnd = random.randint(0, last)
  
  last = len(quotes) - 1
  print last

  print([rnd])

if __name__== "__main__":
  main()
