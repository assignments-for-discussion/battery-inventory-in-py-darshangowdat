
def count_batteries_by_usage(cycles):
  int a=0,b=0,c=0
  for i in cycles:
    if i<400:
      a = a+1
    elif i<919:
      b= b+1
    else:
      c=c+1
   return a,b,c


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  a,b,c = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  if(a == 2):
    print('low=2')
  if(b == 3):
    print('medium=3')
  if(c == 1):
    print('high=1')
    
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
