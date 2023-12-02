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
        wordCombo = {'fiveight':[5,8],'sevenine':[7,9],'oneight':[1,8],'twone':[2,1],'threeight':[3,8],'nineight':[9,8],'eightwo':[8,2],'eighthree':[8,3]}
        wordtoint = {"one":1,"two":2,"three":3,"four":4,
                      "five":5,"six":6,"seven":7,"eight":8,"nine":9}
        numlist = ['one','two','three','four','five','six','seven','eight','nine']
        nums = []
        nums = re.findall(r"(oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|\d|one|two|three|four|five|six|seven|eight|nine)",x, flags=re.IGNORECASE)
        for index, z in enumerate(nums):
            if str(z).isdigit():
                z = int(z)
                nums[index] = z
            elif z in wordCombo:
                nums[index] = wordCombo[z][0]
                nums.insert(index+1,wordCombo[z][1])
            else:
                nums[index] = wordtoint[z]
        answer.append(int(str(nums[0]) + str(nums[-1])))
    num = 0
    for x in answer: 
        try:
            if str(x)[1]:
                pass
            num += x
        except: 
            num += int(str(x) + str(x))
    print(num)
if __name__ == "__main__":
     part1()
     part2()
