# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def preprocessing(train_data_path, test_data_path):
    contiousAttr = [0, 2, 4, 10, 11, 12]
    maxList = []
    minList = []
    data = []

    with open(train_data_path, encoding="utf-8") as f:
        train_set = f.read().splitlines()

    testArray = [[] for j in range(14)]
    for dataline in train_set:
        s = dataline.split(", ")
        if len(s) == 15:
            s.pop(13)
            if "?" not in s:
                for i in range(14):
                    if i == 0 or i == 2 or i == 4 or i == 10 or i == 11 or i == 12:
                        testArray[i].append(int(s[i]))
                    else:
                        testArray[i].append(s[i])
    for i in contiousAttr:
        maxV = max(testArray[i]) + 1
        minV = min(testArray[i])
        maxList.append(maxV)
        minList.append(minV)

    print(maxList)
    print(minList)
    return discretize_sample(testArray, contiousAttr,maxList,minList)


def discretize_sample(dataset, contiousAttr, maxList, minList):
    discretizedata = []
    for i in range(6):
        row = contiousAttr[i]
        length = len(dataset[row])
        for j in range(length):
            newV = discretize_attribute(dataset[row][j], maxList[i], minList[i])
            dataset[row][j] = str(newV)
    '''
    discretizedata.append()
    for sample in dataset:
        for i in range(6):
            index = contiousAttr[i]
            newV= discretize_attribute(sample[index], max_list[i], min_list[i])
            sample[index] = str(new_value)
        discretizedata.append(sample)
    '''
    print(dataset)

    return dataset


def discretize_attribute(value, max, min):
    gap = (max+1 - min) / 10  # discretize feature into ten categories
    return (int(value) - min) // gap


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_data_file = "adult.data"
    test_data_file = "adult.test"

    data = preprocessing(train_data_file, test_data_file)

    for sample in data:
        print(sample)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
