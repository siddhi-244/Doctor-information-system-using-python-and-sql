from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import re
from datetime import date

from tkcalendar import DateEntry

import pymysql

class Doctor:
    def __init__(self,root):
        self.root=root
        titlespace=" "
        self.root.title(132*titlespace +"Doctor information system")
        self.root.geometry("1220x790+0+0")
        # self.root.resizable(0,0)
        # self.root.config(bg="powder blue")

        # variables
        d_id=StringVar()
        d_name=StringVar()
        
        d_spec=StringVar()
        em=StringVar()
        email=StringVar()
        d_hos=StringVar()
        d_country=StringVar()
        d_exp=StringVar()
        d_birth=StringVar()
        
        d_city=StringVar()
        d_deg=StringVar()
        
        d_shift=StringVar()
        d_gender=StringVar()
        d_patients=StringVar()
        d_web=StringVar()
        d_sal=StringVar()



        s1=IntVar()
        s2=IntVar()
        s3=IntVar()
        s4=IntVar()
        exp=IntVar()
        days=StringVar()
        age=StringVar()
        num=StringVar()
        phone=StringVar()



        


         # function
        def iExit():
            iExit= tkinter.messagebox.askyesno("DOCTOR INFORMATION SYSTEM"," Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def submit():

            submit=tkinter.messagebox.askyesno("Confirm","Do  you want to submit")
            phone=re.compile(r'^(0/91)?[7-9][0-9]{9}$')
            email=re.compile(r"[^@]+@[^@]+\.[^@]+")


            # if  d_id.get()=="" or  d_name.get()=="" or d_spec.get()=="":
            #     tkinter.messagebox.showerror("Warning","Enter correct details")

            

            if submit>0:

                if (phone.match(num.get())and not(email.match(em.get())) ):
                    tkinter.messagebox.showerror("Warning","Enter correct email ")

                elif (not(phone.match(num.get())) and  email.match(em.get())):
                    tkinter.messagebox.showerror("Warning","Enter correct phone number ")
                elif (not(phone.match(num.get())) and  not(email.match(em.get()))):
                    tkinter.messagebox.showerror("Warning","Enter correct email ")
                    tkinter.messagebox.showerror("Warning","Enter correct phone number ")
                else:
                    try:
                        sqlCon=pymysql.connect(host="localhost",user="root",database="doctors")
                        cur=sqlCon.cursor()
                        cur.execute("select * from doctors where id=%s",d_id.get())
                        row=cur.fetchone()
                        if row!=None:
                            tkinter.messagebox.showerror("Error","ID already exists")
                        else:
                            cur.execute("insert into doctors values (%s, %s, %s, %s, %s ,%s ,%s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s, %s, %s)",(
                                d_id.get(),d_name.get(),d_spec.get(),em.get(),d_hos.get(),d_country.get(),d_exp.get(),d_birth.get(),d_city.get(),
                                d_deg.get(),d_shift.get(),d_gender.get(),d_patients.get(),d_web.get(),d_sal.get(),age.get(),days.get(),num.get()))

                            sqlCon.commit()
                            sqlCon.close()
                            tkinter.messagebox.showinfo("Success","Data entered sucessfully")
                    except Exception as es:
                        tkinter.messagebox.showerror("Error",f"Error due to :{str(es)}")



        def display():
            sqlCon=pymysql.connect(host="localhost",user="root",database="doctors")
            cur=sqlCon.cursor()
            cur.execute("select * from doctors")
            result=cur.fetchall()
            if len(result) !=0:
                self.doc_records.delete(*self.doc_records.get_children())
                for row in result:
                    self.doc_records.insert('',END,values=row)
            sqlCon.commit()
            sqlCon.close()
            

        def view(ev):
            viewinfo=self.doc_records.focus()
            data=self.doc_records.item(viewinfo)
            row=data['values']
            d_id.set(row[0])
            d_name.set(row[1])
            d_spec.set(row[2])
            em.set(row[3])
            d_hos.set(row[4])
            d_country.set(row[5])
            d_exp.set(row[6])
            d_birth.set(row[7])
            d_city.set(row[8])
            d_deg.set(row[9])
            d_shift.set(row[10])
            d_gender.set(row[11])
            d_patients.set(row[12])
            d_web.set(row[13])
            d_sal.set(row[14])
            age.set(row[15])
            days.set(row[16])
            num.set(row[17])


        def update():
            sqlCon=pymysql.connect(host="localhost",user="root",database="doctors")
            cur=sqlCon.cursor()
            cur.execute("update  doctors  set  Name=%s, Specialisation=%s, email=%s, hospital=%s ,country=%s ,experience=%s,birth= %s,city= %s, Degree=%s, shift=%s, gender=%s ,patients_treated=%s ,website=%s, salary=%s, age=%s, available=%s, number=%s where id=%s",(
                    d_name.get(),d_spec.get(),em.get(),d_hos.get(),d_country.get(),d_exp.get(),d_birth.get(),d_city.get(),
                    d_deg.get(),d_shift.get(),d_gender.get(),d_patients.get(),d_web.get(),d_sal.get(),age.get(),days.get(),num.get(),d_id.get()))
            sqlCon.commit()
            display()
            sqlCon.close()
            tkinter.messagebox.showinfo("Sucess","Record Updated")


        def delete():
            sqlCon=pymysql.connect(host="localhost",user="root",database="doctors")
            cur=sqlCon.cursor()
            cur.execute("delete from   doctors where id=%s",d_id.get())
            sqlCon.commit()
            display()
            sqlCon.close()
            tkinter.messagebox.showinfo("Sucess","Record Deleted")
            Reset()


        def search():
            try:
                sqlCon=pymysql.connect(host="localhost",user="root",database="doctors")
                cur=sqlCon.cursor()
                cur.execute("select * from  doctors where id=%s",d_id.get())
                row=cur.fetchone()
                d_id.set(row[0])
                d_name.set(row[1])
                d_spec.set(row[2])
                em.set(row[3])
                d_hos.set(row[4])
                d_country.set(row[5])
                d_exp.set(row[6])
                d_birth.set(row[7])
                d_city.set(row[8])
                d_deg.set(row[9])
                d_shift.set(row[10])
                d_gender.set(row[11])
                d_patients.set(row[12])
                d_web.set(row[13])
                d_sal.set(row[14])
                age.set(row[15])
                days.set(row[16])
                num.set(row[17])
                sqlCon.commit()
            except:
                tkinter.messagebox.showerror("Sorry","No record found")
                Reset()
          
            sqlCon.close()
            








        def Reset():
            self.docid.delete(0,END)
            age.set("")
            self.docname.delete(0,END)
            self.docmail.delete(0,END)
            self.docspec.set("")
            self.dochos.delete(0,END)
            self.docdeg.set("")
            self.docage.delete(0,END)
            self.docid.delete(0,END)
            d_exp.set("")
            self.patientstreated.delete(0,END)
            self.doccity.set("")
            self.doccountry.set("")
            self.g1.deselect()
            self.g2.deselect()
            self.g3.deselect()
            self.docphno.delete(0,END)
            days.set("")
            self.shift.set("")
            self.birth.delete(0,END)
            self.website.delete(0,END)
            self.docsal.delete(0,END)



        

            


                
        mainframe=Frame(self.root,bd=10,width=1220,height=800,relief=RIDGE,bg='cadet blue')
        mainframe.grid()


        titleframe=Frame(mainframe,bd=7,width=1220,height=100,relief=RIDGE)
        titleframe.grid(row=0,column=0)

        topframe=Frame(mainframe,bd=5,bg="white",width=1220,height=700,relief=RIDGE)
        topframe.grid(row=1,column=0)

        leftframe=Frame(topframe,bd=5,width=1200,height=400,bg="cadet blue",relief=RIDGE,pady=0,padx=2)
        leftframe.pack(side=LEFT)
        leftframe1=Frame(leftframe,bd=5,width=1100,height=180,relief=RIDGE,bg='white')
        leftframe1.pack(side=TOP)
        leftframetitle=Frame(leftframe1,bd=4,width=550,height=160,padx=10,relief=RIDGE)
        leftframetitle.grid(row=0,column=0)
        leftframetitle1=Frame(leftframe1,bd=4,width=550,height=160,relief=RIDGE,padx=10)
        leftframetitle1.grid(row=0,column=2)

        rightframe=Frame(topframe,bd=5,width=100,height=400,padx=2,pady=1,bg="cadet blue",relief=RIDGE)
        rightframe.pack(side=RIGHT)
        rightframe1=Frame(rightframe,bd=5,width=100,height=200,padx=5,pady=80,bg="white",relief=RIDGE)
        rightframe1.pack(side=TOP)

        

        # labels
        self.lbltitle=Label(titleframe,font=('arial',40,'bold'),text="Doctor Information System",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=250)

        self.lbl=Label(leftframetitle,font=('arial',20,'bold'),text="Personal Details")
        self.lbl.grid(row=0,column=0,padx=0,pady=10,sticky=W)


        self.lbl1=Label(leftframetitle1,font=('arial',20,'bold'),text="Work Details")
        self.lbl1.grid(row=0,column=0,padx=0,pady=10,sticky=W)


        self.lbldocname=Label(leftframetitle,font=('arial',14,'bold'),text="Doctor Name",bd=7)
        self.lbldocname.grid(row=1,column=0,sticky=W,padx=5)
        self.docname=Entry(leftframetitle,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_name)
        self.docname.grid(row=1,column=1,sticky=W,padx=5)

        self.lbldocid=Label(leftframetitle1,font=('arial',14,'bold'),text="Doctor ID",bd=7)
        self.lbldocid.grid(row=1,column=0,sticky=W,padx=5)
        self.docid=Entry(leftframetitle1,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_id)
        self.docid.grid(row=1,column=1,sticky=W,padx=5)

        self.lbldocage=Label(leftframetitle,font=('arial',14,'bold'),text="Doctor Age",bd=7)
        self.lbldocage.grid(row=2,column=0,sticky=W,padx=5)
        self.docage=Spinbox(leftframetitle,font=('arial',14,'bold'),bd=5,width=20,justify='left',textvariable=age,from_=22,to=100)
        self.docage.grid(row=2,column=1,sticky=W,padx=5)



        self.lbldocspec=Label(leftframetitle1,font=('arial',14,'bold'),text="Doctor Specialization",bd=7)
        self.lbldocspec.grid(row=2,column=0,sticky=W,padx=5)
        self.docspec=ttk.Combobox(leftframetitle1,font=('arial',14,'bold'),width=20,state='readonly',textvariable=d_spec)
        self.docspec['values']=('','allergist','anesthesiologist','cardiologist','dentist','dermatologist','gynecologist','neurologist','pediatrician')
        self.docspec.current(0)
        self.docspec.grid(row=2,column=1,sticky=W,padx=5)

        


    

        

        self.lbldocmail=Label(leftframetitle,font=('arial',14,'bold'),text="Doctor Email",bd=7)
        self.lbldocmail.grid(row=3,column=0,sticky=W,padx=5)
        self.docmail=Entry(leftframetitle,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=em)
        self.docmail.grid(row=3,column=1,sticky=W,padx=5)
        
       

        self.lbldochos=Label(leftframetitle1,font=('arial',14,'bold'),text="Hospital Name",bd=7)
        self.lbldochos.grid(row=3,column=0,sticky=W,padx=5)
        self.dochos=Entry(leftframetitle1,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_hos)
        self.dochos.grid(row=3,column=1,sticky=W,padx=5)

        self.lblcountry=Label(leftframetitle,font=('arial',14,'bold'),text="Country",bd=7)
        self.lblcountry.grid(row=4,column=0,sticky=W,padx=5)
        self.doccountry=ttk.Combobox(leftframetitle,font=('arial',14,'bold'),state='readonly',width=20,textvariable=d_country)
        self.doccountry['values']=('','Afghanisthan','Bangladesh','Belgium','Brazil','Canada','China','India','USA',)
        self.doccountry.current(0)
        self.doccountry.grid(row=4,column=1,sticky=W,padx=5)

        self.lbldocexp=Label(leftframetitle1,font=('arial',14,'bold'),text="Years of Experience",bd=7)
        self.lbldocexp.grid(row=4,column=0,sticky=W,padx=5)
        self.docexp=Spinbox(leftframetitle1,font=('arial',14,'bold'),bd=5,width=20,justify='left',textvariable=d_exp,from_=0,to=50)
        self.docexp.grid(row=4,column=1,sticky=W,padx=5)


        

        



        self.lblbirth=Label(leftframetitle,font=('arial',14,'bold'),text="Birth Date",bd=7)
        self.lblbirth.grid(row=5,column=0,sticky=W,padx=5)
        self.birth=DateEntry(leftframetitle,justify='left',locale='en_US',width=36,height=5,textvariable=d_birth)
        self.birth.grid(row=5,column=1,sticky=W,padx=5)



        self.lbldays=Label(leftframetitle1,font=('arial',14,'bold'),text="No of days available",bd=7)
        self.lbldays.grid(row=5,column=0,sticky=W,padx=5)
        self.docdays=Spinbox(leftframetitle1,font=('arial',14,'bold'),bd=5,width=20,justify='left',textvariable=days,from_=0,to=7)
        self.docdays.grid(row=5,column=1,sticky=W,padx=5)



       


        self.lbldoccity=Label(leftframetitle,font=('arial',14,'bold'),text="City",bd=7)
        self.lbldoccity.grid(row=6,column=0,sticky=W,padx=5)
        self.doccity=ttk.Combobox(leftframetitle,font=('arial',14,'bold'),width=20,justify='left',state='readonly',textvariable=d_city)
        self.doccity['values']=(' ','Ahemdabad','Andheri','Aurangabad','Delhi','Hyderabad','Mumbai','Nagpur','Navi Mumbai','Pune','Thane')
        self.doccity.current(0)
        self.doccity.grid(row=6,column=1,sticky=W,padx=5)




       

        


        


        self.lbldocdeg=Label(leftframetitle1,font=('arial',14,'bold'),text="Doctor Degree",bd=7)
        self.lbldocdeg.grid(row=6,column=0,sticky=W,padx=5)
        self.docdeg=ttk.Combobox(leftframetitle1,font=('arial',14,'bold'),width=20,justify='left',state='readonly',textvariable=d_deg)
        self.docdeg['values']=('','MBBS','BDS','PHD','MD')
        self.docdeg.current(0)
        self.docdeg.grid(row=6,column=1,sticky=W,padx=5)


        self.lbldocphno=Label(leftframetitle,font=('arial',14,'bold'),text="Doctor Phone No.",bd=7)
        self.lbldocphno.grid(row=7,column=0,sticky=W,padx=5)
        self.docphno=Entry(leftframetitle,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=num)
        self.docphno.grid(row=7,column=1,sticky=W,padx=5)




        self.lbldocshift=Label(leftframetitle1,font=('arial',14,'bold'),text="Shift",bd=7)
        self.lbldocshift.grid(row=7,column=0,sticky=W,padx=5)
        self.shift=ttk.Combobox(leftframetitle1,font=('arial',14,'bold'),width=20,justify='left',state='readonly',textvariable=d_shift)
        self.shift['values']=('','Morning','Evening','Night')
        self.shift.current(0)
        self.shift.grid(row=7,column=1,sticky=W,padx=5)

        


       

         


        self.lbldocgender=Label(leftframetitle,text="Doctor Gender",font=('arial',14,'bold'),bd=7,)
        self.lbldocgender.grid(row=8,column=0,sticky=W,padx=5)
        self.g1=Radiobutton(leftframetitle,font=('arial',14,'bold'),text="Male",width=3,value="Male",variable=d_gender)
        # self.g1.grid(row=8,column=1,sticky=W,padx=0)
        self.g1.place(x=220,y=322)
        self.g2=Radiobutton(leftframetitle,font=('arial',14,'bold'),text="Female",width=5,value="Female",variable=d_gender)
        # self.g2.grid(row=8,column=2,sticky=W,padx=0)
        self.g2.place(x=290,y=322)
        self.g3=Radiobutton(leftframetitle,font=('arial',14,'bold'),text="Other",width=5,value="Other",variable=d_gender)
        self.g3.place(x=380,y=322)



        

        

        self.lblpatientsteated=Label(leftframetitle1,font=('arial',14,'bold'),text="Patients Treated",bd=7)
        self.lblpatientsteated.grid(row=8,column=0,sticky=W,padx=5)
        self.patientstreated=Entry(leftframetitle1,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_patients)
        self.patientstreated.grid(row=8,column=1,sticky=W,padx=5)

        self.lblwebsite=Label(leftframetitle1,font=('arial',14,'bold'),text="Hospital Website",bd=7)
        self.lblwebsite.grid(row=9,column=0,sticky=W,padx=5)
        self.website=Entry(leftframetitle1,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_web)
        self.website.grid(row=9,column=1,sticky=W,padx=5)


        self.lbldocsal=Label(leftframetitle,font=('arial',14,'bold'),text="Doctor Salary",bd=7)
        self.lbldocsal.grid(row=9,column=0,sticky=W,padx=5)
        self.docsal=Entry(leftframetitle,font=('arial',14,'bold'),bd=5,width=21,justify='left',textvariable=d_sal)
        self.docsal.grid(row=9,column=1,sticky=W,padx=5)



        #table

        scroll=Scrollbar(leftframe,orient=VERTICAL)
        

        self.doc_records=ttk.Treeview(leftframe,height=13,columns=("id","Name","Spec","mail","hospital","country","Experience","birth","city","deg","shift","gender","patients_treated","website","salary","age","days","ph_number"),
        yscrollcommand=scroll.set)

        scroll.pack(side=RIGHT,fill=Y)
        
        scroll.config(command=self.doc_records.yview)
                                                                                                


        self.doc_records.heading("id",text="ID")
        self.doc_records.heading("Name",text="Name")
        self.doc_records.heading("Spec",text="Specialization")
        self.doc_records.heading("mail",text="email")
        self.doc_records.heading("hospital",text="Hospital Name")
        self.doc_records.heading("country",text="Country")
        self.doc_records.heading("Experience",text="Experience")
        self.doc_records.heading("birth",text="Birth Date")
        self.doc_records.heading("city",text="City")
        self.doc_records.heading("deg",text="Degree")
        self.doc_records.heading("shift",text="Shift")
        self.doc_records.heading("gender",text="Gender")
        self.doc_records.heading("patients_treated",text="No of Patients treated")
        self.doc_records.heading("website",text="Website")
        self.doc_records.heading("salary",text="Salary")
        self.doc_records.heading("age",text="Age")
        self.doc_records.heading("days",text="Days available")
        self.doc_records.heading("ph_number",text="Ph no")

        
        
        self.doc_records['show']='headings'


        self.doc_records.column("id",width=20)
        self.doc_records.column("Name",width=30)
        self.doc_records.column("Spec",width=60)
        self.doc_records.column("mail",width=30)
        self.doc_records.column("hospital",width=40)
        self.doc_records.column("country",width=35)
        self.doc_records.column("Experience",width=60)
        self.doc_records.column("birth",width=50)
        self.doc_records.column("city",width=30)
        self.doc_records.column("deg",width=30)
        self.doc_records.column("shift",width=30)
        self.doc_records.column("gender",width=30)
        self.doc_records.column("patients_treated",width=105)
        self.doc_records.column("website",width=60)
        self.doc_records.column("salary",width=30)
        self.doc_records.column("age",width=30)
        self.doc_records.column("days",width=90)
        self.doc_records.column("ph_number",width=30)
        
        
        
        
        
        
        
        







        
        self.doc_records.pack(fill=BOTH,expand=1)
        self.doc_records.bind("<ButtonRelease-1>",view)

        # buttons
        self.addbtn=Button(rightframe1,font=('arial',16,'bold'),text="SUBMIT",bd=4,padx=24,pady=1,
        width=5,height=2,command=submit)
        self.addbtn.grid(row=0,column=0,pady=3)

        self.displaybtn=Button(rightframe1,font=('arial',16,'bold'),text="DISPLAY",bd=4,padx=24,pady=1,
        width=5,height=2,command=display)
        self.displaybtn.grid(row=1,column=0,pady=3)

        self.updatebtn=Button(rightframe1,font=('arial',16,'bold'),text="UPDATE",bd=4,padx=24,pady=1,
        width=5,height=2,command=update)
        self.updatebtn.grid(row=2,column=0,pady=3)

        self.deletebtn=Button(rightframe1,font=('arial',16,'bold'),text="DELETE",bd=4,padx=24,pady=1,
        width=5,height=2,command=delete)
        self.deletebtn.grid(row=3,column=0,pady=3)

        self.searchbtn=Button(rightframe1,font=('arial',16,'bold'),text="SEARCH",bd=4,padx=24,pady=1,
        width=5,height=2,command=search)
        self.searchbtn.grid(row=4,column=0,pady=3)

        self.resetbtn=Button(rightframe1,font=('arial',16,'bold'),text="RESET",bd=4,padx=24,pady=1,
        width=5,height=2,command=Reset)
        self.resetbtn.grid(row=5,column=0,pady=3)


        self.exitbtn=Button(rightframe1,font=('arial',16,'bold'),text="EXIT",bd=4,padx=24,pady=1,
        width=5,height=2,command=iExit )
        self.exitbtn.grid(row=6,column=0,pady=3)

        Reset()

        


       






        

if __name__=='__main__':
    root=Tk()
    application=Doctor(root)
    root.mainloop()








       