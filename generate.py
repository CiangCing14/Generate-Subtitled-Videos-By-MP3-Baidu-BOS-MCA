import cv2,time,eyed3,os
from moviepy.editor import VideoFileClip,AudioFileClip
l=[]
#在这里输入MP3文件们所在的路径。
for a in os.walk(pa:='[MP3s PATH]'):
    a[2].sort()
    for b in a[2]:
        if a[0]==pa:
            if b[-4:]=='.mp3':
                mi=eyed3.load(f:='%s/%s'%(a[0],b))
                l.append([f,mi.info.time_secs])
print('\n'.join([repr(a)for a in l]))
for a in l:
    if not os.path.exists(r:='%s.mp4'%('.'.join(a[0].split('/')[-1].split('.')[:-1]))):
        if not os.path.exists(r2:='%s_r.mp4'%('.'.join(r.split('.')[:-1]))):
            print('“%s”影片开始生成。'%r)
            videoWriter = cv2.VideoWriter(r,cv2.VideoWriter_fourcc(*'MP4V'),60,(1920,1080),True)
            img=cv2.imread('back.png')
            b=0
            le=int(60*a[1])+1
            nn=0
            while b<le:
                if b==0:t1=time.time()
                videoWriter.write(img)
                b+=1
                if b%360==0:
                    nn+=1
                    t2=time.time()
                    p=t2-t1
                    rs=(le/360-nn)*p
                    if nn!=1:print('\033[A\033[A')
                    print('耗时%fs，还剩%dm%fs，%d / %d。'%(p,int(rs//60%60),round(rs%60,5),b,le))
                    t1=time.time()
            videoWriter.release()
            print('“%s”影片生成完毕。'%r)
        else:print('“%s”影片已经生成。'%r)
    else:print('“%s”影片已经生成。'%r)
    if not os.path.exists(r2):
        print('“%s”影片开始生成。'%r2)
        t1=time.time()
        os.system('ffmpeg -i \'%s\' -i \'%s\' -c:v copy -c:a copy \'%s\''%(r,a[0],r2))
        t2=time.time()
        rs=t2-t1
        print('“%s”影片生成完毕，共耗时%dm%ds。'%(r2,rs//60%60,rs//60))
        os.remove(r)
        print('前置空影片“%s”已经删除。'%r)
    else:print('“%s”影片已经生成。'%r2)
