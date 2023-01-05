class TooSmallCapacity(Exception):
    def __str__(self):
        return "Message capacity should be bigger than header capacity"
