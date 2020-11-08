
class Ulility:
    def createList():
        list1=[]
        try:
            a=int(input("Enter the no of element of 1st list: "))
            print()
            for i in range(a):
                value=input("Enter the element of list: ")
                list1.append(value)
            return list1
        except:
            print("PROVIDE CORRECT INPUT")






