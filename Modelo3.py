from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Find_Region import *
import cv2
from time import *
import threading
from CapTime import *

root = Tk()

class GUI():

    def __init__(self):
        self.root = root
        self.tela()
        self.notebook()
        self.frame1()
        self.frames1()
        self.widgets1()
        self.frame2()
        self.frames2()
        self.widgets2()
        self.frame3()
        self.frames3()
        self.widgets3()
        self.frame4()
        self.frames4()
        self.widgets4()

        root.mainloop()

    def tela(self):
        self.root.title("Modelo Híbrido de Predição")
        self.root.configure(background='steelblue')
        self.root.geometry("800x400")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000,height=600)
        self.root.minsize(width=700,height=400)

    def notebook(self):
        self.nb = ttk.Notebook(self.root)
        self.nb.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)

    def frame1(self):
        self.f1 = Frame(self.nb, bg='white')
        self.nb.add(self.f1, text="Configuração do MHP")

    def frames1(self):
        self.f1_1 = Frame(self.f1, bg='whitesmoke')
        self.f1_1.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.98)

        self.f1_2 = Frame(self.f1, bg='light gray')
        self.f1_2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.98)

    def widgets1(self):

        self.lb_Horizonte = Label(self.f1_1, text="Horizonte de predição", bg='whitesmoke', anchor=W)
        self.lb_Horizonte.place(relx=0.05, rely=0.02, relwidth=0.4, relheight=0.1)

        self.var = DoubleVar()
        self.scale = Scale(self.f1_1,orient='horizontal', from_=1, to=60, variable = self.var, bg='whitesmoke')
        self.scale.place(relx=0.6,rely=0.02, relwidth=0.3,relheight=0.15, anchor=N)

        self.HP_label = Label(self.f1_2,bg='light gray')
        self.HP_label.place(relx=0.05, rely=0.02, relheight=0.1)

        self.btHP = Button(self.f1_1, text="Estabelecer", command=self.selHP)
        self.btHP.place(relx=0.8, rely=0.02,relheight=0.1,relwidth=0.18)

        self.lb_Localização = Label(self.f1_1, text="Localização", bg='whitesmoke', anchor=W)
        self.lb_Localização.place(relx=0.05, rely=0.14, relwidth=0.4, relheight=0.1)

        self.lb_Latitude = Label(self.f1_1, text="Latitude", bg='whitesmoke', anchor=W)
        self.lb_Latitude.place(relx=0.15, rely=0.26, relwidth=0.4, relheight=0.05)

        self.entry_Latitude = Entry(self.f1_1)
        self.entry_Latitude.place(relx=0.45, rely=0.26, relwidth=0.3, relheight=0.05)

        self.lb_Longitude = Label(self.f1_1, text="Longitude", bg='whitesmoke', anchor=W)
        self.lb_Longitude.place(relx=0.15, rely=0.38, relwidth=0.4, relheight=0.05)

        self.entry_Longitude = Entry(self.f1_1)
        self.entry_Longitude.place(relx=0.45, rely=0.38, relwidth=0.3, relheight=0.05)

        self.btLC = Button(self.f1_1, text="Estabelecer", command=self.selLC)
        self.btLC.place(relx=0.8, rely=0.24, relheight=0.2, relwidth=0.18)

        self.Localização_label = Label(self.f1_2, bg='light gray', anchor=W)
        self.Localização_label.place(relx=0.05, rely=0.14, relwidth=0.4, relheight=0.05)

        self.Longitude_label = Label(self.f1_2,bg='light gray', anchor=W)
        self.Longitude_label.place(relx=0.05, rely=0.38, relwidth=0.4, relheight=0.05)

        self.Latitude_label = Label(self.f1_2,bg='light gray',anchor=W)
        self.Latitude_label.place(relx=0.05, rely=0.26, relwidth=0.4, relheight=0.05)

        self.Local_label = Label(self.f1_2, bg='light gray', anchor=W)
        self.Local_label.place(relx=0.05, rely=0.50, relwidth=0.4, relheight=0.05)

        self.Dados_text = Text(self.f1_2, bg='light gray')
        self.Dados_text.place(relx=0.05, rely=0.62, relwidth=0.9, relheight=0.35)

        self.btLimpar = Button(self.f1_1, text="Limpar", fg='Red', command=self.Limpar)
        self.btLimpar.place(relx=0.8, rely=0.46, relheight=0.2, relwidth=0.18)

    def selHP(self):
        selec = "Horizonte de predição  = " + str(self.var.get()) + " minuto(s)"
        self.HP_label.config(text=selec)

    def selLC(self):
        if str(self.entry_Longitude.get()) == '' or str(self.entry_Latitude.get())== '':
            messagebox.showwarning(title="Erro", message="Longitude e Latitude necessarios")
        else:
            self.Localização_label.config(text="Localização")
            self.Longitude_label.config(text="Longitude = " + str(self.entry_Longitude.get()))
            self.Latitude_label.config(text="Latitude = " + str(self.entry_Latitude.get()))
            self.Local_label.config(text="Cidade = " + Find_Region(str(self.entry_Latitude.get()),str(self.entry_Longitude.get())))
            self.Dados_text.insert(INSERT, "Dados técnicos do sistema solar:\n")
            self.Dados_text.insert(INSERT, "- Capacidade nominal:\n")
            self.Dados_text.insert(INSERT, "- Número de módulos:\n")
            self.Dados_text.insert(INSERT, "- Modelos:\n")
            self.Dados_text.insert(INSERT, "- Paneles:\n")

    def Limpar(self):
        self.entry_Latitude.delete(0, END)
        self.entry_Longitude.delete(0, END)
        self.HP_label.config(text="")
        self.Localização_label.config(text="")
        self.Longitude_label.config(text="")
        self.Latitude_label.config(text="")
        self.Local_label.config(text="")
        self.Dados_text.delete('1.0',END)

    def frame2(self):
        self.f2 = Frame(self.nb, bg='white')
        self.nb.add(self.f2, text="Câmera MCD" )

    def frames2(self):
        self.f2_1 = Frame(self.f2, bg='whitesmoke')
        self.f2_1.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.98)

        self.f2_2 = Frame(self.f2, bg='light gray')
        self.f2_2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.98)

    def widgets2(self):

        self.lb_TipoCamera = Label(self.f2_1, text="Tipo de câmera", bg='whitesmoke', anchor=W)
        self.lb_TipoCamera.place(relx=0.05, rely=0.02, relwidth=0.4, relheight=0.1)

        self.combo_TipoCamera = ttk.Combobox(self.f2_1, values=[" --- ","USB genérica", "Wifi"])
        self.combo_TipoCamera.place(relx=0.08, rely=0.1, relwidth=0.25)

        self.btCamera = Button(self.f2_1, text="Estabelecer", command=self.checkcmbo)
        self.btCamera.place(relx=0.8, rely=0.08, relheight=0.1, relwidth=0.18)

        self.lb_HorizonteCap = Label(self.f2_1, text="Horizonte de captura", bg='whitesmoke', anchor=W)
        self.lb_HorizonteCap.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)

        self.var2 = DoubleVar()
        self.scale = Scale(self.f2_1, orient='horizontal', from_=1, to=60, variable=self.var2, bg='whitesmoke')
        self.scale.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.15, anchor=N)

        self.btEstabelecerHC = Button(self.f2_1, text="Estabelecer", command=self.selHC)
        self.btEstabelecerHC.place(relx=0.8, rely=0.3, relheight=0.1, relwidth=0.18)

        self.btTestCam = Button(self.f2_1, text="Testar Camera", command=self.testCamera)
        self.btTestCam.place(relx=0.08, rely=0.5, relheight=0.1)

        self.btIniciarCap = Button(self.f2_1, text="Iniciar", command=threading.Thread(target=play).start)
        self.btIniciarCap.place(relx=0.38, rely=0.5, relheight=0.1, relwidth=0.18)

        self.btFimCap = Button(self.f2_1, text="Finalizar", command=stop)
        self.btFimCap.place(relx=0.58, rely=0.5, relheight=0.1, relwidth=0.18)

        self.Camara_label = Label(self.f2_2, bg='light gray')
        self.Camara_label.place(relx=0.05, rely=0.2, relheight=0.1)

        self.HC_label = Label(self.f2_2, bg='light gray')
        self.HC_label.place(relx=0.05, rely=0.3, relheight=0.1)

    def checkcmbo(self):
        if self.combo_TipoCamera.get() == "USB genérica":
            self.btLimpar2 = Button(self.f2_1, text="Limpar", fg='Red', command=self.LimparUSB2)
            self.btLimpar2.place(relx=0.8, rely=0.46, relheight=0.2, relwidth=0.18)
            self.lb_USBsele = Label(self.f2_2, text="", bg='whitesmoke', anchor=W)
            self.lb_USBsele.place(relx=0.45, rely=0.02, relheight=0.1)
            messagebox.showinfo("Aviso", "Seleccionar input")
            self.inputUSB = Scrollbar(self.f2_1)
            self.inputUSB.place(relx=0.45, rely=0.1, relwidth=0.3, relheight=0.05)
            self.lb_USB = Label(self.f2_1, text="Seleccionar", bg='whitesmoke', anchor=W)
            self.lb_USB.place(relx=0.45, rely=0.02, relheight=0.1)

            self.mylist = Listbox(self.f2_1, yscrollcommand=self.inputUSB.set)
            for line in range(0, 10):
                self.mylist.insert(END, "input " + str(line))
                #   self.mylist.blind("<Double-1>", lambda e: self.lb_USBsele.configure(text="input " +str(line)))
            self.mylist.place(relx=0.4, rely=0.1, relwidth=0.3, relheight=0.2)

            self.inputUSB.config(command=self.mylist.yview)
            self.btLimpar2 = Button(self.f2_1, text="Limpar", fg='Red', command=self.LimparUSB2)
            self.btLimpar2.place(relx=0.8, rely=0.46, relheight=0.2, relwidth=0.18)
            self.lb_USBsele = Label(self.f2_2, text="", bg='whitesmoke', anchor=W)
            self.lb_USBsele.place(relx=0.45, rely=0.02, relheight=0.1)



        elif self.combo_TipoCamera.get() == "Wifi":
            self.btLimpar2 = Button(self.f2_1, text="Limpar", fg='Red', command=self.LimparWifi2)
            self.btLimpar2.place(relx=0.8, rely=0.46, relheight=0.2, relwidth=0.18)
            messagebox.showinfo("Aviso", "Definir endereço")
            self.lb_Wifi = Label(self.f2_1, text="Endereço", bg='whitesmoke', anchor=W)
            self.lb_Wifi.place(relx=0.45, rely=0.02, relheight=0.1)
            self.entry_Wifi = Entry(self.f2_1)
            self.entry_Wifi.place(relx=0.45, rely=0.1, relwidth=0.3, relheight=0.05)

            #self.btEstabelecerHC.bind("<Button>", btEstabelecerHC.config(commadn=self.btEstabelecerHC))

        else:
            messagebox.showinfo("Aviso", "Seccione o tipo de camera")

        self.btLimpar2 = Button(self.f2_1, text="Limpar", fg='Red', command=self.LimparUSB2)
        self.btLimpar2.place(relx=0.8, rely=0.46, relheight=0.2, relwidth=0.18)

    def LimparUSB2(self):
        self.lb_USB.destroy()
        self.inputUSB.destroy()
        self.mylist.destroy()
        self.mylist.destroy()
        self.btLimpar2.destroy()

    def LimparWifi2(self):
        self.lb_Wifi.destroy()
        self.entry_Wifi.destroy()
        self.btLimpar2.destroy()

    def selHC(self):
        selec = "Horizonte de Captura  = " + str(self.var2.get()) + " minuto(s)"
        self.HC_label.config(text=selec)
        CamaraSelec = str(self.combo_TipoCamera.get())
        self.Camara_label.config(text= CamaraSelec)

    def EnderecoWIFI(self):
        self.lb_EnderecoWifi = Label(self.f2_2, text="Endereço", bg='whitesmoke', anchor=W)
        self.lb_EnderecoWifi.place(relx=0.45, rely=0.02, relheight=0.1)

    def testCamera(self):
        test = cv2.VideoCapture(0)
        i=0
        while True:
            ret, frame = test.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)
            cv2.waitKey(1)
            if i>100:
                break
            else:
                i=i+1

        test.release()
        cv2.destroyAllWindows()

    def frame3(self):
        self.f3 = Frame(self.nb, bg='white')
        self.nb.add(self.f3, text="Dados Meteorológicos MCD")

    def frames3(self):
        self.f3_1 = Frame(self.f3, bg='whitesmoke')
        self.f3_1.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.98)

        self.f3_2 = Frame(self.f3, bg='light gray')
        self.f3_2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.98)

    def widgets3(self):

        self.lb_ServicoDeCaptura = Label(self.f3_1, text="Serviço de captura", bg='whitesmoke', anchor=W)
        self.lb_ServicoDeCaptura.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.1)

        self.lb_HorizonteCap = Label(self.f3_1, text="Horizonte de captura", bg='whitesmoke', anchor=W)
        self.lb_HorizonteCap.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

        self.var2 = DoubleVar()
        self.scale = Scale(self.f3_1, orient='horizontal', from_=1, to=60, variable=self.var2, bg='whitesmoke')
        self.scale.place(relx=0.25, rely=0.3, relwidth=0.3, relheight=0.15, anchor=N)

        self.btTestCam = Button(self.f3_1, text="Testar Camera", command=self.testCamera)
        self.btTestCam.place(relx=0.08, rely=0.5, relheight=0.2)

        self.btInCap = Button(self.f3_1, text="Iniciar \ncaptura", fg='black', command=self.Limpar)
        self.btInCap.place(relx=0.4, rely=0.5, relheight=0.2, relwidth=0.2)

        self.btFinCap = Button(self.f3_1, text="Finalizar \ncaptura", fg='black', command=self.Limpar)
        self.btFinCap.place(relx=0.7, rely=0.5, relheight=0.2,relwidth=0.2)


    def frame4(self):
        self.f4 = Frame(self.nb, bg='white')

        self.nb.add(self.f4, text="Sistema Híbrido de Predição SHP")

        #self.btIniciarCap = Button(self.f4_1, text="Iniciar")
        #self.btIniciarCap.place(relx=0.38, rely=0.5, relheight=0.1, relwidth=0.18)

        #self.btFimCap = Button(self.f4_1, text="Finalizar")
        #self.btFimCap.place(relx=0.58, rely=0.5, relheight=0.1, relwidth=0.18)


    def frames4(self):
        self.f4_1 = Frame(self.f4, bg='whitesmoke')
        self.f4_1.place(relx=0.01, rely=0.01, relwidth=0.48, relheight=0.98)

        self.f4_2 = Frame(self.f4, bg='light gray')
        self.f4_2.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.98)

    def widgets4(self):

        self.lb_HorizontePredicao = Label(self.f4_1, text="Horizonte de Prediçao", bg='whitesmoke', anchor=W)
        self.lb_HorizontePredicao.place(relx=0.07, rely=0.02, relheight=0.1)

        self.combo_HorizontePredicao = ttk.Combobox(self.f4_1, values=[" --- ", "1", "5", "15", "30", "60"])
        self.combo_HorizontePredicao.place(relx=0.08, rely=0.12, relwidth=0.25)

        self.btHP4 = Button(self.f4_1, text="Estabelecer", command=self.checkcmbo4)
        self.btHP4.place(relx=0.7, rely=0.08, relheight=0.1, relwidth=0.18)

        self.btCarregar = Button(self.f4_1, text="Carregar \nML", fg='black', command=self.CarregaModelo)
        self.btCarregar.place(relx=0.08, rely=0.25, relheight=0.2, relwidth=0.18)

        self.btInPred = Button(self.f4_1, text="Iniciar \npredição", fg='black', command=self.IniciarPredicao)
        self.btInPred.place(relx=0.5, rely=0.25, relheight=0.2, relwidth=0.18)

        self.btInPred = Button(self.f4_1, text="Finalizar \npredição", fg='black', command=self.FinalizarPredicao)
        self.btInPred.place(relx=0.7, rely=0.25, relheight=0.2, relwidth=0.18)

    def checkcmbo4(self):
        if self.combo_HorizontePredicao.get() == "":
            messagebox.showinfo("Aviso", "Definir horizonte")
        else:
            self.lb_HP4 = Label(self.f4_2, text=f"Horizonte de Prediçao: {self.combo_HorizontePredicao.get()}", bg='light gray', anchor=W)
            self.lb_HP4.place(relx=0.07, rely=0.09, relheight=0.1)

    def CarregaModelo(self):
        self.lb_CM = Label(self.f4_2, text="Modelo carregado", bg='light gray', anchor=W)
        self.lb_CM.place(relx=0.07, rely=0.19)

    def IniciarPredicao(self):
        self.lb_IP = Label(self.f4_2, text=f"Iniciando prediçao...{asctime(localtime())}"
                                           "\n testar camera "
                                           , bg='light gray', anchor=W)

        self.lb_IP.place(relx=0.07, rely=0.39)
        #sleep(5)

        #self.testCamera()
        self.lb_TC = Label(self.f4_2, text="\n Testar dados meteorológicos"
                                           "\n Carregar modelos de ML", bg='light gray', anchor=W )
        self.lb_TC.place(relx=0.07, rely=0.49)

    def FinalizarPredicao(self):
        self.lb_FP = Label(self.f4_2, text=f"Prediçao finalizada {asctime(localtime())} ", bg='light gray', anchor=W)
        self.lb_FP.place(relx=0.07, rely=0.69)

GUI()