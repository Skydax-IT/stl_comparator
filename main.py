import os
from os import listdir
from os.path import isfile, join
import numpy as np
from stl import mesh
from scipy.spatial import cKDTree
from mpl_toolkits import mplot3d
from matplotlib import pyplot


# List all files available to compare
def show_files(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print("Files available for comparison:", onlyfiles)


# Calculate the volume of a given mesh
def calculate_volume(mesh, indice):
    volume = mesh.get_mass_properties()[0] * 1000000
    print("Volume of mesh", indice, ": ", volume, "cm3")
    

# Calculate the surface area of a given mesh    
def calculate_area(mesh, indice):
    area = mesh.areas.sum() * 10000
    print("Area of mesh", indice, ": ", area, "cm2")
    

# Convert a given mesh into an array of 3D points
def generate_points(mesh):
    points = np.array([point for point in mesh.points])
    return points


# Create a KDTree from a given array of 3D points
def create_KDTree(points_array):
    tree = cKDTree(points_array)
    return tree


# For each 3D points in a given points array find the nearest KDTree neighbor point
def find_nearest_neighbors(tree, points_array):
    distances, indices = tree.query(points_array, k=1)
    return(distances, indices)


# Calculate the mean distance from several distances
def calculate_mean_dist(distances):
    mean_dist = np.mean(distances) * 1000
    print("Mean of distances: ", mean_dist, "mm")
    return mean_dist


# Calculate the standard deviation from several distances
def calculate_std_dist(distances):
    std_dist = np.std(distances) * 1000
    print("Standard deviation: ", std_dist, "mm")
    return std_dist


# Main function
def main():
    
    # Open the directory containing the STL files
    directory = "C:/Users/PSUPP_elicata/OneDrive - ALTEN Group/Documents/stl_comparator/files_to_compare"
    os.chdir(directory)
    show_files(directory)
    
    # Choose the STL files to import
    # file1 = "BelugaOrigin.stl"
    # file2 = "BelugaModified.stl"
    file1 = input("Paste the full name of the file 1: ")
    file2 = input("Paste the full name of the file 2: ")

    # Import the STL files
    mesh1 = mesh.Mesh.from_file(file1)
    mesh2 = mesh.Mesh.from_file(file2)
    
    # Get the volumed of the meshes
    volume_mesh1 = calculate_volume(mesh1, 1)
    volume_mesh2 = calculate_volume(mesh2, 2)
    
    # Get the areas of the meshes
    area_mesh1 = calculate_area(mesh1, 1)
    area_mesh2 = calculate_area(mesh2, 2)
    
    # Generate the points 
    points1 = generate_points(mesh1)
    points2 = generate_points(mesh2)
    
    # Create kd_tree
    kd_tree = create_KDTree(points1)
    
    # Find the nearest neighbor for each point in the first points cloud
    distances, indices = find_nearest_neighbors(kd_tree, points2)
    
    # Calculate the mean distance between the nearest neighbors
    mean_distance = calculate_mean_dist(distances)
    std_distance = calculate_std_dist(distances)
    
    
main()