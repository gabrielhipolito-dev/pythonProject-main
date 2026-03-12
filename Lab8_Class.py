import tkinter as tk
import tkinter.filedialog
from tkinter import *
from tkcalendar import DateEntry  # imported tkcalendar for creation of calendar dropdown entry
from PIL import ImageTk, Image


hoyo_font = "HYWenHei 85W"
# hoyo_font = "Verdana"       #uncomment if font is not installed


# --------------------------------------- OOP Class ----------------------- #
class OopDesign:
    def __init__(self):
        # initial parameters for methods
        self.frame1 = self.label1 = self.entry1 = self.calendar1 = self.button1 = self.option1 = None

        # initial parameters for new_image method
        self.length = self.width = self.path = self.image = self.img_thumb = self.label2 = None

    def new_frame(self, container, x, y, w, h, bg):
        #   creates a blank frame with its width, height, and color properties
        self.frame1 = Frame(container, width=w, height=h, bg=bg)
        self.frame1.place(x=x, y=y)

    def new_label_title(self, container, text, x, y):
        #   creates a label with brown text and gray bg, using a large font size
        self.label1 = Label(container, text=text, fg="#FFFFFF", bg="#38688F", font=(hoyo_font, 48))
        self.label1.place(x=x, y=y, anchor="center")

    def new_label(self, container, text, x, y):
        #   creates a label with brown text and gray bg
        self.label1 = Label(container, text=text, fg="#8A6138", bg="#c3c7c3", font=(hoyo_font, 11), justify="left")
        self.label1.place(x=x, y=y)

    def new_entry(self, container, x, y, w):
        #   creates an entry with corresponding width
        self.entry1 = Entry(container, width=w, fg="black", border=2, bg="white", font=(hoyo_font, 11))
        self.entry1.place(x=x, y=y)
        return self.entry1

    def new_entry_pass(self, container, x, y, w):
        #   creates an entry with corresponding width
        self.entry1 = Entry(container, width=w, fg="black", border=2, bg="white", font=(hoyo_font, 11), show="*")
        self.entry1.place(x=x, y=y)
        return self.entry1

    def new_calendar(self, container, x, y, w):
        # creates a DateEntry object
        self.calendar1 = DateEntry(container, width=w, fg="black", border=2, bg="white", font=(hoyo_font, 11))
        self.calendar1.place(x=x, y=y)
        return self.calendar1

    def new_option(self, root, container, x, y, w, choices):
        #   creates an OptionMenu object
        var = StringVar(root)
        var.set("Select 1")
        self.option1 = OptionMenu(container, var, *choices)
        self.option1.config(width=w, font=(hoyo_font, 9))
        self.option1.place(x=x, y=y)
        return self.option1, var

    def new_button(self, container, text, x, y, fg, bg, w, h):
        #   creates a button with the given width, height, and color properties
        self.button1 = Button(container, width=w, height=h, text=text, fg=fg, bg=bg, font=(hoyo_font, 10))
        self.button1.place(x=x, y=y)
        return self.button1

    def new_command_button(self, container, text, x, y, fg, bg, w, h, command):
        #   creates a button with the given width, height, and color properties
        self.button1 = Button(container, width=w, height=h, text=text, fg=fg, bg=bg, font=(hoyo_font, 10),
                              command=command)
        self.button1.place(x=x, y=y)
        return self.button1

    def new_image(self, container, path, x, y, length, width):
        self.length, self.width, self.path = length, width, path
        self.image = Image.open(path)
        self.img_thumb = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.label2 = Label(container, image=self.img_thumb)
        self.label2.place(x=x, y=y)

    # ------------------------ Optimizations  ------------------------#
    def new_label_entry(self, container, text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding entry
        self.new_label(container, text, x, y)
        entry1 = self.new_entry(container, x, y + 30, w)
        return entry1

    def new_label_entry_2(self, container, text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding entry on its right
        self.new_label(container, text, x, y)
        entry1 = self.new_entry(container, x+250, y, w)
        return entry1

    def new_label_entry_3(self, container, text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding entry with less spacing
        self.new_label(container, text, x, y)
        entry1 = self.new_entry(container, x, y + 25, w)
        return entry1

    def new_label_entry_pass(self, container, text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding entry with hidden input
        self.new_label(container, text, x, y)
        entry1 = self.new_entry_pass(container, x, y + 25, w)
        return entry1

    def new_label_calendar(self, container, text, x, y, w):
        #   creates a label with brown text and gray bg, as well as its corresponding calendar entry
        self.new_label(container, text, x, y)
        calendar1 = self.new_calendar(container, x, y + 30, w)
        return calendar1

    def new_label_option(self, root, container, text, x, y, w, choices):
        #   creates a label with brown text and gray bg, as well as its corresponding option menu
        self.new_label(container, text, x, y)
        option1, var = self.new_option(root, container, x, y + 30, w, choices)
        return option1, var


# ------------------------ Window Initialization ------------------------#
def window_startup(title, res):
    #   creates the initial Tk() object, scrollbar, and sub-frames
    window = tk.Tk()
    window.title(title)
    window.geometry(res)

    #   Creating Main_Frame
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)

    #   Creating a Canvas inside the Main_Frame
    canvas = Canvas(main_frame, bg="GRAY")
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #   Adding a Scrollbar to the Canvas
    v_scroll = Scrollbar(canvas, command=canvas.yview)
    v_scroll.pack(side=RIGHT, fill=Y)

    #   Configuring Canvas Commands
    canvas.configure(yscrollcommand=v_scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #   Creating Secondary Frame inside Canvas
    sub_frame = Frame(canvas, bg="GRAY")

    #   Creating a Window inside Canvas, which contains the Secondary Frame
    canvas.create_window((0, 0), window=sub_frame, anchor="nw")

    #   Adding scroll wheel input to move scrollbar
    def mouse_scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    sub_frame.bind_all("<MouseWheel>", mouse_scroll)

    return window, sub_frame


# ------------------------ Frame Creation ------------------------#
def frame_startup_b(sub_frame):
    heading_frame = Frame(sub_frame, width=1166, height=275, bg="#38688F")
    info_frame = Frame(sub_frame, width=1166, height=275, bg="#c3c7c3")
    dept_frame = Frame(sub_frame, width=1166, height=150, bg="#c3c7c3")
    contact_info = Label(sub_frame, text="Contact Info:", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))
    contact_frame = Frame(sub_frame, width=1166, height=150, bg="#c3c7c3")
    address = Label(sub_frame, text="Address: ", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))
    address_frame = Frame(sub_frame, width=1166, height=325, bg="#c3c7c3")
    bot_frame = Frame(sub_frame, width=1166, height=75, bg="GRAY")

    heading_frame.grid(row=0, column=0, padx=(100, 50), pady=(0, 5))
    info_frame.grid(row=1, column=0, padx=(100, 50), pady=5)
    dept_frame.grid(row=2, column=0, padx=(100, 50), pady=5)
    contact_info.grid(row=3, column=0, padx=(100, 50), pady=5, sticky="nw")
    contact_frame.grid(row=4, column=0, padx=(100, 50), pady=5)
    address.grid(row=5, column=0, padx=(100, 50), pady=5, sticky="nw")
    address_frame.grid(row=6, column=0, padx=(100, 50), pady=5)
    bot_frame.grid(row=7, column=0, padx=(100, 50), pady=5)

    return heading_frame, info_frame, dept_frame, contact_info, contact_frame, address, address_frame, bot_frame


def frame_startup_c(sub_frame):
    heading_frame = Frame(sub_frame, width=1166, height=275, bg="#38688F")
    info_frame = Frame(sub_frame, width=1166, height=500, bg="#C3C7C3")
    income_heading_frame = Frame(sub_frame, width=1166, height=30, bg="GRAY")
    income_frame = Frame(sub_frame, width=1166, height=250, bg="#C3C7C3")
    honorarium_heading_frame = Frame(sub_frame, width=1166, height=30, bg="GRAY")
    honor_frame = Frame(sub_frame, width=1166, height=350, bg="#C3C7C3")
    other_heading_frame = Frame(sub_frame, width=1166, height=30, bg="GRAY")
    other_frame = Frame(sub_frame, width=1166, height=200, bg="#C3C7C3")
    summary_heading_frame = Frame(sub_frame, width=1166, height=30, bg="GRAY")
    summary_frame = Frame(sub_frame, width=1166, height=150, bg="#c3c7c3")

    heading_frame.grid(row=0, column=0, padx=(100, 50), pady=(0, 5))
    info_frame.grid(row=2, column=0, padx=(100, 50), pady=5)
    income_heading_frame.grid(row=3, column=0, padx=(100, 50), pady=5)
    income_frame.grid(row=4, column=0, padx=(100, 50), pady=(0, 5))
    honorarium_heading_frame.grid(row=5, column=0, padx=(100, 50), pady=5)
    honor_frame.grid(row=6, column=0, padx=(100, 50), pady=(0, 5))
    other_heading_frame.grid(row=7, column=0, padx=(100, 50), pady=5)
    other_frame.grid(row=8, column=0, padx=(100, 50), pady=(0, 5))
    summary_heading_frame.grid(row=9, column=0, padx=(100, 50), pady=5)
    summary_frame.grid(row=10, column=0, padx=(100, 50), pady=(0, 5))

    basic_info = Label(sub_frame, text="Employee Basic Info:", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))
    basic_income = Label(income_heading_frame, text="Basic Income:", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))
    regular_deductions = Label(income_heading_frame, text="Regular Deductions:", fg="WHITE", bg="GRAY",
                               font=(hoyo_font, 14))
    honorarium = Label(honorarium_heading_frame, text="Honorarium Income:", fg="WHITE", bg="GRAY",
                       font=(hoyo_font, 14))
    other_deductions = Label(honorarium_heading_frame, text="Other Deductions:", fg="WHITE", bg="GRAY",
                             font=(hoyo_font, 14))
    other_income = Label(other_heading_frame, text="Other Income:", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))
    deduction_summary = Label(other_heading_frame, text="Deduction Summary:", fg="WHITE", bg="GRAY",
                              font=(hoyo_font, 14))
    summary_income = Label(summary_heading_frame, text="Other Income:", fg="WHITE", bg="GRAY", font=(hoyo_font, 14))

    basic_info.grid(row=1, column=0, padx=(100, 50), pady=5, sticky="nw")
    regular_deductions.place(x=550, y=0)
    basic_income.place(x=0, y=0)
    honorarium.place(x=0, y=0)
    other_deductions.place(x=550, y=0)
    other_income.place(x=0, y=0)
    deduction_summary.place(x=550, y=0)
    summary_income.place(x=0, y=0)

    return heading_frame, info_frame, income_frame, honor_frame, other_frame, summary_frame


