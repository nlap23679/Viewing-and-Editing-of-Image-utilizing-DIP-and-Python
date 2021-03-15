import PySimpleGUI as sg
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
import matplotlib.pyplot as plt

first_line = [sg.FileBrowse(), sg.Input(key="filepath")]
second_line = [sg.Button("Original Image", key="Original Image", size=(15, 1)),
               sg.Button("Contour", key="Contour", size=(15, 1)),
               sg.Button("Blur", key="Blur", size=(15, 1))]
third_line = [sg.Save(key="Save"), sg.Cancel()]
image_line = [sg.Image(key="showimage"), sg.Image(key="edit_image")]

layout = [first_line, second_line, third_line, image_line]
Title = "Image Viewer and Editor"

window = sg.Window(Title, layout)

while True:
    event, value = window.read()
    im_path = value["filepath"]

    if event == "Original Image":
        im = Image.open(im_path)
        window["showimage"].update(data=ImageTk.PhotoImage(im))

    if event == "Contour":
        im = Image.open(im_path)
        new_im = im.filter(ImageFilter.EMBOSS)
        #new_im = show()

    if event == "Blur":
        im = Image.open(im_path)
        new_im = im.filter(ImageFilter.BLUR)
        window["edit_image"].update(data=ImageTk.PhotoImage(new_im))

    if event == "Save":
        im.save('new_im.jpg')

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
window.close()
