amount = eval(input())

nowAmount = int(amount * 100)

num_100 = nowAmount // 100
nowAmount %= 100

num_25 = nowAmount // 25
nowAmount %= 25

num_10 = nowAmount // 10
nowAmount %= 10

num_5 = nowAmount // 5
nowAmount %= 5

num_1 = nowAmount

print("dollars:", num_100, '\n', "quarters:", num_25, '\n', "dimes:", num_10, '\n',
      "nickels:", num_5, '\n', "pennies:", num_1, '\n')
