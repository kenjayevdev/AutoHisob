from tkinter import*
import random
import os
from tkinter import messagebox
from datetime import datetime

# ============main============================

class BillApp:
    def __init__(self, root):
        self.root = root
        
        self.root.geometry("1350x700+0+0")
        self.root.title("💻 AutoHisob")
        bg_color = "#26272C"
        title = Label(self.root, text="💻 AutoHisob", font=("Segoe UI", 20, "bold"), pady=2, bd=12, bg="#00BCD4", fg="#FFFFFF", relief=GROOVE)
        title.pack(fill=X)
        
    # ================variables=======================
    
        self.apple = IntVar()
        self.pear = IntVar()
        self.peach = IntVar()
        self.pomegranate = IntVar()
        self.lemon = IntVar()
        self.fig = IntVar()
        
    # ============groceries==============================
       
        self.rice = IntVar()
        self.carrot = IntVar()
        self.potato = IntVar()
        self.beans = IntVar()
        self.onion = IntVar()
        self.oil = IntVar()
        
        
        self.coca_cola = IntVar()
        self.gorilla = IntVar()
        self.pepsi = IntVar()
        self.mojito = IntVar()
        self.fanta = IntVar()
        self.flash = IntVar()
        
    
        self.fruits_price = StringVar()
        self.groceries_price = StringVar()
        self.drinks_price = StringVar()
        
    
        self.customer_name = StringVar()
        self.customer_phone = StringVar()
        self.bill_number = StringVar()
        x = random.randint(1000, 9999)
        self.bill_number.set(str(x))
        self.search_bill = StringVar()
        
    
        self.fruits_tax = StringVar()
        self.groceries_tax = StringVar()
        self.drinks_tax = StringVar()
        
    
        F1 = LabelFrame(self.root, text="Mijoz Tafsilotlari", font=('Arial', 14, 'bold'), bd=10, fg="#FFFFFF", bg="#1E1E2E")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Mijoz Nomi:", bg="#1E1E2E", fg="#F5F5F5", font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.customer_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Mijoz Telefoni:", bg="#1E1E2E", fg="#F5F5F5", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.customer_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Hisob Raqami:", bg="#1E1E2E", fg="#F5F5F5", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Qidirish", command=self.find_bill, width=10, bd=7, bg="#535C68", fg="#F5F5F5", font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    
        F2 = LabelFrame(self.root, text="Mevalar", font=('Arial', 14, 'bold'), bd=10, fg="#FFFFFF", bg="#000000")
        F2.place(x=5, y=180, width=325, height=380)

        apple_lbl = Label(F2, text="Olma", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        apple_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        apple_txt = Entry(F2, width=10, textvariable=self.apple, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        apple_txt.grid(row=0, column=1, padx=10, pady=10)

        pear_lbl = Label(F2, text="Nok", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        pear_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        pear_txt = Entry(F2, width=10, textvariable=self.pear, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pear_txt.grid(row=1, column=1, padx=10, pady=10)

        peach_lbl = Label(F2, text="Shaftoli", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        peach_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        peach_txt = Entry(F2, width=10, textvariable=self.peach, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        peach_txt.grid(row=2, column=1, padx=10, pady=10)

        pomegranate_lbl = Label(F2, text="Anor", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        pomegranate_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        pomegranate_txt = Entry(F2, width=10, textvariable=self.pomegranate, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pomegranate_txt.grid(row=3, column=1, padx=10, pady=10)

        lemon_lbl = Label(F2, text="Limon", font =('times new roman', 16, 'bold'), bg = "#000000", fg = "#F5F5F5")
        lemon_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        lemon_txt = Entry(F2, width=10, textvariable=self.lemon, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        lemon_txt.grid(row=4, column=1, padx=10, pady=10)

        fig_lbl = Label(F2, text="Anjir", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        fig_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        fig_txt = Entry(F2, width=10, textvariable=self.fig, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fig_txt.grid(row=5, column=1, padx=10, pady=10)

    
        F3 = LabelFrame(self.root, text="Oziq-Ovqat Mahsulotlari", font=('Arial', 14, 'bold'), bd=10, fg="#FFFFFF", bg="#000000")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Guruch", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        carrot_lbl = Label(F3, text="Sabzi", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        carrot_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        carrot_txt = Entry(F3, width=10, textvariable=self.carrot, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        carrot_txt.grid(row=1, column=1, padx=10, pady=10)

        potato_lbl = Label(F3, text="Kartoshka", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        potato_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        potato_txt = Entry(F3, width=10, textvariable=self.potato, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        potato_txt.grid(row=2, column=1, padx=10, pady=10)

        beans_lbl = Label(F3, text="Loviya", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        beans_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        beans_txt = Entry(F3, width=10, textvariable=self.beans, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        beans_txt.grid(row=3, column=1, padx=10, pady=10)

        onion_lbl = Label(F3, text="Piyoz", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        onion_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        onion_txt = Entry(F3, width=10, textvariable=self.onion, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        onion_txt.grid(row=4, column=1, padx=10, pady=10)

        oil_lbl = Label(F3, text="Yog'", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        oil_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        oil_txt = Entry(F3, width=10, textvariable=self.oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        oil_txt.grid(row=5, column=1, padx=10, pady=10)

    
        F4 = LabelFrame(self.root, text="Sovuq Ichimliklar", font=('Arial', 14, 'bold'), bd=10, fg="#FFFFFF", bg="#000000")
        F4.place(x=670, y=180, width=325, height=380)

        coca_cola_lbl = Label(F4, text="Coca-Cola", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        coca_cola_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        coca_cola_txt = Entry(F4, width=10, textvariable=self.coca_cola, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coca_cola_txt.grid(row=0, column=1, padx=10, pady=10)

        gorilla_lbl = Label(F4, text="Gorilla", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        gorilla_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        gorilla_txt = Entry(F4, width=10, textvariable=self.gorilla, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        gorilla_txt.grid(row=1, column=1, padx=10, pady=10)

        pepsi_lbl = Label(F4, text="Pepsi", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        pepsi_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        pepsi_txt = Entry(F4, width=10, textvariable=self.pepsi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pepsi_txt.grid(row=2, column=1, padx=10, pady=10)

        mojito_lbl = Label(F4, text="Moxito", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        mojito_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        mojito_txt = Entry(F4, width=10, textvariable=self.mojito, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mojito_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        flash_lbl = Label(F4, text="Flash", font=('times new roman', 16, 'bold'), bg="#000000", fg="#F5F5F5")
        flash_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        flash_txt = Entry(F4, width=10, textvariable=self.flash, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flash_txt.grid(row=5, column=1, padx=10, pady=10)
    
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Hisob Varaqa", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    
        F6 = LabelFrame(self.root, text="Jami Hisob", font=('Arial', 14, 'bold'), bd=10, fg="#FFFFFF", bg="#1E1E2E")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Mevalar Narx", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.fruits_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Oziq-Ovqat Narxi", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.groceries_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Sovuq Ichimliklar Narxi", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Solig'i", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.fruits_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Solig'i", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.groceries_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Solig'i", font=('times new roman', 14, 'bold'), bg="#1E1E2E", fg="#F5F5F5")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)
    
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Jami", bg="#4CAF50", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.generate_bill, text="Chek Yaratish", bd=2, bg="#2196F3", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Tozalash", bg="#FF9800", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Chiqish", bd=2, bg="#F44336", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        #fruits
        self.f_p_p = self.peach.get()*10000
        self.f_a_p = self.apple.get()*15000
        self.f_pe_p = self.pear.get()*20000
        self.f_po_p = self.pomegranate.get()*30000
        self.f_l_p = self.lemon.get()*25000
        self.f_f_p = self.fig.get()*35000
        self.total_fruits_price = float(self.f_pe_p+self.f_p_p+self.f_po_p+self.f_l_p+self.f_f_p+self.f_a_p)

        self.fruits_price.set(str(self.total_fruits_price) + " UZS ")
        self.f_tax = round((self.total_fruits_price*0.05), 2)
        self.fruits_tax.set(str(self.f_tax) + " UZS ")
        #groceries
        self.g_r_p = self.rice.get()*20000
        self.g_c_p = self.carrot.get()*10000
        self.g_p_p = self.potato.get()*8000
        self.g_b_p = self.beans.get()*7000
        self.g_o_p = self.onion.get()*6000
        self.g_oi_p = self.oil.get()*22000
        self.total_groceries_price = float(self.g_r_p+self.g_c_p+self.g_p_p+self.g_b_p+self.g_o_p+self.g_oi_p)

        self.groceries_price.set(str(self.total_groceries_price) + " UZS ")
        self.g_tax = round((self.total_groceries_price*0.2), 2)
        self.groceries_tax.set(str(self.g_tax) + " UZS ")
        #drinks
        self.d_c_p = self.coca_cola.get()*15000
        self.d_g_p = self.gorilla.get()*12000
        self.d_p_p = self.pepsi.get()*14000
        self.d_m_p = self.mojito.get()*13000
        self.d_f_p = self.fanta.get()*15000
        self.d_fl_p = self.flash.get()*12000
        self.total_drinks_price = float(self.d_c_p+self.d_g_p+self.d_p_p+self.d_m_p+self.d_f_p+self.d_fl_p)

        self.drinks_price.set(str(self.total_drinks_price) + " UZS ")
        self.d_tax = round((self.total_drinks_price * 0.1), 2)
        self.drinks_tax.set(str(self.d_tax) + " UZS ")

        self.total_bill = float(self.total_fruits_price+self.total_groceries_price+self.total_drinks_price+self.f_tax+self.g_tax+self.d_tax)

#==============welcome-bill==============================

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        today = datetime.today()
        date = today.strftime("%d.%m.%Y")
        self.txtarea.insert(END, "\tXaridingiz Uchun Tashakkur\n")
        self.txtarea.insert(END, f"\nBugun: {date}")
        self.txtarea.insert(END, f"\nHisob Raqami: {self.bill_number.get()}")
        self.txtarea.insert(END, f"\nMijoz Nomi: {self.customer_name.get()}")
        self.txtarea.insert(END, f"\nTelefon Raqami: {self.customer_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Mahsulotlar\t\tMiqdor\t\tNarxi")


    def generate_bill(self):
        if self.customer_name.get() == "" or self.customer_phone.get() == "":
            messagebox.showerror("Xatolik", "Mijoz Tafsilotlari Majburiy")
        elif self.fruits_price.get() == "UZS 0.0" and self.groceries_price.get() == "UZS 0.0" and self.drinks_price.get()=="UZS 0.0":
            messagebox.showerror("Xatolik", "Hech qanday mahsulot sotib olinmagan")
        else:
            self.welcome_bill()
            
    
        if self.apple.get() != 0:
            self.txtarea.insert(END, f"\n Olma\t\t{self.apple.get()}\t\t{self.f_a_p}")
        if self.pear.get() != 0:
            self.txtarea.insert(END, f"\n Nok\t\t{self.pear.get()}\t\t{self.f_pe_p}")
        if self.peach.get() != 0:
            self.txtarea.insert(END, f"\n Shaftoli\t\t{self.peach.get()}\t\t{self.f_p_p}")
        if self.pomegranate.get() != 0:
            self.txtarea.insert(END, f"\n Anor\t\t{self.pomegranate.get()}\t\t{self.f_po_p}")
        if self.lemon.get() != 0:
            self.txtarea.insert(END, f"\n Limon\t\t{self.lemon.get()}\t\t{self.f_l_p}")
        if self.fig.get() != 0:
            self.txtarea.insert(END , f"\n Anjir\t\t{self.fig.get()}\t\t{self.f_f_p}")
            
    
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Guruch\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.carrot.get() != 0:
            self.txtarea.insert(END, f"\n Sabzi\t\t{self.carrot.get()}\t\t{self.g_c_p}")
        if self.potato.get() != 0:
            self.txtarea.insert(END, f"\n Kartoshka\t\t{self.potato.get()}\t\t{self.g_p_p}")
        if self.beans.get() != 0:
            self.txtarea.insert(END, f"\n Loviya\t\t{self.beans.get()}\t\t{self.g_b_p}")
        if self.onion.get() != 0:
            self.txtarea.insert(END, f"\n Piyoz\t\t{self.onion.get()}\t\t{self.g_o_p}")
        if self.oil.get() != 0:
            self.txtarea.insert(END, f"\n Yog'\t\t{self.oil.get()}\t\t{self.g_oi_p}")
            
        
        if self.coca_cola.get() != 0:
            self.txtarea.insert(END, f"\n Coca-Cola\t\t{self.coca_cola.get()}\t\t{self.d_c_p}")
        if self.gorilla.get() != 0:
            self.txtarea.insert(END, f"\n Gorilla\t\t{self.gorilla.get()}\t\t{self.d_g_p}")
        if self.pepsi.get() != 0:
            self.txtarea.insert(END, f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_p_p}")
        if self.mojito.get() != 0:
            self.txtarea.insert(END, f"\n Moxito\t\t{self.mojito.get()}\t\t{self.d_m_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
        if self.flash.get() != 0:
            self.txtarea.insert(END, f"\n Flash\t\t{self.flash.get()}\t\t{self.d_fl_p}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            
        
        if self.fruits_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n\n Mevalar Solig'i\t\t\t{self.fruits_tax.get()}")
        if self.groceries_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Oziq-Ovqat Solig'i\t\t\t{self.groceries_tax.get()}")
        if self.drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Ichimliklar Solig'i\t\t\t{self.drinks_tax.get()}")

        self.txtarea.insert(END, f"\n\n Jami:\t\t\t {self.total_bill} UZS")
        self.txtarea.insert(END, f"\n--------------------------------------")
        self.save_bill()

    
    def save_bill(self):
        op = messagebox.askyesno("Hisobni saqlang", "Siz hisobni saqlamoqchimisiz?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            # Papka mavjudligini tekshirish
            if not os.path.exists("Saved"):
                os.makedirs("Saved")
            f1 = open("Saved/"+str(self.bill_number.get())+".txt", "w", encoding='utf-8')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saqlandi", f"Buyurtma raqami: {self.bill_number.get()} Muvaffaqiyatli Saqlandi ✅")
        else:
           return

    
    def find_bill(self):
        """Hisobni qidirish funksiyasi"""
        try:
            if not self.search_bill.get():
                messagebox.showerror("Xatolik", "Iltimos, hisob raqamini kiriting")
                return
                
            # Papka mavjudligini tekshirish
            if not os.path.exists("Saved"):
                messagebox.showerror("Xatolik", "Saqlangan hisoblar topilmadi")
                return
                
            file_path = f"Saved/{self.search_bill.get()}.txt"
            if os.path.exists(file_path):
                with open(file_path, "r", encoding='utf-8') as f1:
                    bill_data = f1.read()
                    self.txtarea.delete('1.0', END)
                    self.txtarea.insert(END, bill_data)
                messagebox.showinfo("Muvaffaqiyatli", f"Hisob {self.search_bill.get()} topildi")
            else:
                messagebox.showerror("Xatolik", "Hisob topilmadi")
        except Exception as e:
            messagebox.showerror("Xatolik", f"Hisobni yuklashda xatolik: {str(e)}")

    
    def clear_data(self):
        op = messagebox.askyesno("Tozalash", "Siz haqiqatan ham tozalashni xohlaysizmi?")
        if op > 0:
            self.apple.set(0)
            self.pear.set(0)
            self.peach.set(0)
            self.pomegranate.set(0)
            self.lemon.set(0)
            self.fig.set(0)
            
    
            self.rice.set(0)
            self.carrot.set(0)
            self.potato.set(0)
            self.beans.set(0)
            self.onion.set(0)
            self.oil.set(0)
            
    
            self.coca_cola.set(0)
            self.gorilla.set(0)
            self.pepsi.set(0)
            self.mojito.set(0)
            self.fanta.set(0)
            self.flash.set(0)
            
    
            self.fruits_price.set("")
            self.groceries_price.set("")
            self.drinks_price.set("")

            self.fruits_tax.set("")
            self.groceries_tax.set("")
            self.drinks_tax.set("")

            self.customer_name.set("")
            self.customer_phone.set("")

            self.bill_number.set("")
            x = random.randint(1000, 9999)
            self.bill_number.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    
    def exit_app(self):
        op = messagebox.askyesno("Chiqish", "Siz haqiqatan ham chiqishni xohlaysizmi?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = BillApp(root)
root.mainloop()