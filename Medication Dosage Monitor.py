# Medication Dosage Monitor Exercises
# ABZUMS AI Course - Part 3 
# Naznin Hoseini

import tkinter as tk 

# .::  step 1 : input Data for patient  ::.

patients  = [
    {
        'name': 'Alice', 
        'age': 30, 
        'weight': 60, 
        'dosages': [
            {'time': '08:00', 'dose': 10},
            {'time': '12:00', 'dose': 40}
        ]
    },
        {  'name': 'Bob', 
        'age': 16, 
        'weight': 40, 
        'dosages': [
            {'time': '08:00', 'dose': 5},
            {'time': '12:00', 'dose': -5}
        ]
    }
]


# .:: step2 : calculate safe dose  ::.

def get_safe_range(age , weight):
    if age >= 18:
        return 0.1 *weight , 0.5 * weight
    else :
        return 0.05 * weight , 0.3 * weight 
    
def dosage_safety_check(dose,min , max):
    return "safe" if min <= dose <= max  else "unsafe"
    
#.:: step3 : Analayze patient ::.
def report ():
    output =""
    for i in patients:
        age = i["age"]
        weight = i["weight"]
        name = i["name"]
        dosages = i["dosages"]
        
        min , max = get_safe_range(age , weight)
        valid_count = 0
        for med in dosages:
            time = med["time"]
            dose = med["dose"]

            if dose <= 0:
                print(f"  Invalid dose at {time}: Dose must be positive.")
                continue

            valid_count += 1
            result = dosage_safety_check(dose, min, max)
            print(f"  {time}: Dose={dose} mg - {result}")

        output += f"name is {name} , age:{age} , \n"
        output += f" weight:{weight}kg ,  safe dose is :{min}-{max} mg \n"
        output += f" total valid doses: {valid_count}"
    return output

#  ※ creat GUI window using tkinter ※   
root = tk.Tk()
root.title("patient,s dose")


#  ※ creat a form to organize layout ※
def new_func(root):
    frame = tk.Frame(root , padx=20 , pady=20)
    return frame

frame = new_func(root)
frame.pack()
# ※ Title label ※
tk.Label(frame, text="Patient Report", font=("Arial", 16)).pack(pady=10)

# ※ Text box to display report ※
text_box = tk.Text(frame, height=20, width=70)
text_box.pack()

# ※ Insert report into text box ※
report_text = report()

text_box.insert(tk.END, report_text)

#  ※ Run the GUI loop ※
root.mainloop()


