a = input("Enter the name of  student :")
reg_no = (input("Enter the reg number :"))
age = int(input("Enter ur age :"))
if(age>22):
    degree=input("Enter the name of  degree :")
    cgpa =float( input("Enter the cgpa :"))
    mark_12 = float(input("Enter the 12th mark  :"))
    mark_10 = float(input("Enter the 10th mark :"))
    if(cgpa*10)>60:
        print("Ready for placement")