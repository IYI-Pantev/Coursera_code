def number_increment(numbers):
    def increase():
        new_nums = [i+1 for i in numbers]
        return new_nums
    return increase()

print(number_increment([1, 2, 3]))