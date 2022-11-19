# 1
FirstArray = [7, 5, 10, 14, 3, 9, 7]
SecondArray = [9, 10, 3, 4, 2, 5, 7, 1]
# 2
print("First array length:", len(FirstArray))
print("Second array length:", len(SecondArray))
# 3
FirstArray.insert(0, 15)
# 4
print("7 found in first araay at index:", FirstArray.index(7))
print("7 found in second araay at index:", SecondArray.index(7))
# 5
FirstArray.append(1)
SecondArray.append(14)
# 6
ThirdArray = FirstArray.copy()
# 7
ThirdArray.extend(SecondArray)
# 8
print("Third array count of 7:", ThirdArray.count(7))
# 9
ThirdArray.sort()
# 10
ThirdArray.remove(7)
# 11
FourthArray = ThirdArray.copy()
# 12
FourthArray.reverse()
# 13
print("Thrid array:", ThirdArray)
print("Fourth array:", FourthArray)
