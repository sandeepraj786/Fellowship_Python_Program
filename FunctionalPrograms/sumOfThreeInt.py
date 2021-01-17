"""
author -sandeep raj
date -10-11-2020
time -01:09
package -BaicCorePrograms
problem Statement-'Sum of three Integer adds to ZERO.
"""

class Triplet:


    def findTriplets(self,arr, n):

        """

        :param arr:
        :param n:
        :return:
        """
        found = True
        for i in range(0, n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if (arr[i] + arr[j] + arr[k] == 0):
                        print("*************Triplet **********")
                        print(arr[i], arr[j], arr[k])
                        found = True

        # If no triplet with 0 sum
        # found in array
        if (found == False):
            print(" not exist ")





if __name__ == '__main__':
    arr = []
    a = int(input("Enter the no of element: "))
    for i in range(a):
        b = int(input("Enter an elemnt : "))
        arr.append(b)
    print("*****Array Element***********")
    print(arr)
    print()

    n = len(arr)

    triplet=Triplet()
    triplet.findTriplets(arr,n)



