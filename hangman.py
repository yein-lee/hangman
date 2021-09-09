from tkinter import *
import tkinter as tk
import random

right = 0
wrong = 0


def hangman_game():
    window = tk.Tk()
    window.title("HANGMAN")
    window.configure(width=670, height=650, bg="white")
    canvas = tk.Canvas(window, width=670, height=650, bg="white")

    # 단어 리스트
    words_list = ["import", "export", "sun", "number", "note", "late", "lean",
                  "move", "active", "crazy", "hard", "slam", "crush", "beach",
                  "ice", "cream", "train", "wonder", "nice", "love",
                  "freind", "city"]

    # 게임할 단어를 결정하고 글자수만큼 밑줄을 그어준다.
    word = random.choice(words_list)
    n = len(word)
    for i in range(n):
        label = Label(window, text="_", font=("궁서체", 80), bg="white")
        label.place(x=335 - (n / 2) * 100 - (n / 2 - 1 / 2) * 10 + i * 110, y=300)

    # Life
    life = Label(window, text="Life", font=("궁서체", 25), bg="white")
    life.place(x=0, y=0)

    # ♥
    heart_row = 80
    heart_col = 0
    for j in range(8):
        heart = Label(window, text="♥", font=("궁서체", 30), bg="white", fg="red")
        heart.place(x=heart_row, y=heart_col)
        heart_row += 55

    # 알파벳 버튼
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                     "y", "z"]

    alp_row = 10
    alp_col = 500
    for alp_button in alphabet_list:
        def process(t=alp_button):
            click(t)

        Button(window, text=alp_button, font=("궁서체", 30), command=process).place(x=alp_row,
                                                                                 y=alp_col)
        alp_row += 50
        if alp_row > 650:
            alp_col += 70
            alp_row = 10

    # 알파벳을 클릭하였을 때
    def click(key):
        global right, wrong
        digit = word.find(key)

        # 맞았을 때
        if digit >= 0:
            alp_label = Label(window, font=("궁서체", 80), bg="white", text=key)
            alp_label.place(x=335 - (n / 2) * 100 - (n / 2 - 1 / 2) * 10 + digit * 110, y=300)
            right += 1

            if right == n:
                right = 0
                wrong = 0
                window.destroy()
                # 게임에서 이겼다는 것을 알리는 창을 생성한다.
                window2 = Tk()
                l1 = Label(window2, text="you win!", font=("궁서체", 60),
                           fg="red")
                l2 = Label(window2, text="Do you want to play",
                           font=("궁서체", 60))
                l3 = Label(window2, text="once more?",
                           font=("궁서체", 60))
                b = Button(window2, text=h, font=("궁서체", 40), command=process_replay)

                l1.pack()
                l2.pack()
                l3.pack()
                b.pack()


        # 틀렸을 때
        else:
            # life가 틀릴 때 마다 하나씩 없어진다.
            delete_heart = Label(window, text=" ", font=("궁서체", 60), bg="white")
            delete_heart.place(x=465 - 55 * wrong, y=0)
            wrong += 1

            # 게임에서 졌다는 것을 알리는 창을 생성한다.
            if wrong > 7:
                right = 0
                wrong = 0
                window.destroy()
                window3 = Tk()
                l1 = Label(window3, text="you lose!", font=("궁서체", 60),
                           fg="red")
                l2 = Label(window3, text="The answer is", font=("궁서체", 60))
                l3 = Label(window3, text=word, font=("궁서체", 60),
                           fg="green")
                l4 = Label(window3, text="Do you want to play",
                           font=("궁서체", 60))
                l5 = Label(window3, text="once more?",
                           font=("궁서체", 60))
                b = Button(window3, text=h, font=("궁서체", 40), command=process_replay)
                l1.pack()
                l2.pack()
                l3.pack()
                l4.pack()
                l5.pack()
                b.pack()


h = "replay"

def process_replay(t=h):
    click_replay(t)


def click_replay(key):
    hangman_game()

if __name__ == '__main__':
    hangman_game()