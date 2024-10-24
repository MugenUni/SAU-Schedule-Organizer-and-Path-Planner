# SAU-Schedule-Organizer-and-Path-Planner
This project was developed for the Fall 2023 Data Structures and Algorithms course at Southern Arkansas University (SAU) as a group assignment. The main purpose of the project is to help students organize their class schedules and navigate the SAU campus efficiently by finding the shortest paths between buildings.

## Table of Contents
 * [Requirements](#requirements)
 * [Features](#features)
 * [Files](#files)
 * [How It Works](#how-it-works)
 * [My Contribution](#my-contribution)
 * [Technologies Used](#technologies-used)
 * [Possible Future Enhancements](#possible-future-enhancements)
 * [Getting Started](#getting-started)
## Requirements
To run this project, you will need the following:

* **Python 3.6 (or higher)**: Ensure that Python 3.6 or higher is installed on your system. You can download it from python.org.
* **Libraries**: The program uses standard Python libraries such as:
  * `re` (for regular expressions)
  * `heapq` (for priority queue implementation in Dijkstra’s algorithm)
You can install any missing libraries using `pip`.

## Features
* **Class Schedule Organizer**: The program allows users to input their weekly class schedule and organizes it chronologically for each day of the week.

* **Shortest Path Finder**: After organizing the schedule, the program can calculate the shortest walking path between any two buildings on campus. It provides detailed route directions, including:
  * Distance (in meters)
  * Estimated walking time
  * Cardinal directions

* **Graph Representation of Campus**: The SAU campus is represented as a graph, with buildings as vertices and walkable paths as edges. The graph was manually constructed to reflect actual campus paths.
## Files
* `TermProject2.py`: The main file containing the core logic for the class schedule organizer and pathfinding functions. This file also handles user input and output.
* `Term_Project_Campus_Graph.py`: This file defines the graph structure of the SAU campus. It includes all the buildings and paths used by the pathfinding algorithm.
* **Images (Optional)**: Visual representations of the campus layout and graph structure.
## How It Works
1. The user inputs their class schedule, including details such as:
    * Class names
    * Instructor name
    * Days of the week
    * Start and end times
    * Building and room locations
    * Credit Hours
2. The schedule is displayed in chronological order for each day of the week.
3. The user is prompted to find the shortest path between any two buildings. The program:
    * Takes input for the starting and destination buildings.
    * Calculates the shortest path using Dijkstra's algorithm.
    * Displays the walking distance, time estimate, and directions.
4. The user can repeat the pathfinding process until they choose to exit.
## My Contribution
In this project, I contributed by:

* **Creating the Campus Graph**: I manually constructed the graph that represents the buildings and walkable paths on the SAU campus.
* **Integrating the Graph into the Main Program**: I ensured the graph was properly integrated with the main program's pathfinding functionality.
## Technologies Used
* **Python**: The core programming language for the project.
* **Data Structures**: The project extensively uses graphs and priority queues (heap) to represent the campus and find the shortest paths.
* **Algorithms**: Dijkstra's algorithm is implemented to compute the shortest path between two campus buildings.
## Possible Future Enhancements
* **Real-Time Data Integration**: Add GPS support to track user movements and suggest real-time paths.
* **Campus Map Overlay**: Display the path on a visual map of the SAU campus.
* **Accessibility Enhancements**: Incorporate support for elevators and ramps for individuals with mobility issues.
## Getting Started
To run the project:

1. Clone this repository.
2. Run `TermProject2.py` in a Python environment.
3. Follow the prompts to enter your schedule and find campus paths.
