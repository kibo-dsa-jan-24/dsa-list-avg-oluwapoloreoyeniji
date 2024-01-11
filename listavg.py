class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = 0
        for i in self.lst:
            self.total += i

    def add(self, num):
        self.lst.append(num)
        self.total += num

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        return self.total / len(self.lst)
    
### getting the length once will def reduce the time as no more time/memory is spent on doing that

# sample usage
# my_list = ListAverage([1, 2, 3])
# my_list.add('d')
# print(my_list.lst)