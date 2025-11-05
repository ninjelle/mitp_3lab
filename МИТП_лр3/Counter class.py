class Counter:
    
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def increment(self, step=1):
        self.value += step
        return self.value
    
    def decrement(self, step=1):
        self.value -= step
        return self.value
    
    def get_value(self):
        return self.value
    
    def reset(self, new_value=0):
        self.value = new_value
        return self.value
    
    def __str__(self):
        return f"Current value={self.value}"


if __name__ == "__main__":

    counter = Counter()
    print(f"Start value: {counter.get_value()}")

    counter.increment()
    print(f"After increment(): {counter.get_value()}")
    
    counter.increment(5)
    print(f"After increment(5): {counter.get_value()}")

    counter.decrement(2)
    print(f"After decrement(2): {counter.get_value()}")
    
    counter.decrement()
    print(f"After decrement(): {counter.get_value()}")

    counter.reset()
    print(f"After reset(): {counter.get_value()}")
    
    counter.reset(10)
    print(f"After reset(10): {counter.get_value()}")
    
    print(f"\n{counter}")
