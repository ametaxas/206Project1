import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	fh = open(file, "r")
	people = [(person.strip()).split(',') for person in fh.readlines()]
	heading = people[0]
	final_list = []
	for person in people[1:]:
		new_dic = {}
		for ind in range(len(person)): #iterate through indices to add a new dictionary with each piece of info
			new_dic[heading[ind]] = person[ind]
		final_list.append(new_dic)
	return final_list

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	init_list = []
	for dic in data:
		init_list.append(dic[col])
	for dic in data:
		if dic[col] == sorted(init_list)[0]:
			return (dic['First'] + " " + dic['Last'])

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	class_size = {}
	for dic in data:
		if dic['Class'] not in class_size:
			class_size[dic['Class']] = 0
		class_size[dic['Class']] += 1
	return [(year, class_size[year]) for year in sorted(class_size, key = lambda x: class_size[x], reverse = True)]



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	most_pop_day = {}
	for dic in a:
		day = dic['DOB'].split('/')[1]
		if day not in most_pop_day:
			most_pop_day[day] = 0
		most_pop_day[day] += 1
	return int(sorted(most_pop_day, key = lambda x: most_pop_day[x], reverse = True)[0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	current_date = [int(x) for x in (input("What is the current date? MM/DD/YYYY:")).split('/')]
	ages = []
	for dic in a:
		date = [int(x) for x in dic['DOB'].split('/')]
		ages.append ((current_date[2] - date[2]) + ((current_date[0] - date[0])/12) + ((current_date[1] - date[1])/365)) #year plus month plus day
	return int((sum(ages) / len(ages)))


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	outfile = open(fileName, 'w')
	def pullInfo(dic):
		return (dic['First'],dic['Last'],dic['Email'])
	master_dic = {}
	for dic in a:
		master_dic[a.index(dic)] = dic[col] #key is the index of the dif, value is the sorted key
	for ind in sorted(master_dic, key = lambda x: master_dic[x]):
		x = pullInfo(a[int(ind)]) #pulling first, last and email
		outfile.write("{},{},{}\n".format(*x))  #writing info into csv
	outfile.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

