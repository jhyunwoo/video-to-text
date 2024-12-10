import subprocess
from main import video_data

for i in range(len(video_data)):
    cmd = [
        "ffmpeg",
        "-i", "video/"+video_data[i]["title"]+".mp4",
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        "audio/"+video_data[i]["title"]+".mp3"
    ]

    # 명령 실행
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(video_data[i]["title"]+".mp4", "파일을 MP3로 성공적으로 변환했습니다.")
    else:
        print("변환 실패:")
        print(result.stderr)