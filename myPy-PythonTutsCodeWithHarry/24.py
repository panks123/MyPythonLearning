# *args and **kwargs


def funargs(normal,*args,**kwargs):
    print(type(args))  # type of args is always tuple whether we pass list or tuple
    print(normal)
    for i in args:
        print(i)

    print()
    print(type(kwargs))  # type of kwargs is always dictionary
    for key,value in kwargs.items():
        print(f"{key} is a {value}")


a=["Harry","Garry","Larry","Marie","Tarry"]   #list
n="Normal"
kw={"Harry":"Instructor","Larry":"Doctor","Garry":"Trainer","Marie":"Follower","Tarry":"Teacher"}
funargs(n,*a,**kw)

a=("Harry","Garry","Larry","Marie","Tarry")   #tuple
n="Normal"
kw={"Harry1":"Instructor","Larry1":"Doctor","Garry1":"Trainer","Marie1":"Follower","Tarry1":"Teacher"}
funargs(n,*a,**kw)