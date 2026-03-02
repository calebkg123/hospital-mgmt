import pickle
import datetime
import os
import math
from prettytable import PrettyTable #python -m pip install -U prettytable

def add_patient():
    file1=open("hospital.dat","ab")
    file2=open("patients.dat","ab")
    
    print(f'{"ADD PATIENT RECORD":^130}')
    n=int(input(f'{"Enter number of patients: ":>65}'))
    for i in range(n):
        pid=int(input(f'{"Enter patient ID: ":>65}'))
        nm=input(f'{"Enter full name: ":>65}')
        gen=input(f'{"Enter gender (M/F): ":>65}').upper()
        if gen not in "MF":
            print(f'{"Enter only M or F":^130}')
            gen=input(f'{"Enter gender (M/F): ":>65}').upper()
            
        dob=input(f'{"Enter date of birth [dd-mm-yyyy]: ":>65}')
        d,m,y=dob.split("-")
        date=datetime.datetime.now()
        ageyr=(int(date.strftime("%Y"))-int(y))
        agemon=abs((int(date.strftime("%m"))-int(m)))
        reg=date.strftime("%d-%m-%Y %H:%M")
        
        ph=int(input(f'{"Enter phone number: ":>65}'))
        addr=input(f'{"Enter address: ":>65}')
        print()
        
        rec1={pid:[nm,gen,dob,ph,addr,reg]}
        pickle.dump(rec1,file1)
        for k,v in rec1.items():
            print(f'{"Patient ID: ":>65}',k)
            print(f'{"Name: ":>65}',v[0])
            print(f'{"Gender: ":>65}',v[1])
            print(f'{"DOB: ":>65}',v[2])
            print(f'{"Age: ":>65}',ageyr,"Y",agemon,"M")
            print(f'{"Phone: ":>65}',v[3])
            print(f'{"Address: ":>65}',v[4])
            print(f'{"Registered: ":>65}',v[5])
            print()
            
        rec2={pid:[0]}
        pickle.dump(rec2,file2)
    file1.close()
    file2.close()
    
def read_patient():
    file=open("hospital.dat","rb")
    print(f'{"ACCESS PATIENT RECORD":^130}')
    itm=int(input(f'{"Enter patient ID: ":>65}'))
    print()
    flag=0
    try:
        while True:
            date=datetime.datetime.now()
            rec=pickle.load(file)
            for k,v in rec.items():
                if k==itm:
                    d,m,y=v[2].split("-")
                    ageyr=(int(date.strftime("%Y"))-int(y))
                    agemon=abs((int(date.strftime("%m"))-int(m)))
                    print(f'{"Patient ID: ":>65}',k)
                    print(f'{"Name: ":>65}',v[0])
                    print(f'{"Gender: ":>65}',v[1])
                    print(f'{"DOB: ":>65}',v[2])
                    print(f'{"Age: ":>65}',ageyr,"Y",agemon,"M")
                    print(f'{"Phone: ":>65}',v[3])
                    print(f'{"Address: ":>65}',v[4])
                    print(f'{"Registered: ":>65}',v[5])
                    print()
                    flag=1
    except EOFError:
        pass
    file.close()

    if flag==0:
        print(f'{"ID not found.":^130}')

