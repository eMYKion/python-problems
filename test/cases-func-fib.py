seq = [0, 1]
n = 30
nums = int(n)
while (nums > 0):
    seq.append(seq[-1]+seq[-2])
    nums -= 1


cases = {
    i: ((i,),seq[i]) for i in range(n)
}
