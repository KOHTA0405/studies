 # Closure: 状態を保持したままの関数を作ることができる

def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power  ## power関数の戻り値として、exponentが固定されたinner_powerが返される


power_four_func = power(4)
# print(power_four_func(3))


# 状態が動的な場合
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))