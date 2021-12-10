# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import DecisionTree
from DecisionTree import *


def zanding(data):
    array = [[] for j in range(14)]
    for dataline in data:
        s = dataline.split(", ")
        if len(s) == 15:
            s.pop(13)
            if "?" not in s:
                for i in range(14):
                    if i == 0 or i == 2 or i == 4 or i == 10 or i == 11 or i == 12:
                        array[i].append(int(s[i]))
                    else:
                        array[i].append(s[i])
    return array


def preprocessing(train_data_path, test_data_path):
    contiousAttr = [0, 2, 4, 10, 11, 12]
    maxList = []
    minList = []
    data = []

    with open(train_data_path, encoding="utf-8") as f:
        train_set = f.read().splitlines()
    with open(test_data_path, encoding="utf-8") as f:
        test_set = f.read().splitlines()

    train_array = zanding(train_set)
    test_array = zanding(test_set)

    for i in contiousAttr:
        maxV = max(train_array[i]) + 1
        minV = min(train_array[i])
        maxList.append(maxV)
        minList.append(minV)

    # print(maxList)
    # print(minList)
    return discretize_sample(train_array, contiousAttr, maxList, minList), discretize_sample(test_array, contiousAttr,
                                                                                             maxList, minList)


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
    # print(dataset)

    return dataset


def discretize_attribute(value, max, min):
    gap = (max + 1 - min) / 10  # discretize feature into ten categories
    return (int(value) - min) // gap


def testing_single(record, tree):
    true_label = record[13][0]
    while isinstance(tree, dict):
        treeKey = list(tree.keys())[0]
        keyIndex = fts.index(treeKey)
        value = record[keyIndex][0]
        if value in tree[treeKey]:
            if isinstance(tree[treeKey][value], dict):
                tree = tree[treeKey][value]
            else:
                if tree[treeKey][value] == true_label:
                    return 1
                else:
                    return 0
        else:
            if "<=50K" == true_label:
                return 1
            else:
                return 0


def testing(data, tree):
    total = len(data[0])
    correct = 0

    for i in range(total):
        array = [[] for j in range(14)]
        for j in range(14):
            array[j].append(data[j][i])
        correct += testing_single(array, tree)

    return correct / total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    train_data_file = "adult.data"
    test_data_file = "adult.test"

    train_data, test_data = preprocessing(train_data_file, test_data_file)
    tree = make_tree(train_data, fts)
    print(tree)

    print(testing(test_data, tree))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
