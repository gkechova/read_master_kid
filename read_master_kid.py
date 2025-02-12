from os import sep
import random
import tkinter as tk

from words.words_dictionary import words


def get_image_name(word):
    image_name = "images" + sep + word + ".png"
    return image_name


def get_word_text_split_by_syllables(syllables_lst) -> str:
    word_text_str_parted = ""
    for i in range(len(syllables_lst)):
        word_text_str_parted += syllables_lst[i][1].upper()
        try:
            if syllables_lst[i + 1][1] == " " or syllables_lst[i][1] == " ":
                word_text_str_parted += "   "
            else:
                word_text_str_parted += " - "
        except IndexError:
            pass

    return word_text_str_parted


class ReadMasterKid(tk.Frame):

    def __init__(self, master):
        master.configure(bg="white")
        self.syllables_buttons = dict()
        super().__init__(master)
        self.pack()

        # Create text entry for solved syllables
        self.word_text = tk.Label(bg='White', fg='#23331D', font=("arial", 24, 'italic'))
        self.word_text.place(x=140, y=390)
        # Create text entry for solved syllables which displays the syllables separated by dash
        self.word_text_parted = tk.Label(bg='White', fg='#23331D', font=("arial", 24, 'underline'))
        self.word_text_parted.place(x=140, y=460)

        # Create list to store word syllables
        solved_syllables = list()

        # Get next word from dictionary randomly
        next_word = random.choice(tuple(words.keys()))
        # Get word syllables
        word_syllables = words.get(next_word).copy()
        # Create temp dictionary copy for the next_word only from where to pop the solved syllables
        next_word_dict = {next_word: word_syllables.copy()}
        # Shuffle the word syllables
        random.shuffle(word_syllables)

        # Construct image file name and create image
        word_image = get_image_name(next_word)
        self.display_image = tk.PhotoImage(file=word_image)
        # Display word image
        self.image_label = tk.Label(self.master, image=self.display_image, relief="flat")
        self.image_label.place(x=90, y=40)

        # Create buttons for shuffled syllables
        button_y_position = 40
        button_font_size = 20
        for syl in word_syllables:
            def end_game():
                self.new_game_button = tk.Button(
                    window,
                    font=("arial", button_font_size),
                    bg="#88C96E",
                    fg="#23331D",
                    text="ДРУГА ДУМА",
                    command=restart_game
                )
                self.new_game_button.place(x=600, y=530)

            def restart_game():
                for button in self.syllables_buttons.values():
                    button.destroy()
                self.new_game_button.destroy()
                self.word_text.config(text="")
                self.word_text_parted.config(text="")
                myapp.__init__(window)

            def action(current_syllable=syl):
                # called by each syllable button
                if current_syllable[1] == next_word_dict[next_word][0][1]:
                    # Pop the solved syllable and append it ot the solved
                    solved_syllables.append(next_word_dict[next_word].pop(0))
                    # Display the word progress
                    word_text_str = ''.join((s[1] for s in solved_syllables))
                    word_text_str_parted = get_word_text_split_by_syllables(solved_syllables)
                    self.word_text.config(text=word_text_str)
                    self.word_text_parted.config(text=word_text_str_parted)
                    # Disable button for solved syllable
                    self.syllables_buttons[current_syllable[0]].config(state="disabled")

                    if len(next_word_dict[next_word]) == 0:
                        end_game()

            self.syllables_buttons[syl[0]] = tk.Button(
                window,
                font=("arial", button_font_size),
                bg="white",
                height=1,
                text=syl[1],
                relief="ridge",
                command=action
            )
            self.syllables_buttons[syl[0]].place(x=600 - len(syl[1]) * button_font_size // 2, y=button_y_position)
            button_y_position += 60


window = tk.Tk()
window.title = "Read Master Kid"
window.geometry("800x600")
myapp = ReadMasterKid(window)
myapp.mainloop()
