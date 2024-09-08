from tkinter import *
from chat import get_response, bot_name

BG_COLOR = "#1F1F1F"
BG_SECONDARY = "#2E2E2E"
TEXT_COLOR = "#FFFFFF"
USER_BG_COLOR = "#DCF8C6"  
BOT_BG_COLOR = "#EAEAEA"   
ACCENT_COLOR = "#25D366"   
HOVER_COLOR = "#128C7E"    

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 16 bold"
FONT_SEND = "Helvetica 12 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat-bot :)")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=650, bg=BG_COLOR)
   
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="WelCome 2 da chat 💩", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
       
        line = Label(self.window, width=450, bg=TEXT_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
     
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_SECONDARY, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5, wrap=WORD, bd=0)
        self.text_widget.place(relheight=0.745, relwidth=0.975, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.window)
        scrollbar.place(relx=0.975, rely=0.08, relheight=0.745)
        scrollbar.configure(command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
     
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg=BG_SECONDARY, fg=TEXT_COLOR, font=FONT, bd=0)
        self.msg_entry.place(relwidth=0.70, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Canvas(bottom_label, width=120, height=60, bg=BG_COLOR, bd=0, highlightthickness=0)
        send_button.place(relx=0.73, rely=0.008, relheight=0.06, relwidth=0.26)

        send_button.create_polygon(8, 3, 122, 33, 8, 67, fill=BG_SECONDARY, outline=BG_SECONDARY)
        send_button.create_polygon(5, 1, 120, 30, 5, 64, fill=ACCENT_COLOR, outline=ACCENT_COLOR)
        send_button.create_text(75, 30, text="Send➤", fill="#000000", font=FONT_SEND)

        send_button.bind("<Enter>", lambda e: self._hover_effect(send_button, HOVER_COLOR))
        send_button.bind("<Leave>", lambda e: self._hover_effect(send_button, ACCENT_COLOR))

        send_button.bind("<Button-1>", self._on_enter_pressed)
        
    def _hover_effect(self, widget, color):
        
        widget.itemconfig(2, fill=color)
        widget.itemconfig(2, outline=color)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)

        self._insert_message_right(f"{msg}\n", USER_BG_COLOR, TEXT_COLOR)

        self._show_typing_indicator()

        self.window.after(1000, lambda: self._bot_response(msg))

    def _bot_response(self, msg):
      
        self._remove_typing_indicator()

      
        bot_reply = f"{get_response(msg)}\n"
        self._insert_message_left(bot_reply, BOT_BG_COLOR, TEXT_COLOR)  
        
    def _insert_message_right(self, msg, bg_color, fg_color):
 
        self.text_widget.configure(state=NORMAL)
        self.text_widget.tag_configure("right", justify='right', foreground=fg_color,  lmargin1=10, rmargin=10, spacing3=10)
        self.text_widget.insert(END, "\n" + msg, "right")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    def _insert_message_left(self, msg, bg_color, fg_color):
    
        self.text_widget.configure(state=NORMAL)
        self.text_widget.tag_configure("left", justify='left', foreground=fg_color,  lmargin1=10, rmargin=10, spacing3=10)
        self.text_widget.insert(END, "\n" + msg, "left")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


    def _show_typing_indicator(self):
        
        self.text_widget.configure(state=NORMAL)
        self.typing_label = Label(self.text_widget, text=f"{bot_name} is typing...", font=FONT, bg=BG_COLOR, fg="#888888")
        self.text_widget.window_create(END, window=self.typing_label)
        self.text_widget.see(END)
        self.text_widget.configure(state=DISABLED)

    def _remove_typing_indicator(self):
       
        self.text_widget.configure(state=NORMAL)
        if self.typing_label:
            self.typing_label.destroy() 
        self.text_widget.configure(state=DISABLED)

        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
