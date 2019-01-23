#this file contains the database I created to train my decision tree and the code that creates a decision tree and the predictions

#Reading source: https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/

dataset1 = {1: [2,1,1]}
dataset2 = {1: [1,1,1], 2: [2,1,3], 3: [3,0,0]}
dataset3 = {1: [5,6,7], 2: [6,1,1], 3: [3,0,0], 4: [2,2,2], 5: [0,0,0,], 6: [4,2,6]}
dataset4 = {1: [4,6,1], 2: [2,0,0], 3: [9,2,6], 4: [3,2,1], 5: [5,1,1]}
dataset5 = {1: [2,1,1], 2: [5,3,1], 3: [3,0,0], 4: [4,5,2], 5: [0,0,0], 6: [8,3,4], 7: [9,4,6], 8:[4,1,1]}
dataset6 = {1: [7,8,2], 2: [5,2,6], 3: [8,4,6], 4: [2,0,0], 5: [4,1,3], 6:[5,2,1]}
dataset7 = {1: [2,3,1], 2: [5,2,2], 3: [3,3,3], 4: [2,0,2], 5: [3,3,3]}

#button category is most difficult globally
dataset8 = {1: [2,4,1]}
dataset9 = {1: [1,1,1], 2: [2,8,3], 3: [3,1,0]}
dataset10 = {1: [5,10,7], 2: [6,3,1], 3: [3,7,0], 4: [2,3,2], 5: [0,1,0], 6: [4,9,6]}
dataset11 = {1: [4,8,1], 2: [2,2,0], 3: [9,11,6], 4: [3,3,1], 5: [5,7,1]}
dataset12 = {1: [2,5,1], 2: [5,6,1], 3: [3,3,0], 4: [4,5,2], 5: [0,2,0], 6: [8,7,4], 7: [9,10,6], 8:[4,7,1]}
dataset13 = {1: [7,8,2], 2: [5,8,6], 3: [8,7,6], 4: [2,5,0], 5: [4,7,3], 6:[5,8,1]}
dataset14 = {1: [2,5,1], 2: [5,4,2], 3: [3,3,3], 4: [8,9,2], 5: [3,5,3]}
dataset22 = {1: [2,5,1], 2: [1,0,0]}

#control category is most difficult globally
dataset15 = {1: [2,4,7]}
dataset16 = {1: [1,1,1], 2: [2,2,6], 3: [3,1,7]}
dataset17 = {1: [5,7,7], 2: [6,3,9], 3: [3,3,8], 4: [2,3,2], 5: [0,1,8], 6: [4,7,9]}
dataset18 = {1: [4,5,6], 2: [2,2,3], 3: [9,6,10], 4: [3,3,6], 5: [5,3,9]}
dataset19 = {1: [2,1,3], 2: [5,3,8], 3: [3,0,2], 4: [4,5,8], 5: [0,0,0], 6: [3,3,4], 7: [9,4,10], 8:[4,1,7]}
dataset20 = {1: [7,8,8], 2: [5,2,6], 3: [8,4,9], 4: [2,0,3], 5: [4,1,7], 6:[5,2,9]}
dataset21 = {1: [2,3,6], 2: [5,2,6], 3: [3,3,3], 4: [8,5,10], 5: [3,3,5]}

#categories are tied
#swipe and button are tied
dataset23 = {1: [1,1,1], 2: [2,2,6], 3: [3,3,7]}
#button and control are tied
dataset24 = {1: [2,2,3], 2: [2,5,4], 3: [3,1,1]}
#swipe and control are tied
dataset25 = {1: [3,1,3], 2: [2,2,6], 3: [7,1,3]}
#all three tied
dataset26 = {1: [1,1,1], 2: [2,5,6], 3: [7,4,3]}


def extractData1(dataset):
    x = 0
    for user in dataset:
        x += dataset[user][0]
    return x

def extractData2(dataset):
    x = 0
    for user in dataset:
        x += dataset[user][1]
    return x

def extractData3(dataset):
    x = 0
    for user in dataset:
        x += dataset[user][2]
    return x
    
    
