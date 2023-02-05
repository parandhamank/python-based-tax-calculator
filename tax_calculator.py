#---------------------------------------------------------------------------------------------------
#importing modules
from tkinter import *
#---------------------------------------------------------------------------------------------------
def isSalaried():
    global sal
    if (var_sal.get() == 1) and (var_non_sal.get() == 0):
        label_isSal.config(width=20, bg='green', text="Salaried person")
        sal = 1
    elif (var_sal.get() == 0) and (var_non_sal.get() == 1):
        label_isSal.config(width=20, bg='green', text="non-Salaried person")
        sal = 0
    else:
        label_isSal.config(width=30, bg='red', text="Choose either one option")
        sal = ''
#---------------------------------------------------------------------------------------------------
def isAge():
    global age
    if (var_less_than_60.get() == 1) and (var_greater_than_60.get() == 0) and (var_greater_than_80.get() == 0):
        label_isAge.config(width=20, bg='green', text="Your age is less than 60")
        age = 59
    elif (var_less_than_60.get() == 0) and (var_greater_than_60.get() == 1) and (var_greater_than_80.get() == 0):
        label_isAge.config(width=20, bg='green', text="Your age is greater than 60")
        age = 61
    elif (var_less_than_60.get() == 0) and (var_greater_than_60.get() == 0) and (var_greater_than_80.get() == 1):
        label_isAge.config(width=20, bg='green', text="Your age is greater than 80")
        age = 81
    else:
        label_isAge.config(width=20, bg='red', text="Choose either one option")
        age = ''
#---------------------------------------------------------------------------------------------------
def isTax():
    global taxRegime
    if (var_new_tax.get() == 1) and (var_old_tax.get() == 0):
        label_whichTax.config(width=20, bg='green', text="Selected new tax regime")
        taxRegime = 1
    elif (var_new_tax.get() == 0) and (var_old_tax.get() == 1):
        label_whichTax.config(width=20, bg='green', text="Selected old tax regime")
        taxRegime = 0
    else:
        label_whichTax.config(width=30, bg='red', text="Choose either one option")
        taxRegime = ''
#---------------------------------------------------------------------------------------------------
def out():
    total_deduction = 0
    if (sal == '') or (age == '') or (taxRegime == ''):
        output.delete(0.0, END) #Clear outbox
        output.insert(END, "Error")
        output_1.delete(0.0, END) #Clear outbox
        output_1.insert(END, "Error")
        return
    try:
        TAXABLE_INCOME = int(taxableIncome.get())
        HRA = int(hra.get())
        LTA = int(lta.get())
        EPF = int(epf.get())
        PPF = int(ppf.get())
        TERM_INS = int(term_ins.get())
        MEDICAL_INS = int(medical_ins.get())
        EDU_LOAN = int(edu_loan.get())
    except:
        output.delete(0.0, END) #Clear outbox
        output.insert(END, "Error")
        output_1.delete(0.0, END) #Clear outbox
        output_1.insert(END, "Error")
        return
    if (sal == 1):
        total_deduction = total_deduction + 50000
    
    TAXABLE_INCOME = TAXABLE_INCOME - total_deduction
    if (taxRegime == 1):
        output.delete(0.0, END) #Clear outbox
        output.insert(END, str(TAXABLE_INCOME))
    else:
        TAXABLE_INCOME = TAXABLE_INCOME - (HRA + LTA + EPF + PPF + TERM_INS + MEDICAL_INS + EDU_LOAN)
        output.delete(0.0, END) #Clear outbox
        output.insert(END, str(TAXABLE_INCOME))
    
    tax_to_be_paid = 0
    if (TAXABLE_INCOME > 500000):
        if (taxRegime == 1): #new regime
            if (TAXABLE_INCOME > 1500000):
                #>15L
                tax_to_be_paid = ((TAXABLE_INCOME - 1500000) * 0.3) + 187500
            elif (TAXABLE_INCOME > 1250000):
                tax_to_be_paid = ((TAXABLE_INCOME - 1250000) * 0.25) + 125000
            elif (TAXABLE_INCOME > 1000000):
                #>10L
                tax_to_be_paid = ((TAXABLE_INCOME - 1000000) * 0.2) + 75000
            elif (TAXABLE_INCOME > 750000):
                #>7.5
                tax_to_be_paid = ((TAXABLE_INCOME - 750000) * 0.15) + 37500
            else:
                tax_to_be_paid = ((TAXABLE_INCOME - 500000) * 0.1) + 12500
        else: #old regime
            if (TAXABLE_INCOME > 1000000):
                tax_to_be_paid = ((TAXABLE_INCOME - 1000000) * 0.3) + 112500
            else:
                tax_to_be_paid = ((TAXABLE_INCOME - 500000) * 0.2) + 12500
    output_1.delete(0.0, END) #Clear outbox
    output_1.insert(END, str(tax_to_be_paid))
