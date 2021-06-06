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
Provide the songs in as previously stated (no spaces!)
>""").split(",")
    for link in multi_names:
        os.system(cmd + link)

else:
    raise TypeError("Incorrect input")
