def badge_maker(name):
    return "Hello, my name is " + name + "."

print(badge_maker("Arel"))

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges


def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, start=1):
        room_assignments.append("Hello, {}! You'll be assigned to room {}!".format(name, i))
    return room_assignments


def printer(names):
     # Get badge messages
    badges = batch_badge_creator(names)
    # Print badge messages
    for badge in badges:
        print(badge)
    
    # Get room assignments
    room_assignments = assign_rooms(names)
    # Print room assignments
    for assignment in room_assignments:
        print(assignment)

# Example list of names
speakers = ["Arel", "Carol"]

# Print badges and room assignments for the speakers
printer(speakers)
