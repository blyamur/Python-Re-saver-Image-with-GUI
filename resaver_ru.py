import os
import shutil
import random
import string
import webbrowser
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance

__author__ = "Mons (https://blog.mons.ws) https://github.com/blyamur/"

new = 1
url = "https://blog.mons.ws"
root = Tk()
root.title("Image Re-save \ Пересохранялка") #заголовок окна
root.configure(background='#7267BE') #общий цвет фона окна
#factor = 1   #степень улучшения изображения (раскомментируем если вас не устраивает качество)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2 
w = w - 200 # смещение от середины
h = h - 200
root.geometry('460x210+{}+{}'.format(w, h)) #поиск центра экрана и размещение окна по центру

#root.wm_iconbitmap('icon.ico') #при наличия необходимости иметь в приложении иконку, раскомментируем
#root.maxsize('460', '230') #раскомментируем  при необходимости изменять размер окна
#root.minsize('460', '230') #раскомментируем  при необходимости изменять размер окна
root.resizable(False, False) #запретить изменение размеров. Комментируем  при необходимости изменять размер окна
def open_file():
	try:
		file_open = filedialog.askopenfilename(title='Пожалуйста выберите Изображение', filetypes=[('Image Files', ['.jpeg', '.jpg', '.png'])])
		full_name = path.basename(file_open) #Текущее название изображения
		file_dir = os.path.dirname(os.path.abspath(file_open)) #путь к папке источнику
		dir_name = path.splitext(full_name)[0] #название
		new_name = ''.join(random.choice(string.ascii_letters) for _ in range(16))+'_'+dir_name #Новое название
		ext_name = path.splitext(full_name)[1] #Расширение
		fl = Label(text=str(full_name[:45])+'...', foreground="#FFE15F",background="#7267BE", #Текущее название 45 знаков
			padx="2", pady="2", font="8").place(relx = 0.5, 
			rely = 0.65,
			anchor = 'center')
		if ext_name.lower().endswith(('.jpeg', '.jpg', '.png')):
			try:
				img = Image.open(file_open)
				#enhancer = ImageEnhance.Sharpness(img) #(раскомментируем если вас не устраивает качество)
				#img = enhancer.enhance(factor) #(раскомментируем если вас не устраивает качество)
				#изображение сохраняется как BMP
				img.save(file_dir + '/' + new_name + '.bmp')
				#изображение повторно открывается
				imgs = Image.open(file_dir + '/' + new_name + '.bmp')
				#изображение сохраняется под новым названием и старым расширением
				imgs.save(file_dir + '/' + new_name + ext_name)
				#изображение  BMP удаляется
				os.remove(file_dir + '/' + new_name + '.bmp')
				messagebox.showinfo("Готово"," Изображение пересохранено!\n" ) #Image re-saved
			except:
				messagebox.showerror("Ошибка", " Что-то пошло не так!") #Something went wrong
		else:
			messagebox.showerror("Ошибка", " Вы не выбрали файл!") #You haven't selected a file
	except:
		messagebox.showerror("Ошибка", " Перезапустите программу!") #Restart the program

def openweb():
	webbrowser. open(url, new=new)

Label(root, text = 'Выберите Изображение [.JPG,.PNG]',font =('Verdana', 12),foreground=('#FFF'),background=('#7267BE')).pack(side = TOP, pady = 10) # Select an image
errmsg = 'Error!'
select_button = Button(text="Выбрать файл",background="#625292",foreground="#FFFFFF",padx="10",pady="8",border="0",font="16",command=open_file).place(relx = 0.5,rely = 0.45,anchor = 'center') # Select a file
copy_right = Button(text="© 2021 Mons", foreground="#FFF",background="#7267BE", activebackground="#7267BE",border="0",activeforeground="#7AB900",
				padx="15", pady="6", font=("Verdana", 8),cursor="hand2",relief=FLAT,command=openweb).pack(side=BOTTOM)
root.mainloop()
