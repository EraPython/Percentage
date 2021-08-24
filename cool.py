from tkinter import *
import tkinter.ttk as ttk

def main():
    root = Tk()
    root.title("Find percentage")
    root.resizable(False,False)

    __author__ = "EraPython"

    # Percentage function
    def percentage():
        try:
            mark_list = list()
            mark_list.append(int(maths_marks_entry.get()))
            mark_list.append(int(science_marks_entry.get()))
            mark_list.append(int(hindi_marks_entry.get()))
            mark_list.append(int(english_marks_entry.get()))
            mark_list.append(int(marathi_marks_entry.get()))
            mark_list.append(int(sst_marks_entry.get()))
            percentage = sum(mark_list) / (int(total_mark_entry.get()) * len(mark_list)) * 100
            label = ttk.Label(root, text=round(percentage))
            label.grid(row=8,column=1)
        except:
            error_label = ttk.Label(root, text="Error while executing the program\nthis might have happened\n because of plotting \ndecimal number in entries")
            error_label.grid(row=8,column=1)


    # Maths section
    maths_marks_label = ttk.Label(root, text="Enter your maths marks: ")
    maths_marks_label.grid(row=1,column=1)
    maths_marks_entry = ttk.Entry(root, width=50)
    maths_marks_entry.grid(row=1,column=2)


    # Science section
    science_marks_label = ttk.Label(root, text="Enter your science marks: ")
    science_marks_label.grid(row=2,column=1)
    science_marks_entry = ttk.Entry(root, width=50)
    science_marks_entry.grid(row=2,column=2)


    # Hindi section
    hindi_marks_label = ttk.Label(root, text="Enter your hindi marks: ")
    hindi_marks_label.grid(row=3,column=1)
    hindi_marks_entry = ttk.Entry(root, width=50)
    hindi_marks_entry.grid(row=3,column=2)


    # English section
    english_marks_label = ttk.Label(root, text="Enter your english marks: ")
    english_marks_label.grid(row=4,column=1)
    english_marks_entry = ttk.Entry(root, width=50)
    english_marks_entry.grid(row=4,column=2)


    # Marathi section
    marathi_marks_label = ttk.Label(root, text="Enter your marathi marks: ")
    marathi_marks_label.grid(row=5,column=1)
    marathi_marks_entry = ttk.Entry(root, width=50)
    marathi_marks_entry.grid(row=5,column=2)


    # SST section
    sst_marks_label = ttk.Label(root, text="Enter your sst marks: ")
    sst_marks_label.grid(row=6,column=1)
    sst_marks_entry = ttk.Entry(root, width=50)
    sst_marks_entry.grid(row=6,column=2)


    # Total marks section
    total_mark_label = ttk.Label(root, text="Total marks for maths: ")
    total_mark_label.grid(row=7,column=1)
    total_mark_entry = ttk.Entry(root, width=50)
    total_mark_entry.grid(row=7,column=2)

    # Button
    button = ttk.Button(root, text="Find percentage",width=20.5, command=percentage)
    button.grid(row=9,column=2)

    root.mainloop()

if __name__ == "__main__":
    print("Running the main file.")
    print("Calculate with my percentage calculator :wink:, suggested for indian students.")
    main()
