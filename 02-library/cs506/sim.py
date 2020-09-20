def euclidean_dist(x, y):
    if len(x) != len(y):
        raise ValueError('lengths must be equal')
    elif x == [] or y == []:
        raise ValueError('lengths must not be zero')
    distance_components = [0 for num in range(len(x))]
    for i in range(len(x)):
        distance_components[i] = (x[i] - y[i])**2
    return sum(distance_components)**0.5

def manhattan_dist(x, y):
    if len(x) != len(y):
        raise ValueError('lengths must be equal')
    elif x == [] or y == []:
        raise ValueError('lengths must not be zero')
    distance_components = [0 for num in range(len(x))]
    for i in range(len(x)):
        distance_components[i] = abs(x[i] - y[i])
    return sum(distance_components)

def jaccard_dist(x, y):
    if len(x) != len(y):
        raise ValueError('lengths must be equal')
    elif x == [] or y == []:
        raise ValueError('lengths must not be zero')
    union = len(x)
    intersection = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            intersection += 1
    return 1 - intersection / union


def cosine_sim(x, y):
    if len(x) != len(y):
        raise ValueError('lengths must be equal')
    elif x == [] or y == []:
        raise ValueError('lengths must not be zero')
    x_length = sum([num**2 for num in x])**0.5
    y_length = sum([num**2 for num in y])**0.5
    if x_length == 0 or y_length == 0:
        raise ValueError('lengths must not be zero')
    inner_product = sum([x[i] * y[i] for i in range(len(x))])
    cosine_val = inner_product / (x_length * y_length)
    return cosine_val

# Feel free to add more
