from tkinter import Button, Label, Frame, PhotoImage, ttk,Canvas
import tkinter as tk
from PIL import Image, ImageTk,ImageSequence
import cv2
import cvzone
from threading import Thread
import imageio
import numpy as np
import os
from gallary import fun
from secure import secure
#from secure import open_image_file

window=tk.Tk()
window.configure(bg='black')
canvas = tk.Canvas(window,width=1370,height=730)
canvas.place(x=0,y=0)
canvas.pack()
button=tk.Button(canvas,text='ok',width=5,height=1)
#button.place(x=600,y=100)


def code(image_path):
    fun(image_path)

#-----------------------------------------------media declaration------------------------------------------------------#

video_path = "C:\\Users\gowrishankar\Downloads\pexels-maxime-francis-2246476.jpg"
#cap = cv2.VideoCapture(video_path)
video_path=cv2.imread(video_path)

# Load the overlay image with transparency
image_path = "C:\\Users\gowrishankar\Downloads\major_files\\build\\build\\assets\\frame0\entry_2.png"
overlay_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
overlay_image_left=cv2.resize(overlay_image,(182,655))


image_path = "C:\\Users\gowrishankar\Downloads\major_files\\build\\build\\assets\\frame0\entry_1.png"
overlay_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
overlay_image_right=cv2.resize(overlay_image,(1106,574))

image_path = "C:\\Users\gowrishankar\Downloads\major_files\\build\\assets\\frame0\entry_4.png"
overlay_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
overlay_image_top=cv2.resize(overlay_image,(396,34))

home_gif_path = 'C:\\Users\gowrishankar\Desktop\projects\major\\build\\assets\\frame0\home.png'
#home=Image.open(home_gif_path)
home_image = cv2.imread(home_gif_path , cv2.IMREAD_UNCHANGED)
home_gif_top=cv2.resize(home_image,(50,50))



camera_gif_path = r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\camera.png"
camera_gif = cv2.imread(camera_gif_path, cv2.IMREAD_UNCHANGED)
camera_gif_top=cv2.resize(camera_gif,(50,50))

download_gif_path = r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\download (1).png"
download_gif = cv2.imread(download_gif_path, cv2.IMREAD_UNCHANGED)
download_gif_top=cv2.resize(download_gif,(50,50))

favorate_gif_path = r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\fav.png"
favorate_gif = cv2.imread(favorate_gif_path, cv2.IMREAD_UNCHANGED)
favorate_gif_top=cv2.resize(favorate_gif,(50,50))

social_media_gif_path = r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\social_media.png"
social_media_gif = cv2.imread(social_media_gif_path, cv2.IMREAD_UNCHANGED)
social_media_gif_top=cv2.resize(social_media_gif,(50,50))

search_gif_path=r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\search.png"
search_gif = cv2.imread(search_gif_path, cv2.IMREAD_UNCHANGED)
search_gif_top=cv2.resize(search_gif,(50,50))

settings_gif_path=r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\settings.png"
settings_gif = cv2.imread(settings_gif_path, cv2.IMREAD_UNCHANGED)
settings_gif_top=cv2.resize(settings_gif,(50,50))

account_gif_path=r"C:\Users\gowrishankar\Desktop\projects\major\build\assets\frame0\account.png"
account_gif = cv2.imread(account_gif_path, cv2.IMREAD_UNCHANGED)
account_gif_top=cv2.resize(account_gif,(50,50))


#--------------------------------------image animation & label values---------------------------------------------------------#


overlay_image_left_move=-200
overlay_image_right_move=900
overlay_image_top_move=-270
desired_width = 1370
desired_height = 730

refresh_rate=5
flag=0
home_value = 0
camera_value=0
download_value=0
favorate_value=0
social_media_value=0
search_value=0
settings_value=0
account_value=0


#---------------------------------------image animation----------------------------------------------------------------#

def image_left_move(frame):


    global overlay_image_left_move

    if overlay_image_left_move <= 20:

        left_img = cvzone.overlayPNG(frame, overlay_image_left, [overlay_image_left_move, 60])

        overlay_image_left_move +=20
        return left_img

    else :

        left_img = cvzone.overlayPNG(frame, overlay_image_left, [20, 60])


        return left_img


def image_right_move(left_img):

    global overlay_image_right_move

    if overlay_image_right_move >=140 :

        right_img = cvzone.overlayPNG(left_img, overlay_image_right, [230, overlay_image_right_move])
        overlay_image_right_move -=30
        return right_img

    else :
        right_img = cvzone.overlayPNG(left_img, overlay_image_right, [230, 140])

        return right_img

