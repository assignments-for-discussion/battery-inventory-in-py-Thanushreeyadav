
def count_batteries_by_usage(cycles):
  #dict is a data structure to store the number of batteries of varying charge. 
  dict = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  #Iterate through the each battery's number of charge cycles & increment the dictionary values according to classification given.
  #added tests to catch string values or negative values passed to the function
  for i in cycles:
    if not isinstance(i,int):
      raise Exception("Enter numeric values only!")
    if i < 0:
      raise Exception("value can not be negative!")
    if i >= 910:
      dict['highCount'] += 1
    elif i >= 410 and i < 910:
      dict['mediumCount'] += 1
    elif i >= 0 and i < 410:
      dict['lowCount'] += 1
  return dict

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
