
S = ""

def rec(nums,step,N): #step → + を挿入する場所

    if step == N:
        nums = list(map(int,nums))
        return sum(nums)

    else:
        num = S[step]
        nums2 = nums[::]
        nums2[-1] += num
        nums.append(num)
        return rec(nums,step+1,N) + rec(nums2,step+1,N)
        #+を入れたパターン#+を入れなかったパターン



def func():
    global S
    S = input()
    N =len(S)
    print(rec([S[0]],1,N))

if __name__ == '__main__':
    func()