dataset = [
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 0,0,0,"Swipe"],#SWIPE
[extractData1(dataset2), extractData2(dataset2), extractData3(dataset2), 0,0,0,"Swipe"],#SWIPE
[extractData1(dataset3), extractData2(dataset3), extractData3(dataset3), 0,0,0,"Swipe"],#SWIPE
[extractData1(dataset4), extractData2(dataset4), extractData3(dataset4), 0,0,0,"Swipe"],#SWIPE
[extractData1(dataset7), extractData2(dataset7), extractData3(dataset7), 0,0,0,"Swipe"],#SWIPE
[extractData1(dataset2), extractData2(dataset2), extractData3(dataset2), 3,0,0,"Swipe"], #SWIPE
[extractData1(dataset3), extractData2(dataset3), extractData3(dataset3), 0,5,0,"Button"], #BUTTON
[extractData1(dataset4), extractData2(dataset4), extractData3(dataset4), 0,0,5,"Control"], #CONTROL
[extractData1(dataset5), extractData2(dataset5), extractData3(dataset5), 5,3,4,"Swipe"], #SWIPE
[extractData1(dataset6), extractData2(dataset6), extractData3(dataset6), 1,2,6,"Control"], #CONTROL
[extractData1(dataset8), extractData2(dataset8), extractData3(dataset8), 2,3,6,"Control"], #CONTROL
[extractData1(dataset9), extractData2(dataset9), extractData3(dataset9), 5,4,2,"Button"], #BUTTON
[extractData1(dataset10), extractData2(dataset10), extractData3(dataset10), 3,6,2,"Button"], #BUTTON
[extractData1(dataset11), extractData2(dataset11), extractData3(dataset11), 4,4,4,"Button"], #BUTTON
[extractData1(dataset12), extractData2(dataset12), extractData3(dataset12), 0,0,5,"Control"], #CONTROL
[extractData1(dataset13), extractData2(dataset13), extractData3(dataset13), 6,2,3,"Swipe"], #SWIPE
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 1,1,1,"Control"], #CONTROL
[extractData1(dataset16), extractData2(dataset16), extractData3(dataset16), 0,0,3,"Control"], #CONTROL
[extractData1(dataset17), extractData2(dataset17), extractData3(dataset17), 1,6,4,"Control"], #CONTROL
[extractData1(dataset18), extractData2(dataset18), extractData3(dataset18), 2,6,2,"Button"], #BUTTON
[extractData1(dataset19), extractData2(dataset19), extractData3(dataset19), 2,8,9,"Control"], #CONTROL
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 6,2,1,"Swipe"], #SWIPE
[extractData1(dataset22), extractData2(dataset22), extractData3(dataset22), 1,2,1,"Control"], #CONTROL
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 4,2,7,"Control"], #CONTROL
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 4,2,5,"Swipe"], #SWIPE
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 4,8,2,"Button"], #BUTTON
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 4,7,2,"Swipe"], #SWIPE
[extractData1(dataset1), extractData2(dataset1), extractData3(dataset1), 2,5,2,"Swipe"], #SWIPE
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 4,2,5,"Control"], #CONTROL
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 2,6,5,"Control"], #CONTROL
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 4,12,5,"Button"], #BUTTON
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 4,6,6,"Control"], #CONTROL
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 4,8,6,"Control"], #CONTROL
[extractData1(dataset20), extractData2(dataset20), extractData3(dataset20), 4,10,6,"Button"], #BUTTON
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 1,2,2,"Button"], #BUTTON
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 1,2,5,"Button"], #BUTTON
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 1,2,8,"Control"], #CONTROL
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 5,2,1,"Button"], #BUTTON
[extractData1(dataset15), extractData2(dataset15), extractData3(dataset15), 7,2,2,"Swipe"], #SWIPE
[extractData1(dataset23), extractData2(dataset23), extractData3(dataset23), 4,9,10,"Button"], #Button
[extractData1(dataset23), extractData2(dataset23), extractData3(dataset23), 4,9,15,"Control"], #Control
[extractData1(dataset23), extractData2(dataset23), extractData3(dataset23), 4,2,7,"Swipe"], #Swipe
[extractData1(dataset23), extractData2(dataset23), extractData3(dataset23), 4,2,10,"Control"], #Control
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 1,1,2,"Control"], #Control
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 5,2,3,"Control"], #Control
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 7,2,3,"Swipe"], #Swipe
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 5,3,2,"Button"], #Button
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 7,3,2,"Swipe"], #Swipe
[extractData1(dataset24), extractData2(dataset24), extractData3(dataset24), 1,3,7,"Control"], #Control
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 4,2,2,"Swipe"], #Swipe
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 4,5,2,"Swipe"], #Swipe
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 4,9,2,"Button"], #Button
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 2,2,3,"Control"], #Control
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 2,6,3,"Control"], #Control
[extractData1(dataset25), extractData2(dataset25), extractData3(dataset25), 2,9,3,"Button"], #Button
[extractData1(dataset26), extractData2(dataset26), extractData3(dataset26), 2,4,3,"Button"], #Button
[extractData1(dataset26), extractData2(dataset26), extractData3(dataset26), 2,3,4,"Control"], #Control
[extractData1(dataset26), extractData2(dataset26), extractData3(dataset26), 4,3,3,"Swipe"], #Swipe
[extractData1(dataset26), extractData2(dataset26), extractData3(dataset26), 3,3,3,"Swipe"], #Swipe
[extractData1(dataset6), extractData2(dataset6), extractData3(dataset6), 6,5,4,"Swipe"], #Swipe
[extractData1(dataset21), extractData2(dataset21), extractData3(dataset21), 3,5,8,"Control"], #Swipe
]


