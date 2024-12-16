import subprocess

video_data = [
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/d8c3b3d6-3155-4f45-98b1-13e89e78d024/mp4/d8c3b3d6-3155-4f45-98b1-13e89e78d024.mp4/index.m3u8",
        "title": "책의역사로본서구문명_역사적배경(4)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/b980d796-11e5-4f03-b598-7879ff5c7f98/mp4/b980d796-11e5-4f03-b598-7879ff5c7f98.mp4/index.m3u8",
        "title": "책의역사로본서구문명_7장_인쇄기술의발전(1)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/74317fcf-a770-46cb-a4fc-94ede0c2287d/mp4/74317fcf-a770-46cb-a4fc-94ede0c2287d.mp4/index.m3u8",
        "title": "책의역사로본서구문명_7장_인쇄기술의발전(2)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/3ac7408d-85dd-43b6-9668-d44b6c88f501/mp4/3ac7408d-85dd-43b6-9668-d44b6c88f501.mp4/index.m3u8",
        "title": "책의역사로본서구문명_역사적배경(5)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/8411419f-fe19-4a68-8e55-0c5613aeeff4/mp4/8411419f-fe19-4a68-8e55-0c5613aeeff4.mp4/index.m3u8",
        "title": "책의역사로본서구문명_제7장_인쇄기술의발전(3)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/dc8fac54-cb68-45d0-b4c8-f7b72c4c62ad/mp4/dc8fac54-cb68-45d0-b4c8-f7b72c4c62ad.mp4/index.m3u8",
        "title": "책의역사로본서구문명_제11장_산업혁명시대의책문화(1)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/6dc0ef4f-5aa3-495c-a20e-f2e31966f75a/mp4/6dc0ef4f-5aa3-495c-a20e-f2e31966f75a.mp4/index.m3u8",
        "title": "책의역사로본서구문명_제11장_산업혁명시대의책문화(2)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/8ad531ff-b4e0-4d5e-80d2-c34ea25dcde0/mp4/8ad531ff-b4e0-4d5e-80d2-c34ea25dcde0.mp4/index.m3u8",
        "title": "책의역사로본서구문명_제11장_산업혁명시대의책문화(3)",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/c36034aa-8830-4526-bfc2-4689a01d800a/mp4/c36034aa-8830-4526-bfc2-4689a01d800a.mp4/index.m3u8",
        "title": "책의역사로본서구문명_역사적배경(5)-2",
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