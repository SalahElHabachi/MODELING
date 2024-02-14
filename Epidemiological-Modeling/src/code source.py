from tkinter import *
import numpy as np
from tkinter import messagebox
from PIL import Image, ImageTk
from math import sin
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.integrate import odeint
from tkinter import filedialog
import datetime
import scipy.spatial.transform._rotation_groups


# =======================       variables   Globales    =============================
t = np.linspace(0, 30, 100000)
# ===========================================================================

# ======================          La méthode main() : lancement de l'app   ===========
def main():
    root = Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None
# =========================================================================

class Window:
    def __init__(self, root):
        self.status=''
        self.root = root
        self.root.title("  HBSIM : Modélisation épidémiologique ... Modèles : SIR , SIRS et SIRI ")
        self.root.geometry("2000x700")
        
        # ==========================================  logo EMi   ICON  =========
        self.emi = Image.open('../image/emi1.jpg', mode='r')
        self.img = ImageTk.PhotoImage(self.emi)
        self.root.iconphoto(False, self.img)
        #======================================================================================================================
        
        #====================================================  images des booutons & label ==============================================
        self.tracerimg = PhotoImage(file='../image/tracer.png')
        self.quitimg = PhotoImage(file='../image/quitt.png')
        self.initimg = PhotoImage(file='../image/init.png')
        self.saveimg=PhotoImage(file='../image/save.png')
        self.etatimg=PhotoImage(file='../image/etat.png')
        self.schemaimg=PhotoImage(file='../image/schema.png')

        # schema img
        dsir = Image.open('../image/sir1.png')
        dsirs = Image.open("../image/sirs1.png")
        dsiri = Image.open("../image/siri1.png")
        #resize
        resize_sir = dsir.resize((124, 329))
        resize_sirs = dsirs.resize((126, 329))
        resize_siri = dsiri.resize((126, 329))
        # img models
        self.sir = ImageTk.PhotoImage(resize_sir)
        self.sirs = ImageTk.PhotoImage(resize_sirs)
        self.siri = ImageTk.PhotoImage(resize_siri)

        inito = Image.open("../image/inito.png")
        resize_inito = inito.resize((126, 329))
        self.inito = ImageTk.PhotoImage(resize_inito)
        
        #=======================================================================================================================
        # ===================================================  background image  =================================================
        self.bg0 = ImageTk.PhotoImage(file='../image/bg2.png')
        bg0 = Label(self.root, image=self.bg0).place(x=0, y=0)
        self.root.config(bg="black")
        #========================================================================================================================
        #===================================================== les Propriétés de le Classe Window  ==================================
        self.tit = ''                         #.... les titre du graphe ....
        self.test = 0                      #.... le test de l'ption séléctionnée ....
        self.sel = IntVar()          # .... la variable commune des options ....
        self.etat=''

        #========================================================================================================================
        
        # =========================================================== Les Frames =================================================
        self.frame_opt = LabelFrame(self.root, width='200', height='600', padx=20,pady=30, bg='gray', text='Choisir un modele : ', font='Algerian',highlightbackground="black",highlightthickness=2) 
        self.frame_opt.place(x=822, y=31)
        
        self.frame_donnees = LabelFrame(self.root, width='300', height='222', pady=30, bg='gray', text='Saisie de données ', font='Algerian',highlightbackground="black",highlightthickness=2)
        self.frame_donnees.place(x=822, y=185)
        Label(self.frame_donnees, text='', bg='gray' , pady='75').grid(row=6,column=1)
        
        self.frame_etat = LabelFrame(self.root, width='113', height='126', pady=5, bg='gray', text='ETAT : ', font='Algerian',highlightbackground="black",highlightthickness=2)
        self.frame_etat.place(x=670, y=31)
        self.etatl=Label(self.frame_etat,text=''
                         ,font=('Algerian',12),width='12',bg='gray')    # label etat
        self.etatl.grid(row=1,column=0, pady=23, padx=5)

        self.frame_schema = LabelFrame(self.root, width='113', height='126', pady=5, bg='gray', text='SCHEMAS : ', font='Algerian',highlightbackground="black",highlightthickness=2)
        self.frame_schema.place(x=670, y=185)
        self.schema=Label(self.frame_schema,image=self.inito)
        self.schema.grid(row=1,column=0)
        # ========================================================================================================================
        # ===========================================  initialisation des parametres  =================================================
        self.beta = 0
        self.gamma = 1
        self.teta = 0
        self.I0 = 0
        self.S0 = 0
        self.R0=self.beta/self.gamma
        # ========================================================================================================================
        # =========================================================== les inputs : Parametres ========================================
        # ===============================================================   beta  ===================================================
        self.label = Label(self.frame_donnees, text=" Taux d'incidence  β          : ",
                           width='20', font=('Lancer', 14, 'bold'))
        self.label.grid(row=2, column=1, padx=15, pady=10)
        self.beta_entry = Entry(self.frame_donnees, font=(
            'Lancer', 14, 'bold'), width='10')
        self.beta_entry.grid(row=2, column=3, pady=10, padx=15)
   
        # ========================================================================================================================
        
        # ===============================================================  gamma  =================================================
        Label(self.frame_donnees, text=" Taux de guérison γ           : ", font=(
            'Lancer', 14, 'bold'), width='20').grid(row=3, column=1, padx=15, pady=10)
        self.gamma_entry = Entry(self.frame_donnees, font=(
            'Lancer', 14, 'bold'), width='10')
        self.gamma_entry.grid(row=3, column=3, pady=10, padx=15)

        # =========================================================================================================================
        # ===============================================================  teta  =====================================================
        self.lb_teta = Label(self.frame_donnees, text="Taux d\'Immunité                :"
                        , width='20', font=('Lancer', 14, 'bold'))

        self.lb_teta.grid(row=4, padx=15, column=1, pady=10)
        self.teta_entry = Entry(self.frame_donnees, font=(
            'Lancer', 14, 'bold'), width='10')
        self.teta_entry.grid(row=4, column=3, pady=10, padx=15)
        # ==========================================================================================================================
        
        # ===============================================================  I0  =======================================================
        Label(self.frame_donnees, text=" Effectif I0                             : ", width='20', font=(
            'Lancer', 14, 'bold')).grid(row=1, column=1, pady=10, padx=15)
        self.I0_entry = Entry(self.frame_donnees, font=(
            'Lancer', 14, 'bold'), width='10')
        self.I0_entry.grid(row=1, column=3, pady=10, padx=15)
        # =========================================================================================================================
        # ======================================================= Les options SIR SIRS SIRI =========================================
        self.tit = ''
        self.test = 0
        self.sel = IntVar()
        SIR_opt = Radiobutton(self.frame_opt, text='Le modèle SIR',
                              variable=self.sel, value=1, bg='lightgreen',overrelief='sunken',command=self.mm)
        SIR_opt.pack(side=LEFT, fill=BOTH, expand='true', pady=10, padx=5)
        SIRS_opt = Radiobutton(self.frame_opt, text='Le modèle  SIRS',
                               variable=self.sel, value=2, bg='orange',overrelief='sunken', command=self.mm)
        SIRS_opt.pack(side=LEFT, fill=BOTH, expand='true',ipady=10,
                      pady=10, padx=20, anchor='w')
        SIRI_opt = Radiobutton(self.frame_opt, text='Le modèle  SIRI',
                               variable=self.sel, value=3, bg='salmon',overrelief='sunken', command=self.mm)
        SIRI_opt.pack(side=LEFT, fill=BOTH, expand='true', pady=10, padx=5)
        # =========================================================================================================================
        #  ======================================================= LES BUTTONS ==================================================
        # ************************************************************** TRACER  Button  ******************************************************
        button1 = Button(self.root, image=self.tracerimg,
                         bg='gray',borderwidth = 0, command=self.update_values)
        button1.place(x=837, y=457)
        self.root.bind("<Return>", self.update_values)
        self.plot_values()
        # ***************************************************************************************************************************************
        # ************************************************************  SHOW ETAT bouton  ***************************************************
        self.btn_etat=Button(self.frame_etat,image=self.etatimg,bg='gray',borderwidth = 0,command=self.show_etat)
        self.btn_etat.grid(row=0,column=0,pady=6.5,padx=2)
        # *************************************************************************************************************************************** 

        # ************************************************************** QUITTER bouton  *****************************************************
        button2 = Button(image=self.quitimg, bg='gray',borderwidth = 0,relief='sunken', command=self.destr)
        button2.place(x=1075, y=530)
        # *************************************************************************************************************************************** 
        # ************************************************************  REINITIALISER bouton  ************************************************
        button3 = Button(self.root, image=self.initimg,bg='gray', borderwidth = 0,command=self.init)
        button3.place(y=530, x=837)
        # ****************************************************************************************************************************************
        # ******************************************************  ENREGISTRER_GRAPHE bouton   ********************************************
        save_btn = Button(self.root, text='SAVE',bg='gray',borderwidth = 0,image=self.saveimg,

                          command=self.save, font=('Algeria'))
        save_btn.place(y=457, x=1105)
        #*****************************************************************************************************************************************
        # ******************************************************  SCHEMA  bouton   ********************************************
        schema_btn = Button(self.frame_schema, image=self.schemaimg,bg='gray',borderwidth = 0
                            , font=('Algeria'),command=self.ddd)
        schema_btn.grid(row=0,column=0,pady=22,padx=1)
        #*****************************************************************************************************************************************
        pass
        # ===========================================================================================================================

    # =========================================================  les équations diff ===================================================
    def SIR_model(self, y, t, beta, gamma):
        S, I, R = y
        dS_dt = -self.beta*S*I
        dI_dt = self.beta*S*I-self.gamma*I
        dR_dt = self.gamma*I
        return([dS_dt, dI_dt, dR_dt])

    def SIRS_model(self, y, t, beta, gamma, teta):
        S, I, R = y
        dS_dt = -self.beta*S*I+self.teta*R
        dI_dt = self.beta*S*I-self.gamma*I
        dR_dt = self.gamma*I-self.teta*R
        return([dS_dt, dI_dt, dR_dt])

    def SIRI_model(self, y, t, beta, gamma, teta):
        S, I, R = y
        dS_dt = -self.beta*S*I
        dI_dt = self.beta*S*I-self.gamma*I+self.teta*R
        dR_dt = self.gamma*I-self.teta*R
        return([dS_dt, dI_dt, dR_dt])
       # =============================================================Fin équa diff =====================================================
       
