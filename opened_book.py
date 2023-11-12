# Patch update: Adds an opened book page to main.py
# - Add open_book_frame to main group of main frames
# - Replace the master of the opened_book frames

###############################################################################################################################################################################
open_book_frame = customtkinter.CTkFrame(main_content_frame,width=Main_app.winfo_screenwidth(),height=Main_app.winfo_screenheight(),fg_color="#F2E8BD")

# TEMP OPEN BOOK
# Replace home_frame with opened book frame.

open_book_frame = customtkinter.CTkFrame(home_frame, width=1360, height=765,fg_color="#F2E8BD")

# Opened book frames.

opened_book_picture_frame = customtkinter.CTkFrame(home_frame, width=250,height=300,fg_color="#414240",corner_radius=0)
opened_book_picture_frame.place(x=140,y=20)

opened_book_author_title_frame = customtkinter.CTkFrame(home_frame, width=720,height=90,fg_color="#B88B68",corner_radius=0)
opened_book_author_title_frame.place(x=430, y=20)

opened_book_other_text_frame = customtkinter.CTkFrame(home_frame, width=720,height=170,fg_color="#614D40",corner_radius=0)
opened_book_other_text_frame.place(x=430, y=110)

opened_book_synopsis_title = customtkinter.CTkFrame(home_frame, width=1005,height=80,fg_color="#614D40",corner_radius=0)
opened_book_synopsis_title.place(x=140, y=350)

opened_book_synopsis_textbody = customtkinter.CTkFrame(home_frame, width=1005,height=800,fg_color="#B88B68",corner_radius=0)
opened_book_synopsis_textbody.place(x=140, y=420)

book_status_combobox = customtkinter.CTkComboBox(home_frame,border_color="#614D40", fg_color="#B88B68", dropdown_fg_color="#B88B68", values=["Book Status", "Reading", "Plan to read", "Completed", "Dropped"]) 
book_status_combobox.place(x=430, y=290)

# Book title and author texts
book_title_text = customtkinter.CTkLabel(opened_book_author_title_frame, width=720, height=40, font=("Quando", 40),  text_color="white", text="Book title goes here.")
book_title_text.place(x=10, y=10)

book_author_text = customtkinter.CTkLabel(opened_book_author_title_frame, width=720, height=20, font=("Quando", 20),  text_color="white", text="Author name goes here.")
book_author_text.place(x=10, y=60)

# Other book info texts
book_genre_title = customtkinter.CTkLabel(opened_book_other_text_frame, anchor=customtkinter.W, width=150, height=30, font=("Quando", 22), text_color="white", text="GENRE: ")
book_genre_title.place(x=10, y=20)

book_genre_placeholder = customtkinter.CTkLabel(opened_book_other_text_frame, anchor=customtkinter.W,width=570, height=30, font=("Quando", 22), text_color="white",  text="Genre1, Genre2, Genre3")
book_genre_placeholder.place(x=170, y=20)#


book_theme_title = customtkinter.CTkLabel(opened_book_other_text_frame, anchor=customtkinter.W, width=150, height=30, font=("Quando", 22), text_color="white",  text="THEME: ")
book_theme_title.place(x=10, y=55)

book_theme_placeholder = customtkinter.CTkLabel(opened_book_other_text_frame,anchor=customtkinter.W, width=570, height=30, font=("Quando", 22),  text_color="white", text="Theme1, Theme2, Theme3")
book_theme_placeholder.place(x=170, y=55)#


book_keywords_title = customtkinter.CTkLabel(opened_book_other_text_frame, anchor=customtkinter.W, width=200, height=30, font=("Quando", 22), text_color="white",  text="KEYWORDS: ")
book_keywords_title.place(x=10, y=90)

book_keywords_placeholder = customtkinter.CTkLabel(opened_book_other_text_frame,anchor=customtkinter.W, width=570, height=30, font=("Quando", 22), text_color="white",  text="Keyword1, Keyword2, Keyword3")
book_keywords_placeholder.place(x=170, y=90)#


book_rating_title = customtkinter.CTkLabel(opened_book_other_text_frame, anchor=customtkinter.W, width=150,  height=30, font=("Quando", 22), text_color="white",  text="RATING: ")
book_rating_title.place(x=10, y=125)

book_rating_placeholder = customtkinter.CTkLabel(opened_book_other_text_frame,anchor=customtkinter.W, width=570, height=30, font=("Quando", 22), text_color="white",  text="5/5")
book_rating_placeholder.place(x=170, y=125)#


# Synopsis title and text body
book_synopsis_title = customtkinter.CTkLabel(opened_book_synopsis_title, anchor=customtkinter.W, width=1005, height=85, font=("Quando", 45),  text_color="white", text="SYNOPSIS")
book_synopsis_title.place(x=15, y=-10)#

book_synopsis_body = customtkinter.CTkLabel(opened_book_synopsis_textbody, width=1005, height=800, font=("Quando", 25), wraplength=980, justify="center", text_color="white", text="My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone.")
book_synopsis_body.place(x=0, y=-160)#

###############################################################################################################################################################################
