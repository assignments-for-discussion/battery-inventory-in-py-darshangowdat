
def count_batteries_by_usage(cycles):
  count={"low":0, "medium":0, "high":0}
  for i in cycles:
    if i<400:
      count["low"] = count["low"]+1
    elif i>=400 and i <919:
      count["medium"] =count["medium"]+1
    else:
      count["high"] = count["high"]+1
   
  return count


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print(counts)
  assert(counts["low"] == 2)
  assert(counts["medium"] == 3)
  assert(counts["high"] == 1)
    
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
