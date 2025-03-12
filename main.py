import subprocess

video_data = [
    {
        "url": "https://tqozw4vr7987.edge.naverncp.com/hls/b6yd7gaFWdlIc3gQXQj~-Q__/b064188a-6f19-462a-ab00-84811075ef43/mp4/b064188a-6f19-462a-ab00-84811075ef43.mp4/index.m3u8",
        "title": "2주차 채플",
    },
]

if __name__ == '__main__':
    # ffmpeg 명령어를 리스트로 작성
    # '-y' 옵션은 출력 파일이 이미 존재할 경우, 덮어쓰기를 허용하는 옵션
    for i in range(len(video_data)):
        print(video_data[i]["title"], "다운로드 중...")
        cmd = [
            "ffmpeg",
            "-i", video_data[i]["url"],
            "-c", "copy",
            "-y",
            "video/"+video_data[i]["title"]+".mp4"
        ]

        # subprocess.run을 이용해 명령어 실행
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(video_data[i]["title"], "다운로드 완료")
        else:
            print("다운로드 실패:")
            print(result.stderr)