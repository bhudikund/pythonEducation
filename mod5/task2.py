class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        val = self.start.data
        self.start = self.start.nref
        self.start.pref = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.end is None:
            self.start = Node(val)
            self.end = self.start
        else:
            self.end.nref = Node(val)
            self.end.nref.pref = self.end
            self.end= self.end.nref

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        prefNode = self.start
        for i in range(n-1):
            prefNode = prefNode.nref

        nextNode = prefNode.nref
        newNode = Node(val)

        newNode.nref = nextNode
        newNode.pref = prefNode

        prefNode.nref = newNode
        nextNode.pref = newNode


    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref


test = Queue()
test.push(1)
test.push(2)
test.push(3)
test.insert(1, 4)

test.print()