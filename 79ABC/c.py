import itertools
def rec (nums,st,step,cot,hugo):
    if step==4:
        if cot == 7:
            print(st+"=7")
            exit()
    else:

        if hugo > 0:
            temp = "+" + str(nums[step])
            cot += nums[step]
        else:
            temp = "-" + str(nums[step])
            cot -= nums[step]
        rec(nums,st+temp,step+1,cot,1)
        rec(nums, st+temp, step + 1, cot, -1)


def do():
    nums = list(map(int,list(input())))
    rec(nums,str(nums[0]),1,nums[0],1)
    rec(nums,str(nums[0]),1,nums[0],-1)


if __name__ == "__main__":
    do()