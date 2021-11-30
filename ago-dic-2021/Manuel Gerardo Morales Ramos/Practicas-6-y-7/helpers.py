def insertion_sort(object_list: list) -> list:
    try:
        for x in range(1, len(object_list), 1):
            current = object_list[x]
            y = x - 1

            while(y >= 0 and int(object_list[y][1]) < int(current[1])):
                object_list[y + 1] = object_list[y]
                y -= 1
                
            object_list[y + 1] = current
            
        return object_list
    except Exception:
        raise Exception
