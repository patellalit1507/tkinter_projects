from tkinter import *
from pytube import YouTube

root=Tk()
root.title("Youtube Video downloader")
root.geometry('600x600')
link=StringVar()

#def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
     #percent = (100*(file_size-remaining))/file_size
    # print("{:00.0f}% downloaded".format(percent))
def combine(videoname,fp=25):
    import moviepy.editor as mpe
    my_clip=mpe.VideoFileClip(videoname.mp4)
    my_audio=mpe.AudioFileClip(videoname.webm)
    final_clip=my_clip.set_audio(my_audio)
    final_clip.write_videofile(videoname,fps=fp)

def dwn_video():

     Url=YouTube(str(link.get()))
     mystreams=Url.streams
     print(mystreams.filter(res="720p",progressive=False).all)

     video=Url.streams.filter(res='720p',progressive=False).first()
     Audio=Url.streams.filter().last()

     #file_size=mystreams.filesize
     #print("{} mb".format(file_size/1000000))
     try:
         video.download('C:/Users/ASUS/PycharmProjects/pythonProject/assignment')
         Audio.download("C:/Users/ASUS/PycharmProjects/pythonProject/assignment")

         Label(root, text='DOWNLOADED', font='arial 15').place(x=250, y=300)
         videoname=video.title

         combine(videoname)
     except:
         print("some error occured ")
def main():
      get_link=Entry(root,text=link,bg="pink",width=40,font=("arial",14))
      btn_submit=Button(root,text="Download",font=("Arial"),command=dwn_video)
      get_link.place(x=100,y=200)
      btn_submit.place(x=250,y=250)

main()


root.mainloop()
