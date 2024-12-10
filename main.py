import subprocess

video_data = [
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/f3c04906-4ac7-419e-898b-cbec3940d5fb/mp4/f3c04906-4ac7-419e-898b-cbec3940d5fb.mp4/index.m3u8",
        "title": "기독교와세계문화_9주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/5dbeb766-8337-42a9-9d9e-83fd359be35f/mp4/5dbeb766-8337-42a9-9d9e-83fd359be35f.mp4/index.m3u8",
        "title": "기독교와세계문화_9주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/d1dc0c48-8992-4c94-9652-241bcfe1731e/mp4/d1dc0c48-8992-4c94-9652-241bcfe1731e.mp4/index.m3u8",
        "title": "기독교와세계문화_10주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/9f3a36dc-351f-4b3b-86c9-8ffd8996cd75/mp4/9f3a36dc-351f-4b3b-86c9-8ffd8996cd75.mp4/index.m3u8",
        "title": "기독교와세계문화_10주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/b4ffcba6-f3e0-4c7e-9fd6-03cd89b07b59/mp4/b4ffcba6-f3e0-4c7e-9fd6-03cd89b07b59.mp4/index.m3u8",
        "title": "기독교와세계문화_11주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/07dd0932-4b92-4f72-972f-8c8e767c604a/mp4/07dd0932-4b92-4f72-972f-8c8e767c604a.mp4/index.m3u8",
        "title": "기독교와세계문화_11주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/f8c9636b-3660-480e-a18b-33784181ef72/mp4/f8c9636b-3660-480e-a18b-33784181ef72.mp4/index.m3u8",
        "title": "기독교와세계문화_12주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/d6d18adf-2771-4646-96bd-9df93245315a/mp4/d6d18adf-2771-4646-96bd-9df93245315a.mp4/index.m3u8",
        "title": "기독교와세계문화_12주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/ffab1630-f18c-40d4-9a95-ade4e3d12271/mp4/ffab1630-f18c-40d4-9a95-ade4e3d12271.mp4/index.m3u8",
        "title": "기독교와세계문화_12주차_3",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/769eb26f-cc63-44af-ba11-eb262303fced/mp4/769eb26f-cc63-44af-ba11-eb262303fced.mp4/index.m3u8",
        "title": "기독교와세계문화_13주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/a74cca51-3079-4ccc-ab6a-b3c9e83da628/mp4/a74cca51-3079-4ccc-ab6a-b3c9e83da628.mp4/index.m3u8",
        "title": "기독교와세계문화_13주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/dc2556d4-3bed-4cb0-b40e-9c61e3c65bef/mp4/dc2556d4-3bed-4cb0-b40e-9c61e3c65bef.mp4/index.m3u8",
        "title": "기독교와세계문화_14주차_1",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/02c60642-3905-40f4-9cfe-cef762c10b72/mp4/02c60642-3905-40f4-9cfe-cef762c10b72.mp4/index.m3u8",
        "title": "기독교와세계문화_14주차_2",
    },
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/ac1c892b-fe3b-43b4-a2ea-7920aad0950f/mp4/ac1c892b-fe3b-43b4-a2ea-7920aad0950f.mp4/index.m3u8",
        "title": "기독교와세계문화_14주차_3",
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