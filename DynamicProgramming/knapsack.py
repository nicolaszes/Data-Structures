# 背包问题
def m(i, j):
  '''
  形参i：背包中可存物品数量
  形参j：背包剩余容量
  返回值：当前最优值
  '''
  if i == -1 or j == 0:
    return 0

  if j >= w[i]:
    m1 = m(i - 1, j) #能装但不装
    m2 = m(i - 1, j - w[i]) + v[i] #装
    # print(w[i], v[i], m1, m2)
    if m1 > m2:
      return m1
    else:
      return m2

  return m(i - 1, j) #不能装

w = [2, 1, 3, 2, 2] #重量
v = [12, 10, 20, 15, 18] #价值
print(m(3, 8))