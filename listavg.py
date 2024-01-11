class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.length = len(lst)

    def add(self, num):
        self.lst.append(num)

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        # implement this method
        return 
    
### getting the length once will def reduce the time as no more time/memory is spent on doing that
