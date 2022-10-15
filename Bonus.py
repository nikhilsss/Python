time_year=int(input("enter the number you served the company:"))
salary=int(input("your salary is:"))
if time_year>=10:
    print(salary+salary*0.1)
elif time_year>=6:
    print(salary+salary*0.08)
else:
    print(salary+salary*0.05)