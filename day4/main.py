# read input
with open('./input.txt','r') as f:
    file = f.read()
    file = file.split("\n")
    if file[-1] == '': file.pop(-1);
# line by line find the winning numbers
anser = 0
for x in file:
    line_num = 0
    x = x.split(':')[1]
    nums = x.split(' | ')
    win_nums = nums[1].split(' ')
    #num = nums[0].split(' ')
    num = [i for i in nums[0].split(' ') if i != ''] 
    for x in num:
        if x in win_nums:
            is_in = 1
        else:
            is_in = 0
        line_num += is_in
        print(f'{x} is in {is_in}')
    print(line_num)
    if line_num > 1:
        s = 1
        for x in range(line_num-1):
            s = s *2
        anser += s
    elif line_num > 0:
        anser +=1
print(anser)
# frist number is 1 pont the rest doble it
