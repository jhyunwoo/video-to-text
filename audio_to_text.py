import os
from openai import OpenAI
client = OpenAI()

# 파일명을 출력할 폴더 경로
folder_path = "sliced_audio"

# os.listdir을 통해 해당 폴더의 모든 항목(파일/폴더) 이름 가져오기
for filename in os.listdir(folder_path):
    print(filename)
    audio_file = open(f"{folder_path}/{filename}", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    print(transcription)
    file_path = "text/"+filename+".txt"

    # 파일 열기 (쓰기 모드)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(transcription)