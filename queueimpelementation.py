from pythonds.basic import Queue
def hotline(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())
    return simqueue.dequeue()
print(hotline(["mon","tue","wed","day",4,5,"for"],3))