def frame_startup_d(sub_frame):
    heading_frame = Frame(sub_frame, width=1166, height=275, bg="#38688F")
    info_frame = Frame(sub_frame, width=1166, height=500, bg="#c3c7c3")

    heading_frame.grid(row=0, column=0, padx=(100, 50), pady=(0, 5))
    info_frame.grid(row=2, column=0, padx=(100, 50), pady=5)

    basic_info = Label(sub_frame, text="USER ACCOUNT INFORMATION:", fg="WHITE", bg="GRAY", font=(hoyo_font, 18))
    basic_info.grid(row=1, column=0, padx=(100, 50), pady=5, sticky="nw")

    return heading_frame, info_frame


def frame_startup_login(sub_frame):
    heading_frame = Frame(sub_frame, width=1166, height=275, bg="#38688F")
    content_frame = Frame(sub_frame, width=1166, height=275, bg="#c3c7c3")

    heading_frame.grid(row=0, column=0, padx=(100, 50), pady=(0, 5))
    content_frame.grid(row=1, column=0, padx=(100, 50), pady=5)

    return heading_frame, content_frame


def frame_startup_admin(sub_frame):
    heading_frame = Frame(sub_frame, width=1166, height=275, bg="#38688F")
    content_frame = Frame(sub_frame, width=1166, height=150, bg="#c3c7c3")
    data_frame = Frame(sub_frame, width=1166, height=450, bg="#c3c7c3")

    heading_frame.grid(row=0, column=0, padx=(100, 50), pady=(0, 5))
    content_frame.grid(row=1, column=0, padx=(100, 50), pady=5)
    data_frame.grid(row=2, column=0, padx=(100, 50), pady=5)

    return heading_frame, content_frame, data_frame


