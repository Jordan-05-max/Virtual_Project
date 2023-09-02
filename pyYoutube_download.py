from pytube import YouTube


def downloader(link, path: str, filename: str):
    """
    Downloads any YouTube video selected by user
    :param link: stores YouTube video url given by user
    :param path: file path to store video downloaded
    :param filename: stores filename and file format
    :return: None
    """
    yt: object = YouTube(link)
    video = yt.streams.get_highest_resolution()

    try:
        print("Download starts")
        video.download(path, filename)

    except:
        print("Problem occurred")
    print("Download completed!")


url = input("Enter the video's url: ")
file_name = input("Filename: ")
file = f"{file_name}.mp4"
output_path: str = "C:/Users/jorda/Downloads/py_youtube"

downloader(url, output_path, file)