def mod_patient():
    print(f'{"MODIFY PATIENT RECORD":^130}')
    itm=int(input(f'{"Enter patient ID: ":>65}'))
    print()

    #reading old record
    file=open("hospital.dat","rb")
    flag=0
    try:
        while True:
            rec=pickle.load(file)
            for k,v in rec.items():
                if k==itm:
                    print(f'{"Patient ID: ":>65}',k)
                    print(f'{"Name: ":>65}',v[0])
                    print(f'{"Gender: ":>65}',v[1])
                    print(f'{"DOB: ":>65}',v[2])
                    print(f'{"Phone: ":>65}',v[3])
                    print(f'{"Address: ":>65}',v[4])
                    print(f'{"Registered: ":>65}',v[5])
                    print()
                    flag=1
    except EOFError:
        pass
    file.close()

    if flag==0:
        print(f'{"ID not found.":^130}')    

    #modify name
    def mod_nm():
        f1=open("hospital.dat","rb")
        f2=open("temp.dat","wb")
        try:
            while True:
                rec=pickle.load(f1)
                for k,v in rec.items():
                    if k==itm:
                        new_nm=input(f'{"Enter new name: ":>65}')
                        rec.update({k:[new_nm,v[1],v[2],v[3],v[4],v[5]]})
                        print()
                    pickle.dump(rec,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("hospital.dat")
        os.rename("temp.dat","hospital.dat")
        
        #reading new record
        file=open("hospital.dat","rb")
        try:
            while True:
                rec=pickle.load(file)
                for k,v in rec.items():
                    if k==itm:
                        print(f'{"Patient ID: ":>65}',k)
                        print(f'{"Name (*NEW*): ":>65}',v[0])
                        print(f'{"Gender: ":>65}',v[1])
                        print(f'{"DOB: ":>65}',v[2])
                        print(f'{"Phone: ":>65}',v[3])
                        print(f'{"Address: ":>65}',v[4])
                        print(f'{"Registered: ":>65}',v[5])
                        print()
        except EOFError:
            pass
        file.close()
       
    #modify gender
    def mod_gen():
        f1=open("hospital.dat","rb")
        f2=open("temp.dat","wb")
        try:
            while True:
                rec=pickle.load(f1)
                for k,v in rec.items():
                    if k==itm:
                        new_gen=input(f'{"Enter new gender (M/F): ":>65}').upper()
                        if new_gen not in "MF":
                            print(f'{"Enter only M or F":>65}')
                            new_gen=input(f'{"Enter new gender (M/F): ":>65}').upper()    
                        rec.update({k:[v[0],new_gen,v[2],v[3],v[4],v[5]]})
                        print()
                    pickle.dump(rec,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("hospital.dat")
        os.rename("temp.dat","hospital.dat")
        
        #reading new record
        file=open("hospital.dat","rb")
        try:
            while True:
                rec=pickle.load(file)
                for k,v in rec.items():
                    if k==itm:
                        print(f'{"Patient ID: ":>65}',k)
                        print(f'{"Name: ":>65}',v[0])
                        print(f'{"Gender (*NEW*): ":>65}',v[1])
                        print(f'{"DOB: ":>65}',v[2])
                        print(f'{"Phone: ":>65}',v[3])
                        print(f'{"Address: ":>65}',v[4])
                        print(f'{"Registered: ":>65}',v[5])
                        print()
        except EOFError:
            pass
        file.close()

    #modify date of birth
    def mod_dob():
        f1=open("hospital.dat","rb")
        f2=open("temp.dat","wb")
        try:
            while True:
                rec=pickle.load(f1)
                for k,v in rec.items():
                    if k==itm:
                        new_dob=input(f'{"Enter new DOB: ":>65}')
                        nd,nm,ny=new_dob.split("-")
                        date=datetime.datetime.now()
                        ageyr=(int(date.strftime("%Y"))-int(ny))
                        agemon=abs((int(date.strftime("%m"))-int(nm)))
                        rec.update({k:[v[0],v[1],new_dob,v[3],v[4],v[5]]})
                        print()
                    pickle.dump(rec,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("hospital.dat")
        os.rename("temp.dat","hospital.dat")
        
        #reading new record
        file=open("hospital.dat","rb")
        try:
            while True:
                rec=pickle.load(file)
                for k,v in rec.items():
                    if k==itm:
                        print(f'{"Patient ID: ":>65}',k)
                        print(f'{"Name: ":>65}',v[0])
                        print(f'{"Gender: ":>65}',v[1])
                        print(f'{"DOB (*NEW*): ":>65}',v[2])
                        print(f'{"Age (*NEW*): ":>65}',ageyr,"Y",agemon,"M")
                        print(f'{"Phone: ":>65}',v[3])
                        print(f'{"Address: ":>65}',v[4])
                        print(f'{"Registered: ":>65}',v[5])
                        print()
        except EOFError:
            pass
        file.close()

    #modify phone
    def mod_ph():
        f1=open("hospital.dat","rb")
        f2=open("temp.dat","wb")
        try:
            while True:
                rec=pickle.load(f1)
                for k,v in rec.items():
                    if k==itm:
                        new_ph=int(input(f'{"Enter new phone: ":>65}'))
                        rec.update({k:[v[0],v[1],v[2],new_ph,v[4],v[5]]})
                        print()
                    pickle.dump(rec,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("hospital.dat")
        os.rename("temp.dat","hospital.dat")
        
        #reading new record
        file=open("hospital.dat","rb")
        try:
            while True:
                rec=pickle.load(file)
                for k,v in rec.items():
                    if k==itm:
                        print(f'{"Patient ID: ":>65}',k)
                        print(f'{"Name: ":>65}',v[0])
                        print(f'{"Gender: ":>65}',v[1])
                        print(f'{"DOB: ":>65}',v[2])
                        print(f'{"Phone (*NEW*): ":>65}',v[3])
                        print(f'{"Address: ":>65}',v[4])
                        print(f'{"Registered: ":>65}',v[5])
                        print()
        except EOFError:
            pass
        file.close()

    #modify address
    def mod_addr():
        f1=open("hospital.dat","rb")
        f2=open("temp.dat","wb")
        try:
            while True:
                rec=pickle.load(f1)
                for k,v in rec.items():
                    if k==itm:
                        new_addr=input(f'{"Enter new address: ":>65}')
                        rec.update({k:[v[0],v[1],v[2],v[3],new_addr,v[5]]})
                        print()
                    pickle.dump(rec,f2)
        except EOFError:
            pass
        f1.close()
        f2.close()
        os.remove("hospital.dat")
        os.rename("temp.dat","hospital.dat")
        
        #reading new record
        file=open("hospital.dat","rb")
        try:
            while True:
                rec=pickle.load(file)
                for k,v in rec.items():
                    if k==itm:
                        print(f'{"Patient ID: ":>65}',k)
                        print(f'{"Name: ":>65}',v[0])
                        print(f'{"Gender: ":>65}',v[1])
                        print(f'{"DOB: ":>65}',v[2])
                        print(f'{"Phone: ":>65}',v[3])
                        print(f'{"Address (*NEW*): ":>65}',v[4])
                        print(f'{"Registered: ":>65}',v[5])
                        print()
        except EOFError:
            pass
        file.close()

    while flag==1:
        print(f'{"1 - ":>65}{"Name"}')
        print(f'{"2 - ":>65}{"Gender"}')
        print(f'{"3 - ":>65}{"DOB"}')
        print(f'{"4 - ":>65}{"Phone"}')
        print(f'{"5 - ":>65}{"Address"}')
        print(f'{"6 - ":>65}{"EXIT"}')
        inp=int(input(f'{"Enter detail to modify: ":>65}'))
        if inp==1:
            mod_nm()
        elif inp==2:
            mod_gen()
        elif inp==3:
            mod_dob()
        elif inp==4:
            mod_ph()
        elif inp==5:
            mod_addr()
        else:
            break
            
def del_patient():
    print(f'{"DELETE PATIENT RECORD":^130}')
    itm=int(input(f'{"Enter patient ID: ":>65}'))
    print()

    f1=open("hospital.dat","rb")
    f2=open("temp.dat","wb")
    flag=0

    try:
        while True:
            rec=pickle.load(f1)
            for k,v in rec.items():
                if k!=itm:
                    pickle.dump(rec,f2)
                elif k==itm:
                    print(f'{"The following record will be deleted.":^130}')
                    print(f'{"Patient ID: ":>65}',k)
                    print(f'{"Name: ":>65}',v[0])
                    print(f'{"Registered: ":>65}',v[5])
                    flag=1       
    except:
            pass

    if flag==0:
        print(f'{"ID not found.":^130}')

    f1.close()
    f2.close()
    os.remove("hospital.dat")
    os.rename("temp.dat","hospital.dat")
    
def appointment():
    print(f'{"PATIENT APPOINTMENT":^130}')
    itm=int(input(f'{"Enter patient ID: ":>65}'))
    print()
    file=open("patients.dat","rb")
    f2=open("hospital.dat","rb")
    f3=open("temp_patients.dat","wb")
    flag=0
    file.seek(0)

    try:
        while True:
            rec=pickle.load(f2)
            for k,v in rec.items():
                if k==itm:
                    flag=1
                    print(f'{"Patient ID: ":>65}',k)
                    print(f'{"Name: ":>65}',v[0])
                    print(f'{"Registered: ":>65}',v[5])
                    print()
    except EOFError:
        pass
    f2.close()

    if flag==0:
        print(f'{"ID not found.":^130}')

    def Card():
        print(f'{"Doctors available in cardiology department:":^130}')
        print(f'{"1 - ":>56}{"Dr. Hebah Ben Salamah"}')
        print(f'{"2 - ":>56}{"Dr. Fahad Al-Mutawa"}')
        n=int(input(f'{"Choose doctor: ":>74}'))
        print()
        print(f'{"1 - ":>56}{"Initial checkup"}')
        print(f'{"2 - ":>56}{"Follow-up checkup"}')
        print(f'{"3 - ":>56}{"Post-surgery"}')
        print(f'{"4 - ":>56}{"Emergency"}')
        val=int(input(f'{"Enter your option: ":>74}'))
        print()
        
        if n==1:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:
                            if val==1:
                                v.append("C 11")
                            elif val==2:
                                v.append("C 12")
                            elif val==3:
                                v.append("C 13")
                            elif val==4:
                                v.append("C 14")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}')
                        pickle.dump(rec,f3)  
            except EOFError:
                pass                      
        elif n==2:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:
                            if val==1:
                                v.append("C 21")
                            elif val==2:
                                v.append("C 22")
                            elif val==3:
                                v.append("C 23")
                            elif val==4:
                                v.append("C 24")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)     
            except EOFError:
                pass
        else:
            print(f'{"Incorrect option.":^130}')  
        file.close()
        f3.close()
        os.remove("patients.dat")
        os.rename("temp_patients.dat","patients.dat")
            
    def ENT():
        print(f'{"Doctors available in ENT department:":^130}')
        print(f'{"1 - ":>56}{"Dr. Ashraf Yousef"}')
        print(f'{"2 - ":>56}{"Dr. Jefna Sagir"}')
        n=int(input(f'{"Choose doctor: ":>74}'))
        print()
        print(f'{"1 - ":>56}{"Initial checkup"}')
        print(f'{"2 - ":>56}{"Follow-up checkup"}')
        print(f'{"3 - ":>56}{"Post-surgery"}')
        print(f'{"4 - ":>56}{"Emergency"}')
        val=int(input(f'{"Enter your option: ":>74}'))
        
        if n==1:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:
                            if val==1:
                                v.append("E 11")
                            elif val==2:
                                v.append("E 12")
                            elif val==3:
                                v.append("E 13")
                            elif val==4:
                                v.append("E 14")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)
            except EOFError:
                pass   
        elif n==2:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("E 21")
                            elif val==2:
                                v.append("E 22")
                            elif val==3:
                                v.append("E 23")
                            elif val==4:
                                v.append("E 24")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}')
                        pickle.dump(rec,f3)
            except EOFError:
                pass
        else:
            print(f'{"Incorrect option.":^130}')
            
        file.close()
        f3.close()
        os.remove("patients.dat")
        os.rename("temp_patients.dat","patients.dat")
        
        
    def Gen():
        print(f'{"Doctors available in General Surgery department:":^130}')
        print(f'{"1 - ":>56}{"Dr.  Wisam Raj"}')
        print(f'{"2 - ":>56}{"Dr.  Allen Singala"}')
        n=int(input(f'{"Choose doctor: ":>74}'))
        print()
        print(f'{"1 - ":>56}{"Initial checkup"}')
        print(f'{"2 - ":>56}{"Follow-up checkup"}')
        print(f'{"3 - ":>56}{"Post-surgery"}')
        print(f'{"4 - ":>56}{"Emergency"}')
        val=int(input(f'{"Enter your option: ":>74}'))
        
        if n==1:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("G 11")
                            elif val==2:
                                v.append("G 12")
                            elif val==3:
                                v.append("G 13")
                            elif val==4:
                                v.append("G 14")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)           
            except EOFError:
                pass  
        elif n==2:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("G 21")
                            elif val==2:
                                v.append("G 22")
                            elif val==3:
                                v.append("G 23")
                            elif val==4:
                                v.append("G 24")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)       
            except EOFError:
                pass
        else:
            print(f'{"Incorrect option.":^130}')
            
        file.close()
        f3.close()
        os.remove("patients.dat")
        os.rename("temp_patients.dat","patients.dat")
        
        
    def Neur():
        print(f'{"Doctors available in Neurology department:":^130}')
        print(f'{"1 - ":>56}{"Dr.  Abdul Hamid"}')
        print(f'{"2 - ":>56}{"Dr.  Mina Gamal"}')
        n=int(input(f'{"Choose doctor: ":>74}'))
        print()
        print(f'{"1 - ":>56}{"Initial checkup"}')
        print(f'{"2 - ":>56}{"Follow-up checkup"}')
        print(f'{"3 - ":>56}{"Post-surgery"}')
        print(f'{"4 - ":>56}{"Emergency"}')
        val=int(input(f'{"Enter your option: ":>74}'))
        
        if n==1:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("N 11")
                            elif val==2:
                                v.append("N 12")
                            elif val==3:
                                v.append("N 13")
                            elif val==4:
                                v.append("N 14")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)     
            except EOFError:
                pass
        elif n==2:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("N 21")
                            elif val==2:
                                v.append("N 22")
                            elif val==3:
                                v.append("N 23")
                            elif val==4:
                                v.append("N 24")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)                            
            except EOFError:
                pass
        else:
            print(f'{"Incorrect option.":^130}')
            
        file.close()
        f3.close()
        os.remove("patients.dat")
        os.rename("temp_patients.dat","patients.dat")
            
    def Phys():
        print(f'{"Doctors available in Physiotherapy department:":^130}')
        print(f'{"1 - ":>56}{"Dr.  Dema Aman"}')
        print(f'{"2 - ":>56}{"Dr.  Maryam Al-Mulla"}')
        n=int(input(f'{"Choose doctor: ":>74}'))
        print()
        print(f'{"1 - ":>56}{"Initial checkup"}')
        print(f'{"2 - ":>56}{"Follow-up checkup"}')
        print(f'{"3 - ":>56}{"Post-surgery"}')
        print(f'{"4 - ":>56}{"Emergency"}')
        val=int(input(f'{"Enter your option: ":>74}'))
        
        if n==1:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:
                            if val==1:
                                v.append("P 11")
                            elif val==2:
                                v.append("P 12")
                            elif val==3:
                                v.append("P 13")
                            elif val==4:
                                v.append("P 14")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)                          
            except EOFError:
                pass    
        elif n==2:
            try:
                while True:
                    rec=pickle.load(file)
                    for k,v in rec.items():
                        if k==itm:                        
                            if val==1:
                                v.append("P 21")
                            elif val==2:
                                v.append("P 22")
                            elif val==3:
                                v.append("P 23")
                            elif val==4:
                                v.append("P 24")
                            else:
                                print(f'{"Incorrect option.":^130}')
                            print(f'{"Saved.":^130}') 
                        pickle.dump(rec,f3)
            except EOFError:
                pass
        else:
            print(f'{"Incorrect option.":^130}')
            
        file.close()
        f3.close()
        os.remove("patients.dat")
        os.rename("temp_patients.dat","patients.dat")
    
    if flag==1:
        print(f'{"1 - ":>56}{"Cardiology"}')
        print(f'{"2 - ":>56}{"Ear, Nose, and Throat (ENT)"}')
        print(f'{"3 - ":>56}{"General Surgery"}')
        print(f'{"4 - ":>56}{"Neurology"}')
        print(f'{"5 - ":>56}{"Physiotherapy"}')
        n=int(input(f'{"Choose department: ":>74}'))
        print()
        if n==1:
            Card()
        elif n==2:
            ENT()
        elif n==3:
            Gen()
        elif n==4:
            Neur()
        elif n==5:
            Phys()

