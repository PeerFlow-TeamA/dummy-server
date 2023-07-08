class SortValueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    
class CategoryValueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message