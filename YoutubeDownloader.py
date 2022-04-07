from pytube import YouTube
from colorama import init, Fore

def on_complete(stream, filepath):
    print('Download Complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100), 2)}%'
    print(progress_string)

init()
videoLink = input('Youtube Link: ')
video_object = YouTube(videoLink,
                       on_complete_callback = on_complete,
                       on_progress_callback = on_progress)

#Video Information
print(Fore.RED + f'Title: {video_object.title}')
print(Fore.GREEN + f'Length: {round(video_object.length / 60, 2)} minutes')
print(Fore.YELLOW + f'Views: {video_object.views / 1000000} million')
print(Fore.BLUE + f'Author: {video_object.author}')

#Download
print('Download: (B)est | (L)ow | (A)udio | (E)xit')
userChoice = input('Choice: ')

if(userChoice == 'b' or userChoice == 'B'):
    video_obj.streams.get_highest_resolution().download()
elif(userChoice == 'l' or userChoice == 'L'):
    video_obj.streams.get_lowest_resolution().download()
elif(userChoice == 'a' or userChoice == 'A'):
    video_obj.streams.get_audio_only().download()
