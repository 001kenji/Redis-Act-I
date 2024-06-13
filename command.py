import redis,json
r= redis.StrictRedis(host='localhost',port=6379,db=0)

def Deconstract(*props):
    val = str()
    for x in props:
        val += f' {x}'
    return val

#Testing strings
def StringImpliment(val=None,get=False,key=None):
    if get:
        val = r.get(key)
        print('\nResult string: ',val)
        return
    else:
        r.set(key,val,nx=True)
        print('String set: ',key," : ",val)
    
def ListImplimentation(val=None,get=False,key=None,start=0,end=0):
    if get:
        val = r.lrange(key,start=start,end=end)
        print('\nResult List: ',val)
    else:
        #strval = Deconstract(*val)
        r.rpush(key,*val)
        print('Added List to redis')

def SetImplimentation(val=None,key=None,get=False):
    if get:
        printval = r.smembers(key)
        print('\nResult Sets: ',printval)
    else:
        r.sadd(key,*val)
        print('Added Sets to redis')

def SortedSetsImplimentation(val=None,key=None,start=0,end=0,get=False):
    if get:
        printval = r.zrangebyscore(key,min=start,max=end)
        print('\nResult Sorted Sets: ',printval)
    else:
        r.zadd(key,val,nx=True)
        print('Added Sorted Sets to redis')

def HashesImplimentation(val=None,key=None,get=False):
    if get:
        printval = dict(r.hgetall(key))
        print('\nResult Hashes: ',printval)
    else:
        r.hset(key,mapping=val)
        print('Added Hashes to redis')

##dealing with strings

StringImpliment(get=False,key='country',val='My Country')
StringImpliment(get=True,key='country')

##dealing with lists
myList = ['2.2','4','1','cool',9,'it is']
ListImplimentation(get=False,val=myList,key='My-List1')
ListImplimentation(get=True,key='My-List1',start=0,end=4)

##Dealing with sets
myset = {'Joe','car','2','text','phone','mate','house'}
SetImplimentation(get=False,key='My-Set1',val=myset)
SetImplimentation(get=True,key='My-Set1')

##Dealing with sorted sets
mySortedSet = {
    'jake' : 0,
    'lap':1,
    'stock' : 2,
    'shoes' :3,
    'jack' : 4,
    'zero' : 0
}
SortedSetsImplimentation(get=False,val=mySortedSet,key='My-SortedSet')
SortedSetsImplimentation(get=True,key='My-SortedSet',start=0,end=4)

myHash = {
    'name' : 'John Doe',
    'age' : 22,
    'hobbie' : 'dancing'
}
##Dealing with Hashes
HashesImplimentation(key='My-Hash:1',get=False,val=myHash)
HashesImplimentation(key='My-Hash:1',get=True)
