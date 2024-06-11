import tkinter as tk
from tkinter import filedialog, messagebox
import socket

def run_program(file_path, name, file_type): 
    host = '0.0.0.0'
    port = 8082

    name1 = name
    file_type1 = file_type



    counter = 1
  
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        while(counter <= 2):
            with open(file_path, "r") as fi:
                data = fi.read()
                message = name1, "::", data#;;{file_type1}"
                #sock.sendall(data.encode())
                sock.sendall(message.encode())
                
               # sock.send(name.endcode())
                counter = counter + 1
        sock.close()
        messagebox.showinfo("Success", "File", file_path, "sent successfully!")
    except ConnectionRefusedError:
        messagebox.showerror("Error", "Unable to connect to the server. Make sure the server is running.")
    except IOError:
        messagebox.showerror("Error", "Failed to read the file. Please enter a valid filename.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

#create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("400x300")

#create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()



#allow the user to upload a file from their computer
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.config(state='normal')
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        file_entry.config(state='readonly')

        input_text = entry.get()
        name = input_text


        file_type = entry2.get()

        run_program(file_path, name, file_type)
        


name_label = tk.Label(root, text = "Name the file:")
name_label.pack(pady = 10)
entry = tk.Entry(root, width = 50)
entry.pack(pady = 10)

type_label = tk.Label(root, text = "File type:")
type_label.pack(pady = 10)
entry2 = tk.Entry(root, width = 10)
entry2.pack(pady = 10)

label = tk.Label(root, text="Select a file to upload:")
label.pack(pady=10)
file_entry = tk.Entry(root, width=50, state='readonly')
file_entry.pack(pady=10)



button = tk.Button(root, text="Click Me", command=upload_file)
button.pack()

     





# Run the application
root.mainloop()

