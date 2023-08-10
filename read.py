'''
@Author: Shreyash More

@Date: 2023-08-06 11:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-08-10 13:34:30

@Title : Create a get post api for video and image

'''
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

# creating a post operation for images
@app.post("/upload/image/")
async def upload_image(image: UploadFile = File(...)):
    with open(f"uploaded_images/{image.filename}", "wb") as f:
        f.write(await image.read())
    return {"message": "Image uploaded successfully!"}

# creating a post operation for videos
@app.post("/upload/video/")
async def upload_video(video: UploadFile = File(...)):
    with open(f"uploaded_videos/{video.filename}", "wb") as f:
        f.write(await video.read())
    return {"message": "Video uploaded successfully!"}

# creating a get operation for images
@app.get("/image/{filename}/")
async def get_image(filename: str):
    return FileResponse(f"uploaded_images/{filename}", media_type="image/jpeg")

# creating a post operation for videos
@app.get("/video/{filename}/")
async def get_video(filename: str):
    return FileResponse(f"uploaded_videos/{filename}", media_type="video/mp4")