# ------------------------ Other Functions ------------------------#
def change_data(widget, data):
    #   modifies the text of an existing Entry widget
    clear_data(widget)
    widget.insert(0, str(data))
    widget.configure(state="readonly")


def clear_data(widget):
    #   deletes the text of an existing Entry widget
    widget.configure(state="normal")
    widget.delete(0, "end")


def popup_box(message):
    #   creates a new Tkinter window with a short message
    root = tk.Tk()
    root.title("Furina's Employee Program")
    root.geometry("200x100+588+284")
    txt = Label(root, text=message)
    txt.place(relx=0.5, rely=0.5, anchor="center")


def open_pic():
    #   opens a file explorer window to search for a picture filepath
    filetypes = (('JPG', '*.jpg'), ('PNG', '*.png'), ('All Files', '*.*'))
    filepath = tkinter.filedialog.askopenfilename(title="Search Picture Path", initialdir="/", filetypes=filetypes)
    return filepath


def clear_widget(source_frame):
    #   deletes all widgets created on a frame
    for child in source_frame.winfo_children():
        child.destroy()


def grid_cell_1(frame, data, r, c, align):
    #   creates an Entry widget that is placed using the grid() command
    text = StringVar()
    text.set(data)
    cell = tk.Entry(frame, width=5, textvariable=text, font=(hoyo_font, 7), justify=align)
    cell.grid(row=r, column=c)
    cell.config(state="readonly")


def grid_cell_2(frame, data, r, c, align):
    #   creates an Entry widget that is placed using the grid() command
    text = StringVar()
    text.set(data)
    cell = tk.Entry(frame, width=12, textvariable=text, font=(hoyo_font, 10), justify=align)
    cell.grid(row=r, column=c)
    cell.config(state="readonly")
