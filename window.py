import datetime
from threading import Thread
from time import (sleep,strftime)
from os import (path, remove)

from tkinter import (BOTH, INSERT, END, Button, Entry, Frame,
    Text, IntVar, Label, Menu,StringVar, Tk, ttk, OptionMenu,
    LabelFrame,Checkbutton,SOLID, messagebox, Scrollbar,
    scrolledtext, Radiobutton, Toplevel)

from window_functions import Window_stuff_functions
from database import pc_data, expances_and_income

class Window_stuff(Frame, Window_stuff_functions):
    '''class window_stuff defines and puts widgets
    in main window or master window'''

    def __init__(self, master = None):
        Frame.__init__(self, master)
        Window_stuff_functions.__init__(self)
        self.master = master
        self.pack(expand=1, fill=BOTH)
        self.default_font = 'Consolas'
        self.default_frame_bg = '#f5f0e1'
        #self.config(bg=self.default_frame_bg)
        self.main_window_stuff()
        self.pc_not_run_dict = {}
        self.pc_run_dict = {}
        
    def main_window_stuff(self):
        #12345678901234567890123456789012345678901234567890123456789012345678901  72 lengh
        # master or root Settings (top header title and geometry)
        self.master.title('DotCom InterNet Public Service')
        self.master.geometry('1280x1024')
        self.master.protocol("WM_DELETE_WINDOW", lambda : 0)
        #self.master.iconbitmap('cafe.ico')

        # main frame title defined
        self.title = Label(self, text='DotCom InterNet Public Service',
            font=(self.default_font,25, 'bold'),
            bg='black',
            fg='white')
        self.title.pack(fill=BOTH)

        # Main menu defined
        self.menu_bar = Menu(self, bg='black',
            fg='white')
        self.master.config(menu=self.menu_bar)

        # Main menu headers Defined
        # file Header
        file_header = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='File',
            menu=file_header)
        file_header.add_command(label='Exit',
            command=self.master.destroy)
        # Edit Header
        edit_header = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Edit',
            menu=edit_header)
        edit_header.add_command(label='Settings',
            command=self.setting_frame)
        edit_header.add_command(label='Theme')
        edit_header.add_command(label='Font')
        # Account header
        account_header = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Account',
            menu=account_header)
        account_header.add_command(label='Administrator',
            command=lambda:self.password_page(self.administrator_page,'oknplm'))

        # PC frames in main frame defined
        self.frame_center = Frame(self)
        self.frame_center.pack(anchor='center')
        
        self.frame1 = Frame(self.frame_center, relief=SOLID, bd=1)
        self.frame1.grid(row=0, column=0, padx=15, pady=20, ipady=20, rowspan=20)
        spacing1 = Label(self.frame1, font=(self.default_font, 9),
        text='     PC      Time   Rs     Close  ', fg='white', bg='black')
        spacing1.grid(row=0,column=1, columnspan=5, pady=30, padx=5, sticky='W')
        self.frame2 = Frame(self.frame_center, relief=SOLID, bd=1)
        self.frame2.grid(row=0, column=1, padx=15, pady=20, ipady=20, rowspan=20)
        spacing2 = Label(self.frame2, font=(self.default_font, 9),
        text='     PC      Time   Rs     Close  ', fg='white', bg='black')
        spacing2.grid(row=0,column=1, columnspan=5, pady=30, padx=5, sticky='W')
        self.frame3 = Frame(self.frame_center, relief=SOLID, bd=1)
        self.frame3.grid(row=0, column=2, padx=15, pady=20, ipady=20, rowspan=20)
        spacing3 = Label(self.frame3, font=(self.default_font, 9),
        text='     PC      Time   Rs     Close  ', fg='white', padx=5, bg='black')
        spacing3.grid(row=0,column=1, columnspan=5, pady=30, padx=5, sticky='W')

        # income and expances frame
        self.expances_and_income_frame = Frame(self.frame_center, relief=SOLID, bd=1)
        self.expances_and_income_frame.grid(row=0, column=4, sticky='NS', pady=20, padx=15, rowspan=20)

        # Expances and income Entries
        expances_label = Label(self.expances_and_income_frame, text='Expances',font=(self.default_font,15), fg='white', bg='black')
        expances_label.grid(row=0, column=0, columnspan=2, sticky='EW', pady=20, padx=10)

        expances_label2 = Label(self.expances_and_income_frame, text='Description',font=(self.default_font))
        expances_label2.grid(row=1, column=0, sticky='e', pady=5, padx=10)

        expances_emtry = Entry(self.expances_and_income_frame, font=(self.default_font), width=10)
        expances_emtry.grid(row=1, column=1, sticky='E', pady=5, padx=10)

        expances_label3 = Label(self.expances_and_income_frame, text='Amount',font=(self.default_font))
        expances_label3.grid(row=2, column=0, sticky='E', pady=5, padx=10)

        

        expances_emtry2 = Entry(self.expances_and_income_frame, font=(self.default_font), width=10)
        expances_emtry2.grid(row=2, column=1, sticky='E', pady=5, padx=10)

        expances_button = Button(self.expances_and_income_frame, text='Done',font=(self.default_font,10),
                                 command=lambda:self.expances_done(expances_emtry, expances_emtry2), bg='gray88')
        expances_button.grid(row=3, column=1, sticky='E', pady=5, padx=10)


        income_label = Label(self.expances_and_income_frame, text='Income',font=(self.default_font,15), fg='white', bg='black')
        income_label.grid(row=4, column=0, columnspan=2, sticky='EW', padx=10, pady=20)

        income_label2 = Label(self.expances_and_income_frame, text='Description ',font=(self.default_font))
        income_label2.grid(row=5, column=0, sticky='E', pady=5, padx=10)

        income_label3 = Label(self.expances_and_income_frame, text='Amount ',font=(self.default_font))
        income_label3.grid(row=6, column=0, sticky='E', pady=5, padx=10)

        income_emtry = Entry(self.expances_and_income_frame, font=(self.default_font), width=10)
        income_emtry.grid(row=5, column=1, sticky='E', pady=5, padx=10)

        income_emtry2 = Entry(self.expances_and_income_frame, font=(self.default_font), width=10)
        income_emtry2.grid(row=6, column=1, sticky='E', pady=5, padx=10)

        income_button = Button(self.expances_and_income_frame, text='Done',font=(self.default_font,10),
                               command=lambda:self.income_done(income_emtry, income_emtry2), bg='gray88')
        income_button.grid(row=7, column=1, sticky='E', pady=5, padx=10)
        ## final close button
        self.final_close = Button(self.expances_and_income_frame,
                            text='Final Close',
                            font=(self.default_font,10, 'bold'),
                            bd=2,
                            bg='gray88',
                            state='disabled',
                            command=lambda:self.delete_final_date_file(self))
        self.final_close.grid(row=9, column=0, columnspan=2, padx=15, pady=20, sticky='EW')

        ## Change pc button
        self.change_pc_b = Button(self.expances_and_income_frame,
                            text='Change Pc',
                            font=(self.default_font,10, 'bold'),
                            bd=2,
                            bg='gray88',
                            state='disabled',
                            command=self.change_pc)
        self.change_pc_b.grid(row=12, column=0, columnspan=2, padx=15, pady=20, sticky='EW')

        ## Account button
        self.account_b = Button(self.expances_and_income_frame,
                            text='Today Account',
                            font=(self.default_font,10, 'bold'),
                            bd=2,
                            bg='gray88',
                            command=lambda:self.password_page(self.define_today_frame, 'Ahsan'))
        self.account_b.grid(row=8, column=0, columnspan=2, padx=15, pady=20, sticky='EW')

        self.customer = Button(self.expances_and_income_frame,
                            text='Customer Detail',
                            font=(self.default_font,10, 'bold'),
                            bd=2,
                            bg='gray88',
                            command=lambda:self.customer_detail())
        self.customer.grid(row=10, column=0, columnspan=2, padx=15, pady=20, sticky='EW')

        self.customer_detail_pop_b = Button(self.expances_and_income_frame,
                            text='Add Contact',
                            font=(self.default_font,10, 'bold'),
                            bd=2,
                            bg='gray88',
                            command=lambda:self.customer_detail_popup())
        self.customer_detail_pop_b.grid(row=11, column=0, columnspan=2, padx=15, pady=20, sticky='EW')
        
    def setting_frame(self):
        self.main_frame_forget(self)
        self.frame_setting = Frame(self.master)
        self.frame_setting.pack(fill=BOTH, expand=1)

        notebook = ttk.Notebook(self.frame_setting)
        notebook.pack(fill=BOTH, expand=1)

        tab1_frame = Frame(self.frame_setting, bg='blue')
        tab2_frame = Frame(self.frame_setting,bg='gray')

        notebook.add(tab1_frame, text='Host list')
        notebook.add(tab2_frame, text='tab-2 frame')

        self.back_button = Button(tab1_frame, text='<--Back', command=lambda:self.current_frame_forget(self, self.frame_setting))
        self.back_button.pack()
        self.back_button2 = Button(tab2_frame, text='<--Back', command=lambda:self.current_frame_forget(self, self.frame_setting))
        self.back_button2.pack()
        
    def password_page(self, frame, passwd_for_password_page):
        self.main_frame_forget(self)
        
        self.passwd_page = Frame(self.master)
        self.passwd_page.pack(fill=BOTH, expand=1)

        self.a_today_default_font = 'Consolas'
        back_button = Button(self.passwd_page, text='<--Back', command=lambda:self.current_frame_forget(self, self.passwd_page))
        back_button.pack(anchor='nw',pady=10,padx=10)

        self.l = LabelFrame(self.passwd_page,text='Password Page',font=(self.a_today_default_font,20))
        self.l.pack(fill=BOTH,expand=1)

        self.passwd_label = Label(self.l,text='Enter password', font=(self.a_today_default_font,20))
        self.passwd_label.pack()

        self.passwd_entry_var = StringVar()
        self.passwd_entry = Entry(self.l,show="*",textvariable=self.passwd_entry_var,
        font=(self.a_today_default_font,20), width=10)
        self.passwd_entry.pack()

        self.passwd_button = Button(self.l, text='Done',

        command=lambda:self.password_done(frame, passwd_for_password_page), font=(self.a_today_default_font,20))
        self.passwd_button.pack(pady=5)

    def password_done(self, frame, passwd_for_password_page):
        if self.passwd_entry_var.get() == passwd_for_password_page:
            frame()
        else:
            self.passwd_entry.delete(0, END)

    def define_today_frame(self):
        #date = str(datetime.date.today())
        with open('final_date','r') as final:
            date = final.readline()
        self.current_frame_forget(self, self.passwd_page)
        self.main_frame_forget(self)

        self.today_frame2 = Frame(self.master)
        self.today_frame2.pack(fill=BOTH, expand=1)

        # back button of frame
        back_button = Button(self.today_frame2, text='<--Back', command=lambda:self.current_frame_forget(self, self.today_frame2))
        back_button.grid(row=0, column=0,sticky='NW',pady=10,padx=10)

        page_title = Label(self.today_frame2, text='Today Account Balance',
        font=(self.a_today_default_font,20))
        page_title.grid(row=0, column=1, sticky=('EW'), columnspan=3)

        # blank spacing
        blanl_label = Label(self.today_frame2, text='      ')
        blanl_label.grid(row=0, column=1, sticky='W')

        # date label
        date_label = Label(self.today_frame2, text='Date  ',
        font=(self.a_today_default_font,20))
        date_label.grid(row=2, column=1, sticky='E', pady=10)

        # set date entry var to date
        self.date_entry_var = StringVar()
        self.date_entry_var.set(date)

        # date entry widget
        date_entry = Label(self.today_frame2, textvariable=self.date_entry_var,
        font=(self.a_today_default_font,20))
        date_entry.grid(row=2, column=2, sticky='W')
        

        # Create some lebels and entrys

        # space label
        space = Label(self.today_frame2, text='   ')
        space.grid(row=1, column=3)
        # qty label
        qty_label = Label(self.today_frame2, text='Qty  ',
        font=(self.a_today_default_font,20))
        qty_label.grid(row=3, column=1, pady=10, sticky='E')
        # qty entry widget
        qty_entry = Entry(self.today_frame2, font=(self.a_today_default_font,20),
        width=8)
        qty_entry.grid(row=3, column=2, sticky='W')
        # total earned label
        Total_earned_label = Label(self.today_frame2,text='PCs Total Earning  ',
        font=(self.a_today_default_font,20))
        Total_earned_label.grid(row=4,column=1, sticky='E', pady=10)
        # total earned entry
        Total_earned_entry = Entry(self.today_frame2,
            width=8,
            font=(self.a_today_default_font,20))
        Total_earned_entry.grid(row=4,column=2, sticky='W')

        
        # difference label
        difference = Label(self.today_frame2, text='Total Difference  ',
        font=(self.a_today_default_font,20))
        difference.grid(row=5, column=1, sticky='E', pady=10)
        # difference entry widget
        difference_entry = Entry(self.today_frame2, width=8,
        font=(self.a_today_default_font,20))
        difference_entry.grid(row=5, column=2, sticky='W')
        # income label
        Other_Income = Label(self.today_frame2, text='Total Income  ',
        font=(self.a_today_default_font,20))
        Other_Income.grid(row=6, column=1, sticky='E', pady=10)
        # income entry
        Other_Income_entry = Entry(self.today_frame2, width=8,
        font=(self.a_today_default_font,20))
        Other_Income_entry.grid(row=6, column=2, sticky='W')
        # expances label
        Expances = Label(self.today_frame2, text='Total Expances  ',
        font=(self.a_today_default_font,20))
        Expances.grid(row=7, column=1, sticky='E', pady=10)
        # expances entry
        Expances_entry = Entry(self.today_frame2, width=8,
        font=(self.a_today_default_font,20))
        Expances_entry.grid(row=7, column=2, sticky='W')
        # total after label
        total_after = Label(self.today_frame2, text='After Income and Expances  ',
        font=(self.a_today_default_font,20))
        total_after.grid(row=8, column=1, sticky='E', pady=10)
        # total after entry widget
        total_after_entry = Entry(self.today_frame2, width=8,
        font=(self.a_today_default_font,20))
        total_after_entry.grid(row=8, column=2, sticky='W')
        # check again button
        Check_button = Button(self.today_frame2,text='Check Again',
        font=(self.a_today_default_font,15),command=lambda:self.check_today(self, Total_earned_entry,
        qty_entry, total_after_entry, Expances_entry, Other_Income_entry, difference_entry))
        Check_button.grid(pady=50,padx=10, row=9, column=1)
        # detal button
        detail_button = Button(self.today_frame2,text='Detail',
        font=(self.a_today_default_font,15),command=lambda:self.pc_data_page(self.today_frame2))
        detail_button.grid(pady=50,padx=10, row=9, column=2)
        
        self.check_today(self, Total_earned_entry, qty_entry, total_after_entry,
        Expances_entry, Other_Income_entry, difference_entry)

        #self.change_pc()
    
    def pc_data_page(self, frame):

        # frame forget
        self.current_frame_forget(self, frame)
        self.main_frame_forget(self)

        # define frame in self.master
        l_title = Frame(self.master)
        l_title.pack(fill=BOTH, expand=1)

        # frame title label
        self.l_frame = Label(l_title, text='Detailed Account View', font=('Consolas', 20))
        self.l_frame.grid(row=0, column=1, columnspan=8, sticky='w', pady=5, padx=10)

        # Pc data label title
        pc_data_label = Label(l_title, text='Pc Data', font=('Consolas',15), fg='white', bg='black')
        pc_data_label.grid(row=1, column=2, sticky='EW', pady=20)

        # Income label title
        income_label = Label(l_title, text='Income Data', font=('Consolas',15), fg='white', bg='black')
        income_label.grid(row=1, column=3, sticky='EW', columnspan=2, pady=20)

        # Expances label title
        expances_label = Label(l_title, text='Expances Data', font=('Consolas',15), fg='white', bg='black')
        expances_label.grid(row=1, column=5, sticky='EW', columnspan=2, pady=20)
        
        
        date = Label(l_title, text='  #      Time      Pc-no  Pc-T    R   Re   Diff', font=('Consolas',12))
        date.grid(row=2, column=2, sticky='W', pady=5, padx=10)

        dicription_income = Label(l_title, text='  Description', font=('Consolas',12))
        dicription_income.grid(row=2, column=3, sticky='W', padx=10)
        amount_income = Label(l_title, text='  Amount', font=('Consolas',12))
        amount_income.grid(row=2, column=4, sticky='W', padx=10)

        dicription_expances = Label(l_title, text='  Description', font=('Consolas',12))
        dicription_expances.grid(row=2, column=5, sticky='W', padx=10)
        amount_expances = Label(l_title, text='  Amount', font=('Consolas',12))
        amount_expances.grid(row=2, column=6, sticky='W', padx=10)

        # define text widget where pc-data will be placed
        detail_text1 = scrolledtext.ScrolledText(l_title, width=48, height=40, font=(self.default_font,12))
        detail_text1.grid(row=3, column=2, rowspan=7, padx=10, pady=5)
        detail_text1.focus()
        
        # define text widget where income will be placed
        detail_income = scrolledtext.ScrolledText(l_title, width=30, height=40, font=(self.default_font,12))
        detail_income.grid(row=3, column=3, rowspan=7, columnspan=2, padx=10, pady=5, sticky='N')
        detail_income.focus()
        
        # define text widget where expances will be placed
        detail_expances = scrolledtext.ScrolledText(l_title, width=30, height=40, font=(self.default_font,12))
        detail_expances.grid(row=3, column=5, rowspan=7, columnspan=2, padx=10, pady=5, sticky='N')
        detail_expances.focus()


        back_button = Button(l_title, text='<--Back', command=lambda:self.change_frame(self, l_title, self.today_frame2))
        back_button.grid(row=0, column=0,pady=10,padx=10)

        self.detail_check_today(self, detail_text1, detail_income, detail_expances)

    def change_pc(self):
        if len(self.pc_not_run_dict) > 0:
            self.change_pc_b.config(state='disabled')

            self.pc_not_run_dict = {k: v for k, v in sorted(self.pc_not_run_dict.items(), key=lambda item: item[0])}
            self.pc_run_dict = {k: v for k, v in sorted(self.pc_run_dict.items(), key=lambda item: item[0])}
            
            change_pc = Frame(self.expances_and_income_frame)
            change_pc.grid(row=12, column=0, columnspan=2, padx=15, sticky='EW')##pack(anchor='n')

            self.from_text = Label(change_pc, text='From', font=(self.default_font,11))
            self.from_text.grid(row=0, column=0, padx=3, pady=5)
            
            self.change_option1_var = StringVar()
            self.change_option1_var.set(None)
            change_option1 = OptionMenu(change_pc, self.change_option1_var, *self.pc_run_dict)
            change_option1.grid(row=0, column=1, padx=3, pady=5)

            self.to_text = Label(change_pc, text='To', font=(self.default_font,11))
            self.to_text.grid(row=1, column=0, padx=3, pady=5)
            
            self.change_option2_var = StringVar()
            self.change_option2_var.set(None)
            change_option2 = OptionMenu(change_pc, self.change_option2_var, *self.pc_not_run_dict)
            change_option2.grid(row=1, column=1, padx=3, pady=5)

            change_button = Button(change_pc, text='Done', command=lambda:self.change(self, change_pc), font=(self.default_font, 10))
            change_button.grid(row=1, column=2, padx=3, pady=5)

    def administrator_page(self):

        date = str(datetime.date.today())
        self.current_frame_forget(self, self.passwd_page)
        self.main_frame_forget(self)
        a_today_default_font = 'Consolas'
        self.admin_frame = Frame(self.master)
        self.admin_frame.pack(fill='both', expand=1)
        # back button of frame
        
        back_button = Button(self.admin_frame, text='<--Back',
            command=lambda:self.current_frame_forget(self, self.admin_frame))
        back_button.pack(anchor='nw',pady=10,padx=10)

        l_frame = LabelFrame(self.admin_frame,
            text='Administrator Page',
            font=(a_today_default_font,20))
        l_frame.pack(fill='both', expand=1)

        l_title = Frame(l_frame)
        l_title.pack(anchor='center', ipady=30)

        self.from_date_var = StringVar()
        self.to_date_var = StringVar()

        From_label = Label(l_title, text='From Date  ',
         font=(a_today_default_font, 20))
        From_label.grid(row=1, column=1, pady=10, sticky='E')

        From_entry = Entry(l_title,
            textvariable=self.from_date_var,
            font=(a_today_default_font, 20),
            width=10)
        From_entry.grid(row=1, column=2, pady=10, sticky='W')

        to_label = Label(l_title,
            text='To  ',
            font=(a_today_default_font, 20))
        to_label.grid(row=2, column=1, pady=10, sticky='E')

        to_entry = Entry(l_title,
            textvariable=self.to_date_var,
            font=(a_today_default_font, 20),
            width=10)
        to_entry.grid(row=2, column=2, pady=10, sticky='W')

        self.from_date_var.set(date)
        self.to_date_var.set(date)

        # qty label
        qty_label = Label(l_title, text='Qty  ',
        font=(a_today_default_font,20))
        qty_label.grid(row=3, column=1, pady=10, sticky='E')
        # qty entry widget
        qty_entry = Entry(l_title, font=(a_today_default_font,20),
        width=8)
        qty_entry.grid(row=3, column=2, sticky='W')
        # total earned label
        Total_earned_label = Label(l_title,text='Earning  ',
        font=(a_today_default_font,20))
        Total_earned_label.grid(row=4,column=1, sticky='E', pady=10)
        # total earned entry
        Total_earned_entry = Entry(l_title,width=8,
        font=(a_today_default_font,20))
        Total_earned_entry.grid(row=4,column=2, sticky='W')

        
        # difference label
        difference = Label(l_title, text='Difference  ',
        font=(a_today_default_font,20))
        difference.grid(row=5, column=1, sticky='E', pady=10)
        # difference entry widget
        difference_entry = Entry(l_title, width=8,
        font=(a_today_default_font,20))
        difference_entry.grid(row=5, column=2, sticky='W')
        # income label
        Other_Income = Label(l_title, text='Income  ',
        font=(a_today_default_font,20))
        Other_Income.grid(row=6, column=1, sticky='E', pady=10)
        # income entry
        Other_Income_entry = Entry(l_title, width=8,
        font=(a_today_default_font,20))
        Other_Income_entry.grid(row=6, column=2, sticky='W')
        # expances label
        Expances = Label(l_title, text='Expances  ',
        font=(a_today_default_font,20))
        Expances.grid(row=7, column=1, sticky='E', pady=10)
        # expances entry
        Expances_entry = Entry(l_title, width=8,
        font=(a_today_default_font,20))
        Expances_entry.grid(row=7, column=2, sticky='W')
        # total after label
        total_after = Label(l_title, text='   Total After  ',
        font=(a_today_default_font,20))
        total_after.grid(row=8, column=1, sticky='E', pady=10)
        # total after entry widget
        total_after_entry = Entry(l_title, width=8,
        font=(a_today_default_font,20))
        total_after_entry.grid(row=8, column=2, sticky='W')
        # check again button

        check_b = Button(l_title, text='Check', font=(a_today_default_font, 15),
            command=lambda:self.administrator_from_to_check(self, Total_earned_entry, qty_entry, total_after_entry,
        Expances_entry, Other_Income_entry, difference_entry))
        check_b.grid(row=9, column=1, pady=15, padx=10)

        detail_b = Button(l_title, text='Detail', font=(a_today_default_font, 15),
            command=lambda:self.admin_detail(self, self.admin_frame))
        detail_b.grid(row=9, column=2, pady=15, padx=10)

    def admin_detail(parent, self, admin_frame):
        # frame forget
        self.current_frame_forget(self, admin_frame)
        self.main_frame_forget(self)

        # define frame in self.master
        l_title = Frame(self.master)
        l_title.pack(fill=BOTH, expand=1)

        # frame title label
        self.l_frame = Label(l_title, text='Administrator Detailed Account View', font=('Consolas', 20))
        self.l_frame.grid(row=0, column=1, columnspan=8, sticky='w', pady=5, padx=10)

        # Pc data label title
        pc_data_label = Label(l_title, text='Pc Data', font=('Consolas',15), fg='white', bg='black')
        pc_data_label.grid(row=1, column=1, sticky='EW', pady=16)

        # Income label title
        income_label = Label(l_title, text='Income Data', font=('Consolas',15), fg='white', bg='black')
        income_label.grid(row=1, column=2, sticky='EW', columnspan=4, pady=16)

        # Expances label title
        expances_label = Label(l_title, text='Expances Data', font=('Consolas',15), fg='white', bg='black')
        expances_label.grid(row=1, column=6, sticky='EW', columnspan=4, pady=16)

        
        date = Label(l_title, text='  #    Date        Time      Pc-no  Pc-T    R   Re   Diff', font=('Consolas',10))
        date.grid(row=2, column=1, sticky='W', pady=5, padx=10)

        date_income = Label(l_title, text='  Date', font=('Consolas',10))
        date_income.grid(row=2, column=2, sticky='W', padx=10)
        time_income = Label(l_title, text='  Time', font=('Consolas',10))
        time_income.grid(row=2, column=3, sticky='W', padx=10)
        dicription_income = Label(l_title, text='  Description', font=('Consolas',10))
        dicription_income.grid(row=2, column=4, sticky='W', padx=10)
        amount_income = Label(l_title, text='Amount', font=('Consolas',10))
        amount_income.grid(row=2, column=5, sticky='W', padx=10)

        date_expances = Label(l_title, text='  Date', font=('Consolas',10))
        date_expances.grid(row=2, column=6, sticky='W', padx=10)
        time_expances = Label(l_title, text='  Time', font=('Consolas',10))
        time_expances.grid(row=2, column=7, sticky='W', padx=10)
        dicription_expances = Label(l_title, text='  Description', font=('Consolas',10))
        dicription_expances.grid(row=2, column=8, sticky='W', padx=10)
        amount_expances = Label(l_title, text='Amount', font=('Consolas',10))
        amount_expances.grid(row=2, column=9, sticky='W', padx=10)

        # define text widget where pc-data will be placed
        detail_text1 = scrolledtext.ScrolledText(l_title, width=60, height=40, font=(self.default_font,10,'bold'))
        detail_text1.grid(row=3, column=1, rowspan=7, padx=10, pady=5)
        detail_text1.focus()
        
        # define text widget where income will be placed
        detail_income = scrolledtext.ScrolledText(l_title, width=40, height=40, font=(self.default_font,10,'bold'))
        detail_income.grid(row=3, column=2, rowspan=7, columnspan=4, padx=10, pady=5, sticky='N')
        detail_income.focus()
        
        # define text widget where expances will be placed
        detail_expances = scrolledtext.ScrolledText(l_title, width=40, height=40, font=(self.default_font,10,'bold'))
        detail_expances.grid(row=3, column=6, rowspan=7, columnspan=4, padx=10, pady=5, sticky='N')
        detail_income.focus()


        back_button = Button(l_title, text='<--Back', command=lambda:self.change_frame(self, l_title, self.admin_frame))
        back_button.grid(row=0, column=0,pady=10,padx=10)

        self.admin_detail_check(self, detail_text1, detail_income, detail_expances)

    def customer_detail(self):

        self.main_frame_forget(self)

        # Create labelframe in root
        frame = LabelFrame(self.master, text='Customer Debt', font=('Consolas',15))
        frame.pack(fill='both', expand=1, padx=10, pady=10)

        back_button = Button(frame,  text='Back', command=lambda:self.current_frame_forget(self, frame),
            font=('Verdana',10))
        back_button.pack(pady=10,padx=15, anchor='nw', side='top')
        # search frame for search and delete 
        search_frame = Frame(frame)
        search_frame.pack()
        check_var = StringVar()
        # search label
        search_label = Label(search_frame, text='Search',
            font=('Consolas'))
        search_label.grid(column=1, row=1, pady=10, padx=10)
        # search entry
        self.search_entry = Entry(search_frame,
            font=('Consolas',15))
        self.search_entry.grid(column=2, row=1, pady=10, padx=10)
        # by name check button
        check_name = Radiobutton(search_frame, text='by Name',
            variable=check_var,
        value='name',
        font=('Consolas'))
        check_name.grid(column=3, row=1, pady=10,padx=10)
        # by phone check button 
        check_phone = Radiobutton(search_frame, text='by Phone',
            variable=check_var,
            value='phone',
            font=('Consolas'))
        check_phone.grid(column=4, row=1, pady=10, padx=10)
        # by description check button
        check_phone = Radiobutton(search_frame, text='by Description',
            variable=check_var,
            value='description',
            font=('Consolas'))
        check_phone.grid(column=5, row=1, pady=10,padx=10)
        check_name.select()

        delete_row_label = Label(search_frame, text='     Delete Record',
            font=('Consolas'))
        delete_row_label.grid(column=6, row=1, pady=10,padx=10)
        delete_row_entry = Entry(search_frame,
            font=('Consolas',15),
            width=5)
        delete_row_entry.grid(column=7, row=1, pady=10,padx=10)
        delete_row_entry.bind('<Return>', lambda extra, :self.delete_customer_record(delete_row_entry))

        # Customer data in tree view
        area=('#', 'Customer Name', 'Phone', 'Cashier Name', 'Description', 'Total', 'Received', 'Debt', 'Date', 'Time')
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=3, font=('Consolas', 12, 'bold'), rowheight=30) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Consolas', 13)) # Modify the font of the headings

        tv = ttk.Treeview(frame, columns=('0','1','2','3','4','5','6','7','8','9'),
            show='headings',
            height=10,
            style="mystyle.Treeview")

        tv.pack(padx=10, pady=10)

        tv.column('0', width='30', anchor='e')
        tv.column('1', width='150', anchor='c')
        tv.column('2', width='70', anchor='c')
        tv.column('3', width='150', anchor='c')
        tv.column('4', width='150', anchor='c')
        tv.column('5', width='70', anchor='c')
        tv.column('6', width='100', anchor='c')
        tv.column('7', width='70', anchor='c')
        tv.column('8', width='100', anchor='c')
        tv.column('9', width='100', anchor='c')

        tv.heading('0', text=area[0])
        tv.heading('1', text=area[1])
        tv.heading('2', text=area[2])
        tv.heading('3', text=area[3])
        tv.heading('4', text=area[4])
        tv.heading('5', text=area[5])
        tv.heading('6', text=area[6])
        tv.heading('7', text=area[7])
        tv.heading('8', text=area[8])
        tv.heading('9', text=area[9])

        frame1 = LabelFrame(frame, text='Customer Total',
            font=('Consolas',15))
        frame1.pack(padx=10, pady=10)

        # create total labels, variables and entrys
        total_qty_var = StringVar()
        total_debt_var = StringVar()

        total_qty_label = Label(frame1, text='Qty ',
            font=('Consolas',13))
        total_qty_label.grid(column=0, row=1, padx=10, pady=10)
        total_debt_label = Label(frame1, text='Total Debt ',
            font=('Consolas',13))
        total_debt_label.grid(column=0, row=2, padx=10, pady=10)

        total_qty_entry = Label(frame1, textvariable=total_qty_var,
            font=('Consolas',13))
        total_qty_entry.grid(column=1, row=1, padx=10, pady=10)
        total_debt_entry = Label(frame1, textvariable=total_debt_var,
            font=('Consolas',13))
        total_debt_entry.grid(column=1, row=2, padx=10, pady=10)

        self.search_entry.bind('<Return>',
            lambda a:self.customer_detail_search(check_var.get(),self.search_entry.get(), tv, total_qty_var, total_debt_var))
        self.customer_detail_insert(self, tv, total_qty_var, total_debt_var)

    def customer_detail_popup(self):
        def costumer_debt_done(pc_close_popup):
            # Insert Data fromtkinter variables
            name = name_entry_var.get()
            phone = phone_entry_var.get()
            description = desc_entry_var.get()
            # only do this when this is true
            # insert (costumer_name, phone, receiver_name, amount, recv_amount, debt_amount, date, time)
            self.debt_insert(name, phone, 0, description,
                        0,
                        0,
                        0,
                        0,
                        0)
            # destroy top level
            pc_close_popup.destroy()
        
        pc_close_popup = Toplevel(highlightthickness=2)
        pc_close_popup.grab_set()
        pc_close_popup.geometry('450x230+412+412')
        pc_close_popup.overrideredirect(1)
        pc_close_popup.config(highlightbackground = "red")
        frame = LabelFrame(pc_close_popup, text='Customer Detail', bd=1, relief='solid')
        frame.pack(anchor='center', expand=1, fill='both', padx=10, pady=10)


        name_label = Label(frame,
            text='Customer Name ',
            font=('Consolas')
            )
        name_label.grid(column=0, row=1, padx=25, pady=5, sticky='W')

        number_label = Label(frame,
            text='Customer Phone ',
            font=('Consolas')
            )
        number_label.grid(column=0, row=2, padx=25, pady=5, sticky='W')

        # recv_label = Label(frame,
        #     text='Cashier Name',
        #     font=('Consolas')
        #     )
        # recv_label.grid(column=0, row=3, padx=25, pady=5, sticky='W')

        desc_label = Label(frame,
            text='Description ',
            font=('Consolas')
            )
        desc_label.grid(column=0, row=4, padx=25, pady=5, sticky='W')

        name_entry_var = StringVar()
        phone_entry_var = StringVar()
        # self.recv_entry_var = StringVar()
        desc_entry_var = StringVar()

        name_entry = Entry(frame, textvariable=name_entry_var,
                           font=('Consolas'))
        name_entry.grid(column=1, row=1, padx=10, pady=5)

        phone_entry = Entry(frame, textvariable=phone_entry_var,
                            font=('Consolas')
                            )
        phone_entry.grid(column=1, row=2, padx=10, pady=5)

        # recv_entry = Entry(frame, textvariable=self.recv_entry_var,
        #                    font=('Consolas'))
        # recv_entry.grid(column=1, row=3, padx=10, pady=5)

        desc_entry = Entry(frame, textvariable=desc_entry_var,
                           font=('Consolas'))
        desc_entry.grid(column=1, row=4, padx=10, pady=5)

        cancel_button = Button(frame, text='Cancel',
                            font=('Verdana',10),
                            command=lambda:pc_close_popup.destroy())
        cancel_button.grid(column=1, row=5, pady=5, padx=70, sticky='E')

        done_button = Button(frame, text='Done',
                            font=('Verdana',10),
                            command=lambda:costumer_debt_done(pc_close_popup))
        done_button.grid(column=1, row=5, pady=5, padx=10, sticky='E')

        
        

        
        
        

        

        


