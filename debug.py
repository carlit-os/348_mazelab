import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(title, map1, map2):
	result=True
	print(title)
	for y in range(0,common.constants.MAP_HEIGHT):
		v=""
		for x in range(0,common.constants.MAP_WIDTH):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	return result
	

					 

data2 = ("0000000000"
"1111110101"
"0300010101"
"1111010101"
"0001010101"
"0100010101"
"1111010101"
"0000000101"
"0111111100"
"0000000101"
"0111111120"
"0000000010")
			  
gold_df2 = ("0000005554"
  "1111115151"
  "0555515151"
  "1111515151"
  "4441515151"
  "4144515151"
  "1111515151"
  "4444555151"
  "4111111154"
  "4444444151"
  "4111111154"
  "4444444414")
					 
gold_bf2 = ("4444445554"
  "1111115151"
  "0555515151"
  "1111515151"
  "4441515151"
  "4144515151"
  "1111515151"
  "4444555151"
  "4111111154"
  "4440000151"
  "4111111154"
  "4000000014")



all_passed = True



gold_dfmap2 = common.init_map();
common.set_map(gold_dfmap2, gold_df2)
gold_bfmap2 = common.init_map()
common.set_map(gold_bfmap2, gold_bf2)

dfmap2 = common.init_map()
common.set_map(dfmap2, data2)
df2 = student_code.df_search(dfmap2)
tdf2 = "Empty map first depth search results:";
cdf2 = check_result(tdf2,dfmap2,gold_dfmap2)
if df2:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

bfmap2 = common.init_map()
common.set_map(bfmap2, data2)
bf2 = student_code.bf_search(bfmap2)
tbf2 = "Empty map first breadth search results:"
cbf2 = check_result(tbf2,bfmap2,gold_bfmap2)
if bf2:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

all_passed = all_passed and cdf2 and cbf2 and df2 and bf2 



print("\n\r")
if all_passed:
	print( bcolors.GREEN+"all test cases passed"+bcolors.NORMAL)
	exit(0)
else:
	print( bcolors.RED+"Not all test cases passed"+bcolors.NORMAL)
	exit(1)
