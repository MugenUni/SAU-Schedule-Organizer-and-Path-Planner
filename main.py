import re
import heapq
import Term_Project_Campus_Graph as CG

days_dict = {'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday', 'R': 'Thursday', 'F': 'Friday'}
building_dict = {'WIL': 'Wilson', 'BAB': 'Brinson', 'SCI': 'Science', 'AGR': 'Agriculture',
                 'BLN': 'Blanchard', 'BCT': 'Bruce', 'EDU': 'Education', 'ENG': 'Engineering',
                 'OVR': 'Overstreet', 'WNB': 'Warton Nursing Building', 'REY': 'Reynolds',
                 'BPL': 'the big parking lot',
                 'CLK': 'Clocktower', 'MAG': 'Magale Library', 'FNT': 'The Fountain'}


BLUE = "\033[94m"

RESET = "\033[0m"
walking_speed_meters_per_second = 1.2

building_locations = {
    'AGR': (0, 0), 'SCI': (0, 108), 'ENG': (-122, 0),
    'WNB': (-86, 108), 'EDU': (-26, 45), 'OVR': (-141, -141),
    'CLK': (-107, -69), 'BCT': (-208, -65), 'MAG': (65, -97),
    'REY': (-45, -78), 'BAB': (-103, 105), 'WIL': (-302, -84),
    'BLN': (-84, 160), 'FNT': (-105, -126), 'BPL': (-115, 115)
}

compass_directions = {
    'north': 'north',
    'south': 'south',
    'east': 'east',
    'west': 'west',
    'northwest': 'northwest',
    'northeast': 'northeast',
    'southwest': 'southwest',
    'southeast': 'southeast'
}

# Function to determine compass direction based on coordinates
def get_direction(dx, dy):
    if dx == 0:
        return compass_directions['north'] if dy > 0 else compass_directions['south']
    elif dy == 0:
        return compass_directions['east'] if dx > 0 else compass_directions['west']

    # Determine the combination of directions
    horizontal_direction = compass_directions['east'] if dx > 0 else compass_directions['west']
    vertical_direction = compass_directions['north'] if dy > 0 else compass_directions['south']

    # Use combinations for diagonal directions
    return f"{vertical_direction}-{horizontal_direction}"


def calculate_distance_and_time(graph, building1, building2):
    path, cost = find_path(building1, building2)
    if path:
        # Calculate time in minutes
        time_seconds = cost / walking_speed_meters_per_second
        time_minutes = time_seconds / 60
        return f"You will walk a total of {cost} meters. This will take you {time_minutes:.2f} minutes."
    else:
        return "No path found between the specified buildings."

# Define the graph with distances and directions between buildings
direction_graph = {
    'AGR': {'REY': 'east', 'BCT': 'southeast', 'BAB': 'southeast', 'WIL': 'southeast',
            'BPL': 'southeast',  'SCI': 'south', 'BLN': 'southeast'},
    'SCI': {'AGR': 'north', 'BPL': 'east', 'BLN': 'southeast', 'ENG': 'southeast'},
    'ENG': {'SCI': 'northwest', 'WNB': 'southeast', 'BPL': 'northeast', 'BLN': 'east',
            'EDU': 'southeast', 'AGR': 'northwest'},
    'WNB': {'ENG': 'northwest', 'EDU': 'north', 'WIL': 'northeast', 'OVR': 'northeast'},
    'EDU': {'WNB': 'south', 'BLN': 'northwest', 'ENG': 'northwest', 'OVR': 'east',
            'WIL': 'northeast'},
    'OVR': {'WNB': 'southwest', 'EDU': 'west', 'WIL': 'northwest', 'CLK': 'northeast',
            'BCT': 'northeast'},
    'CLK': {'OVR': 'southwest', 'WIL': 'southwest', 'BAB': 'northwest', 'REY': 'northwest',
            'MAG': 'north'},
    'BCT': {'OVR': 'southwest', 'MAG': 'northwest', 'BAB': 'southwest', 'AGR': 'northwest'},
    'MAG': {'BCT': 'southeast', 'CLK': 'south', 'BAB': 'southwest', 'REY': 'west'},
    'REY': {'MAG': 'east', 'CLK': 'southeast', 'BAB': 'south', 'FNT': 'southwest',
            'BPL': 'southwest', 'AGR': 'west'},
    'BAB': {'WIL': 'south', 'FNT': 'southwest', 'BPL': 'west', 'AGR': 'northwest',
            'REY': 'north', 'MAG': 'northeast', 'BCT': 'northeast', 'CLK': 'southeast'},
    'WIL': {'AGR': 'northwest', 'BAB': 'north', 'CLK': 'northeast', 'OVR': 'southeast',
            'WNB': 'southwest', 'EDU': 'southwest', 'BLN': 'west', 'BPL': 'northwest'},
    'BLN': {'WIL': 'east', 'EDU': 'southeast', 'ENG': 'west', 'SCI': 'northwest',
            'FNT': 'north', 'REY': 'northeast', 'AGR': 'northwest'},
    'FNT': {'BAB': 'northeast', 'REY': 'northeast', 'BPL': 'northwest'},
    'BPL': {'FNT': 'southeast', 'ENG': 'southwest', 'SCI': 'west', 'AGR': 'northwest',
            'REY': 'northeast', 'BAB': 'east', 'WIL': 'southeast'},
}

