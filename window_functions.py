from tkinter import (BOTH, END, INSERT, Button, Entry, Frame, IntVar, Label, Menu,
                     StringVar, Tk, ttk, OptionMenu, LabelFrame,
                     Checkbutton, SUNKEN, RAISED, messagebox)
from os import (path, remove, mkdir)
from database import pc_data, expances_and_income, customer_debt
import datetime
from time import sleep


class Window_stuff_functions(pc_data, customer_debt, expances_and_income):
    def __init__(self):
        self.final_close_file()
        self.final_date = self.final_date_read()
        self.make_dirs()

        #creates data.db and its tables
        pc_data.__init__(self)

        #creates debt.db and its tables
        customer_debt.__init__(self)

    def make_dirs(self):
        if not path.exists('restore'):
            mkdir('restore')

    def delete_final_date_file(parent, self):
        final_message = messagebox.askquestion('Final Close ',
            message='Are you sure you want to final close Dotcom InterNet Public Service Software')
        if final_message == 'yes':
            if path.exists('final_date'):
                remove('final_date')
                self.master.destroy()
                
            return
        if  final_message == 'no':
            return

    def final_close_file(self):
        # if final_date file not exist create and insert date
        if not path.exists('final_date'):
            with open('final_date','w') as final:
                final.write(str(datetime.date.today()))
        return None

    def final_date_read(self):
        # if final_date file exist then read date from it
        if path.exists('final_date'):
            with open('final_date','r') as final:
                date = final.readline()
        return date
        
    def main_frame_forget(parent, self):
        '''if you want to put any widget from main or self frame call this function'''
        self.pack_forget()
        self.master.config(menu='')
    
    def current_frame_forget(parent, self, frame):
        frame.pack_forget()
        self.master.config(menu=self.menu_bar)
        self.pack(fill=BOTH, expand=1)
    
    def change_frame(parent, self, from_frame, to_frame):
        self.current_frame_forget(self, from_frame)
        self.main_frame_forget(parent)
        to_frame.pack(fill=BOTH, expand=1)

    def decrypt(self,data):
        a_key = 'a bcdefghijklmn\nopqrstuvwxyz1234567890:-ABCDEFGHIJKLM.NOPQRSTUVWXYZ'
        key = 12
        decrypted = ''
        for i in data:
            position = (a_key.find(i))
            new_position = (position-key)%66
            decrypted += a_key[new_position]
        return decrypted

        changed_date = self.date_entry_var.get()
        with open('data','rt')as f:
                text_list = f.readlines()
        qty = 0
        earned_total = 0
        for line in text_list:
            line = line.rstrip('\n')
            line = self.decrypt(line)
            if not line.startswith(changed_date):
                continue
            else:
                qty += 1
                earn = int(line[25:])
                earned_total += earn
        self.Total_earned_entry.delete(0,END)
        self.qty_entry.delete(0,END)
        self.Total_earned_entry.insert(0,earned_total)
        self.qty_entry.insert(0,qty)

    def income_done(self, description, amount):
        description_get = description.get()
        amount_get = amount.get()
        if len(description_get) > 0 and len(amount_get) > 0 and amount_get.isdigit():
            description.delete(0, END)
            amount.delete(0, END)
            e_a_i_object = expances_and_income()
            e_a_i_object.insert_income(description_get, amount_get)
            return None
        else:
            return None

    def expances_done(self, description, amount):
        description_get = description.get()
        amount_get = amount.get()
        if len(description_get) > 0 and len(amount_get) > 0 and amount_get.isdigit():
            description.delete(0, END)
            amount.delete(0, END)
            e_a_i_object = expances_and_income()
            e_a_i_object.insert_expances(description_get, amount_get)
            return None
        else:
            return None

    def check_today(parent, self, Total_earned_entry, qty_entry, total_after_entry,
        Expances_entry, Other_Income_entry, difference_entry):

        # get date from date entry
        date = self.date_entry_var.get()
        
        # retrive data from data base based on today date
        p = pc_data()
        today = p.retrive_today(date)
        qty = today['qty']
        earned_total = today['total_rate']
        difference_total = today['total_difference']
        
        i_e_object = expances_and_income()
        expance = i_e_object.retrive_expances(date)
        income = i_e_object.retrive_income(date)

        # delete data before insertimg data
        Total_earned_entry.delete(0, END)
        qty_entry.delete(0, END)
        total_after_entry.delete(0, END)
        Expances_entry.delete(0, END)
        Other_Income_entry.delete(0, END)
        difference_entry.delete(0, END)

        # Insert data in entries
        Total_earned_entry.insert(0,earned_total)
        qty_entry.insert(0,qty)
        total_after_entry.insert(0, str((int(earned_total)+int(income))-int(expance)))
        Expances_entry.insert(0, expance)
        Other_Income_entry.insert(0, income)
        difference_entry.insert(0, difference_total)

    def detail_check_today(parent, self, text_widget, detail_income, detail_expances):

        date = self.date_entry_var.get()
        retrive = pc_data()
        data_list = retrive.retrive(date)
        income_and_expances = expances_and_income()
        income = income_and_expances.retrive_income_for_text_box(date)
        expances = income_and_expances.retrive_expances_for_text_box(date)

        c = 1
        for x in data_list:
            text_widget.insert(INSERT, '  '+'{:<5}'.format(c))
            #text_widget.insert(INSERT, '{:>10}'.format(x[1]))
            text_widget.insert(INSERT, '{:>10}'.format(x[2]))
            text_widget.insert(INSERT, '{:>7}'.format(x[3]))
            text_widget.insert(INSERT, '{:>6}'.format(x[4]))
            text_widget.insert(INSERT, '{:>5}'.format(x[5]))
            text_widget.insert(INSERT, '{:>5}'.format(x[6]))
            text_widget.insert(INSERT, '{:>5}'.format(x[7])+'\n\n')
            c += 1

        for x in income:
            detail_income.insert(INSERT, '  '+'{:<20}'.format(x[0])+'{:>5}'.format(x[1])+'\n\n')

        for x in expances:
            detail_expances.insert(INSERT, '  '+'{:<20}'.format(x[0])+'{:>5}'.format(x[1])+'\n\n')


        #text_widget.config(state='disabled')
        detail_income.config(state='disabled')
        detail_expances.config(state='disabled')

    def change(parent, self, frame):

        frame.grid_forget()
        
        self.change_pc_b.config(state='normal')

        self.pc_not_run_dict[self.change_option2_var.get()].s = self.pc_run_dict[self.change_option1_var.get()].s

        self.pc_not_run_dict[self.change_option2_var.get()].m = self.pc_run_dict[self.change_option1_var.get()].m

        self.pc_not_run_dict[self.change_option2_var.get()].h = self.pc_run_dict[self.change_option1_var.get()].h

        self.pc_not_run_dict[self.change_option2_var.get()].e_time_var.set(str(self.pc_not_run_dict[self.change_option2_var.get()].h)+':'+str(self.pc_not_run_dict[self.change_option2_var.get()].m).zfill(2))
        self.pc_not_run_dict[self.change_option2_var.get()].e_rate_var.set(str(self.pc_not_run_dict[self.change_option2_var.get()].__rate_calculator__()))
        self.pc_not_run_dict[self.change_option2_var.get()].tooltip_check_var.set(self.pc_run_dict[self.change_option1_var.get()].tooltip_check_var.get())
        
        self.pc_not_run_dict[self.change_option2_var.get()].check_b_var.set(1)

        self.pc_not_run_dict[self.change_option2_var.get()].start('start_from_change_pc')
        
        self.pc_run_dict[self.change_option1_var.get()].__change_stop__()

    def administrator_from_to_check(parent, self, Total_earned_entry, qty_entry,
        total_after_entry, Expances_entry, Other_Income_entry,
        difference_entry):

        # delete data before insertimg data
        Total_earned_entry.delete(0, END)
        qty_entry.delete(0, END)
        total_after_entry.delete(0, END)
        Expances_entry.delete(0, END)
        Other_Income_entry.delete(0, END)
        difference_entry.delete(0, END)

        p = pc_data()
        from_to_date = p.retrive_administrator(self.from_date_var.get(),
        self.to_date_var.get())

        qty = from_to_date['qty']
        earned_total = from_to_date['total_rate']
        difference_total = from_to_date['total_difference']
        i_e_object = expances_and_income()
        expance = i_e_object.retrive_administrator_expances(self.from_date_var.get(),
        self.to_date_var.get())
        income = i_e_object.retrive_administrator_income(self.from_date_var.get(),
        self.to_date_var.get())

        #income = i_e_object.retrive_income(date)

        # Insert data in entries
        Total_earned_entry.insert(0,earned_total)
        qty_entry.insert(0,qty)
        total_after_entry.insert(0, str((int(earned_total)+int(income))-int(expance)))
        Expances_entry.insert(0, expance)
        Other_Income_entry.insert(0, income)
        difference_entry.insert(0, difference_total)

    def admin_detail_check(parent, self, text_widget, detail_income, detail_expances):
        retrive = pc_data()
        data_list = retrive.admin_detail_pc_data(self.from_date_var.get(), self.to_date_var.get() )
        income_and_expances = expances_and_income()
        income = income_and_expances.retrive_income_for_text_box_admin(self.from_date_var.get(), self.to_date_var.get() )
        expances = income_and_expances.retrive_expances_for_text_box_admin(self.from_date_var.get(), self.to_date_var.get() )

        c = 1
        for x in data_list:
            text_widget.insert(INSERT, '  '+'{:<5}'.format(c))
            text_widget.insert(INSERT, '{:>10}'.format(x[1]))
            text_widget.insert(INSERT, '{:>10}'.format(x[2]))
            text_widget.insert(INSERT, '{:>7}'.format(x[3]))
            text_widget.insert(INSERT, '{:>6}'.format(x[4]))
            text_widget.insert(INSERT, '{:>5}'.format(x[5]))
            text_widget.insert(INSERT, '{:>5}'.format(x[6]))
            text_widget.insert(INSERT, '{:>5}'.format(x[7])+'\n\n')
            c += 1

        for x in income:
            detail_income.insert(INSERT, '  '+'{:<10}'.format(x[0])+'{:>10}'.format(x[1])+'{:>12}'.format(x[2])+'{:>5}'.format(x[3])+'\n\n')

        for x in expances:
            detail_expances.insert(INSERT, '  '+'{:<10}'.format(x[0])+'{:>10}'.format(x[1])+'{:>12}'.format(x[2])+'{:>5}'.format(x[3])+'\n\n')

    def customer_detail_insert(self, parent, tv, qty_var, debt_var):
        data1 = self.debt_retrive_tv()
        # count qty and debt
        qty_debt_tup = self.customer_detail_count(data1)
        # inserts data from debt.db to treeview
        for t in data1:
            tv.insert('', 'end',values=t)
        qty_var.set(qty_debt_tup[0])
        debt_var.set(qty_debt_tup[1])

    def customer_detail_search(self, var, search, tv, qty_var, debt_var):
        search = '%'+search+'%'
        if var == 'name':
            # get searched data from database
            text_list = self.search_by_name(search)
            # count qty and debt
            qty_debt_tup = self.customer_detail_count(text_list)
            # delete data from treeview
            for x in tv.get_children():
                tv.delete(x)


            for t in text_list:
                tv.insert('', 'end', values=t)

            qty_var.set(qty_debt_tup[0])
            debt_var.set(qty_debt_tup[1])
            return None

        elif var == 'phone':
            # get searched data from database
            text_list = self.search_by_phone(search)
             # count qty and debt
            qty_debt_tup = self.customer_detail_count(text_list)

            for x in tv.get_children():
                tv.delete(x)


            for t in text_list:
                tv.insert('', 'end', values=t)

            qty_var.set(qty_debt_tup[0])
            debt_var.set(qty_debt_tup[1])
            return None
        else:
            # get searched data from database
            text_list = self.search_by_description(search)
             # count qty and debt
            qty_debt_tup = self.customer_detail_count(text_list)

            for x in tv.get_children():
                tv.delete(x)


            for t in text_list:
                tv.insert('', 'end', values=t)

            qty_var.set(qty_debt_tup[0])
            debt_var.set(qty_debt_tup[1])
            return None

    def delete_customer_record(self, delete_entry):
        row_id = delete_entry.get()
        delete_entry.delete(0, END)
        if not row_id.isdigit():
            messagebox.showinfo('Invalid id',
                message='Please Enter a Valid record id')
        else:
            self.date = self.final_date_read()
            debt = self.get_debt_from_row(row_id)
            if debt == None:
                messagebox.showinfo('Invalid id',
                message='Please Enter a Valid record id')
            else:
                self.delete_record(row_id)
                self.insert_income('From debt', debt[0])

    def customer_detail_count(self, data):
        qty = 0
        debt = 0
        for tuples in data:
            qty += 1
            debt += int(tuples[7])
        return (qty, debt)





    


