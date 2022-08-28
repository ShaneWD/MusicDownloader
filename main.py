import os
import subprocess

# command for downloading YouTube videos as MP3 with best audio quality
cmd = "yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 -4 "

multi_names = input("""
https://youtu.be/IaMxH8aU1fZ https://www.youtube.com/watch?v=XsKdV3uL3bH

Provide the songs as stated above (no  apostrophes, or quotation marks! Differentiate with a space.)
>""").split(" ")

song_count = 0
for link in multi_names:
    # Initiates the download
    os.system(cmd + link)

    # Records the listed information that it provides while running the following command
    raw_data = subprocess.check_output(
        ["yt-dlp", "-f", "bestaudio", "--extract-audio",
         "--audio-format", "mp3", "--audio-quality", "0", link],
        shell=True)

    song_count += 1

    # separate the raw data at every new line
    data = raw_data.decode('utf-8', errors="backslashreplace").split('\n')
    file_name = []
    for result in data:

        # Add all data following the word "Destination"
        if "Destination" in result:
            if result[-4:].lower() == "webm":
                file_name.append(result.split(":")[1][1:-4])
                # Only saves info past the colon
                # removes the initial space & the "webm" text
                # uploads that information to a list
            else:
                file_name.append(result.split(":")[1][1:-3])
                # removes the "m4a" text
                # uploads that information to a list

    # Only need the first result
    file_name = file_name[0]
    file_name = file_name + "mp3"

    # Remove the unneeded code from the filename
    new_name = file_name[0:-18]
    new_name = new_name + ".mp3"

    os.system(f"""rename "{file_name}" "{new_name}" """)

    # Give useful information to the user
    print(
        f""" -> Old file name: "{file_name}"
 -> New file name: "{new_name}" 
CHECKED SONG #{str(song_count)} \n""")
