x=["hello","hell"]
#y=filter(lambda x:len(x)>3,x)
def ans(x):
    return len(x)>=3
y=filter(ans,x)
print(list(y))