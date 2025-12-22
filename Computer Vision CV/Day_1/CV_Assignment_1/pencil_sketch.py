import cv2
import numpy as np
import customtkinter as Ctk
from PIL import Image
from tkinter import filedialog

Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

class GUI(Ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500")
        self.after(0,self.fullscreen)
        self.title("SKETCHER PRO")
        self.grid_columnconfigure(1,weight = 1)
        self.grid_rowconfigure(0,weight = 1)
        self.image_address = None
        self.original_image = None
        self.kernel_size_value = 27
        self.final_image = None

        self.sidebar_frame = Ctk.CTkFrame(self,width = 400, corner_radius=15,fg_color = 'grey')
        self.sidebar_frame.grid(row=0,column=0,sticky ='nsew',padx=(20,0),pady =20)
        self.sidebar_frame.grid_propagate(False)

        self.main_frame = Ctk.CTkFrame(self,corner_radius = 15,fg_color='grey')
        self.main_frame.grid(row=0,column=1,sticky = 'nsew',padx=20,pady =20)
        self.main_frame.grid_rowconfigure(0,weight=0)
        self.main_frame.grid_rowconfigure(1,weight=1)
        self.main_frame.grid_columnconfigure(0,weight=1)

        self.top_main_frame = Ctk.CTkFrame(self.main_frame,corner_radius=15,fg_color="black")
        self.top_main_frame.grid(row = 0,column = 0,sticky = 'nsew',padx = 10,pady = 10)
        self.top_main_frame.grid_columnconfigure(0,weight=1)
        self.top_main_frame.grid_columnconfigure(1,weight=0)

        self.input_box = Ctk.CTkEntry(self.top_main_frame,placeholder_text="Enter file path",font=("Roboto", 24, "normal"))
        self.input_box.grid(row=0,column=0,sticky = 'nsew',padx=10,pady=10)

        self.submit_image_button = Ctk.CTkButton(self.top_main_frame,text = "Submit",font=("Roboto", 24, "normal"),command=self.submit)
        self.submit_image_button.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)

        self.bottom_main_frame = Ctk.CTkFrame(self.main_frame,corner_radius=15,fg_color='black')
        self.bottom_main_frame.grid(row=1,column= 0,sticky ='nsew',padx = 10,pady=10)
        self.bottom_main_frame.grid_columnconfigure(0,weight=1,uniform='half_split')
        self.bottom_main_frame.grid_columnconfigure(1,weight=1,uniform='half_split')
        self.bottom_main_frame.grid_rowconfigure(0,weight=1)

        self.original_image_label = Ctk.CTkLabel(self.bottom_main_frame,text='Original Image',font = ("Arial",30,"normal"),fg_color = 'grey',corner_radius=15)
        self.original_image_label.grid(row=0,column=0,sticky = 'nsew', padx=(20,20),pady = 20)

        self.final_image_label = Ctk.CTkLabel(self.bottom_main_frame,text='Final Image',font = ("Arial",30,"normal"),fg_color = 'grey',corner_radius=15)
        self.final_image_label.grid(row=0,column=1,sticky = 'nsew', padx=(20,20),pady = 20)

        self.sidebar_frame.grid_columnconfigure(0,weight = 1)
        self.sidebar_frame.grid_rowconfigure(2,weight=1)

        self.app_title_label = Ctk.CTkLabel(self.sidebar_frame,text="SKETCHER PRO",fg_color="black",font=("Arial",20,"bold"),corner_radius=15)
        self.app_title_label.grid(row=0,column=0,padx=10,pady=20,sticky='nsew')

        self.mode = Ctk.CTkSegmentedButton(self.sidebar_frame,values=["Grayscale","Color"],fg_color="black",font=("Arial",20,"bold"),corner_radius=15,command = self.trigger_conversion)
        self.mode.grid(row=1,column = 0,padx=10,pady=10,sticky='nsew')
        self.mode.set("Color")
        
        self.kernel_size = Ctk.CTkSlider(self.sidebar_frame,from_=3,to=51,number_of_steps=24,corner_radius=15,orientation="vertical",command=self.read_kernel_value)
        self.kernel_size.grid(row=2,column=0,padx=10,pady=10,sticky='ns')

        self.kernel_size_label = Ctk.CTkLabel(self.sidebar_frame,fg_color = "black",text="27.0",font=("Arial",20,"bold"),corner_radius=15)
        self.kernel_size_label.grid(row=3,column=0,padx=10,pady=10,sticky ='nsew')

        self.save_button = Ctk.CTkButton(self.sidebar_frame,text="Save",font=("Arial",20,"bold"),corner_radius=15,command=self.save)
        self.save_button.grid(row=4,column=0,sticky ='nsew',padx=10,pady=20)

    
    def fullscreen(self):
        try:
            self.state("zoomed")
        except Exception:
            self.attributes('-zoomed',True)

    def submit(self):
        self.image_address = self.input_box.get()
        self.original_image = cv2.imread(self.image_address)
        if self.original_image is None:
            self.original_image_label.configure(text = "File not Found",image = None)
            self.final_image_label.configure(text='Final Image',font = ("Arial",30,"normal"),image = None)
            return
        available_width = max(self.original_image_label.winfo_width()-20,1)
        available_height = max(self.original_image_label.winfo_height()-20,1)
        rgb_img = cv2.cvtColor(self.original_image,cv2.COLOR_BGR2RGB)
        PIL_img = Image.fromarray(rgb_img)
        img_w,img_h = PIL_img.size
        ratio = min(available_width/img_w,available_height/img_h)
        CTkimg = Ctk.CTkImage(light_image=PIL_img,dark_image=PIL_img,size=(int(img_w*ratio),int(img_h*ratio)))
        self.original_image_label.configure(image = CTkimg,text='')
        self.trigger_conversion()
    
    def read_kernel_value(self,value):
        self.kernel_size_label.configure(text=value)
        self.kernel_size_value = int(value)
        self.trigger_conversion()

    def read_mode(self):
        current_mode = self.mode.get()
        return current_mode
    
    def grayscale_conversion(self):
        self.final_image_label.configure(text="",image = '')
        self.update_idletasks()
        grayscale_img = cv2.cvtColor(self.original_image,cv2.COLOR_BGR2GRAY).astype(np.float32)
        inverted_grayscale_img = 255-grayscale_img
        inverted_grayscale_blurred_img = cv2.GaussianBlur(inverted_grayscale_img,(int(self.kernel_size_value),int(self.kernel_size_value)),0)
        self.final_image = np.zeros(grayscale_img.shape).astype(np.float32)
        for i in range(grayscale_img.shape[0]):
            for j in range(grayscale_img.shape[1]):
                if inverted_grayscale_blurred_img[i,j] != 0:
                    self.final_image[i,j] = (grayscale_img[i,j]*256)/(255-inverted_grayscale_blurred_img[i,j])
                else:
                    self.final_image[i,j] = 255


        self.final_image = np.clip(self.final_image,0,255).astype(np.uint8)
        self.display_final_image(8)

    def color_conversion(self):
        self.final_image_label.configure(text="",image = '')
        self.update_idletasks()
        hsv_image = cv2.cvtColor(self.original_image,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv_image)
        s=(s*0.7).astype(np.uint8)
        self.final_image_label.configure(text="",image = '')
        self.update_idletasks()
        grayscale_img = cv2.cvtColor(self.original_image,cv2.COLOR_BGR2GRAY).astype(np.float32)
        inverted_grayscale_img = 255-grayscale_img
        inverted_grayscale_blurred_img = cv2.GaussianBlur(inverted_grayscale_img,(int(self.kernel_size_value),int(self.kernel_size_value)),0)
        self.final_image = np.zeros(grayscale_img.shape).astype(np.float32)
        for i in range(grayscale_img.shape[0]):
            for j in range(grayscale_img.shape[1]):
                if inverted_grayscale_blurred_img[i,j] != 0:
                    self.final_image[i,j] = (grayscale_img[i,j]*256)/(255-inverted_grayscale_blurred_img[i,j])
                else:
                    self.final_image[i,j] = 255
        self.final_image = np.clip(self.final_image,0,255).astype(np.uint8)

        self.final_image = cv2.merge([h,s,self.final_image])
        self.display_final_image(55)

    def display_final_image(self,mode):
        available_width = max(self.final_image_label.winfo_width()-20,1)
        available_height = max(self.final_image_label.winfo_height()-20,1)
        rgb_img = cv2.cvtColor(self.final_image,mode)
        PIL_img = Image.fromarray(rgb_img)
        img_w,img_h = PIL_img.size
        ratio = min(available_width/img_w,available_height/img_h)
        CTkimg = Ctk.CTkImage(light_image=PIL_img,dark_image=PIL_img,size=(int(img_w*ratio),int(img_h*ratio)))
        self.final_image_label.configure(image = CTkimg,text='')

    def trigger_conversion(self,value='Grayscale'):
        if self.original_image is None:
            return 
        value=self.mode.get()
        if value == 'Grayscale':
            self.grayscale_conversion()
        else:
            self.color_conversion()

    def save(self):
        if self.final_image is None:
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension = ".png"
        )

        if not file_path:
            return

        if self.mode.get() == "Grayscale":
            rgb_img = cv2.cvtColor(self.final_image, cv2.COLOR_GRAY2RGB)
            PIL_img = Image.fromarray(rgb_img)
            PIL_img.save(file_path)
        else:
            rgb_img = cv2.cvtColor(self.final_image, cv2.COLOR_HSV2RGB)
            PIL_img = Image.fromarray(rgb_img)
            PIL_img.save(file_path)
        

def main():
    
    Sketcher_pro = GUI()
    Sketcher_pro.mainloop()

main()



