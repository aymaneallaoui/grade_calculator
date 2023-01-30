import tkinter as tk

def grade_percentages(scores):
    below_5 = 0
    between_5_and_7_5 = 0
    above_7_5 = 0
    total_students = len(scores)
    
    for score in scores:
        if score < 5:
            below_5 += 1
        elif score >= 5 and score <= 7.5:
            between_5_and_7_5 += 1
        else:
            above_7_5 += 1
    
    below_5_percent = (below_5 / total_students) * 100
    between_5_and_7_5_percent = (between_5_and_7_5 / total_students) * 100
    above_7_5_percent = (above_7_5 / total_students) * 100
    
    # Create a new tkinter window
    root = tk.Tk()
    root.title("Grade Percentages")
    
    # Create labels to display the results
    above_7_5_label = tk.Label(root, text="Above 7.5/10: {:.2f}%".format(above_7_5_percent))
    above_7_5_label.pack()
    between_5_and_7_5_label = tk.Label(root, text="Between 5/10 and 7.5/10: {:.2f}%".format(between_5_and_7_5_percent))
    between_5_and_7_5_label.pack()
    below_5_label = tk.Label(root, text="Below 5/10: {:.2f}%".format(below_5_percent))
    below_5_label.pack()
    total_students_label = tk.Label(root, text="Total Students: {}".format(total_students))
    total_students_label.pack()
    
    # Run the GUI
    root.mainloop()

scores = [7.00,5.25,5.25,5.50,5.00,6.00,4.75,7.50,5.50,6.25]
