fts = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
       'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week']
fts_domain = {'age': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
              'workclass': ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov',
                            'Without-pay', 'Never-worked'],
              'fnlwgt': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
              'education': ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc',
                            '9th',
                            '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool'],
              'education-num': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
              'marital-status': ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed',
                                 'Married-spouse-absent',
                                 'Married-AF-spouse'],
              'occupation': ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
                             'Prof-specialty',
                             'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing',
                             'Transport-moving',
                             'Priv-house-serv', 'Protective-serv', 'Armed-Forces'],
              'relationship': ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'],
              'race': ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'],
              'sex': ['Female', 'Male'],
              'capital-gain': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
              'capital-loss': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
              'hours-per-week': ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0']}
labels = ['<=50K', '>50K']


def major(label_value):
    val = [0, 0]  # <=50K, >50K
    for i in label_value:
        if i == labels[0]:
            val[0] += 1
        else:
            val[1] += 1
    if val[0] > val[1]:
        return 0
    else:
        return 1


def info_gini(data, attr):
    gini = 0
    count = len(data[0])
    print("count: ", count)
    for val in fts_domain[attr]:
        num_0 = 0
        num_1 = 0
        idx = fts.index(attr)
        for i in range(count):
            if data[idx][i] == val:
                if data[13][i] == labels[0]:
                    num_0 += 1
                else:
                    num_1 += 1
        print(num_0, num_1)
        total = num_0 + num_1
        if total != 0:
            gini += total / count * (1 - pow((num_0 / total), 2) - pow((num_1 / total), 2))

    return gini


def split(data, attributes):
    min_gini = 0.5
    best_attr = ""

    for attr in attributes:
        gini = info_gini(data, attr)
        if gini < min_gini:
            min_gini = gini
            best_attr = attr
    return best_attr


def divide(data, bestAttributes, value):
    examples = [[] for j in range(14)]
    best_idx = fts.index(bestAttributes)
    for index in range(len(data[0])):
        if data[best_idx][index] == value:
            for j in range(14):
                examples[j].append(data[j][index])

    return examples


def make_tree(data, attributes):
    p_label = major(data[13])
    if len(data[0]) <= 1:
        return labels[p_label]
    elif data[13].count(data[13][0]) == len(data[13]):
        return data[13][0]
    else:
        best_attr = split(data, attributes)
        if best_attr == "":
            return labels[p_label]
        print("best attr:", best_attr)

        tree = {best_attr: {}}
        for val in fts_domain[best_attr]:
            subset = divide(data, best_attr, val)
            if len(subset[0]) == 0:
                return labels[p_label]
            else:
                newAttr = [x for x in attributes]
                newAttr.remove(best_attr)
                subTree = make_tree(subset, newAttr)
                tree[best_attr][val] = subTree

    return tree
