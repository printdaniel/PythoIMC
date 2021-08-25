from tkinter import*
import tkinter.messagebox


class ImcCalc:
    def __init__(self,root):
        self.root=root
        self.root.title("Calculadora IMC")
        self.root.geometry("300x300+0+0")
        self.root.config(bg="#060505")

        self.Altura = DoubleVar()
        self.Peso = DoubleVar()
        self.Res = DoubleVar()
        self.res = 0

        encabezado = Label(root, text="Registro de Altura"
                           , width=20, font=('arial', 
                            16, 'bold'), bg='#FFC300')
        encabezado.grid(row=0, column=0, columnspan=2)

        frame = LabelFrame(self.root,text='Ingreso de Datos',bg="#FFA262",padx=20,pady=20,)
        frame.grid(row=1, column=0,columnspan=3,pady=10,sticky='W')

        frame1 = LabelFrame(self.root,text='Controles',bg="#FFA262",padx=20, pady=20)
        frame1.grid(row=2,column=0,columnspan=2,pady=10,padx=10,sticky='W')

        self.frame3 = LabelFrame(self.root, text='Su imc es...',bg='#FFA262')
        self.frame3.grid(row=1, column=1,pady=10,padx=10)

        # LABELS
        label_alt = Label(frame, text='Altura:',font=('arial', 12, 'bold'),
                          bg="#FFA262")
        label_pes = Label(frame, text='Peso:', font=('arial', 12, 'bold'),
                          bg="#FFA262")

        # GRID LABEL
        label_alt.grid(row=1, column=0, sticky='W')
        label_pes.grid(row=2, column=0, sticky='W')

        # ENTRY
        e_alt = Entry(frame, width=5, textvariable=self.Altura)
        e_pes = Entry(frame, width=5, textvariable=self.Peso)

        # ENTRY GRID
        e_alt.grid(row=1, column=1)
        e_pes.grid(row=2, column=1)

        #INFO LABEL
        
        info_label = Label(self.frame3, text=str(self.res))
        info_label.grid(row=0,column=0)

        #Botones

        btn_imc = Button(frame1,text="IMC", width=12,command= self.imc_funcion)
        btn_imc.grid(row=0,column=0)

        btn_salir = Button(frame1,text="Salir",width=10,command=root.destroy)
        btn_salir.grid(row=0,column=1)

    def imc_funcion(self):
        res = self.Peso.get()/(self.Altura.get()*self.Altura.get())

        self.info_label = Label(self.frame3, text=str(round(res, 2)))
        self.info_label.grid(row=0,column=0)

if __name__=='__main__':
    root=Tk()
    applicaton=ImcCalc(root)
    root.mainloop()
