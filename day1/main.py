import re
with open("input.txt","r") as file:
    input = file.read()
input = input.split("\n")
def part1():
    answer = []
    for index, x in enumerate(input):
        if x == "":            
            break
        res = [int(i) for i in x if i.isdigit()]
        answer.append(int(str(res[0]) + str(res[-1])))
    num = 0
    for x in answer: 
        try:
            if str(x)[1]:
                pass
            num += x
        except: num += int(str(x) + str(x))
    print(num)

def part2():
    answer =[]
    for x in input:
        if x == "":
            break
        wordtoint = {"one":1,"two":2,"three":3,"four":4,
                      "five":5,"six":6,"seven":7,"eight":8,"nine":9}
        nums = []
        nums = re.findall(r"([1-9]|one|two|three|four|five|six|seven|eight|nine)",x, flags=re.IGNORECASE)
        for  index, z in enumerate(nums):
            if z.isdigit():
                z = int(z)
                nums[index] = z
            else:
                nums[index] = wordtoint[z]
        answer.append(int(str(nums[0]) + str(nums[-1])))
    num = 0
    for x in answer:
        num += x
    print(num)
if __name__ == "__main__":
#     part1()
     part2()
