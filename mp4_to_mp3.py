import subprocess

video_data = [
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/9a8bb5a4-b2b5-4722-9ede-8b7df826ce67/mp4/9a8bb5a4-b2b5-4722-9ede-8b7df826ce67.mp4/index.m3u8",
        "title": "재산거래와법_7주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/9c46869c-3941-449b-b13d-2f8675cb47c3/mp4/9c46869c-3941-449b-b13d-2f8675cb47c3.mp4/index.m3u8",
        "title": "재산거래와법_9주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/43f51ef8-d547-4541-a3fa-9344b3437893/mp4/43f51ef8-d547-4541-a3fa-9344b3437893.mp4/index.m3u8",
        "title": "재산거래와법_10주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/e0731bca-e444-4a4d-bcdf-31b83c1eda80/mp4/e0731bca-e444-4a4d-bcdf-31b83c1eda80.mp4/index.m3u8",
        "title": "재산거래와법_11주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/c774f06b-c601-4958-b9a0-e28a4181ad65/mp4/c774f06b-c601-4958-b9a0-e28a4181ad65.mp4/index.m3u8",
        "title": "재산거래와법_12주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/f359949d-6372-4534-a2e3-142e41b39e58/mp4/f359949d-6372-4534-a2e3-142e41b39e58.mp4/index.m3u8",
        "title": "재산거래와법_13주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/ca0834bc-5df8-4e57-a542-fe5223b7185d/mp4/ca0834bc-5df8-4e57-a542-fe5223b7185d.mp4/index.m3u8",
        "title": "재산거래와법_14주차",
    },
]

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