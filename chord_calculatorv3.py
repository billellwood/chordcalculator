from itertools import permutations
import tkinter as tk


notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
         "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"]

def convert_notes_to_intervals(input_notes):

    new = list(permutations(input_notes))
    nl = [[] for i in new]
    for i in new:
        for j in i:
            if notes.index(j) < notes.index(i[0]):
                nl[new.index(i)].append(notes.index(j) + 12)
            else:
                nl[new.index(i)].append(notes.index(j))
    return nl

class Diads:
    def __init__(self, input_notes):
        self.input_notes = input_notes
        self.perms = convert_notes_to_intervals(self.input_notes)
    
    def chord_finder(self):
        chords = []
        for i in self.perms:
            if i[1] - i[0] == 2: 
                chords.append("{} Major 2nd".format(notes.i[0]))     
            if i[1] - i[0] == 4:
                chords.append("{} Major 3rd".format(notes[i[0]]))    
            if i[1] - i[0] == 9:
                chords.append("{} Major 6nd".format(notes.i[0]))     
            if i[1] - i[0] == 11:
                chords.append("{} Major 7th".format(notes[i[0]]))                
            if i[1] - i[0] == 3:
                chords.append("{} Minor 3rd".format(notes[i[0]]))
            if i[1] - i[0] == 8:
                chords.append("{} Minor 6th".format(notes.i[0]))      
            if i[1] - i[0] == 10:
                chords.append("{} Minor 7th".format(notes[i[0]]))         
            if i[1] - i[0]== 5:
                chords.append("{} Perfect 4".format(notes[i[0]]))
            if i[1] - i[0] == 7:
                chords.append("{} Perfect 5".format(notes[i[0]]))  
            if i[1] - i[0] == 4:  
                chords.append("{} Diminished 4".format(notes[i[0]])) 
            if i[1] - i[0] == 6:  
                chords.append("{} Diminished 5".format(notes[i[0]]))
            if i[1] - i[0] == 6:
                chords.append("{} Augmented 4".format(notes[i[0]]))                 
        return chords
                
class Triads:   
    def __init__(self, input_notes):
        self.input_notes = input_notes
        self.perms = convert_notes_to_intervals(self.input_notes)     
        
    def chord_finder(self):
        chords = []
        for i in self.perms:
            if i[1] - i[0] == 4 and i[2] - i[0] == 7:
                chords.append("{} Major".format(notes[i[0]]))
            if i[1] - i[0] == 3 and i[2] - i[0] == 7:
                chords.append("{} Minor".format(notes[i[0]]))
            if i[1] - i[0] == 4 and i[2] - i[0] == 9:
                chords.append("{} Major 6".format(notes[i[0]]))
            if i[1] - i[0] == 3 and i[2] - i[0] == 8:
                chords.append("{} Minor 6".format(notes[i[0]]))
            if i[1] - i[0] == 4 and i[2] - i[0] == 11:
                chords.append("{} Major 7".format(notes[i[0]]))
            if i[1] - i[0] == 3 and i[2] - i[0] == 10:
                chords.append("{} Minor 7".format(notes[i[0]]))
            if i[1] - i[0] == 3 and i[2] - i[0] == 6:
                chords.append("{} Diminished".format(notes[i[0]]))
            if i[1] - i[0] == 4 and i[2] - i[0] == 10:
                chords.append("{} Dominant".format(notes[i[0]]))
            if i[1] - i[0] == 4 and i[2] - i[0] == 8:
                chords.append("{} Augmented".format(notes[i[0]]))
            if i[1] - i[0] == 2 and i[2] - i[0] == 7:
                chords.append("{} Sus2".format(notes[i[0]]))      
            if i[1] - i[0] == 5 and i[2] - i[0] == 7:
                chords.append("{} Sus4".format(notes[i[0]]))
        return chords
                
