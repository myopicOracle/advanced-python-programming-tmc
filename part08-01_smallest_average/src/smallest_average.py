# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict) -> dict: 
    person_list = [person1, person2, person3]
    smallest_average = 0
    track_person = 0
    
    # calculate average with loop
    for index, person in enumerate(person_list):
        sum = person["result1"] + person["result2"] + person["result3"]
        avg = sum / 3

        if index == 0:
            smallest_average = avg
            track_person = index
        else:
            if avg < smallest_average:
                smallest_average = avg
                track_person = index 
    
    return person_list[track_person]

    
# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))