def image_top_move(right_img):

   global overlay_image_top_move
   global flag
   if overlay_image_top_move <=70:

       top_img=cvzone.overlayPNG(right_img,overlay_image_top,[250,overlay_image_top_move])
       overlay_image_top_move +=10
       return top_img

   else:
       top_img=cvzone.overlayPNG(right_img,overlay_image_top,[250,70])
       flag =1
       return top_img
#----------------------------------------------video-------------------------------------------------------------------#



def bg_video():


    frame = np.array(video_path)

    # Resize the image to the desired dimensions
    frame = cv2.resize(frame, (desired_width, desired_height))

    left_img = image_left_move(frame)
    right_img = image_right_move(left_img)
    top_img = image_top_move(right_img)
    # Convert the OpenCV image to a Tkinter-compatible format
    img = cv2.cvtColor(top_img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    # Update the Tkinter label with the new frame
    video = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.video = img_tk




    if flag==1:

        secure_label = canvas.create_text(930, 100, text='SECURE', font=('Arial', 15, 'bold'), fill='White')
        canvas.tag_bind(secure_label, '<Button-1>', secure_on_click)
        track_label = canvas.create_text(1070, 100, text='TRACK', font=('Arial', 15, 'bold'), fill='White')
        canvas.tag_bind(track_label, '<Button-1>', track_on_click)


        home()


        #cvzone.overlayPNG(home_image_top, overlay_image_left, [100, 150])



    window.after(refresh_rate,bg_video)




#----------------------------------------------main menu---------------------------------------------------------------#

def home():

    frame_gif = cv2.resize(home_image, (50, 50))
    img = Image.fromarray(frame_gif)
    home_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(105,225, image=home_img_tk, tags=('home_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.home = home_img_tk

    camera()



def camera():

    frame_gif = cv2.resize(camera_gif, (50, 50))
    img = Image.fromarray(frame_gif)
    camera_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(105, 325, image=camera_img_tk, tags=('camera_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.camera = camera_img_tk
    download()

def download():


        frame_gif = cv2.resize(download_gif, (50, 50))
        img = Image.fromarray(frame_gif)
        download_img_tk = ImageTk.PhotoImage(img)

        download = canvas.create_image(105, 425, image=download_img_tk, tags=('download_gif_frames'))

        canvas.bind('<Button-1>', onclick)  # lambda event,img=img:exe(event,img)
        canvas.download_gif = download_img_tk

        favorate()
        # window.after(second, lambda: download((frame_num + 1) % download_gif_frames.get_length()))


def favorate():

    frame_gif = cv2.resize(favorate_gif, (50, 50))
    img = Image.fromarray(frame_gif)
    favorate_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(105, 525, image=favorate_img_tk, tags=('favorate_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.favorate = favorate_img_tk

    social_media()


def social_media():

    frame_gif = cv2.resize(social_media_gif, (50, 50))
    img = Image.fromarray(frame_gif)
    social_media_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(105, 625, image=social_media_img_tk, tags=('social_media_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.social_media = social_media_img_tk

    search(search_value)



def search(frame_num):

    frame_gif = cv2.resize(search_gif, (25, 25))
    img = Image.fromarray(frame_gif)
    search_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(625, 87, image=search_img_tk, tags=('search_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.search = search_img_tk

    settings()



def settings():

    frame_gif = cv2.resize(settings_gif, (35, 35))
    img = Image.fromarray(frame_gif)
    settings_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(1280, 100, image=settings_img_tk, tags=('settings_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.settings = settings_img_tk

    account()


def account():


    frame_gif = cv2.resize(account_gif, (35, 35))
    img = Image.fromarray(frame_gif)
    account_img_tk = ImageTk.PhotoImage(img)

    canvas.create_image(1200, 100, image=account_img_tk, tags=('account_gif_frames'))

    canvas.bind('<Button-1>', onclick)
    canvas.account = account_img_tk


#---------------------------------------------Home images--------------------------------------------------------------#

home_folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\home"
home_images = []
for file in os.listdir(home_folder):
    img_path = os.path.join(home_folder, file)
    home_images.append(img_path)

home_img_file = []
for img_path in home_images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    home_img_file.append(img)

img_x = 300
image_path=0
home_img_label=[]
for pic in home_img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, home_images=home_images,image_path=image_path:code(home_images[image_path]))
 home_img_label.append(label)
 image_path += 1

#---------------------------------------------camera images--------------------------------------------------------------#
camera_label=Label(window,text='camera images')



camera_folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\camera"
camera_images = []
for file in os.listdir(camera_folder):
    img_path = os.path.join(camera_folder, file)
    camera_images.append(img_path)

camera_img_file = []
for img_path in camera_images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    camera_img_file.append(img)

img_x = 300
image_path=0
camera_img_label=[]
for pic in camera_img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, home_images=home_images,image_path=image_path:code(home_images[image_path]))
 camera_img_label.append(label)
 image_path += 1
#---------------------------------------------download images--------------------------------------------------------------#

download_folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\download"
download_images = []
for file in os.listdir(download_folder):
    img_path = os.path.join(download_folder, file)
    download_images.append(img_path)

download_img_file = []
for img_path in download_images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    download_img_file.append(img)

img_x = 300
image_path=0
download_img_label=[]
for pic in download_img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, home_images=home_images,image_path=image_path:code(home_images[image_path]))
 download_img_label.append(label)
 image_path += 1

#---------------------------------------------favorate images--------------------------------------------------------------#

favorate_folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\favorate"
favorate_images = []
for file in os.listdir(favorate_folder):
    img_path = os.path.join(favorate_folder, file)
    favorate_images.append(img_path)

favorate_img_file = []
for img_path in favorate_images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    favorate_img_file.append(img)

img_x = 300
image_path=0
favorate_img_label=[]
for pic in favorate_img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, home_images=home_images,image_path=image_path:code(home_images[image_path]))
 favorate_img_label.append(label)
 image_path += 1

#---------------------------------------------social media images--------------------------------------------------------------#

social_media_folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\social media"
social_media_images = []
for file in os.listdir(social_media_folder):
    img_path = os.path.join(social_media_folder, file)
    social_media_images.append(img_path)

social_media_img_file = []
for img_path in social_media_images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    social_media_img_file.append(img)

img_x = 300
image_path=0
social_media_img_label=[]
for pic in social_media_img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, home_images=home_images,image_path=image_path:code(home_images[image_path]))
 social_media_img_label.append(label)
 image_path += 1

#---------------------------------------------Track images--------------------------------------------------------------#

'''folder = "C:\\Users\\gowrishankar\\Desktop\\projects\\major\\build\\img\\home"
images = []

for file in os.listdir(folder):
    img_path = os.path.join(folder, file)
    images.append(img_path)

img_file = []
for img_path in images:
    img = Image.open(img_path).convert("RGBA")
    img.thumbnail((70, 70))

    img = ImageTk.PhotoImage(img)
    img_file.append(img)

img_x = 300
image_path=0
home_label=[]
for pic in img_file:

 label=Label(window,image=pic)
 label.bind("<Button-1>",lambda event, images=images,image_path=image_path:code(images[image_path]))
 home_label.append(label)
 image_path += 1'''

def onclick(event):

    canvas_id = event.widget.find_withtag(tk.CURRENT)  # Get the item ID under the cursor
    if canvas_id:
        clicked_item = event.widget.gettags(canvas_id[0])  # Get the tags associated with the item

        if 'home_gif_frames' in clicked_item:
            forget()

            global image_path
            img_x = 300

            for label in home_img_label:
             label.place(x=img_x, y=200)
             img_x += 100

        if 'camera_gif_frames' in clicked_item:
            forget()
            camera_label.place(x=500,y=500)

            global image_path
            img_x = 300

            for label in camera_img_label:
                label.place(x=img_x, y=200)
                img_x += 100

        if 'download_gif_frames' in clicked_item:
            forget()

            global image_path
            img_x = 300

            for label in download_img_label:
                label.place(x=img_x, y=200)
                img_x += 100

        if 'favorate_gif_frames' in clicked_item:
            forget()

            global image_path
            img_x = 300

            for label in favorate_img_label:
                label.place(x=img_x, y=200)
                img_x += 100

        if 'social_media_gif_frames' in clicked_item:
            forget()

            global image_path
            img_x = 300

            for label in social_media_img_label:
                label.place(x=img_x, y=200)
                img_x += 100

def secure_on_click(event):
    print('secure')
    secure()
    forget()

def track_on_click(event):
    print('track')
    forget()

def forget():

  global home_img_label
  for label in home_img_label:
      label.place_forget()
  camera_label.place_forget()

  for label in camera_img_label:
      label.place_forget()

  for label in download_img_label:
      label.place_forget()

  for label in favorate_img_label:
      label.place_forget()

  for label in social_media_img_label:
      label.place_forget()



bg_video()

window.resizable(False,False)
window.mainloop()





