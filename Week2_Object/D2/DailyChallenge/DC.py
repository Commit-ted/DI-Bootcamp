class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)
        self.currentPage = 1

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self
    

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

# Get the visible items on the current page (Page 1)
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']

# Move to the next page and get visible items
p.nextPage()
print(p.getVisibleItems())  # Output: ['e', 'f', 'g', 'h']

# Move to the last page and get visible items
p.lastPage()
print(p.getVisibleItems())  # Output: ['y', 'z']

# Move to a specific page (Page 2) and get visible items
p.goToPage(2)
print(p.getVisibleItems())  # Output: ['e', 'f', 'g', 'h']

# Move to an invalid page number (greater than total pages)
p.goToPage(10)
print(p.getVisibleItems())  # Output: ['y', 'z']

# Move to an invalid page number (less than 1)
p.goToPage(-1)
print(p.getVisibleItems())  # Output: ['a', 'b', 'c', 'd']

p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
