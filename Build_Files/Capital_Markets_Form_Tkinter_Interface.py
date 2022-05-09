import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import END
import math


root = tk.Tk()


class Aplication:

    def __init__(self):
        self.text_resultado = None
        self.frame_11 = None
        self.entry3_contas = None
        self.entry2_contas = None
        self.entry1_contas = None
        self.listbox_1 = None
        self.button_options = None
        self.frame_10 = None
        self.frame_8_9 = None
        self.frame_9 = None
        self.frame_8_8 = None
        self.label6_contas = None
        self.frame_8_6 = None
        self.frame_8_7 = None
        self.frame_8_5 = None
        self.label4_contas = None
        self.label2_contas = None
        self.frame_8_4 = None
        self.frame_8_3 = None
        self.frame_8_2 = None
        self.label1_contas = None
        self.frame_8_1 = None
        self.frame_7 = None
        self.combobox_formulas = None
        self.frame_8 = None
        self.combobox_formulas2 = None
        self.label3_contas = None
        self.label2 = None
        self.frame_6 = None
        self.frame_5 = None
        self.frame_4 = None
        self.frame_3 = None
        self.frame_2 = None
        self.label1 = None
        self.frame_1 = None
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.comboboxs_da_tela()
        self.labels_da_tela()
        self.buttons_da_tela()
        self.listboxs_da_tela()
        self.funcoes_inputs()
        root.mainloop()

    def tela(self):
        self.root.title("Formulário do Mercado Financeiro")
        self.root.configure(background='light blue')
        self.root.geometry("788x988")
        self.root.resizable(True, True)

    def frames_da_tela(self):

        self.frame_1 = tk.Frame(self.root, bd=2, bg='#CDC1C5', highlightbackground='red', highlightthickness=6)
        self.frame_1.place(relx=0.4, rely=0.086, relwidth=0.20, relheight=0.03)

        self.frame_2 = tk.Frame(self.root, bd=2, bg='#96CDCD', highlightbackground='green', highlightthickness=6)
        self.frame_2.place(relx=0.20, rely=0.126, relwidth=0.60, relheight=0.15)

        self.frame_3 = tk.Frame(self.root, bd=2, bg='#33A1C9', highlightbackground='blue', highlightthickness=6)
        self.frame_3.place(relx=0.24, rely=0.2816, relwidth=0.40, relheight=0.036)

        self.frame_4 = tk.Frame(self.root, bd=2, bg='#E9967A', highlightbackground='orange', highlightthickness=6)
        self.frame_4.place(relx=0.66, rely=0.2816, relwidth=0.1, relheight=0.036)

        self.frame_5 = tk.Frame(self.root, bd=2, bg='light yellow', highlightbackground='yellow', highlightthickness=6)
        self.frame_5.place(relx=0.24, rely=0.326, relwidth=0.52, relheight=0.1)

        self.frame_6 = tk.Frame(self.root, bd=2, bg='#8A2BE2', highlightbackground='purple', highlightthickness=6)
        self.frame_6.place(relx=0.24, rely=0.436, relwidth=0.40, relheight=0.036)

        self.frame_7 = tk.Frame(self.root, bd=2, bg='#EE1289', highlightbackground='#FF69B4', highlightthickness=6)
        self.frame_7.place(relx=0.66, rely=0.436, relwidth=0.1, relheight=0.036)

    def labels_da_tela(self):
        self.label1 = tk.Label(self.frame_1, background="#CDC1C5", text="Relações")
        self.label1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.label2 = tk.Label(self.frame_2, background='#96CDCD',
                               text="vp: Valor Presente ------------- TJ: Taxa de Juros\n VF: Valor Futuro ----- TI: Tempo de Investimento")
        self.label2.place(relx=0, rely=0, relwidth=1, relheight=1)

    def comboboxs_da_tela(self):

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="#7EC0EE", background="#7EC0EE", Listbox='#7EC0EE')

        self.combobox_formulas = ttk.Combobox(self.frame_3, justify="center", state="readonly",
                                              values=["Valor Presente", "Valor Futuro", "Taxa de Juros",
                                                      "Tempo de Investimento"])
        self.combobox_formulas.set("Selecione a Fórmula Desejada")
        self.combobox_formulas.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.combobox_formulas.option_add('*TCombobox*Listbox.Justify', 'center')
        self.combobox_formulas.option_add("*TCombobox*Listbox*Background", '#7EC0EE')

        self.combobox_formulas2 = ttk.Combobox(self.frame_6, justify="center", state="disable")
        self.combobox_formulas2.set("Selecione a Fórmula Desejada")
        self.combobox_formulas2.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.combobox_formulas2.option_add('*TCombobox*Listbox.Justify', 'center')
        self.combobox_formulas2.option_add("*TCombobox*Listbox*Background", '#7EC0EE')
        self.combobox_formulas2.option_add("*TCombobox*Listbox*value", 'A')

    def funcoes_inputs(self):
        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Valor Presente":
            self.frame_8 = tk.Frame(self.root, bd=2, bg='light gray', highlightbackground='gray', highlightthickness=6)
            self.frame_8.place(relx=0.374, rely=0.482, relwidth=0.252, relheight=0.13)

            self.frame_8_1 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_1.place(relx=0.03, rely=0.02, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_1, background='#EEC900', text="VF",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_2 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_2.place(relx=0.435, rely=0.02, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_2, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_3 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_3.place(relx=0.585, rely=0.02, relwidth=0.385, relheight=0.30)

            self.entry1_contas = tk.Entry(self.frame_8_3, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_4 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_4.place(relx=0.03, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_4, background='#EEC900', text="TJ",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_5 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_5.place(relx=0.435, rely=0.3440, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_5, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_6 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_6.place(relx=0.585, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.entry2_contas = tk.Entry(self.frame_8_6, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_7 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_7.place(relx=0.03, rely=0.67, relwidth=0.385, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_7, background='#EEC900', text="TI",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_8 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_8.place(relx=0.435, rely=0.67, relwidth=0.13, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_8, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_9 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_9.place(relx=0.585, rely=0.67, relwidth=0.385, relheight=0.30)

            self.entry3_contas = tk.Entry(self.frame_8_9, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_9 = tk.Frame(self.root, bd=2, bg='#FF4040', highlightbackground='#FF4040',
                                    highlightthickness=6)
            self.frame_9.place(relx=0.374, rely=0.622, relwidth=0.252, relheight=0.036)

            style = ttk.Style()
            style.theme_use('clam')
            style.configure("TButton", fieldbackground="#E3CF57", background="#E3CF57", justify="center")

            myFont = font.Font(family='Helvetica', size=8)

            self.button_options = tk.Button(self.frame_9, text='Realizar o Cálculo', command=self.calculos)
            self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.button_options['font'] = myFont

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Valor Futuro":
            self.frame_8 = tk.Frame(self.root, bd=2, bg='light gray', highlightbackground='gray', highlightthickness=6)
            self.frame_8.place(relx=0.374, rely=0.482, relwidth=0.252, relheight=0.13)

            self.frame_8_1 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_1.place(relx=0.03, rely=0.02, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_1, background='#EEC900', text="vp",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_2 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_2.place(relx=0.435, rely=0.02, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_2, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_3 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_3.place(relx=0.585, rely=0.02, relwidth=0.385, relheight=0.30)

            self.entry1_contas = tk.Entry(self.frame_8_3, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_4 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_4.place(relx=0.03, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_4, background='#EEC900', text="TJ",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_5 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_5.place(relx=0.435, rely=0.3440, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_5, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_6 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_6.place(relx=0.585, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.entry2_contas = tk.Entry(self.frame_8_6, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_7 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_7.place(relx=0.03, rely=0.67, relwidth=0.385, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_7, background='#EEC900', text="TI",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_8 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_8.place(relx=0.435, rely=0.67, relwidth=0.13, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_8, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_9 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_9.place(relx=0.585, rely=0.67, relwidth=0.385, relheight=0.30)

            self.entry3_contas = tk.Entry(self.frame_8_9, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_9 = tk.Frame(self.root, bd=2, bg='#FF4040', highlightbackground='#FF4040',
                                    highlightthickness=6)
            self.frame_9.place(relx=0.374, rely=0.622, relwidth=0.252, relheight=0.036)

            style = ttk.Style()
            style.theme_use('clam')
            style.configure("TButton", fieldbackground="#E3CF57", background="#E3CF57", justify="center")

            myFont = font.Font(family='Helvetica', size=8)

            self.button_options = tk.Button(self.frame_9, text='Realizar o Cálculo', command=self.calculos)
            self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.button_options['font'] = myFont

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Taxa de Juros":
            self.frame_8 = tk.Frame(self.root, bd=2, bg='light gray', highlightbackground='gray', highlightthickness=6)
            self.frame_8.place(relx=0.374, rely=0.482, relwidth=0.252, relheight=0.13)

            self.frame_8_1 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_1.place(relx=0.03, rely=0.02, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_1, background='#EEC900', text="VF",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_2 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_2.place(relx=0.435, rely=0.02, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_2, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_3 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_3.place(relx=0.585, rely=0.02, relwidth=0.385, relheight=0.30)

            self.entry1_contas = tk.Entry(self.frame_8_3, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_4 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_4.place(relx=0.03, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_4, background='#EEC900', text="vp",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_5 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_5.place(relx=0.435, rely=0.3440, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_5, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_6 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_6.place(relx=0.585, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.entry2_contas = tk.Entry(self.frame_8_6, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_7 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_7.place(relx=0.03, rely=0.67, relwidth=0.385, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_7, background='#EEC900', text="TI",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_8 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_8.place(relx=0.435, rely=0.67, relwidth=0.13, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_8, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_9 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_9.place(relx=0.585, rely=0.67, relwidth=0.385, relheight=0.30)

            self.entry3_contas = tk.Entry(self.frame_8_9, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_9 = tk.Frame(self.root, bd=2, bg='#FF4040', highlightbackground='#FF4040',
                                    highlightthickness=6)
            self.frame_9.place(relx=0.374, rely=0.622, relwidth=0.252, relheight=0.036)

            style = ttk.Style()
            style.theme_use('clam')
            style.configure("TButton", fieldbackground="#E3CF57", background="#E3CF57", justify="center")

            myFont = font.Font(family='Helvetica', size=8)

            self.button_options = tk.Button(self.frame_9, text='Realizar o Cálculo', command=self.calculos)
            self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.button_options['font'] = myFont

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Tempo de Investimento":
            self.frame_8 = tk.Frame(self.root, bd=2, bg='light gray', highlightbackground='gray', highlightthickness=6)
            self.frame_8.place(relx=0.374, rely=0.482, relwidth=0.252, relheight=0.13)

            self.frame_8_1 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_1.place(relx=0.03, rely=0.02, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_1, background='#EEC900', text="VF",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_2 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_2.place(relx=0.435, rely=0.02, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_2, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_3 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_3.place(relx=0.585, rely=0.02, relwidth=0.385, relheight=0.30)

            self.entry1_contas = tk.Entry(self.frame_8_3, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_4 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_4.place(relx=0.03, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.label1_contas = tk.Label(self.frame_8_4, background='#EEC900', text="vp",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label1_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_5 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_5.place(relx=0.435, rely=0.3440, relwidth=0.13, relheight=0.30)

            self.label2_contas = tk.Label(self.frame_8_5, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_6 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_6.place(relx=0.585, rely=0.3440, relwidth=0.385, relheight=0.30)

            self.entry2_contas = tk.Entry(self.frame_8_6, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry2_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_7 = tk.Frame(self.frame_8, bd=1, bg='#EEC900', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_7.place(relx=0.03, rely=0.67, relwidth=0.385, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_7, background='#EEC900', text="TJ",
                                          font=("Copperplate Gothic Bold", 16),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_8 = tk.Frame(self.frame_8, bd=1, bg='#009ACD', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_8.place(relx=0.435, rely=0.67, relwidth=0.13, relheight=0.30)

            self.label3_contas = tk.Label(self.frame_8_8, background="#009ACD", text=":", font=("Courier", 14),
                                          justify="center")
            self.label3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_8_9 = tk.Frame(self.frame_8, bd=1, bg='#BCEE68', highlightbackground='black',
                                      highlightthickness=2)
            self.frame_8_9.place(relx=0.585, rely=0.67, relwidth=0.385, relheight=0.30)

            self.entry3_contas = tk.Entry(self.frame_8_9, background='#EEC900', font=("Arial", 9),
                                          justify="center")
            self.entry3_contas.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.frame_9 = tk.Frame(self.root, bd=2, bg='#FF4040', highlightbackground='#FF4040',
                                    highlightthickness=6)
            self.frame_9.place(relx=0.374, rely=0.622, relwidth=0.252, relheight=0.036)

            style = ttk.Style()
            style.theme_use('clam')
            style.configure("TButton", fieldbackground="#E3CF57", background="#E3CF57", justify="center")

            myFont = font.Font(family='Helvetica', size=8)

            self.button_options = tk.Button(self.frame_9, text='Realizar o Cálculo', command=self.calculos)
            self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.button_options['font'] = myFont

    def funcoes_opcoes(self):
        if self.combobox_formulas.get() == "Valor Presente":
            self.listbox_1.delete(0, END)
            self.listbox_1.insert(END, "Para calcular utilizando na fórmula (VF, TJ e TI): A")

            self.combobox_formulas2['state'] = "readonly"
            self.combobox_formulas2['values'] = ['A']
            self.combobox_formulas2.set("Selecione a Fórmula Desejada")

            self.frame_10 = tk.Frame(self.root, bg='light blue')
            self.frame_10.place(relx=0.24, rely=0.482, relwidth=0.53, relheight=0.598)

        if self.combobox_formulas.get() == "Valor Futuro":
            self.listbox_1.delete(0, END)
            self.listbox_1.insert(END, "Para calcular utilizando na fórmula (vp, TJ e TI): A")

            self.combobox_formulas2['state'] = "readonly"
            self.combobox_formulas2['values'] = ['A']
            self.combobox_formulas2.set("Selecione a Fórmula Desejada")

            self.frame_10 = tk.Frame(self.root, bg='light blue')
            self.frame_10.place(relx=0.24, rely=0.482, relwidth=0.53, relheight=0.598)

        if self.combobox_formulas.get() == "Taxa de Juros":
            self.listbox_1.delete(0, END)
            self.listbox_1.insert(END, "Para calcular utilizando na fórmula (VF, vp e TI): A")

            self.combobox_formulas2['state'] = "readonly"
            self.combobox_formulas2['values'] = ['A']
            self.combobox_formulas2.set("Selecione a Fórmula Desejada")

            self.frame_10 = tk.Frame(self.root, bg='light blue')
            self.frame_10.place(relx=0.24, rely=0.482, relwidth=0.53, relheight=0.598)

        if self.combobox_formulas.get() == "Tempo de Investimento":
            self.listbox_1.delete(0, END)
            self.listbox_1.insert(END, "Para calcular utilizando na fórmula (VF, vp e TJ): A")

            self.combobox_formulas2['state'] = "readonly"
            self.combobox_formulas2['values'] = ['A']
            self.combobox_formulas2.set("Selecione a Fórmula Desejada")

            self.frame_10 = tk.Frame(self.root, bg='light blue')
            self.frame_10.place(relx=0.24, rely=0.482, relwidth=0.53, relheight=0.598)

    # noinspection PyTypeChecker
    def calculos(self):
        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Valor Presente":
            resultados = tk.StringVar()

            VF = float(self.entry1_contas.get())
            TJ = float(self.entry2_contas.get())
            TI = float(self.entry3_contas.get())
            VP1 = (VF / ((1 + (TJ / 100)) ** TI))

            resultados.set(VP1)

            self.frame_11 = tk.Frame(self.root, bd=2, bg='#98F5FF', highlightbackground='black',
                                     highlightthickness=6)
            self.frame_11.place(relx=0.374, rely=0.67, relwidth=0.252, relheight=0.06)

            self.text_resultado = tk.Label(self.frame_11, bd=2, bg='#98F5FF', highlightbackground='black',
                                           textvariable=resultados,
                                           highlightthickness=6)
            self.text_resultado.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Valor Futuro":
            resultados = tk.StringVar()

            vp = float(self.entry1_contas.get())
            TJ = float(self.entry2_contas.get())
            TI = float(self.entry3_contas.get())
            VF1 = (vp * ((1 + (TJ / 100)) ** TI))

            resultados.set(VF1)

            self.frame_11 = tk.Frame(self.root, bd=2, bg='#98F5FF', highlightbackground='black',
                                     highlightthickness=6)
            self.frame_11.place(relx=0.374, rely=0.67, relwidth=0.252, relheight=0.06)

            self.text_resultado = tk.Label(self.frame_11, bd=2, bg='#98F5FF', highlightbackground='black',
                                           textvariable=resultados,
                                           highlightthickness=6)
            self.text_resultado.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Taxa de Juros":
            resultados = tk.StringVar()

            VF = float(self.entry1_contas.get())
            vp = float(self.entry2_contas.get())
            TI = float(self.entry3_contas.get())
            TJ1 = ((VF / vp) ** (1 / TI)) - 1

            resultados.set(TJ1)

            self.frame_11 = tk.Frame(self.root, bd=2, bg='#98F5FF', highlightbackground='black',
                                     highlightthickness=6)
            self.frame_11.place(relx=0.374, rely=0.67, relwidth=0.252, relheight=0.06)

            self.text_resultado = tk.Label(self.frame_11, bd=2, bg='#98F5FF', highlightbackground='black',
                                           textvariable=resultados,
                                           highlightthickness=6)
            self.text_resultado.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

        if self.combobox_formulas2.get() == 'A' and self.combobox_formulas.get() == "Tempo de Investimento":
            resultados = tk.StringVar()

            VF = float(self.entry1_contas.get())
            vp = float(self.entry2_contas.get())
            TJ = float(self.entry3_contas.get())
            TI1 = math.log((VF / vp), (TJ / 100) + 1)

            resultados.set(TI1)

            self.frame_11 = tk.Frame(self.root, bd=2, bg='#98F5FF', highlightbackground='black',
                                     highlightthickness=6)
            self.frame_11.place(relx=0.374, rely=0.67, relwidth=0.252, relheight=0.06)

            self.text_resultado = tk.Label(self.frame_11, bd=2, bg='#98F5FF', highlightbackground='black',
                                           textvariable=resultados,
                                           highlightthickness=6)
            self.text_resultado.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

    def buttons_da_tela(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", fieldbackground="#E3CF57", background="#E3CF57", justify="center")

        myFont = font.Font(family='Helvetica', size=8)

        self.button_options = tk.Button(self.frame_4, text='Aplicar', command=self.funcoes_opcoes)
        self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.button_options['font'] = myFont

        self.button_options = tk.Button(self.frame_7, text='Aplicar', command=self.funcoes_inputs)
        self.button_options.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.button_options['font'] = myFont

    def listboxs_da_tela(self):
        self.listbox_1 = tk.Listbox(self.frame_5, background="light yellow", justify="center")
        self.listbox_1.place(relx=0, rely=0, relwidth=1, relheight=1)


Aplication()
