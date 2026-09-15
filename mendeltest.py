import customtkinter as ctk
from PIL import Image

# กำหนด Theme และสีพื้นหลัง
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TestApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mendle Test Application")
        self.geometry("900x600")

        # จัด Layout หลัก แบ่งเป็น 2 ฝั่ง (ซ้าย: Fixed / ขวา: Scrollable)
        self.grid_columnconfigure(0, weight=0)  # ฝั่งซ้ายขนาดคงที่
        self.grid_columnconfigure(1, weight=1)  # ฝั่งขวาขยายเต็มพื้นที่
        self.grid_rowconfigure(0, weight=1)

        self.setup_left_sidebar()
        self.setup_right_scroll_area()

    def setup_left_sidebar(self):
        # --- ฝั่งซ้าย (Fixed UI / ห้ามขยับ) ---
        left_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # หัวข้อ UI
        title_label = ctk.CTkLabel(left_frame, text="หน้า UI", font=("Kanit", 18, "bold"))
        title_label.pack(pady=(10, 5))

        # ส่วนเลือกระดับความยาก (Radio Buttons)
        difficulty_frame = ctk.CTkFrame(left_frame)
        difficulty_frame.pack(fill="x", padx=10, pady=10)

        diff_title = ctk.CTkLabel(difficulty_frame, text="ความยาก", font=("Kanit", 14, "bold"))
        diff_title.pack(pady=5)

        self.difficulty_var = ctk.StringVar(value="ประถม")
        
        radio_elem = ctk.CTkRadioButton(difficulty_frame, text="ประถม", value="ประถม", variable=self.difficulty_var)
        radio_elem.pack(anchor="w", padx=15, pady=5)
        
        radio_mid = ctk.CTkRadioButton(difficulty_frame, text="มัธยม", value="มัธยม", variable=self.difficulty_var)
        radio_mid.pack(anchor="w", padx=15, pady=5)
        
        radio_uni = ctk.CTkRadioButton(difficulty_frame, text="มหาลัย", value="มหาลัย", variable=self.difficulty_var)
        radio_uni.pack(anchor="w", padx=15, pady=5)

        # แสดงรูป/GIF ด้านล่างซ้าย
        gif_box = ctk.CTkFrame(left_frame, height=200)
        gif_box.pack(fill="both", expand=True, padx=10, pady=10)
        
        gif_label = ctk.CTkLabel(gif_box, text="[ รูป / GIF ]", font=("Kanit", 14))
        gif_label.place(relx=0.5, rely=0.5, anchor="center")

    def setup_right_scroll_area(self):
        # --- ฝั่งขวา (Scrollable Area) ---
        scroll_frame = ctk.CTkScrollableFrame(self)
        scroll_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # ชื่อหัวข้อหลัก
        header_label = ctk.CTkLabel(scroll_frame, text="Mendle test", font=("Kanit", 28, "bold"))
        header_label.pack(pady=10)

        # สร้างข้อคำถาม (เน้น 2 ข้อขึ้นไปเพื่อใช้งานระบบ Scroll)
        self.create_question_block(scroll_frame, q_num=1, text="คำถามข้อที่ 1: ...")
        self.create_question_block(scroll_frame, q_num=2, text="คำถามข้อที่ 2: ...")

    def create_question_block(self, parent, q_num, text):
        # โครงสร้างสำหรับแต่ละข้อคำถาม
        q_frame = ctk.CTkFrame(parent, fg_color="transparent")
        q_frame.pack(fill="x", pady=15, padx=10)

        # ข้อความคำถาม
        q_title = ctk.CTkLabel(q_frame, text=f"{q_num}. {text}", font=("Kanit", 18), anchor="w")
        q_title.pack(fill="x", pady=5)

        # พื้นที่แสดงรูปภาพคำถาม
        img_box = ctk.CTkFrame(q_frame, height=220)
        img_box.pack(fill="x", pady=10)
        
        img_label = ctk.CTkLabel(img_box, text="[ แสดงรูปภาพคำถาม ]", font=("Kanit", 14))
        img_label.place(relx=0.5, rely=0.5, anchor="center")

        # ปุ่มตัวเลือก 4 ช้อยส์ (2x2 Grid)
        btn_frame = ctk.CTkFrame(q_frame, fg_color="transparent")
        btn_frame.pack(fill="x", pady=5)
        
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        opt1 = ctk.CTkButton(btn_frame, text="ชั้น 1", font=("Kanit", 14), height=40)
        opt1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        opt2 = ctk.CTkButton(btn_frame, text="ชั้น 2", font=("Kanit", 14), height=40)
        opt2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        opt3 = ctk.CTkButton(btn_frame, text="ชั้น 3", font=("Kanit", 14), height=40)
        opt3.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        opt4 = ctk.CTkButton(btn_frame, text="ชั้น 4", font=("Kanit", 14), height=40)
        opt4.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
