"""
author -sandeep raj
date -09-11-2020
time -23:55
package -BaicCorePrograms
problem Statement-'Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value..
"""

class HarmonicNumber:
    def harmonic(self):
        '''
                      :param:self
                      :return
                     '''
        n= int(input("enter the value of n: "))
        s=0.0
        for i in range(1, n + 1):
            s = s + 1 / i ;
        print("Sum is", round(s,3))

if __name__=='__main__':
    harmonic_number=HarmonicNumber()
    harmonic_number.harmonic()

