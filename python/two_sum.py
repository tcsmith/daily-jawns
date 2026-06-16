

def two_sum(nums: list[int], target: int) -> list[int]:
    return two_sum_dict(nums=nums, target=target)

def two_sum_enumerate(nums: list[int], target: int) -> list[int]:
    # does not work, tried to be slick w enumerate
    for i, first in enumerate(nums):
        print(i)
        print(nums[i+1:])
        for j, second in enumerate(nums[i+1:]):
            sum = first + second
            if sum == target:
                return [i, j]
    return []    

def two_sum_idx(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_dict(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    # we can do O(n) if we see the current number and we have seen the diff
    # num = 2, target = 9, have we seen 7? nope
    for i, n in enumerate(nums):
        compliment = target - n
        if compliment in seen:
            return [seen[compliment], i]
        seen[n] = i
    return []
    

def main():
    print(two_sum(nums=[2, 7, 11, 15], target=9))
    print(two_sum(nums=[3, 2, 4], target=6))
    print(two_sum(nums=[3, 3], target=6))



if __name__ == "__main__":
    main()