import glob, shutil

for i in glob.glob("/home/anon/Dowloads/cv-corpus-12.0-delta-2022-12-07-en/cv-corpus-12.0-delta-2022-12-07/en/clips/*.mp3"):
    shutil.move(i, f"/home/anon/Dowloads/cv-corpus-12.0-delta-2022-12-07-en/cv-corpus-12.0-delta-2022-12-07/en/clips/non_wakeword{i}.mp3")