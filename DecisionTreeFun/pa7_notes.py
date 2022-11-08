from tabulate import tabulate
import numpy as np
X_train = [
        ["Senior", "Java", "no", "no"],
        ["Senior", "Java", "no", "yes"],
        ["Mid", "Python", "no", "no"],
        ["Junior", "Python", "no", "no"],
        ["Junior", "R", "yes", "no"],
        ["Junior", "R", "yes", "yes"],
        ["Mid", "R", "yes", "yes"],
        ["Senior", "Python", "no", "no"],
        ["Senior", "R", "yes", "no"],
        ["Junior", "Python", "yes", "no"],
        ["Senior", "Python", "yes", "yes"],
        ["Mid", "Python", "no", "yes"],
        ["Mid", "Java", "yes", "no"],
        ["Junior", "Python", "no", "yes"]
    ]

y_train = ["False", "False", "True", "True", "True", "False", "True", "False", "True", "True", "True", "True", "True", "False"]

# TODO: in fit(), programmatically build header and attribute_domains
# using X_train. perhaps store as attributes of MyDecisionTreeClassifier
header = ["att0", "att1", "att2", "att3"]
attribute_domains = {"att0": ["Senior", "Mid", "Junior"], 
        "att1": ["R", "Python", "Java"],
        "att2": ["yes", "no"], 
        "att3": ["yes", "no"]}

# how to represent trees in Python
# 1. nested data structures(like dictionary)
# 2. OOP (Tree Class/Node Class)

# we will use a nested list approach
# at element 0: data type (Attribute, Value, Leaf)
# at element 1: data value(attribute name, value name, class label)
# rest of elements: depends on the type
# example: 

interview_tree_solution =   ["Attribute", "att0",
                                ["Value", "Junior",
                                    ["Attribute", "att3",
                                        ["Value", "no",
                                            ["Leaf", "True",3,5]
                                        ],
                                        ["Value", "yes",
                                            ["Leaf", "False",2,5]
                                        ]
                                    ]
                                ],

                                ["Value", "Mid",
                                    ["Leaf","True",4,14]
                                ],

                                ["Value", "Senior",
                                    ["Attribute", "att2",
                                        ["Value", "no",
                                            ["Leaf", "False",3,5]
                                        ],
                                        ["Value", "yes",
                                            ["Leaf", "True",2,5]
                                        ]
                                    ]
                                ]
                            ]

def select_attribute(instances, attributes):
    # randomly selects index
    # TODO change to entropy selection
    rand_index = np.random.randint(0,len(attributes))
    return attributes[rand_index]

def partition_instances(instances, attribute):
    att_index = header.index(attribute)
    att_domain = attribute_domains["att"+str(att_index)]
    print("attribute domain:", att_domain)

    partitions = {}
    for att_value in att_domain:
        partitions[att_value] = []
        for instance in instances:
            if instance[att_index] == att_value:
                partitions[att_value].append(instance)
    return partitions
def same_class_label(instances):
    first_label = instances[0][-1]
    for instance in instances:
        if instance[-1] != first_label:
            return False
    # get here, all the same
    return True

def tdidt(current_instances, available_attributes):
    # basic approach (uses recursion!!):
    print("available attrs:", available_attributes)
    # select an attribute to split on
    split_attribute = select_attribute(current_instances,available_attributes)
    print("splitting on:", split_attribute)
    available_attributes.remove(split_attribute)
    tree = ["Attribute", split_attribute]
    # group data by attribute domains (creates pairwise disjoint partitions)

    partitions = partition_instances(current_instances, split_attribute) # returns a dict
    print("partitions:", partitions)

    # for each partition, repeat unless one of the following occurs (base case)

    # len of att_partition is numerator 
    # len of current_instanes is denominator
    for att_value, att_partition in partitions.items():
        value_subtree = ["Value", att_value]
        if len(att_partition) > 0 and same_class_label(att_partition):
            print("Case 1: all same class label")
            # CASE 1: all class labels of the partition are the same => make a leaf node
            # MAKE A LEAF NODE HERE 
        elif len(att_partition) > 0 and len(available_attributes) == 0:
            print("Case 2: Clash")
            # CASE 2: no more attributes to select (clash) => handle clash w/majority vote leaf node
        elif len(att_partition) == 0: 
            # CASE 3: no more instances to partition (empty partition) => backtrack and replace attribute node with majority vote leaf node
            print("Case 3: no instances in partition")
            # have to backtrack, overwrite the "tree" above with a leafnode
            tree = ["Leaf"]
        else:
            print("Recurrence")
            subtree = tdidt(att_partition, available_attributes.copy())
            value_subtree.append(subtree)
        if tree[0] != "Leaf":
            tree.append(value_subtree)
    return None


def fit_starter_code():
    # Note the TODO above
    # here would be a good place to programmatically 
    # the header and attribute_domains
    # next I recommend stitchng X_train and y_train together
    # so the class label is at instance [-1]
    train = [X_train[i]+ [y_train[i]] for i in range(len(X_train))]
    available_attributes = header.copy() #tdidt is removing attributes from this as it splits on those attributes
    # pass by obj reference !!
    tree = tdidt(train, available_attributes)
    print("tree:", tree)
    # note that the unit test will assert tree == interview_tree_solution
    pass
fit_starter_code()

def tditd_predict(tree, instance): # finished for project 7
    # are we at a leaf or attribute 
    # leaf is base case
    info_type = tree[0] # either attribute or leaf
    if info_type == "Leaf":
        # base case
        return tree[1] # leaf label (ie True/False/etc...)
    # if here, we are at an attribute
    # we need to figure where in instance, this attribute's val is 
    att_index = header.index(tree[1])
    # loop through all of the value lists looking for a 
    # match to instance[att_index]
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tditd_predict(value_list[2], instance)
    # if here: no match found
    return None



def predict_starer_code(X_test):
    for instance in X_test:
        prediction = tditd_predict(interview_tree_solution, instance)
        print("prediction:", prediction)

X_test = [["Junior", "Java", "yes", "no"],
          ["Junior", "Java", "yes", "yes"],
          ["Intern", "Java", "yes", "no"]  ] # last is outside vals - should return None
y_test_sol = ["True","False", None]
predict_starer_code(X_test)



##################
# Tree Visualization
# create a PDF using the dot program