def patient_bill():
    file=open("patients.dat","rb")
    f1=open("hospital.dat","rb")
    f2=open("print_receipt.txt","w")
    print(f'{"HOSPITAL BILLING":^130}')
    itm=int(input(f'{"Enter patient ID: ":>65}'))
    print()
    flag=0
    tot=0
    c=1
    L=[]

    try:
        while True:
            date=datetime.datetime.now()
            rec1=pickle.load(f1)
            for k,v in rec1.items():
                if k==itm:
                    d,m,y=v[2].split("-")
                    ageyr=(int(date.strftime("%Y"))-int(y))
                    agemon=abs((int(date.strftime("%m"))-int(m)))
                    print(f'{"Patient ID: ":>65}',k)
                    print(f'{"Name: ":>65}',v[0])
                    print(f'{"Gender: ":>65}',v[1])
                    print(f'{"DOB: ":>65}',v[2])
                    print(f'{"Age: ":>65}',ageyr,"Y",agemon,"M")
                    print(f'{"Phone: ":>65}',v[3])
                    print(f'{"Address: ":>65}',v[4])
                    print(f'{"Registered: ":>65}',v[5])
                    print()
                    flag=1
                    
                    info=("Patient ID: "+str(k)+"\n"
                          +"Name: "+v[0]+"\n"+"Gender: "+v[1]+"\n"
                          +"DOB: "+str(v[2])+"\n"
                          +"Age: "+str(ageyr)+" Y "+str(agemon)+" M "+"\n"
                          +"Phone: "+str(v[3])+"\n"
                          +"Address: "+v[4]+"\n"+"\n"
                          +"Date & Time: "+date.strftime("%d-%m-%Y %H:%M"))
    except EOFError:
        pass
    f1.close()

    if flag==0:
        print(f'{"ID not found.":^130}')
        

    x=PrettyTable()
    s3="   "
    s9=3*s3
    x.field_names=([s3+"No"+s3, s3+s3+" Code "+s3+s3, s9+s9+s9+" Description "+s9+s9+s9, s9+"Price"+s9])

    try:
        while True:
            rec=pickle.load(file)
            for k,v in rec.items():
                if k==itm:
                    for ele in v:
                        if ele==0:
                            row=[c,ele,"Open patient file","10.000"]
                        elif ele=="C 11" or ele=="C 21":
                            row=[c,ele,"Initial checkup (Cardiology)","20.000"]
                        elif ele=="E 11" or ele=="E 21":
                            row=[c,ele,"Initial checkup (ENT)","15.000"]                            
                        elif ele=="G 11" or ele=="G 21":
                            row=[c,ele,"Initial checkup (Gen Surgery)","15.000"]                            
                        elif ele=="N 11" or ele=="N 21":
                            row=[c,ele,"Initial checkup (Neurology)","15.000"]                            
                        elif ele=="P 11" or ele=="P 21":
                            row=[c,ele,"Initial checkup (Physiotherapy)","10.000"]
                        
                        elif ele=="C 12" or ele=="C 22":
                            row=[c,ele,"Follow-up checkup (Cardiology)","15.000"]                            
                        elif ele=="E 12" or ele=="E 22":
                            row=[c,ele,"Follow-up checkup (ENT)","10.000"]                            
                        elif ele=="G 12" or ele=="G 22":
                            row=[c,ele,"Follow-up checkup (Gen Surgery)","20.000"]                            
                        elif ele=="N 12" or ele=="N 22":
                            row=[c,ele,"Follow-up checkup (Neurology)","15.000"]                            
                        elif ele=="P 12" or ele=="P 22":
                            row=[c,ele,"Follow-up checkup (Physiotherapy)","10.000"]
                            
                        elif ele=="C 13" or ele=="C 23":
                            row=[c,ele,"Post Surgery (Cardiology)","10.000"]                            
                        elif ele=="E 13" or ele=="E 23":
                            row=[c,ele,"Post Surgery (ENT)","5.000"]                            
                        elif ele=="G 13" or ele=="G 23":
                            row=[c,ele,"Post Surgery (Gen Surgery)","15.000"]                            
                        elif ele=="N 13" or ele=="N 23":
                            row=[c,ele,"Post Surgery (Neurology)","15.000"]                            
                        elif ele=="P 13" or ele=="P 23":
                            row=[c,ele,"Post Surgery (Physiotherapy)","15.000"]
                            
                        elif ele=="C 14" or ele=="C 24":
                            row=[c,ele,"Emergency (Cardiology)","15.000"]                            
                        elif ele=="E 14" or ele=="E 24":
                            row=[c,ele,"Emergency (ENT)","15.000"]
                        elif ele=="G 14" or ele=="G 24":
                            row=[c,ele,"Emergency (Gen surgery)","20.000"]                            
                        elif ele=="N 14" or ele=="N 24":
                            row=[c,ele,"Emergency (Neurology)","20.000"]
                        elif ele=="P 14" or ele=="P 24":
                            row=[c,ele,"Emergency (Physiotherapy)","15.000"]
                            
                        x.add_row(row)
                        tot+=float(row[3])
                        c+=1         
    except EOFError:
        pass

    x.align["No"]="r"
    x.align["Price"] = "l"    
    x.add_row(["","","",""])       
    x.add_row(["","","TOTAL",tot])

    if flag==1:
        if tot!=0:
            f2.write(info)
            f2.write("\n"+"HOSPITAL INVOICE"+"\n")
            print(f'{"HOSPITAL INVOICE":^130}')
            print(x)
            L=str(x)
            f2.writelines(L)
            f2.close()
        else:
            print(f'{"All fees have been paid.":^130}')

    #clearing the pending fees from patients.dat
    f3=open("temp_pat.dat","ab")
    file.seek(0)
    try:
        while True:
            rec3=pickle.load(file)
            for k,v in rec3.items():
                if k==itm:
                    v.clear()
                pickle.dump(rec3,f3)
    except EOFError:
        pass

    file.close()
    f3.close()
    os.remove("patients.dat")
    os.rename("temp_pat.dat","patients.dat")
              
while True:
    print()
    print(f'{"HOSPITAL MANAGEMENT SYSTEM":^130}')
    print()
    print(f'{"--- MAIN MENU ---":^130}')
    print(f'{"A - ":>56}{"Add patient record"}')
    print(f'{"B - ":>56}{"Access patient record"}')
    print(f'{"C - ":>56}{"Modify patient record"}')
    print(f'{"D - ":>56}{"Delete patient record"}')
    print(f'{"E - ":>56}{"Add patient appointment"}')
    print(f'{"F - ":>56}{"Patient billing"}')
    print(f'{"G - ":>56}{"EXIT"}')
    print()
    menuopt=input(f'{"Choose your option: ":>74}')
    print()
    if menuopt in "Aa":
        add_patient()
    elif menuopt in "Bb":
        read_patient()
    elif menuopt in "Cc":
        mod_patient()
    elif menuopt in "Dd":
        del_patient()
    elif menuopt in "Ee":
        appointment()
    elif menuopt in "Ff":
        patient_bill()
    else:
        print(f'{"---- Thank You ----":^130}')
        break