def print_error(message):
    print(f"\033[91mError: {message}\033[0m")

# Function for input validation with a custom prompt
def get_valid_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print_error(error_message)

def validate_num_classes_input(num_classes_input):
    try:
        int(num_classes_input)
        return True
    except ValueError:
        return False

# Function to validate building input
def validate_building_input(building_input):
    return building_input in building_dict

# Function to validate day input
def validate_day_input(day_input):
    return all(day in 'MTWRF' for day in day_input)

# Function to validate time input
def validate_time_input(time_input):
    if time_input.upper() == 'ONL':
        return True
    time_pattern = re.compile(r'^\s*(1[0-2]|0?[1-9]):([0-5][0-9])\s*([APMapm]{2})\s*$')
    return bool(time_pattern.match(time_input))

# Function to validate room number input
def validate_room_number(room_number):
    return room_number.isdigit()

# Function to validate the number of credit hours input
def validate_credit_hours(credit_hours):
    try:
        float(credit_hours)
        return True
    except ValueError:
        return False

# Function to validate the yes/no input
def validate_yes_no_input(response):
    return response.lower() in {'yes', 'no'}

def get_class_schedule():
    schedule = []
    online_classes = []
    total_credit_hours = 0

    num_classes = int(get_valid_input('Enter Your Total Number of Classes: ', validate_num_classes_input, 'Please enter a valid number of classes: '))


    for i in range(num_classes):
        print(f"\nClass {i + 1}:")

        class_name = input("Enter the name of the class: ")
        start_time = get_valid_input("Enter the (00:00 AM/PM) start time (or ONL for online class): ",
                                      validate_time_input, "Invalid time format.")

        if start_time.upper() == 'ONL':
            credit_hours = get_valid_input("Enter the number of credit hours for the online class: ",
                                           validate_credit_hours, "Invalid credit hours.")
            instructor_name = input("Enter the instructor's name for the online class: ")
            online_classes.append((class_name, "N/A", "N/A", "N/A", "Online", "ONL", "N/A", credit_hours, instructor_name))
            total_credit_hours += float(credit_hours)
            continue

        end_time = get_valid_input("Enter the end time (same format): ", validate_time_input, "Invalid time format.")
        room_number = int(get_valid_input("Enter the room number: ", validate_room_number, "Invalid room number."))

        building_name = get_valid_input("Enter the building name (Abbreviated): ",
                                       validate_building_input, "Invalid building abbreviation.")

        days = get_valid_input("Enter the days of the week (in 'MTWRF' format): ",
                               validate_day_input, "Invalid day format.")
        credit_hours = get_valid_input("Enter the number of credit hours: ",
                                       validate_credit_hours, "Invalid credit hours.")
        instructor_name = input("Enter the instructor's name: ")

        if building_name == 'OVR':
            floor = 1 if room_number < 120 else (2 if 120 <= room_number < 201 else (3 if 201 <= room_number < 300 else 4))
        else:
            floor = room_number // 100

        schedule.append((class_name, start_time, end_time, room_number, building_name, days, floor, credit_hours, instructor_name))
        total_credit_hours += float(credit_hours)

    return schedule, online_classes, total_credit_hours

# Function to convert time strings to minutes
def hash_and_sort(schedule):
  hashed = {}
  for i in schedule:
      hashindex = i[2].lower()
      if 'pm' in hashindex:
          hashindex = hashindex.strip(' apm')
          hashindexpart = hashindex.partition(':')
          hashindex = hashindexpart[0] + hashindexpart[2]
          if hashindex.startswith('12'):
              hashindex = int(hashindex)
          hashindex = int(hashindex) + 1200
      else:
          hashindex = hashindex.strip(' apm')
          hashindexpart = hashindex.partition(':')
          hashindex = hashindexpart[0] + hashindexpart[2]
          if hashindex.startswith('12'):
              hashindex = int(hashindex) - 1200
          hashindex = int(hashindex)
      hashed.update({hashindex : i})
  hasheditems = list(hashed.items())
  hasheditems.sort()
  schedule = []
  for i in hasheditems:
      schedule.append(i[1])
  return schedule



