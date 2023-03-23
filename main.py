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

    print('\nCities map:\n')

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
    print("\n--------------------------------------\n")

    if final_distance == 6:
        print(f"You can't reach city {final_city} from city {start_city}.\n")
    else:
        print(f"The shortest distance between city {start_city} and city {final_city} are {final_distance} move.\n")

    print("--------------------------------------\n")


def main_menu():
    response = 0

    while response != '2':
        print('       Chose one option:')
        print('(1) Go from one city to another')
        print('   (2) Stop the application\n')

        response = input()
        
        match response:
            case '1':
                print("--------------------------------------\n")
                iniciar_cidades()
                start_city = int(input('Chose the starting city: '))
                final_city = int(input('Chose the destination city: '))
                go_from_to(start_city, final_city)
            case '2':
                print("--------------------------------------\n")
            case _:
                print('Invalid\n')
                print("--------------------------------------\n")

if __name__ == '__main__':
    main_menu()
