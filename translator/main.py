import tkinter as tk
import googletrans
from googletrans import Translator




class Translatorr(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.geometry("500x500")
        self.src = tk.Label(self, text="From")
        self.dest = tk.Label(self, text="to")

        options = dict(googletrans.LANGUAGES)
        options = [k for k,v in options.items()]
        to = options.copy()

        self.default = tk.StringVar()
        self.default_to = tk.StringVar()
        self.default.set(options[1])
        self.default_to.set(to[3])

        self.options = tk.OptionMenu(self, self.default, *options)
        self.to_options = tk.OptionMenu(self, self.default_to, *to)
        self.options.grid(row=1, column=1)
        self.to_options.grid(row=1, column=2)

        self.src.grid(row=0, column=1)
        self.dest.grid(row=0, column=2)

        self.source_text = tk.Text(self, width=50, height=10)
        self.output_text = tk.Text(self, width=50, height=10)
        self.output_label = tk.Label(self, text="Output")
        self.output_label.grid(row=3, column=1, columnspan=2)

        self.trans_btn = tk.Button(
                self,
                text="Translate",
                command=self.translatation
                )
        self.trans_btn.grid(row=2, column=3, padx=10)

        self.source_text.grid(row=2, column=1, columnspan=2, pady=50)
        self.output_text.grid(row=4, column=1,  columnspan=2)


    def translatation(self):
        translator = Translator()
        src = self.default.get()
        dest = self.default_to.get()
        print(dest)
        text = self.source_text.get("1.0",'end')
        result = translator.translate(text, dest=dest)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result.text)


if __name__ == "__main__":
    app = Translatorr()
    app.mainloop()
