import streamlit as st
import pandas as pd

def solve_sudoku_from_csv(file):
    # Your original Sudoku-solving functions go here
    def horizontal(file):
        df = pd.read_csv(file, header=None)
        lista1 = df.values.tolist()  # Convert DataFrame to list of lists
        return lista1
    def horizontal_2(listai):
        lista1=[]
        i=0    
        k=0
        while i<9:
            j=0
            temp_list=[]
            while j<9:
                temp_list.append(listai[k])
                j+=1
                k+=1
            lista1.append(temp_list)
            i+=1
        return lista1

    def vertical(lista1):
        j=0
        lista2=[]
        while j<9:
            temp_list=[]
            i=0
            while i<9:
                temp_list.append(lista1[i][j])
                i+=1
            lista2.append(temp_list)
            j+=1
        return lista2

    def cuadros(lista1):
        lista3=[]
        j=0
        temp_list=[]
        while j<3:
            i=0
            while i<3:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=0
        temp_list=[]
        while j<3:
            i=3
            while i<6:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=0
        temp_list=[]
        while j<3:
            i=6
            while i<9:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)    
        j=3
        temp_list=[]
        while j<6:
            i=0
            while i<3:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=3
        temp_list=[]
        while j<6:
            i=3
            while i<6:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=3
        temp_list=[]
        while j<6:
            i=6
            while i<9:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=6
        temp_list=[]
        while j<9:
            i=0
            while i<3:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=6
        temp_list=[]
        while j<9:
            i=3
            while i<6:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        j=6
        temp_list=[]
        while j<9:
            i=6
            while i<9:
                temp_list.append(lista1[j][i])
                i+=1
            j+=1
        lista3.append(temp_list)
        return lista3
        
    def concatenar(lista1,lista2,lista3):
        lista4=[]
        i=0
        while i<3:
            k=0
            j=0
            while k<9:
                temp_list=[]
                temp_list.append(lista1[i])
                temp_list.append(lista2[k])
                temp_list.append(lista3[j])
                lista4.append(temp_list)
                k+=1
                if k>=3:
                    j=1
                if k>=6:
                    j=2
            i+=1
        i=3
        while i<6:
            k=0
            j=3
            while k<9:
                temp_list=[]
                temp_list.append(lista1[i])
                temp_list.append(lista2[k])
                temp_list.append(lista3[j])
                lista4.append(temp_list)
                k+=1
                if k>=3:
                    j=4
                if k>=6:
                    j=5
            i+=1
        i=6
        while i<9:
            k=0
            j=6
            while k<9:
                temp_list=[]
                temp_list.append(lista1[i])
                temp_list.append(lista2[k])
                temp_list.append(lista3[j])
                lista4.append(temp_list)
                k+=1
                if k>=3:
                    j=7
                if k>=6:
                    j=8
            i+=1
        for x in range(len(lista4)):
            i=0
            temp_list=[]
            while i<3:
                j=0
                while j<9:
                    temp_list.append(lista4[x][i][j])
                    j+=1
                i+=1
            lista4[x]=temp_list
        return lista4

    def faltantes_horizontal(lista4,listai):
        lista5A=[]
        for i in range(len(listai)):
            temp_list=[]
            if listai[i]==0:
                x=1
                while x<10:
                    y=True
                    for j in lista4[i]:
                        if x==j:
                            y=False
                    if y==True:
                        temp_list.append(x)
                    x+=1
                lista5A.append(temp_list)
            else:
                lista5A.append(temp_list)
        lista5=[]
        i=0
        while i<81:
            temp_list=[]
            x=0
            while x<9:
                temp_list.append(lista5A[i])
                x+=1
                i+=1
            lista5.append(temp_list)
        return lista5
        
    def lista_inicial(lista1):
        listai=[]
        for i in range(len(lista1)):
            for j in range(len(lista1[i])):
                listai.append(lista1[i][j])
        return listai
                
    def solver(lista4,listai):
        for i in range(len(listai)):
            if listai[i]==0:
                x=1
                z=0
                w=0
                while x<10:
                    y=False
                    for j in range(len(lista4[i])):
                        if x==lista4[i][j]:
                            y=True
                    if y==False:
                        z+=1
                        w=x
                    x+=1
                if z==1:
                    listai[i]=w
        return listai

    def solver_2_horizontal(lista5,listai):
        for i in range(len(lista5)):
            x=1
            while x<10:
                y=0
                w=0
                for j in range(len(lista5[i])):
                    for k in range(len(lista5[i][j])):
                        if lista5[i][j][k]==x:
                            y+=1
                            w=j
                if y==1:
                    indice=(i*9)+w
                    listai[indice]=x
                x+=1
        return listai

    def solver_2_vertical(lista6,listai):
        for i in range(len(lista6)):
            x=1
            while x<10:
                y=0
                w=0
                for j in range(len(lista6[i])):
                    for k in range(len(lista6[i][j])):
                        if lista6[i][j][k]==x:
                            y+=1
                            w=j
                if y==1:
                    indice=(w*9)+i
                    listai[indice]=x
                x+=1
        return listai

    def solver_2_cuadros(lista7,listai):
        for i in range(len(lista7)):
            x=1
            while x<10:
                y=0
                w=0
                for j in range(len(lista7[i])):
                    for k in range(len(lista7[i][j])):
                        if lista7[i][j][k]==x:
                            y+=1
                            w=j
                if y==1:
                    indice=(i*3)+(w%3)+((w//3)*9)+(((i//3)*9)*2)
                    listai[indice]=x
                x+=1
        return listai

    def loop(listai):
        y=False
        for i in range(len(listai)):
            if listai[i]==0:
                y=True
        if y==True:
            x=1
        if y==False:
            x=-1
        return x

    def imprimir(lista1):
        output = " "
        k = 0
        for i in lista1:
            if k == 3 or k == 6:
                output += "-" * 23 + "\n"
            k += 1
            l = 0
            for j in i:
                output += "{:2}".format(j)
                if l == 2 or l == 5:
                    output += " |"
                l += 1
            output += "\n"
        st.text(output)
                
    def reducir_listas_horizontal(lista):
        for i in range(len(lista)):
            k=0
            while k<9:
                x=lista[i][k]
                if len(x)==2:
                    for j in range(len(lista[i])):
                        if len(lista[i][j])==2 and i!=j and x==j:
                            st.write("Horizontal {}".format(i))
                k+=1

    def reducir_listas_vertical(lista):
        for i in range(len(lista)):
            k=0
            while k<9:
                x=lista[i][k]
                if len(x)==2:
                    for j in range(len(lista[i])):
                        if len(lista[i][j])==2 and i!=j and x==j:
                            st.write("Vertical {}".format(i))
                k+=1

    def reducir_listas_cuadros(lista):
        for i in range(len(lista)):
            k=0
            while k<9:
                x=lista[i][k]
                if len(x)==2:
                    for j in range(len(lista[i])):
                        if len(lista[i][j])==2 and i!=j and x==j:
                            st.write("Cuadros {}".format(i))
                k+=1
                        

    def program(file):
        lista1=horizontal(file)
        k=0
        for i in lista1:
            for j in i:
                if j!=0:
                    k+=1
        lista2=vertical(lista1)
        lista3=cuadros(lista1)
        lista4=concatenar(lista1,lista2,lista3)
        listai=lista_inicial(lista1)
        listai=solver(lista4,listai)
        x=loop(listai)
        y=0
        while x!=-1 and y<80:
            lista1=horizontal_2(listai)
            lista2=vertical(lista1)
            lista3=cuadros(lista1)
            lista4=concatenar(lista1,lista2,lista3)
            lista5=faltantes_horizontal(lista4,listai)
            listai=solver_2_horizontal(lista5,listai)
            lista6=vertical(lista5)
            listai=solver_2_vertical(lista6,listai)
            lista7=cuadros(lista5)
            listai=solver_2_cuadros(lista7,listai)
            lista1=horizontal_2(listai)
            lista2=vertical(lista1)
            lista3=cuadros(lista1)
            lista4=concatenar(lista1,lista2,lista3)
            listai=solver(lista4,listai)
            x=loop(listai)
            y+=1
        lista1=horizontal_2(listai)
        if x==-1:
            imprimir(lista1)
            st.write("Vueltas: {}".format(y))
            st.write("Casillas Dadas: {}".format(k))
        else:
            m=0
            for i in lista1:
                for j in i:
                    if j!=0:
                        m+=1
            st.write("No se pudo resolver")
            imprimir(lista1)
            st.write("Casillas Dadas: {}".format(k))
            st.write("Numeros Encontrados: {}".format(m-k))
            reducir_listas_horizontal(lista5)
            reducir_listas_vertical(lista6)
            reducir_listas_cuadros(lista7)

    program(file)


st.title("Sudoku Solver by Alan Kalach (2015)")
uploaded_file = st.file_uploader("Upload a CSV file with Sudoku puzzle", type=["csv"])

if uploaded_file is not None:
    # Read the file
    solve_sudoku_from_csv(uploaded_file)

