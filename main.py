import os
import subprocess

# command for downloading YouTube videos as MP3 with best audio quality
cmd = "youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 "

multi_names = input("""
https://youtu.be/code123 https://youtu.be/code321
Provide the songs as previously stated (no spaces, apostrophes, nor quotation marks!)
>""").split(" ")
print("-------->" + str(multi_names))
song_count = 0
for link in multi_names:
    os.system(cmd + link)

    # Record the listed information that it provides while running the download command
    raw_data = subprocess.check_output(
        ["youtube-dl", "-f", "bestaudio", "--extract-audio",
         "--audio-format", "mp3", "--audio-quality", "0", link],
        shell=True)

    song_count += 1

    # Break the raw data at every new line
    data = raw_data.decode('utf-8', errors="backslashreplace").split('\n')
    file_name = []
    for result in data:

        # Add data follows the word "Destination"
        if "Destination" in result:
            file_name.append(result.split(":")[1][1:-4])
            # removes the initial space & the "webm" text
            # upload that information to a list

    # Only need the first result
    file_name = file_name[0]
    file_name = file_name + "mp3"

    # Remove the unneeded code from the filename
    new_name = file_name[0:-16]
    new_name = new_name + ".mp3"

    os.system(f"""rename "{file_name}" "{new_name}" """)

    # Give useful information to the user
    print(
        f""" -> Old file name: "{file_name}"
 -> New file name: "{new_name}" 
CHECKED SONG #{str(song_count)} \n""")
