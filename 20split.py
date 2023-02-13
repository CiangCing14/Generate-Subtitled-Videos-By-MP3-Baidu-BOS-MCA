import os,sys
def a20sp(a):
    r=[]
    while True:
        if len(a)>25:
            r.append(a[:25])
            a=a[25:]
        else:
            r.append(a)
            break
    return'\n'.join(r)
for a in os.walk(sys.path[0]):
    for b in a[2]:
        if b[-3:]=='srt':
            f=open('%s/%s'%(a[0],b),'r');s=f.read().split('\n\n');f.close()
            s=[z.split('\n')for z in s]
            s=[[z[0],z[1],a20sp(z[2])]for z in s]
            s=['\n'.join(z)for z in s]
            s='\n\n'.join(s)
            f=open('%s/%s_new.srt'%(a[0],b.split('.')[0]),'w+');f.write(s);f.close()
