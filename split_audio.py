from pydub import AudioSegment
from main import video_data


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