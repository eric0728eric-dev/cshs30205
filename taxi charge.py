km = int(input())
wait = int(input())

meter = km

fare = 85

if meter >= 1500:
	fare += 5
	meter -= 1500
	fare += (meter // 250) * 5

if wait >= 2:
	fare += (wait // 2) * 10

print("NT$: {}".format(fare))