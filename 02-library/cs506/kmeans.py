from collections import defaultdict
from math import inf
import random
import csv

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    for point in points:
        if point == [] or (len(point) != len(points[0])):
            raise ValueError()
    # Set up a list to hold the coordinates of the new center
    center_coords = [0 for dim in range(len(points[0]))]
    for i in range(len(center_coords)):
        center_coords[i] = sum([point[i] for point in points]) / len(points)
    return center_coords


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = max(assignments) + 1
    new_centers = []
    # For each group of assignments to a single center, calculate the new center for that set of points
    for i in range(k):
        points_nearby = [dataset[j] for j in range(len(dataset)) if assignments[j] == i]
        new_centers.append(point_avg(points_nearby))
    return new_centers


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    if type(a) == int or type(b) == int:
        if type(a) == type(b):
            return abs(a - b)
        # If one of the points passed in is 0, turn it into the n-dimensional zero vector
        elif a == 0:
            a = [0 for i in range(len(b))]
        elif b == 0:
            b = [0 for i in range(len(a))]
        else:
            raise ValueError('lengths must be equal')
    # This part is copied from my sim.py for the first part of Workshop 2
    if len(a) != len(b):
        raise ValueError('lengths must be equal')
    elif a == [] or b == []:
        raise ValueError('lengths must not be zero')
    distance_components = [0 for num in range(len(a))]
    for i in range(len(a)):
        distance_components[i] = (a[i] - b[i])**2
    return sum(distance_components)**0.5

def distance_squared(a, b):
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # Check for an empty dataset
    if dataset == []:
        raise ValueError()
    # Check for a dataset with arrays of different lengths
    length_elem_0 = len(dataset[0])
    for point in dataset:
        if len(point) != length_elem_0:
            raise ValueError()
    # Return k randomly selected points
    selected_points = []
    next_point = []
    for i in range(k):
        next_point = random.choice(dataset)
        # Avoid repetition in the points selected: if we choose a point from
        # the dataset which is already in the list of chosen random points,
        # we need to try again
        while next_point in selected_points:
            next_point = random.choice(dataset)
        selected_points.append(next_point)
    return selected_points

def cost_function(clustering):
    clusters = list(clustering.keys())
    intra_cluster_distances = []
    for i in range(len(clusters)):
        current_cluster = clusters[i]
        current_center = point_avg(clustering[current_cluster])
        single_cluster_cost = sum([distance_squared(current_center, \
            clustering[current_cluster][j]) for j in range(len(clustering[current_cluster]))])
        intra_cluster_distances.append(single_cluster_cost)
    return sum(intra_cluster_distances)


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    # Check for an empty dataset
    if dataset == []:
        raise ValueError()
    # Check for a dataset with arrays of different lengths
    length_elem_0 = len(dataset[0])
    for point in dataset:
        if len(point) != length_elem_0:
            raise ValueError()
    # Pick the very first point
    starting_points = []
    current_point = random.choice(dataset)
    starting_points.append(current_point)
    # Pick the other k-1 centers by the proper procedure
    for i in range(k-1):
        # Set up an array containing all points which are not already centers
        non_centers = []
        for j in range(len(dataset)):
            if dataset[j] not in starting_points:
                non_centers.append(dataset[j])
        # For each non-center point, calculate the sum of squared distances to all current centers
        dist_from_starting_points = [0 for j in range(len(non_centers))]
        for j in range(len(non_centers)):
            dist_from_starting_points[j] = sum([distance_squared(starting_points[m],non_centers[j]) for m in range(len(starting_points))])
        # Find the sum of squared distances for the purposes of selecting one point,
        # then pick a random number on (O, sum_of_squares)
        sum_of_squares = sum(dist_from_starting_points)
        rand_num = random.uniform(0,sum_of_squares)
        # One point at a time, figure out if that point is the one we selected with our random number:
        # If the random number is between the sum of the first m-1 squared distances
        # and the sum of the first m, then the m^th point is being selected
        for m in range(len(non_centers)):
            if rand_num <= sum(dist_from_starting_points[0:m+1]):
                current_point = dataset[m]
                starting_points.append(current_point)
                break
    return starting_points


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
