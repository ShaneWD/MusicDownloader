import os
import subprocess


cmd = "youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 "

multi_names = input("""
https://youtu.be/code123, https://youtu.be/code321
Provide the songs as previously stated (no apostrophes, or quotation marks!)
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

    testing = testing.decode('utf-8', errors="backslashreplace").split('\n')
    file_name = []
    for result in testing:
        if "Destination" in result:
            file_name.append(result.split(":")[1][1:-4])

    file_name = file_name[0]
    file_name = file_name + "mp3"

    new_name = file_name[0:-16]
    new_name = new_name + ".mp3"

    os.system(f"""rename "{file_name}" "{new_name}" """)
    print(f"""Old file name:"{file_name}", New file name: "{new_name}" """)

