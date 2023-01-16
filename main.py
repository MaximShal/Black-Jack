from tkinter import *
from PIL import ImageTk
from Game import Game


def ask_quit():
    quit1 = Toplevel(main)
    quit1.geometry('500x300')
    quit1['bg'] = 'black'
    Label(quit1, text='Ви дійсно бажаєте вийти?', bg='black', fg='white', font=40).place(x=20, y=20)
    Button(quit1, text='Так', command=main.quit,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=50)
    Button(quit1, text='Ні', command=quit1.destroy,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=100, y=50)


def clear_main():
    for widget in main.winfo_children():
        widget.destroy()


def load_bg_picture(path_picture):
    main.image = ImageTk.PhotoImage(file=path_picture)
    bg_logo = Label(main, image=main.image)
    bg_logo.pack(side="top", fill="both")


def back_main():
    clear_main()
    main_menu()


def settings():
    clear_main()
    load_bg_picture('Images/main.png')
    Label(main, text='Налаштування знаходяться у стадії розробки',
          bg='black', fg='red', font=60).place(x=600, y=50)
    Button(main, width=40, height=3,
           text='Назад', command=back_main,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=50)


def pre_game():
    clear_main()
    load_bg_picture('Images/main.png')
    Label(main, text='Обери кількість гравців', bg='black', fg='white', font=40).place(x=150, y=20)
    Button(main, width=40, height=3, text='1', command=lambda x=1: load_game(x),
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=50)
    Button(main, width=40, height=3, text='2', command=lambda x=2: load_game(x),
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=140)
    Button(main, width=40, height=3, text='3', command=lambda x=3: load_game(x),
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=230)
    Button(main, width=40, height=3, text='Назад', command=back_main,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=320)


def load_game(bots_count):
    clear_main()
    load_bg_picture('Images/game_background.png')

    g = Game()
    g.start_game(bots_count)



def main_menu():
    try1 = ImageTk.PhotoImage(file='Images/game_background.png')
    load_bg_picture('Images/main.png')
    Button(main, width=40, height=3,
           text='Нова гра', command=pre_game,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=50)
    Button(main, width=40, height=3,
           text='Налаштування', command=settings,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=140)
    Button(main, width=40, height=3,
           text='Вихід', command=ask_quit,
           activebackground='grey', bg='black', fg='white', font=40, overrelief=FLAT).place(x=50, y=230)

    main.mainloop()


if __name__ == '__main__':
    main = Tk()
    main.title('Black Jack')
    main.geometry('1920x1080')
    main_menu()
