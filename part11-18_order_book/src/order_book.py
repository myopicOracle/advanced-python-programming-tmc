# Write your solution here:

class Task: 
    id_counter = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.description = description
        self.programmer = programmer 
        self.workload = workload
        self.status = False

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.status == True else 'NOT FINISHED'}"

    def is_finished(self):
        return self.status

    def mark_finished(self):
        self.status = True
    

class OrderBook:
    def __init__(self):
        self.orders_list = []

    def add_order(self, description: str, programmer: str, workload: int):
        new_order_obj = Task(description, programmer, workload)
        self.orders_list.append(new_order_obj)

    def all_orders(self):
        return self.orders_list

    def programmers(self):
        return list(set([order.programmer for order in self.orders_list]))

    def mark_finished(self, id: int):
        if id not in [order.id for order in self.orders_list]:
            raise ValueError("order id not found")
        else:
            [order.mark_finished() for order in self.orders_list if order.id == id]

    def finished_orders(self):
        return [order for order in self.orders_list if order.status == True]

    def unfinished_orders(self):
        return [order for order in self.orders_list if order.status == False]

    def status_of_programmer(self, programmer: str):
        if programmer not in [order.programmer for order in self.orders_list]:
            raise ValueError("programmer not found")
        else:        
            finished = [order for order in self.finished_orders() if order.programmer == programmer]
            unfinished = [order for order in self.unfinished_orders() if order.programmer == programmer]
            return (len(finished), len(unfinished), sum([order.workload for order in finished]), sum([order.workload for order in unfinished]))


# # Part 1
# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t2)
# print(t3)

# # Part 2
# my_list = [1,1,3,6,4,1,3]
# my_list2 = list(set(my_list))
# print(my_list)
# print(my_list2)

# # Part 3
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# orders.mark_finished(1)
# orders.mark_finished(2)
# orders.mark_finished(10)

# for order in orders.all_orders():
#     print(order)

# Part 4
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# status = orders.status_of_programmer("Adele")
# print(status)
