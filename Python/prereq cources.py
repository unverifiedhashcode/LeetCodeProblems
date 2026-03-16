import sys
sys.setrecursionlimit(100000)  # set higher depending on input size

print(len(testCaseBIG))
def courseFindRecurBAD(courses, req, past_c):
    print('running w courses:',courses,'req:',req,'past_c:',past_c)
    for course in courses:
        if course[0] == req: # required course is found
            print('requirement', req, 'FOUND in courses!')
            if req in past_c:
                return False
            else:
                past_c.append(course[0])
                return courseFindRecur(courses, course[1],past_c) #only pass in the current and future courses
    return True  # not the most efficeint but whatever

def canFinishBAD(courses):
    for i in range(len(courses)):
        currCourse = courses[i]
        course = currCourse[0]
        req = currCourse[1]
        if courseFindRecur(courses[i:len(courses)], req, [course]) == False:
            return False
    return True

def courseFindRecur(courseGraph, req, pastCourses):

    if req in pastCourses:
        return False

    pastCourses.append(req)

    if req in courseGraph:
        for coRec in courseGraph[req]:
            if not courseFindRecur(courseGraph, coRec, pastCourses):
                return False
    pastCourses.pop()

    return True




def buildGraph(courses):
    courseDict = {}
    #create course dictionary
    for course, req in courses:
        courseDict[course] = [req]

    for course, req in courses:
        if req not in courseDict[course]:
            courseDict[course].append(req)

    print(courseDict)
    return courseDict

def canFinishGood(courses):
    courseGraph = buildGraph(courses)
    for course, req in courses:
        if courseFindRecur(courseGraph,course,[]) is False:
            return False
    return True



if __name__ == '__main__':
    print(canFinishGood(testCaseBIG))
