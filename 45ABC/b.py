import itertools
def rec (nums,st,step,cot,hugo):
    if st==3:
        if cot == 7:
            print(st+"=7")
    else:

        if hugo > 0:
            temp = "+" + str(nums[st])
            cot += nums[st]
        else:
            temp = "-" + str(nums[st])
            cot -= nums[st]
        rec(nums,st+temp,step+1,cot,1)
        rec(nums, st+temp, step + 1, cot, -1)

