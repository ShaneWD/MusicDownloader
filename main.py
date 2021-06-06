import os

cmd = "youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 "

option = input("""
"one" = download one song
"multi" = download multiple songs
>""").lower()

if option == "one":

    link = input("""Link
>""")
    os.system(cmd + link)

elif option == "multi":
    multi_names = input("""
'https://youtu.be/code123','https://youtu.be/code321'
Provide the songs as previously stated (no spaces!)
>""").split(",")
    song_count = 0
    for link in multi_names:
        os.system(cmd + link)
        song_count += 1
        print("checked song #" + str(song_count))


else:
    raise TypeError("Incorrect input")
