# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]


def findTriplets(arr,n):
    found = False
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if found == False:
        print("No Triplet Found")

if __name__ == "__main__":
    findTriplets([-25,-10,-7,-3,2,4,8,10],8)