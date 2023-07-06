def solution(sequence):
      bad_num= 0
      for i in range(1, len(sequence)):
            if(sequence[i] <= sequence[i-1]):
              bad_num += 1
      if (bad_num > 1):
           return False
      elif(sequence[i] <= sequence[i-2] and sequence[i+1]<= sequence[i-1]):
           return False
      else:
           return True

                  

if __name__ == "__main__":
      # print(solution([1,3,2,1]))
      # print(solution([1,3,2]))
      print(solution([1,2,1,2]))

            