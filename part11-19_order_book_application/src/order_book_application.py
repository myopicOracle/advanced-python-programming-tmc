# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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


class OrderBookApplication: 
    def __init__(self):
        self.orderbook = OrderBook()

    def print_help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")


    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ")
        parts = programmer_and_workload.split()
        if len(parts) != 2 or not parts[1].isdigit():
            print("erroneous input")
            return
        programmer = parts[0]
        workload = int(parts[1])
        self.orderbook.add_order(description, programmer, workload)
        print("added!")

    def finished_orders(self):
        orders = self.orderbook.finished_orders()
        if len(orders) == 0: 
            print("no finished tasks")
        else:
            for order in self.orderbook.finished_orders():
                print(order)

    def unfinished_orders(self):
        orders = self.orderbook.unfinished_orders()
        if len(orders) == 0: 
            print("no finished tasks")
        else:
            for order in self.orderbook.unfinished_orders():
                print(order)

    def mark_finished(self):
        id_input = input("id: ")
        if not id_input.isdigit() or int(id_input) not in [order.id for order in self.orderbook.orders_list]:
            print("erroneous input")
            return
        id = int(id_input)
        self.orderbook.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        programmers_list = self.orderbook.programmers()
        for programmer in programmers_list:
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        if programmer not in self.orderbook.programmers():
            print("erroneous input")
            return
        status_tuple = self.orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {status_tuple[0]} not finished {status_tuple[1]}, hours: done {status_tuple[2]} scheduled {status_tuple[3]}")

    def execute(self):
        self.print_help()
        while True:
            command = int(input("command: "))
            if command == 1:
                self.add_order()
            elif command == 2: 
                self.finished_orders()
            elif command == 3: 
                self.unfinished_orders()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.status_of_programmer()
            elif command == 0: 
                break 


app = OrderBookApplication()
app.execute()