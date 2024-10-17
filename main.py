from pytube import YouTube

link = input("Enter the video line here-->")

y_tube = YouTube(link)

print(f'video Title ->{y_tube.title}')
print(f'video description ->{y_tube.description}')

stream = y_tube.streams.all(progressive=True)

video = list(enumerate(stream)) 

for i in stream:
    print(i)

print("================================================")
index = int(input("Give the indext of the desired stream"))

stream[index].download()
print("Success!")