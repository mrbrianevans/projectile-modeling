"""This module modules projectile motion"""

import math
import time

import matplotlib.pyplot as plt


def distance_traveled(angle, initial_velocity, starting_height=0):
    """This function calculates the distance travelled by a projectile"""

    initial_vertical_velocity = initial_velocity * math.sin(math.radians(angle))
    initial_horizontal_velocity = initial_velocity * math.cos(math.radians(angle))

    vertical_acceleration = -9.8
    vertical_distance_travelled = -starting_height

    # quadratic for s = ut + 0.5at^2
    a = 0.5 * vertical_acceleration
    b = initial_vertical_velocity
    c = -vertical_distance_travelled
    d = (b ** 2) - (4 * a * c)

    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)

    time_of_flight = max(sol1, sol2)

    # Horizontal distance calculated using time of flight
    horizontal_distance_travelled = initial_horizontal_velocity * time_of_flight

    return horizontal_distance_travelled


def max_height(angle, initial_velocity, starting_height=0):
    initial_vertical_velocity = initial_velocity * math.sin(math.radians(angle))
    height = initial_vertical_velocity ** 2 / 19.6 + starting_height
    return height


def graph_projectile(angle, initial_velocity, starting_height=0, unit_of_time: float = 0.01):
    """
    This function graphs the tragectory of a projectile
    Args:
        angle: the angle of the initial projection
        initial_velocity: the velocity of the initial projection
        starting_height: the starting height of the projectile
    """
    initial_vertical_velocity = initial_velocity * math.sin(math.radians(angle))
    horizontal_velocity = initial_velocity * math.cos(math.radians(angle))

    x = 0
    y = starting_height
    gravity_velocity = 0

    x_points = [x]
    y_points = [y]

    plt.plot(x_points, y_points)
    axis_limits = [0, distance_traveled(angle, initial_velocity, starting_height) + 1,
                   starting_height, max_height(angle, initial_velocity, starting_height) + 1]
    axis_limits = [0, 100, 0, 100]  # fixed axis for all graphs
    print('axis limits', axis_limits)
    time_of_flight = 0
    while y >= 0:
        # run the simulation for 1 second
        x += horizontal_velocity * unit_of_time
        y += gravity_velocity + initial_vertical_velocity * unit_of_time
        gravity_velocity -= 9.8 * (unit_of_time ** 2)
        time_of_flight += unit_of_time

        # graph the projectile
        x_points.append(x)
        y_points.append(y)
    plt.plot(x_points, y_points)
    plt.axis(axis_limits)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.show()

    print('Time of flight:', time_of_flight)
    print('Max height should be:', max_height(angle, initial_velocity))
    print('Measured max height:', max(y_points))
    print('Horizontal distance traveled should be:', distance_traveled(angle, initial_velocity))
    print('Measured horizontal distance traveled:', x)
    return x_points, y_points


graph_projectile(45, 30, 0, 0.01)


def largest_possible_distance(initial_velocity):
    data = list()
    for i in range(5, 46, 5):
        data.extend(graph_projectile(i, initial_velocity))

    plt.plot(*(tuple(data)))
    plt.axis([0, 100, 0, 100])
    plt.show()


def longest_distances_test():
    speeds = list()
    distances = list()
    for i in range(30):
        distances.append(largest_possible_distance(i))
        speeds.append(i)
    plt.plot(speeds, distances)
    plt.axis([0, 100, 0, 100])
    plt.show()


largest_possible_distance(30)
