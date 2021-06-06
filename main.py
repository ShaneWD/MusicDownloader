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
    print(option)

else:
    raise TypeError("Incorrect input")
