from interfaces import SingletonMeta, IO

def insertion_sort(object_list: list) -> list:
    try:
        for x in range(1, len(object_list), 1):
            current = object_list[x]
            y = x - 1

            while(y >= 0 and int(object_list[y][1]) > int(current[1])):
                object_list[y + 1] = object_list[y]
                y -= 1
                
            object_list[y + 1] = current
            
        return object_list
    except Exception:
        raise Exception

# Applying the Singleton design pattern in order to "test" ways to code this practice.
class Users(metaclass=SingletonMeta):
    def __init__(self, input: IO) -> None:
        self.__users = self.__create_users_list(input)
    
    def __create_users_list(self, input: IO) -> list:
        users = []
        for line in input.Read().split('\n'):
            aux = line.split(' ')
            users.append(
                [aux[0], aux[1]]
            )

        users = insertion_sort(users)

        return users

    def siguiente_usuario(self) -> list:
        return self.__users.pop(0)[0]