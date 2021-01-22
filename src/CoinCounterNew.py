# 穷举法
def select_coin_1(coin_value, total_value):
    min_coin_num = [0]
    for i in range(1, total_value + 1):
        min_coin_num.append(float('inf'))
        for value in coin_value:
           if value <= i and min_coin_num[i - value] + 1 < min_coin_num[i]:
               min_coin_num[i] = min_coin_num[i - value] + 1
    return min_coin_num[-1]

# 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元
# 递归法
def select_coin(coin_value, total_value):
    if total_value == 0:
        return 0
    if total_value == 1:
        return 1
    min_coin_num = [0]
    maxUsableValue = 0
    for value in coin_value:
        if value <= total_value and value > maxUsableValue:
            maxUsableValue = value
    min_coin_num[-1] = total_value // maxUsableValue
    left_value = total_value - min_coin_num[-1] * maxUsableValue
    if left_value > 0:
        min_coin_num.append(select_coin(coin_value, left_value))
    return sum(min_coin_num)

result = select_coin([1, 3, 5], 11)
print("coin number:" + str(result))
