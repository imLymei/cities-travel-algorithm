cities = []

MOVEMENT_ARRAY =[################   Direção das cidades em diagonal:
[0,0,0,0,0,0],  #--5-------0----#
[0,0,1,0,0,0],  #--\|-----/|----#           5 -> 1
[0,0,0,0,1,0],  #---1->2->4-----#           3 -> 2
[0,0,1,0,1,0],  #------|\/|-----#           3 -> 4
[1,0,0,0,0,0],  #-------3-------#           4 -> 0
[0,1,0,0,0,0]   #################
]

class Cidade:
    def __init__(self,city_id):
        self.id = city_id
        self.next = []


    def go_to(self,goal_city,initial_distance = 0):
        smaller_distance = 6
        if self.id == goal_city:
            return initial_distance

        for next_city in self.next:
            distance = initial_distance
            distance += 1
            new_distance = cities[next_city].go_to(goal_city,distance)
            if new_distance < smaller_distance:
                smaller_distance = new_distance

        return smaller_distance
        

def iniciar_cidades():
    new_city = None
    city_id = 0

    print('Cities map:\n')

    for city in MOVEMENT_ARRAY:
        new_city = Cidade(city_id)
        cities.append(new_city)
        next_city_id = 0

        for possible_city in city:
            if possible_city == 1:
                new_city.next.append(next_city_id)
            next_city_id += 1

        if new_city.next != []:
            print(f'City {new_city.id} can go to {new_city.next}.')
        else:
            print(f'City {new_city.id} can not go to another city.')
        city_id += 1

    print('')


def go_from_to(start_city,final_city):
    final_distance = cities[start_city].go_to(final_city)

    if final_distance == 6:
        print(f"You can't reach city {final_city} from city {start_city}.")
    else:
        print(f"The shortest distance between city {start_city} and city {final_city} is {final_distance} units.")


iniciar_cidades()

go_from_to(5, 2)
