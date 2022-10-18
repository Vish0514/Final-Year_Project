from urllib import request


newvideo = request.get("https://youtu.be/OBLiJ0N9ac4")
print(newvideo.read())
