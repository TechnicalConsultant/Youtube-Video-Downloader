from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
res= input ("Choose video resolution you want [0:low, 1:high]:")
#Create new object contains video elements
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the resolution requested by the user
if res == 1:
    ys = yt.streams.get_highest_resolution()
else:
    ys = yt.streams.get_lowest_resolution()
    
#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")