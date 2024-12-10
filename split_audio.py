from pydub import AudioSegment

video_data = [
    {
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/9a8bb5a4-b2b5-4722-9ede-8b7df826ce67/mp4/9a8bb5a4-b2b5-4722-9ede-8b7df826ce67.mp4/index.m3u8",
        'title': "재산거래와법_7주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/9c46869c-3941-449b-b13d-2f8675cb47c3/mp4/9c46869c-3941-449b-b13d-2f8675cb47c3.mp4/index.m3u8",
        'title': "재산거래와법_9주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/43f51ef8-d547-4541-a3fa-9344b3437893/mp4/43f51ef8-d547-4541-a3fa-9344b3437893.mp4/index.m3u8",
        'title': "재산거래와법_10주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/e0731bca-e444-4a4d-bcdf-31b83c1eda80/mp4/e0731bca-e444-4a4d-bcdf-31b83c1eda80.mp4/index.m3u8",
        'title': "재산거래와법_11주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/c774f06b-c601-4958-b9a0-e28a4181ad65/mp4/c774f06b-c601-4958-b9a0-e28a4181ad65.mp4/index.m3u8",
        'title': "재산거래와법_12주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/f359949d-6372-4534-a2e3-142e41b39e58/mp4/f359949d-6372-4534-a2e3-142e41b39e58.mp4/index.m3u8",
        'title': "재산거래와법_13주차",
    },
{
        "url": "https://qszhvydoggzp7663209.cdn.ntruss.com/hls/ca0834bc-5df8-4e57-a542-fe5223b7185d/mp4/ca0834bc-5df8-4e57-a542-fe5223b7185d.mp4/index.m3u8",
        'title': "재산거래와법_14주차",
    },
]

for video in video_data:

    # 처리할 MP3 파일 경로
    input_file = "audio/"+video['title']+".mp3"

    # 오디오 파일 로드
    song = AudioSegment.from_mp3(input_file)

    # 10분 단위(ms 단위 계산)
    ten_minutes = 10 * 60 * 1000  # 10분 * 60초 * 1000ms = 600,000ms

    # 오디오 전체 길이
    audio_length = len(song)

    # 10분 단위로 나눌 횟수 (정수 나눗셈)
    num_chunks = audio_length // ten_minutes

    # 나머지 시간(10분으로 나누어 떨어지지 않을 경우)
    remainder = audio_length % ten_minutes

    # 10분 단위로 파일을 잘라 저장
    for i in range(num_chunks):
        start_time = i * ten_minutes
        end_time = start_time + ten_minutes
        chunk = song[start_time:end_time]
        chunk.export(f"sliced_audio/{video['title']}_{i + 1}.mp3", format="mp3")
        print(f"{video['title']}_{i + 1}.mp3 파일 생성 완료")

    # 남은 부분이 있을 경우 추가로 파일로 저장
    if remainder > 0:
        start_time = num_chunks * ten_minutes
        chunk = song[start_time:]
        chunk.export(f"sliced_audio/{video['title']}_{num_chunks + 1}.mp3", format="mp3")
        print(f"{video['title']}_{num_chunks + 1}.mp3 파일 생성 완료")