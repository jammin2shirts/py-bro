import re

total = 0
with open("test_data/advent_data.txt","r") as r:
	for line in r:
		print(line)
		int1 = re.findall(r"\d",line)[0]	
		int2 = re.findall(r"\d",line)[-1]	
		final_int = int(str(int1) + str(int2))
		print(final_int)
		total += final_int
		print(total)
