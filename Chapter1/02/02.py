from functools import reduce

print(reduce(lambda result, t: (result + t[0] + t[1]), zip('パトカー', 'タクシー'), ''))
