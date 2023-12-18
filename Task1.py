def calculate_area(len,wid):
    if len == wid :
        area = " This is a Square!"
        

    else:
        area = (len * wid)

    return area

len = float(input("Enter the Length = "))
wid = float(input("Enter the Width = "))
c = calculate_area(len, wid)
print(c)

