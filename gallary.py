def fun(image_path):
    from tkinter import Tk,Label,PhotoImage
    from PIL import Image
    from img import extract




    image=Image.open(image_path)
    image.show()
    print("gallery file executed to img file")
    extract(image_path)


    print("gallery file executed")

    '''
    
    window=Tk()
    window_width=window.winfo_screenwidth()
    window_height=window.winfo_screenheight()

    window.geometry("1366x768")

    img=PhotoImage(file=image_path)
    img_width=img.width()
    img_height=img.height()


    x=(window_width-img_width)//2
    y=(window_height-img_height)//2

    label=Label(image=img)
    label.place(x=x,y=y,width=img_width,height=img_height)
    window.mainloop()

    '''




