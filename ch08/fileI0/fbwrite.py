# 바이너리 파일 - 텍스트가 아닌 파일(음성, 영상, 이미지 등)

with open('data.bin', 'wb') as f:
    text = "날씨가 덥다"
    f.write(text.encode())

with open('data.bin', 'rb') as f:
    data = f.read()
    text = data.decode()
    print(text)

    