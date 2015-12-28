
def setDict(student):
	studentInfo = str.split(student,',')
	dict = {}
	dict['name'] = studentInfo[0]
	dict['roll_num'] = int(studentInfo[1])
	dict['english'] = int(studentInfo[2])
	dict['mathematics'] = int(studentInfo[3])
	dict['computer_science'] = int(studentInfo[4])
	return dict

def objectifying(list):
	list = map(setDict ,list)
	return list

def highest(students,subject):
	arrangedInfo = objectifying(students)
	result = reduce(lambda highest,nextValue : nextValue if highest[subject] <= nextValue[subject] else highest, arrangedInfo)
	return result

def lowest(students,subject):
	arrangedInfo = objectifying(students)
	result = reduce(lambda highest,nextValue : nextValue if highest[subject] >= nextValue[subject] else highest, arrangedInfo)
	return result

def above(students,subject,threshold):
	arrangedInfo = objectifying(students)
	result = filter(lambda student : True if student[subject] > threshold else False , arrangedInfo)
	return result

def below(students,subject,threshold):
	arrangedInfo = objectifying(students)
	result = filter(lambda student : True if student[subject] < threshold else False , arrangedInfo)
	return result

def phoneBook(students):
	arrangedInfo = objectifying(students)
	phoneBookData = {}
	for x in range(65 ,91):
		phoneBookData[chr(x)] = []
	for student in arrangedInfo:
		phoneBookData[student["name"][0]].append(student)
	return phoneBookData

def averageOf(students , subject):
	arrangedInfo = objectifying(students)
	result = reduce(lambda sumOfPrevious,nextValue : sumOfPrevious+nextValue[subject] , arrangedInfo ,0)
	average = round(float(result) / len(arrangedInfo))
	return average

def between(students, subject ,score1 ,score2):
	arrangedInfo = objectifying(students)
	result = filter(lambda student : True if student[subject]>=score1 and student[subject]<=score2 else False ,arrangedInfo)
	return result
