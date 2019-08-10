num = 0
divi = 1
def prime(nums):
    global divi
    divi += 1
    for i in range(2, nums):
        if nums % i == 0:
            return None

    print(nums)
while True:
    num += 1
    prime(num)
