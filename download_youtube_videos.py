def iniate():
    import pafy
    import re
    def detailed_info_of_video(url):
        print(url.title)
        print(url.duration)
        print(url.rating)
        print(url.author)
        print(url.length)
        print(url.videoid)
        print(url.viewcount)
        print(url.likes)
        print(url.dislikes)
        print(url.category)


    url = pafy.new(input('Enter the Url or Video ID for Youtube Video: '))
    choice = input("Do you want download the video yes for Y or no for N: ").lower()
    if choice == 'y':
        print('These are streams of video: ',url.streams)
        no = int(input('Enter the Number which is you want to download the videos: '))
        if no > 0 and no <= len(url.streams):
            no = no - 1
            download_video = url.streams[no]
            print('Size of this video: ', download_video.get_filesize())
            download_video.download()
        else:
            print('Wrong Input')
    elif choice == 'n':
        detail_choice = input('Do you want detailed information regarding video, So yes for Y or no for N: ').lower()
        if detail_choice == 'y':
            detailed_info_of_video(url)
        elif detail_choice == 'n':
            print('No Problem')
        else:
            print('Wrong Input')
    else:
        print('Wrong Input')

iniate()
#https://www.youtube.com/watch?v=8UjlXycd9do