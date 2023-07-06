def twoSum(nums: list[int], target: int) -> list[int]:
      resultmap = {}
      for i, num in enumerate(nums):
          if target - num in resultmap:
              return [resultmap[target-num], i]
          resultmap[num] = i

