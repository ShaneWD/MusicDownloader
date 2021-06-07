import os
import subprocess


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
https://youtu.be/code123,https://youtu.be/code321
Provide the songs as previously stated (no spaces, apostrophes, or quotes!)
>""").split(",")
    song_count = 0
    for link in multi_names:
        os.system(cmd + link)
        testing = subprocess.check_output(
            ["youtube-dl", "-f", "bestaudio", "--extract-audio",
             "--audio-format", "mp3", "--audio-quality", "0", link],
            shell=True)

        song_count += 1
        print("checked song #" + str(song_count))

    option_2 = input("""
Remove the trailing code(s) on the file name?
"yes" or "no" 
>""").lower()
    if option_2 == "no":
        pass

    elif option_2 == "yes":
        testing = testing.decode('utf-8', errors="backslashreplace").split('\n')
        file_name = []
        for result in testing:
            if "Destination" in result:
                file_name.append(result.split(":")[1][1:-1])

        print(file_name)

    else:
        raise ValueError("Incorrect input")

else:
    raise TypeError("Incorrect input")