# =============================================================== Les Méthodes =====================================================

    # ***************************************************************** QUITTER fonction *********************************************************
    def destr(self):
        a = messagebox.askquestion(
            "QUITTER  ?", "Est ce que vous êtes sûr de vouloir quitter ? \n")
        if a == 'yes':
            self.root.destroy()
        return 0
    # ***********************************************************************************************************************************************
    # ************************************************************* MM function : Changer le taux  θ ***********************************************
    def mm(self):
        self.test = self.sel.get()
        if self.test == 2:
            self.teta_entry.config(state='normal')
            self.lb_teta.config(text='Taux d\'Imm. provisoire θ :')
            self.tit = 'SIRS'
        elif self.test == 3:
            self.teta_entry.config(state='normal')
            self.lb_teta.config(text='Taux d\'Imm. récidive θ     :')
            self.tit = 'SIRI'
        else:
            self.teta_entry.delete(0, 6)
            self.teta_entry.insert(0, 0)
            self.teta_entry.config(state='disabled')
            self.lb_teta.config(text=' Taux d\'Immunité               :')
            self.tit = 'SIR'
    # ***********************************************************************************************************************************************
    # ************************************************************* MISE_A_JOUR_PARAMETRES function ***************************************
    def update_values(self, event=None):
        if self.test == 0:
            messagebox.showwarning(
                'ERREUR ! ', "  ATTENTION : \n Vous n'avez choisi aucun modèle à simuler !")
            return 0
        self.S0 = 1-float(self.I0_entry.get())
        self.beta = float(self.beta_entry.get())
        self.gamma = float(self.gamma_entry.get())
        self.teta = float(self.teta_entry.get())
        self.I0 = float(self.I0_entry.get())
        self.plot_values()
        return None
    # ***********************************************************************************************************************************************
    def show_etat(self):
        if self.test==0:
            messagebox.showwarning(
                'ERREUR ! ', "  ATTENTION : \n Vous n'avez choisi aucun modèle à simuler !")
        elif self.gamma_entry.get()=='' or self.beta_entry.get()=='':
           messagebox.showwarning(
                'ERREUR ! ', "  ATTENTION : \n Donner des valeurs valides pour  γ  et  β   !")
        elif float(self.gamma_entry.get())==0:
            self.etat='Epidémique !!'
            self.etatl.config(text=self.etat,bg='yellow')
            return 0
        else :
            self.R0=self.beta/self.gamma
            if self.R0<=1 :
                self.etat='LIBRE'
            else :
                self.etat='Epidemique'
            self.etatl.config(text=self.etat,bg='yellow')
    # *************************************************************************** TRACER function **************************************************
    def plot_values(self):
        R0, S0, I0 = 0, self.S0, self.I0
        beta, gamma, teta = self.beta, self.gamma, self.teta
        
        self.figure = plt.figure(figsize=(6.5, 6), dpi=100,facecolor='silver')
        self.ax = self.figure.add_subplot(1,1,1)
        self.figure.subplots_adjust(right=0.899,left=0.083)
        

        self.ax.set_ylabel('EFFECTIF')
        self.ax.set_xlabel('PERIODE')
        self.ax.set_title('Graphe illustrant le modèle '+self.tit)
        self.ax.plot(t, [1 for i in range(100000)], label='N', color='orange')
        
        if self.test == 1:

            sol = odeint(self.SIR_model, [S0, I0, R0], t, args=(beta, gamma))
            self.ax.plot(t, sol[:, 0], label="S(t)", color='Blue')
            self.ax.plot(t, sol[:, 1], label="I(t)", color='Red')
            self.ax.plot(t, sol[:, 2], label="R(t)", color='Green')
        elif self.test == 2:
            sol = odeint(self.SIRI_model, [
                         S0, I0, R0], t, args=(beta, gamma, teta))
            self.ax.plot(t, sol[:, 0], label="S(t)", color='Blue')
            self.ax.plot(t, sol[:, 1], label="I(t)", color='Red')
            self.ax.plot(t, sol[:, 2], label="R(t)", color='Green')
        elif self.test == 3:
            sol = odeint(self.SIRS_model, [S0, I0, R0], t, args=(beta, gamma, teta))
            self.ax.plot(t, sol[:, 0], label="S(t)", color='Blue')
            self.ax.plot(t, sol[:, 1], label="I(t)", color='Red')
            self.ax.plot(t, sol[:, 2], label="R(t)", color='Green')
        self.chart = FigureCanvasTkAgg(self.figure, self.root)
        self.chart.get_tk_widget().place(x=10, y=30)
        plt.grid(color='silver',linestyle='dashed')
        axes = plt.gca()
        axes.set_xlim(0, 30.3)
        axes.set_ylim(-0.02, 1.01)
        self.figure.legend(loc='upper left', mode='expand',ncol=4, shadow=True, fancybox=True)
        self.etatl.config(text='',bg='gray')
    # ***********************************************************************************************************************************************

    # ************************************************************* INFORMATIONS DU GRAPHE function **************************************************
    def get_info_trace(self):
        self.test = self.sel.get()
        if self.test==1 :
            text='I0='+str(self.I0)+ '\nβ= '+str(self.beta)+'\nγ= '+str(self.gamma)+'\n  '+'\nR0='+str(self.beta/self.gamma)
        else:
            text='I0='+str(self.I0)+ '\nβ= '+str(self.beta)+'\nγ= '+str(self.gamma)+'\nθ= '+str(self.teta)+'\nR0='+str(self.beta/self.gamma)
        self.ax.text(1.002, 0.6, 'Paramétres:', horizontalalignment='left',verticalalignment='bottom',transform=self.ax.transAxes,font='Monotype corsiva',style='oblique',fontsize=11) 
        self.ax.text(1.01, 0.4, text, horizontalalignment='left',verticalalignment='bottom',transform=self.ax.transAxes,color='blue',font='Monotype corsiva', fontsize=12,bbox={'facecolor': 'silver', 'alpha': 0.9, 'pad': 1.5,'edgecolor':'gray'}) 
        self.date=datetime.datetime.now() # la date
        self.ax.text(0.65, -0.13, 'Date : '+self.date.strftime('%A %d/%m/%Y %H:%M:%S'),verticalalignment='bottom', horizontalalignment='left',transform=self.ax.transAxes,font='Monotype corsiva',color='gray', fontsize=12) 
    # ***********************************************************************************************************************************************
     

    # ************************************************************* REINITIALISATION function **************************************************
    def init(self):
        self.teta_entry.delete(0, 'end')
        self.beta_entry.delete(0, 'end')
        self.I0_entry.delete(0, 'end')
        self.gamma_entry.delete(0, 'end')
        self.teta = 0
        self.gamma = 0
        self.beta = 0
        self.I0 = 0
        self.S0=0
        self.figure = plt.figure(figsize=(6.5, 6), dpi=100,facecolor='silver')
        self.tit=''
        self. plot_values()
    
        Label(self.frame_schema,image=self.inito).grid(row=1,column=0)
        
        
        
        return None
    # ***********************************************************************************************************************************************

    #******************************************************************  SAVE FIGURE function ****************************************************
    def save(self):
        a = messagebox.askquestion(
            "INFORMATIONS DU GRAPHE : ", "Voulez vous enregistrer la figure avec date et paramétres  ? \n")
        if a == 'yes':
            self.get_info_trace()
        self.dir=filedialog.asksaveasfilename(defaultextension='.png', filetypes=(('PNG FILE','*.png'),('JPG FILE','*.jpg')))
        self.figure.savefig(self.dir,dpi=100)

        
    def ddd(self):

        self.schem=Label(self.frame_schema)
        mg=''
        if self.test==1:
            mg=self.sir
        elif self.test==2:
            mg=self.sirs
        elif self.test==3:
            mg=self.siri
        else :
            messagebox.showwarning(
                'ERREUR ! ', "  ATTENTION : \n Vous n'avez choisi aucun modèle à schématiser !")
            return 0
        self.schem.config(image=mg)
        self.schem.grid(row=1,column=0)                         
    pass
    # ***********************************************************************************************************************************************



main()