dataTest = [
[extractData1(dataset7), extractData2(dataset7), extractData3(dataset7), 8,5,6],
[extractData1(dataset14), extractData2(dataset14), extractData3(dataset14), 2,6,1],
[extractData1(dataset21), extractData2(dataset21), extractData3(dataset21), 3,4,7]
]



def bestSplit(dataset):
    #splits by value for attribute, finds best split using smallest gini index value
    bestGini, bestAttribute, bestValue, bestGroups = None, None, None, None
    categories = set()
    for row in dataset:
        categories.add(row[-1])
    #categories = swipe, button, control
    categories = list(categories)
    for attribute in range(len(dataset[0])-1):
        for sample in dataset:
            splitGroups = splitSet(dataset, attribute, sample[attribute])
            gini = giniIndex(splitGroups, categories)
            if bestGini == None or gini < bestGini:
                bestGini, bestAttribute, bestValue, bestGroups = gini, attribute, sample[attribute], splitGroups
    split = {"attribute": bestAttribute, "value": bestValue, "groups": bestGroups}
    return split


def splitSet(dataset, index, splitValue):
    #separates given set by the splitValue
    #each node can have max two other branches, thus two groups
    leftGroup, rightGroup = [],[]
    for sample in dataset:
        if sample[index] < splitValue:
            leftGroup.append(sample)
        else:
            rightGroup.append(sample)
    return leftGroup,rightGroup

def giniIndex(groups, categories):
    #calculates giniIndex based on how the attribute has been split
    totalSample = 0
    for group in groups:
        totalSample += len(group)
    gini = 0
    for group in groups:
        groupSize = len(group)
        if groupSize != 0:
            score = 0
            for category in categories:
                sampleCategories = []
                for sample in group:
                    sampleCategories.append(sample[-1])
                proportion = sampleCategories.count(category) / groupSize
                score += proportion * (1.0 - proportion)
            gini += score * groupSize / totalSample
    return gini
    

def terminal(group):
    #ends the group and returns most common outcome
    sampleCategories = dict()
    for sample in group:
        sampleCategories[sample[-1]] = sampleCategories.get(sample[-1], 0) + 1
    maxCount, maxCategory = 0, None
    for sample in sampleCategories:
        if sampleCategories[sample] > maxCount:
            maxCount = sampleCategories[sample]
            maxCategory = sample
    return maxCategory


def split(node, maxDepth, minSize, depth):
    leftGroup, rightGroup = node["groups"]
    #base cases
    if len(leftGroup) == 0 or len(rightGroup) == 0:
        node["leftGroup"] = node["rightGroup"] = terminal(leftGroup + rightGroup)
        return
    #depth should not exceed maxDepth
    if depth >= maxDepth:
        node["leftGroup"] = terminal(leftGroup)
        node["rightGroup"] = terminal(rightGroup)
    #recursive steps
    #a group should not be smaller than the minimum size, otherwise continue splitting
    if len(leftGroup) <= minSize:
        node["leftGroup"] = terminal(leftGroup)
    else:
        node["leftGroup"] = bestSplit(leftGroup)
        split(node["leftGroup"], maxDepth, minSize, depth+1)
    if len(rightGroup) <= minSize:
        node["rightGroup"] = terminal(rightGroup)
    else:
        node["rightGroup"] = bestSplit(rightGroup)
        split(node["rightGroup"], maxDepth, minSize, depth+1)


def predict(tree,sample):
    #checks if in left group
    if sample[tree["attribute"]] < tree["value"]:
        #check if not terminal node, base case
        if not isinstance(tree["leftGroup"], dict):
            return tree["leftGroup"]
        #recursive case
        else:
            return predict(tree["leftGroup"], sample)
    #same process, right group
    else:
        #check if not terminal node, base case
        if not isinstance(tree["rightGroup"], dict):
            return tree["rightGroup"]
        #recursive case
        else:
            return predict(tree["rightGroup"], sample)


def decisionTree(train, test, maxDepth, minSize):
    #conducts first split
    baseSplit = bestSplit(train)
    split(baseSplit, maxDepth, minSize, 1)
    tree = baseSplit
    #makes prediction for each test sample
    results = []
    for sample in test:
        prediction = predict(tree, sample)
        results.append(prediction)
    return results

