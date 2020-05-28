from flask import Flask,render_template,request,redirect,flash,url_for

app=Flask(__name__)
app.config['SECRET_KEY']='kladsfjhewgvnjfsndbfjdkljsioskfkjfioekdnkwooweqpncvdfggdfggeehjrgbuemireomuntehl'

@app.route("/")
def home():
    title="Online CGPA Calculator|Anna University|Regulation 2017"
    description="Online CGPA Calculator for Anna University Regulation 2017.This website will provide CGPA calculator for Engineering students of Anna University and affilated colleges for Regulation 2017"
    keywords="CGPA calculator,online CGPA calculator,cgpa calculator,Anna University,Regulation 2017,Online CGPA Calculator,Engineering college,CGPA Calculator for Anna University Regulation 2017"
    return render_template("app_home.html",title=title,description=description,keywords=keywords)

@app.route("/Departmens")
def departments():
    title="Departments|CGPA Calculator Anna University Regulation 2017"
    description="list of departments available to calculate CGPA for Anna University regulation 2017"
    keywords="EIE,ECE,EEE,IT,CSE,MECH,CIVIL,AERONAUTICAL,AUTOMOBILE,BIOMEDICAL,BIOTECHNOLOGY,BIOMEDICAL,AGRICULTURE,ENGINEERING,eie,ece,eee,it,cse,mech,civil,aeronautical engineering,automobile engineering,biomedical engineering,agriculture engineering,biomedical engineering"
    return render_template("departments.html",title=title,description=description,keywords=keywords)

#department wise CGPA calculator

