
def countWays(cfg, nums, flag=False): 
    if len(cfg) == 0:
        return 1 if sum(nums) == 0 else 0
    
    if sum(nums) == 0:
        return 0 if "#" in cfg else 1
    
    if cfg[0] == "#":
        if flag and nums[0] == 0:
            return 0
        return countWays(cfg[1:], (nums[0] - 1, *nums[1:]), True)
    
    if cfg[0] == ".":
        if flag and nums[0] > 0:
            return 0
        return countWays(cfg[1:], nums[1:] if nums[0] == 0 else nums, False)
    
    if flag:
        if nums[0] == 0:
            return countWays(cfg[1:], nums[1:], False)
        return countWays(cfg[1:], (nums[0] - 1, *nums[1:]), True)
    
    return countWays(cfg[1:], nums, False) + countWays(cfg[1:], (nums[0] - 1, *nums[1:]), True)
    

def solution(filename):
    result = 0
    
    with open(filename) as input:
        for line in input:
            config, nums = line.split()
            nums = tuple(map(int,nums.split(",")))
            result += countWays(config, nums)

    return result


if __name__ == '__main__':
    print(solution('2023/day-12/input.txt'))