class Tetrads:   
    def __init__(self, input_notes):
        self.input_notes = input_notes
        self.perms = convert_notes_to_intervals(self.input_notes)
                 
    def chord_finder(self):  
        chords = []          
        for i in self.perms:
            if i[1] - i[0] == 4 and i[2] - i[0] == 7 and i[3] - i[0] == 9:
                chords.append("{} Major 6".format(notes[i[0]]))    
                
            if i[1] - i[0] == 4 and i[2] - i[0] == 7 and i[3] - i[0] == 11:
                chords.append("{} Major 7".format(notes[i[0]]))
                
            if i[1] - i[0] == 3 and i[2] - i[0] == 7 and i[3] - i[0] == 9:
                chords.append("{} Minor 6".format(notes[i[0]]))  
                
            if i[1] - i[0] == 3 and i[2] - i[0] == 7 and i[3] - i[0] == 10:
                chords.append("{} Minor 7".format(notes[i[0]])) 
                
            if i[1] - i[0] == 4 and i[2] - i[0] == 7 and i[3] - i[0] == 10:
                chords.append("{} Dominant 7".format(notes[i[0]]))
                
            if i[1] - i[0] == 10 and i[2] - i[0] == 4 and i[3] - i[0] == 9:
                chords.append("{} 13".format(notes[i[0]]))
                
            if i[1] - i[0] == 4 and i[2] - i[0] == 11 and i[3] - i[0] == 2:
                chords.append("{} Major 9".format(notes[i[0]]))
                             
            if i[1] - i[0] == 3 and i[2] - i[0] == 10 and i[3] - i[0] == 2:
                chords.append("{} Minor 9".format(notes[i[0]]))
     
            if i[1] - i[0] == 3 and i[2] - i[0] == 6 and i[3] - i[0] == 9:
                chords.append("{} Diminished 7".format(notes[i[0]]))
           
            if i[1] - i[0] == 3 and i[2] - i[0] == 6 and i[3] - i[0] == 10:
                chords.append("{} Half Diminished".format(notes[i[0]]))
      
            if i[1] - i[0] == 9 and i[2] - i[0] == 4 and i[3] - i[0] == 7:
                chords.append("{} 6th".format(notes[i[0]]))

            if i[1] - i[0] == 3 and i[2] - i[0] == 7 and i[3] - i[0] == 11:
                chords.append("{} min(maj7)".format(notes[i[0]]))
     
            if i[1] - i[0] == 4 and i[2] - i[0] == 7 and i[3] - i[0] == 2:
                chords.append("{} add2".format(notes[i[0]]))

            if i[1] - i[0] == 3 and i[2] - i[0] == 7 and i[3] - i[0] == 2:
                chords.append("{} madd2".format(notes[i[0]]))

            if i[1] - i[0] == 4 and i[2] - i[0] == 6 and i[3] - i[0] == 10:
                chords.append("{} Dom7b5".format(notes[i[0]]))
        return chords



    
def chord_calculator():
    
    input_notes = user_input.get().split(",")
    for i in input_notes:
        if i not in notes:
            return ValueError("Sorry, those notes aren't correct. Please try again")
    
    if len(input_notes) == 1:
        return ValueError("Sorry, you have to enter more than one note!")
    
    
    if len(input_notes) == 2:
        input_notes = Diads(input_notes)
        return input_notes.chord_finder()

    if len(input_notes) == 3:
        input_notes = Triads(input_notes)
        return input_notes.chord_finder()
        
    if len(input_notes) == 4:
        input_notes = Tetrads(input_notes)
        return input_notes.chord_finder()
               

def running_chord_calculator():
    
    answer = chord_calculator()
    
    lbl_result["text"] = answer
    
    if len(answer) == 0:
        raise ValueError("Oh Damn!")
        
    if len(answer) == 1:
        print("Looks like your chord is:")
        for i in answer:
            return print(i)
    
    if len(answer) > 1:
        for i in answer:
            if answer.index(i) == 0:
                print("The likely chord is: \n{}".format(i))
                print("But the following chords match too:")
            else:
                print(i)

                

   


    
window = tk.Tk()

window.title("Bill's chord calculator")
frm_entry = tk.Frame(master=window)
     
instructions = tk.Label(master = frm_entry,text = "Enter in your combination of notes", 
              foreground = "black")
user_input = tk.Entry(master = frm_entry,width=30)

input_notes = user_input.get()
     
btn = tk.Button(master=window,text = "Enter notes", 
                     command = running_chord_calculator)

lbl_result = tk.Label(master = window, text = input_notes) 

frm_entry.grid(row=0,column=0,padx=10)
instructions.grid(row=0,column=0)
user_input.grid(row=1,column=0)
btn.grid(row=2, column=0, pady=10)
lbl_result.grid(row=5, column=0, padx=10)

     
window.mainloop()
      

   
    
    
    
    

        
    
    
            
     
            
            
            
                                

    
    
        
    
    


        
    
            
            

        
        
            
        
    
    
    