@app.route('/Departments/EIE')
def eie():
    title="Electronics and Instrumentation Engineering|CGPA Calculator Regulation 2017"
    description="CGPA Calculator for Electronics and Instrumentation Engineering Regulation 2017"
    keywords="eie,electronics and instrumentation engineering,EIE,CGPA Calcualtor,Regulation 2017,regulation 2017,cgpa calculator"
    return render_template("eie_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/EEE')
def eee():
    title="EEE|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Electrical and Electronics Engineering Anna University Regulation 2017"
    keywords="eee,Electrical and Electronics engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("eee_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/ECE')
def ece():
    title="ECE|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Electronics and Communication Engineering Anna University Regulation 2017"
    keywords="ece,Electronics and Communication engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("ece_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/IT')
def it():
    title="INFORMATION TECHNOLOGY|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for information technology Anna University Regulation 2017"
    keywords="information technology,cgpa calculator,anna university,regulation 2017"
    return render_template("it_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/CSE')
def cse():
    title="CSE|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Computer Science Engineering Anna University Regulation 2017"
    keywords="Computer Science engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("cse_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/CIVIL')
def civil():
    title="CIVIL ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Civil Engineering Anna University Regulation 2017"
    keywords="civil engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("civil_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/MECH')
def mech():
    title="MECHANICAL ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Mechanical Engineering Anna University Regulation 2017"
    keywords="mechanical engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("mech_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/AUTOMOBILE')
def automobile():
    title="AERONAUTICAL ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Aeronautical Engineering Anna University Regulation 2017"
    keywords="aeronautical engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("automobile_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/AERO')
def aero():
    title="AERONAUTICAL ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Aeronautical Engineering Anna University Regulation 2017"
    keywords="Aeronautical engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("aero_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/BIOMEDICAL')
def bme():
    title="BIOMEDICAL ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Biomedical Engineering Anna University Regulation 2017"
    keywords="biomedical engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("bme_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/AGRI')
def agri():
    title="AGRICULTURE ENGINEERING|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Agriculture Engineering Anna University Regulation 2017"
    keywords="agriculture engineering,cgpa calculator,anna university,regulation 2017"
    return render_template("agri_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Departments/BIOTECH')
def biotech():
    title="BIOTECHNOLOGY|CGPA Calculator Anna University Regulation 2017"
    description="CGPA Calculator for Biotechnology Anna University Regulation 2017"
    keywords="biotechnology,cgpa claculator,regulation 2017,anna university"
    return render_template("biotech_cgpa_calculator.html",title=title,description=description,keywords=keywords)

@app.route('/Other Departments')
def others():
    title="OTHER DEPARTMENTS|CGPA Calculator Anna University Regulation 2017"
    description="custom CGPA calculator for other departments not in the departments list of our website"
    keywords="custom cgpa calculator,other departments,cgpa calculator anna university,regulation 2017"
    return render_template("other_department_cgpa_calculator.html",title=title,description=description,keywords=keywords)

#cgpa calculator function 

@app.route("/Your CGPA",methods=["GET","POST"])
def findCGPA():
    department=request.form.get('department')
    sem_1=request.form.get("sem_1")
    sem_2=request.form.get("sem_2")
    sem_3=request.form.get("sem_3")
    sem_4=request.form.get("sem_4")
    sem_5=request.form.get("sem_5")
    sem_6=request.form.get("sem_6")
    sem_7=request.form.get("sem_7")
    sem_8=request.form.get("sem_8")

    sem_gpa=[sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8]
    cgpa_num=0
    cgpa_denom=0
    for gpa in sem_gpa:
        if gpa=="":
            pass
        else:
            try:
                gpa=float(gpa)
                if (gpa>10 or gpa<0):
                    flash('please enter a value betweeen 0 and 10')
                    return redirect(url_for(department))
                elif gpa==0:
                    pass
                else:
                    cgpa_num+=gpa
                    cgpa_denom+=1
            except ValueError:
                flash("please enter a proper value")
                return redirect(url_for(department))
    try:
        cgpa=cgpa_num/cgpa_denom
        cgpa=round(cgpa,2)
        return render_template("your_cgpa.html",cgpa=cgpa)
    except ZeroDivisionError:
        flash("please enter atleast one semester's CGPA")
        return redirect(url_for(department))

#GPA calculator function

@app.route("/Your GPA",methods=["GET","POST"])
def findGPA():
    subject_no=request.form.get("subject_no")
    sem=request.form.get("semester")
    subject_no=int(subject_no)
    c1=request.form.get('sub1')
    c2=request.form.get('sub2')
    c3=request.form.get('sub3')
    c4=request.form.get('sub4')
    c5=request.form.get('sub5')
    c6=request.form.get('sub6')
    c7=request.form.get('sub7')
    c8=request.form.get('sub8')
    c9=request.form.get('sub9')
    c10=request.form.get('sub10')

    p1=request.form.get("sub1_grade")
    p2=request.form.get("sub2_grade")
    p3=request.form.get("sub3_grade")
    p4=request.form.get("sub4_grade")
    p5=request.form.get("sub5_grade")
    p6=request.form.get("sub6_grade")
    p7=request.form.get("sub7_grade")
    p8=request.form.get("sub8_grade")
    p9=request.form.get("sub9_grade")
    p10=request.form.get("sub10_grade")

    if subject_no==1:
        credit=[c1]
        points=[p1]
    elif subject_no==2:
        credit=[c1,c2]
        points=[p1,p2]
    elif subject_no==3:
        credit=[c1,c2,c3]
        points=[p1,p2,p3]
    elif subject_no==4:
        credit=[c1,c2,c3,c4]
        points=[p1,p2,p3,p4]
    elif subject_no==5:
        credit=[c1,c2,c3,c4,c5]
        points=[p1,p2,p3,p4,p5]
    elif subject_no==6:
        credit=[c1,c2,c3,c4,c5,c6]
        points=[p1,p2,p3,p4,p5,p6]
    elif subject_no==7:
        credit=[c1,c2,c3,c4,c5,c6,c7]
        points=[p1,p2,p3,p4,p5,p6,p7]
    elif subject_no==8:
        credit=[c1,c2,c3,c4,c5,c6,c7,c8]
        points=[p1,p2,p3,p4,p5,p6,p7,p8]
    elif subject_no==9:
        credit=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
        points=[p1,p2,p3,p4,p5,p6,p7,p8,p9]
    elif subject_no==10:
        credit=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
        points=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
    else:
        pass
    gpa_num=0
    gpa_denom=0
    arrears=0

    for i,j in zip(credit,points):
        try:
            i=float(i)
            j=float(j)
        except ValueError:
            flash("please enter all the values properly")
            return redirect(url_for(sem))

        gpa_num+=(i*j)
        if j==0:
            arrears+=1
        else:
            gpa_denom+=i

    gpa=gpa_num/gpa_denom
    gpa=round(gpa,3)
    return render_template("your_gpa.html",gpa=gpa,arrears=arrears)            


#department wise semesters

#EIE

@app.route("/EIE/sem 1")
def eie_sem1():
    return render_template("eie_sem1.html")

@app.route("/EIE/sem 2")
def eie_sem2():
    return render_template("eie_sem2.html")

@app.route('/EIE/sem 3')
def eie_sem3():
    return render_template('eie_sem3.html')

@app.route('/EIE/sem 4')
def eie_sem4():
    return render_template('eie_sem4.html')

@app.route('/EIE/sem 5')
def eie_sem5():
    return render_template('eie_sem5.html')

@app.route('/EIE/sem 6')
def eie_sem6():
    return render_template('eie_sem6.html')

@app.route('/EIE/sem 7')
def eie_sem7():
    return render_template('eie_sem7.html')

@app.route('/EIE/sem 8')
def eie_sem8():
    return render_template('eie_sem8.html')

#EEE

@app.route('/EEE/sem 1')
def eee_sem1():
    return render_template('eee_sem1.html')

@app.route('/EEE/sem 2')
def eee_sem2():
    return render_template('eee_sem2.html')

@app.route('/EEE/sem 3')
def eee_sem3():
    return render_template('eee_sem3.html')

@app.route('/EEE/sem 4')
def eee_sem4():
    return render_template('eee_sem4.html')

@app.route('/EEE/sem 5')
def eee_sem5():
    return render_template('eee_sem5.html')

@app.route('/EEE/sem 6')
def eee_sem6():
    return render_template('eee_sem6.html')

@app.route('/EEE/sem 7')
def eee_sem7():
    return render_template('eee_sem7.html')

@app.route('/EEE/sem 8')
def eee_sem8():
    return render_template('eee_sem8.html')

#ECE

@app.route('/ECE/sem 1')
def ece_sem1():
    return render_template('ece_sem1.html')

@app.route('/ECE/sem 2')
def ece_sem2():
    return render_template('ece_sem2.html')

@app.route('/ECE/sem 3')
def ece_sem3():
    return render_template('ece_sem3.html')

@app.route('/ECE/sem 4')
def ece_sem4():
    return render_template('ece_sem4.html')

@app.route('/ECE/sem 5')
def ece_sem5():
    return render_template('ece_sem5.html')

@app.route('/ECE/sem 6')
def ece_sem6():
    return render_template('ece_sem6.html')

@app.route('/ECE/sem 7')
def ece_sem7():
    return render_template('ece_sem7.html')

@app.route('/ECE/sem 8')
def ece_sem8():
    return render_template('ece_sem8.html')

#IT

@app.route('/IT/sem 1')
def it_sem1():
    return render_template('it_sem1.html')

@app.route('/IT/sem 2')
def it_sem2():
    return render_template('it_sem2.html')

@app.route('/IT/sem 3')
def it_sem3():
    return render_template('it_sem3.html')

@app.route('/IT/sem 4')
def it_sem4():
    return render_template('it_sem4.html')

@app.route('/IT/sem 5')
def it_sem5():
    return render_template('it_sem5.html')

@app.route('/IT/sem 6')
def it_sem6():
    return render_template('it_sem6.html')

@app.route('/IT/sem 7')
def it_sem7():
    return render_template('it_sem7.html')

@app.route('/IT/sem 8')
def it_sem8():
    return render_template('it_sem8.html')

#CSE

@app.route('/CSE/sem 1')
def cse_sem1():
    return render_template('cse_sem1.html')

@app.route('/CSE/sem 2')
def cse_sem2():
    return render_template('cse_sem2.html')

@app.route('/CSE/sem 3')
def cse_sem3():
    return render_template('cse_sem3.html')

@app.route('/CSE/sem 4')
def cse_sem4():
    return render_template('cse_sem4.html')

@app.route('/CSE/sem 5')
def cse_sem5():
    return render_template('cse_sem5.html')

@app.route('/CSE/sem 6')
def cse_sem6():
    return render_template('cse_sem6.html')

@app.route('/CSE/sem 7')
def cse_sem7():
    return render_template('cse_sem7.html')

@app.route('/CSE/sem 8')
def cse_sem8():
    return render_template('cse_sem8.html')

#CIVIL

@app.route('/CIVIL/sem 1')
def civil_sem1():
    return render_template('civil_sem1.html')

@app.route('/CIVIL/sem 2')
def civil_sem2():
    return render_template('eee_sem2.html')

@app.route('/CIVIL/sem 3')
def civil_sem3():
    return render_template('civil_sem3.html')

@app.route('/CIVIL/sem 4')
def civil_sem4():
    return render_template('civil_sem4.html')

@app.route('/CIVIL/sem 5')
def civil_sem5():
    return render_template('civil_sem5.html')

@app.route('/CIVIL/sem 6')
def civil_sem6():
    return render_template('civil_sem6.html')

@app.route('/CIVIL/sem 7')
def civil_sem7():
    return render_template('civil_sem7.html')

@app.route('/CIVIL/sem 8')
def civil_sem8():
    return render_template('civil_sem8.html')

#MECH

@app.route('/MECH/sem 1')
def mech_sem1():
    return render_template('mech_sem1.html')

@app.route('/MECH/sem 2')
def mech_sem2():
    return render_template('mech_sem2.html')

@app.route('/MECH/sem 3')
def mech_sem3():
    return render_template('mech_sem3.html')

@app.route('/MECH/sem 4')
def mech_sem4():
    return render_template('mech_sem4.html')

@app.route('/MECH/sem 5')
def mech_sem5():
    return render_template('mech_sem5.html')

@app.route('/MECH/sem 6')
def mech_sem6():
    return render_template('mech_sem6.html')

@app.route('/MECH/sem 7')
def mech_sem7():
    return render_template('mech_sem7.html')

@app.route('/MECH/sem 8')
def mech_sem8():
    return render_template('mech_sem8.html')

#AUTOMOBILE

@app.route('/AUTOMOBILE/sem 1')
def automobile_sem1():
    return render_template("automobile_sem1.html")

@app.route('/AUTOMOBILE/sem 2')
def automobile_sem2():
    return render_template("automobile_sem2.html")

@app.route('/AUTOMOBILE/sem 3')
def automobile_sem3():
    return render_template("automobile_sem3.html")

@app.route('/AUTOMOBILE/sem 4')
def automobile_sem4():
    return render_template("automobile_sem4.html")

@app.route('/AUTOMOBILE/sem 5')
def automobile_sem5():
    return render_template("automobile_sem5.html")

@app.route('/AUTOMOBILE/sem 6')
def automobile_sem6():
    return render_template("automobile_sem6.html")

@app.route('/AUTOMOBILE/sem 7')
def automobile_sem7():
    return render_template("automobile_sem7.html")

@app.route('/AUTOMOBILE/sem 8')
def automobile_sem8():
    return render_template("automobile_sem8.html")

#AERO

@app.route('/AERO/sem 1')
def aero_sem1():
    return render_template('aero_sem1.html')

@app.route('/AERO/sem 2')
def aero_sem2():
    return render_template('aero_sem2.html')

@app.route('/AERO/sem 3')
def aero_sem3():
    return render_template('aero_sem3.html')

@app.route('/AERO/sem 4')
def aero_sem4():
    return render_template('aero_sem4.html')

@app.route('/AERO/sem 5')
def aero_sem5():
    return render_template('aero_sem5.html')

@app.route('/AERO/sem 6')
def aero_sem6():
    return render_template('aero_sem6.html')

@app.route('/AERO/sem 7')
def aero_sem7():
    return render_template('aero_sem7.html')

@app.route('/AERO/sem 8')
def aero_sem8():
    return render_template('aero_sem8.html')

#BME

@app.route('/BME/sem 1')
def bme_sem1():
    return render_template('bme_sem1.html')

@app.route('/BME/sem 2')
def bme_sem2():
    return render_template('bme_sem2.html')

@app.route('/BME/sem 3')
def bme_sem3():
    return render_template('bme_sem3.html')

@app.route('/BME/sem 4')
def bme_sem4():
    return render_template('bme_sem4.html')

@app.route('/BME/sem 5')
def bme_sem5():
    return render_template('bme_sem5.html')

@app.route('/BME/sem 6')
def bme_sem6():
    return render_template('bme_sem6.html')

@app.route('/BME/sem 7')
def bme_sem7():
    return render_template('bme_sem7.html')

@app.route('/BME/sem 8')
def bme_sem8():
    return render_template('bme_sem8.html')

#AGRI

@app.route('/AGRI/sem 1')
def agri_sem1():
    return render_template('agri_sem1.html')

@app.route('/AGRI/sem 2')
def agri_sem2():
    return render_template('agri_sem2.html')

@app.route('/AGRI/sem 3')
def agri_sem3():
    return render_template('agri_sem3.html')

@app.route('/AGRI/sem 4')
def agri_sem4():
    return render_template('agri_sem4.html')

@app.route('/AGRI/sem 5')
def agri_sem5():
    return render_template('agri_sem5.html')

@app.route('/AGRI/sem 6')
def agri_sem6():
    return render_template('agri_sem6.html')

@app.route('/AGRI/sem 7')
def agri_sem7():
    return render_template('agri_sem7.html')

@app.route('/AGRI/sem 8')
def agri_sem8():
    return render_template('agri_sem8.html')

#BIOTECH

@app.route('/BIOTECH/sem 1')
def biotech_sem1():
    return render_template('biotech_sem1.html')

@app.route('/BIOTECH/sem 2')
def biotech_sem2():
    return render_template('biotech_sem2.html')

@app.route('/BIOTECH/sem 3')
def biotech_sem3():
    return render_template('biotech_sem3.html')

@app.route('/BIOTECH/sem 4')
def biotech_sem4():
    return render_template('biotech_sem4.html')

@app.route('/BIOTECH/sem 5')
def biotech_sem5():
    return render_template('biotech_sem5.html')

@app.route('/BIOTECH/sem 6')
def biotech_sem6():
    return render_template('biotech_sem6.html')

@app.route('/BIOTECH/sem 7')
def biotech_sem7():
    return render_template('biotech_sem7.html')

@app.route('/BIOTECH/sem 8')
def biotech_sem8():
    return render_template('biotech_sem8.html')

#custom GPA calulator

@app.route('/Other Departments/GPA Calculator')
def custom_gpa_calculator():
    return render_template("custom_gpa_calculator.html")

if __name__=="__main__":
    app.run()