def print_class_schedule(schedule, online_classes, total_credit_hours):
    for day in ['M', 'T', 'W', 'R', 'F']:
        print(f"\n{BLUE}{days_dict[day]}:{RESET}")
        day_schedule = [class_info for class_info in schedule if day in class_info[5]]

        if not day_schedule:
            print("  No classes on this day.")
            continue

        # Sort classes within the day by start time
        day_schedule = hash_and_sort(day_schedule)

        for i, (class_info, next_class_info) in enumerate(zip(day_schedule, day_schedule[1:] + [None])):
            class_name, start_time, end_time, room_number, building_name, days, floor, credit_hours, instructor_name = class_info
            print(f"  {class_name} taught by {instructor_name} from {start_time} to {end_time} in room {room_number}, {building_dict[building_name]}, Floor {floor}")

            if next_class_info:
                next_building_name = next_class_info[4]
                distance_and_time_info = calculate_distance_and_time(CG.SAU_Campus.vertices, building_name, next_building_name)
                print(f"    {distance_and_time_info}")

    if online_classes:
        print(f"\n{BLUE}Online Classes:{RESET}")
        for online_class in online_classes:
            print(f"  {online_class[0]} taught by {online_class[8]}")

    print(f"\nTotal Credit Hours: {total_credit_hours}")
    print("\n-----------------------------------------")  # Split line


def find_path(start_building, end_building):
    if start_building in CG.SAU_Campus.vertices and end_building in CG.SAU_Campus.vertices:
        path, cost = shortest_path(CG.SAU_Campus.vertices, start_building, end_building)
    else:
        path = []
        cost = 0.0
        ext = 1
        if start_building + ' ' + str(ext) in CG.SAU_Campus.vertices:
            start_points = []
            while start_building + ' ' + str(ext) in CG.SAU_Campus.vertices:
                start_points.append(start_building + ' ' + str(ext))
                ext += 1
            ext = 1
        else:
            start_points = [start_building]
        if end_building + ' ' + str(ext) in CG.SAU_Campus.vertices:
            end_points = []
            while end_building + ' ' + str(ext) in CG.SAU_Campus.vertices:
                end_points.append(end_building + ' ' + str(ext))
                ext += 1
        else:
            end_points = [end_building]
        signal = False
        for sp in range(len(start_points)):
            for ep in range(len(end_points)):
                if signal:
                    path_chal, cost_chal = shortest_path(CG.SAU_Campus.vertices,
                                                start_points[sp], end_points[ep])
                    if cost_chal < cost:
                        path, cost = path_chal, cost_chal
                else:
                    path, cost = shortest_path(CG.SAU_Campus.vertices,
                                               start_points[sp], end_points[ep])
                signal = True
    return path, cost


def shortest_path(graph, start, end):
    # Priority queue to store (cost, node) tuples
    priority_queue = [(0, start)]

    # Dictionary to track the cost to reach each node
    cost_so_far = {start: 0}

    # Dictionary to track the previous node in the optimal path
    previous = {start: None}
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            # Reconstruct the path if we have reached the destination
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = previous[current_node]
            return path, cost_so_far[end]

        for neighbor, distance in graph[current_node].neighbors.items():
            new_cost = cost_so_far[current_node] + distance

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))

    # If we reach here, there is no path
    return [], float('inf')


def print_path(path, cost):
    print(f"\n{BLUE}Most efficient path going from {path[0]} to {path[-1]}:{RESET}")
    print(path)

    try:
        index = 0
        current_building = path[index]
        while True:
            while 'PVert' in current_building:
                index += 1
                current_building = path[index]
            index += 1
            next_building = path[index]
            while 'PVert' in next_building:
                index += 1
                next_building = path[index]
            current_building = current_building.rstrip(' 1234567890')
            next_building = next_building.rstrip(' 1234567890')
            direction = direction_graph[current_building][next_building]
            print(f"  Head {direction} to {building_dict[next_building].rstrip()}")
            current_building = next_building
    except IndexError:
        pass

    print(f"\n  You will walk a total of {cost:.2f} meters")
    time_seconds = cost / walking_speed_meters_per_second
    time_minutes = time_seconds / 60
    print(f"  This will take you {time_minutes:.2f} minutes")


def ask_for_path():
    response = input("\nWould you like to find a path between two buildings? (yes/no): ").lower()
    if response != 'yes' and response != 'no':
        while response != 'yes' and response != 'no':
            print('Please input a valid response ', end='')
            response = input()
    return response == 'yes'


# Offer to find an efficient path between two buildings
def prompt_for_path():
    while ask_for_path():
        start_building = get_valid_input("Enter the starting building (Abbreviated version): ",
                                            validate_building_input, "Invalid building abbreviation.")
        end_building = get_valid_input("Enter the ending building (Abbreviated version): ",
                                          validate_building_input, "Invalid building abbreviation.")
        path, cost = find_path(start_building, end_building)
        print_path(path, cost)



def main():
    schedule, online_classes, total_credit_hours = get_class_schedule()
    print_class_schedule(schedule, online_classes, total_credit_hours)
    prompt_for_path()
    print("Thank you for using the schedule organizer and path planner!")

# Execute the main program
if __name__ == "__main__":
    main()