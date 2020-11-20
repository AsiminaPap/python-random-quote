import random

def main():
  
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  quotes.append ("The ice is now fractured.")
  del quotes[-1]

if __name__== "__main__":
  main()