#---------------------------------------------------------------------------------------------------
def main():
    #Declaring global variables
    global var_sal
    global var_non_sal
    global label_isSal
    global var_less_than_60
    global var_greater_than_60
    global var_greater_than_80
    global label_isAge
    global var_new_tax
    global var_old_tax
    global label_whichTax
    #--------------------
    global sal
    global age
    global taxRegime
    global taxableIncome
    global hra
    global lta
    global epf
    global ppf
    global term_ins
    global medical_ins
    global edu_loan
    global output
    global output_1
    #--------------------
    sal = ''
    age = ''
    taxRegime = ''

    #tkinter initialization
    window = Tk()
    window.title("Tax Calculator")
    #window.configure(background="lightblue")
    window.configure(background="lightblue")
    window.geometry('1080x720+200+200')
    
    Label(window, bg='aquamarine', fg='blue', width=71, text='Income Tax Calculator', font='Helvetica 18 bold').place(x=0,y=0)

    #Salaried or not
    var_sal = IntVar()
    var_non_sal = IntVar()
    Label(window, bg='lightblue', fg='black', text='1. Salary details', font='Helvetica 12 bold').place(x=0, y=40)
    Checkbutton(window,width=9, text='Salaried', variable=var_sal, onvalue=1, offvalue=0, command=isSalaried).place(x=50,y=70)
    Checkbutton(window,width=9, text='not-Salaried', variable=var_non_sal, onvalue=1, offvalue=0, command=isSalaried).place(x=150,y=70)
    label_isSal = Label(window, bg='red', fg='white', width=20, text='Choose either one option', anchor='w')
    label_isSal.place(x=250,y=70)

    #age
    var_less_than_60 = IntVar()
    var_greater_than_60 = IntVar()
    var_greater_than_80 = IntVar()
    Label(window, bg='lightblue', fg='black', text='2. Age details', font='Helvetica 12 bold').place(x=0, y=100)
    Checkbutton(window,width=10, text='less than 60', variable=var_less_than_60, onvalue=1, offvalue=0, command=isAge).place(x=50,y=130)
    Checkbutton(window,width=10, text='greater than 60', variable=var_greater_than_60, onvalue=1, offvalue=0, command=isAge).place(x=155,y=130)
    Checkbutton(window,width=10, text='greater than 80', variable=var_greater_than_80, onvalue=1, offvalue=0, command=isAge).place(x=260,y=130)
    label_isAge = Label(window, bg='red', fg='white', width=20, text='Choose either one option', anchor='w')
    label_isAge.place(x=365,y=130)

    #Tax regime
    #Salaried or not
    var_new_tax = IntVar()
    var_old_tax = IntVar()
    Label(window, bg='lightblue', fg='black', text='3. Tax Regime', font='Helvetica 12 bold').place(x=0, y=160)
    Checkbutton(window,width=11, text='Old tax regime', variable=var_old_tax, onvalue=1, offvalue=0, command=isTax).place(x=50,y=190)
    Checkbutton(window,width=11, text='New tax regime', variable=var_new_tax, onvalue=1, offvalue=0, command=isTax).place(x=160,y=190)
    label_whichTax = Label(window, bg='red', fg='white', width=20, text='Choose either one option', anchor='w')
    label_whichTax.place(x=270,y=190)

    #Taxable income
    Label(window, bg='lightblue', fg='black', text='3. Total income', font='Helvetica 12 bold').place(x=0, y=220)
    taxableIncome = Entry(window, width=18, bg='white')
    taxableIncome.place(x=50, y=250)

    #HRA
    Label(window, bg='lightblue', fg='black', text='4. HRA', font='Helvetica 12 bold').place(x=0, y=280)
    hra = Entry(window, width=18, bg='white')
    hra.place(x=50, y=310)

    #LTA
    Label(window, bg='lightblue', fg='black', text='5. LTA', font='Helvetica 12 bold').place(x=0, y=340)
    lta = Entry(window, width=18, bg='white')
    lta.place(x=50, y=370)
    
    #Section 80c
    Label(window, bg='lightblue', fg='black', text='6. Section 80C - Investments', font='Helvetica 12 bold').place(x=0, y=400)
    Label(window, bg='lightblue', fg='black', text='EPF', font='Helvetica 10 bold').place(x=50, y=430)
    epf = Entry(window, width=18, bg='white')
    epf.place(x=160, y=430)
    Label(window, bg='lightblue', fg='black', text='PPF', font='Helvetica 10 bold').place(x=50, y=450)
    ppf = Entry(window, width=18, bg='white')
    ppf.place(x=160, y=450)
    Label(window, bg='lightblue', fg='black', text='Term Insurance', font='Helvetica 10 bold').place(x=50, y=470)
    term_ins = Entry(window, width=18, bg='white')
    term_ins.place(x=160, y=470)

    #Section 80D - medical insurance
    Label(window, bg='lightblue', fg='black', text='7. Section 80D - Medical insurance', font='Helvetica 12 bold').place(x=0, y=500)
    medical_ins = Entry(window, width=18, bg='white')
    medical_ins.place(x=50, y=530)

    #Section 80E - Educational loan interest
    Label(window, bg='lightblue', fg='black', text='8. Section 80E - Educational loan interest', font='Helvetica 12 bold').place(x=0, y=560)
    edu_loan = Entry(window, width=18, bg='white')
    edu_loan.place(x=50, y=590)

    Button(window, text='Calculate total taxable amount', font='Helvetica 12 bold', command=out).place(x=150, y=640)
    Label(window, bg='lightblue', fg='black', text='Amount', font='Helvetica 12 bold').place(x=410, y=640)
    Label(window, bg='lightblue', fg='black', text='Tax', font='Helvetica 12 bold').place(x=410, y=670)
    output = Text(window, height=1, width=8,font='Helvetica 14 bold', background='white', fg='green')
    output.place(x=500, y=640)
    output_1 = Text(window, height=1, width=8,font='Helvetica 14 bold', background='white', fg='green')
    output_1.place(x=500, y=670)

    Label(window, bg='lightblue', fg='red', text='Done by Sneka K', font='Helvetica 12 bold').place(x=800, y=690)
    window.mainloop()
#---------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    #calling main function
    main()
#---------------------------------------------------------------------------------------------------