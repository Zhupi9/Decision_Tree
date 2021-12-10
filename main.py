# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def preprocessing(train_data_path, test_data_path):
    contiousAttr = [0, 2, 4, 10, 11, 12]
    maxList = [90,1484705,16,99999,4356,99]
    minList = [17,13769,1,0,0,1]
    data = []
    with open(train_data_path, encoding="utf-8") as f:
        datalist = f.read().splitlines()
    for sample in datalist:
        attr = sample.split(", ")
        attr.pop(13)
        print(attr)
        flag = True
        for value in attr:
            if value == '?':
                print("this sample is removed")
                flag = False
                break
        if flag: data.append(attr)

    return discretize_sample(data, contiousAttr,maxList,minList)


def discretize_sample(dataset, con_attr_list, max_list, min_list):
    discretizedata = []
    for sample in dataset:
        for i in range(6):
            index=con_attr_list[i]
            new_value = discretize_attribute(sample[index], max_list[i], min_list[i])
            sample[index] = str(new_value)
        discretizedata.append(sample)

    return discretizedata


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
