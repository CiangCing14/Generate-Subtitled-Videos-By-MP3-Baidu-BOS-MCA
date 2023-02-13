import os,sys
for a in os.walk(sys.path[0]):
    for b in a[2]:
        if b[-4:]=='.mp4':
            pa='%s/%s'%(a[0],b)
            sn='.'.join(pa.split('.')[:-1])
            os.system('ffmpeg -i "%s" -lavfi "subtitles=%s:force_style=\'Alignment=0,OutlineColour=&H100000000,BorderStyle=1,Outline=1,Shadow=1,Fontsize=28,MarginV=25\'" -crf 28 -c:a copy "%s"'%(pa,'%s_new.srt'%sn,'%s_sub.mp4'%sn))
