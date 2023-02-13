import json,os,sys
for x in os.walk(sys.path[0]):
    for y in x[2]:
        if y[-5:]=='.json':
            f=open(p:='%s/%s'%(x[0],y),'r');t=eval(f.read());f.close()
            r=''
            n=0
            tl=len(t)
            def ms2str(a):
                h=int(a/1000/60/60)
                m=int(a/1000/60)%60
                s=int(a/1000)%60
                ms=a%1000
                return'%s:%s:%s,%s'%(str(h).rjust(2).replace(' ','0'),str(m).rjust(2).replace(' ','0'),str(s).rjust(2).replace(' ','0'),str(ms).rjust(3).replace(' ','0'))
            for b in t:
                if n!=0:r='%s\n\n'%r
                r='%s%d\n%s --> %s\n%s'%(r,n+1,ms2str(b['startTimestampInMS']),ms2str(b['endTimestampInMS']),b['statement'])
                n+=1
            f=open('%s.srt'%'.'.join(p.split('.')[:-1]),'w+');f.write(r);f.close()
