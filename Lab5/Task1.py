class Node:
    def __init__(self, data):
        self.next_node = None
        self.data = data

class MyQueue:

    def __init__(self):
        self.head = None
    

    def add(self, new_node):
        new_node.next_node = self.head
        self.head = new_node


    # Удаляет первый добавленный в очередь элемент
    def remove(self):
        temp_head = self.head
        prev_node = None
        while self.head.next_node != None:
            prev_node = self.head
            self.head = self.head.next_node
        prev_node.next_node = None
        self.head = temp_head


    def to_list(self)->list:
        temp_head = self.head
        return_list = []
        while self.head.next_node != None:
            return_list.append(self.head.data)
            self.head = self.head.next_node
        return_list.append(self.head.data)
        self.head = temp_head
        return_list.reverse()
        return return_list


    def clear(self):
        self.__init__()


    # def show_node(self)->str:
    #     if self.head != None:
    #         return self.head.data
    #     else:
    #         return None

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    

    def __str__(self):
        return "Name : " + str(self.name) + ", Population : " + str(self.population)



# Очередь для чисел
q1 = MyQueue()
q1.add(Node(10))
q1.add(Node(11))
q1.add(Node(12))
q1.add(Node(13))
# Вывод данных из очереди
for i in q1.to_list():
    print(i.__str__())

# Очередь для стран
q2 = MyQueue()
q2.add(Node(Country("Name", 123)))
q2.add(Node(Country("USA", 321)))
# Вывод данных из очереди
for i in q2.to_list():
    print(i.__str__())
