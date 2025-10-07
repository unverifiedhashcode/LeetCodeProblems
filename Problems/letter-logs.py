
def LogSort(logs):
    letList = []
    digList = []
    for log in logs:
        identifier = log.split(' ',1)[0]
        value = log.split(' ',1)[1]
        if value[0].isdigit():
            digList.append([identifier, value])
        else:
            letList.append([identifier, value])

    #sort the letter list
    for i in range(len(letList)-1, 0, -1):
        swapped = False
        for j in range(i):
            if (letList[j][1] > letList[j+1][1]) or ((letList[j][1] == letList[j+1][1]) and (letList[j][0] > letList[j+1][0])):
                temp = letList[j]
                letList[j] = letList[j + 1]
                letList[j + 1] = temp
                swapped = True

        if not swapped:
            break

    for i in range(len(letList)):
        letList[i] = letList[i][0]+' '+letList[i][1]
    for i in range(len(digList)):
        digList[i] = digList[i][0]+' '+digList[i][1]

    finList = letList + digList
    return finList




logs = ["dig1 8 1 5 1","let3 art can","dig2 3 6","let2 own kit dig","let1 art zero"]
print(LogSort(logs))