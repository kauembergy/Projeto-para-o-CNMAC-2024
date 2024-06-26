
import customtkinter
from customtkinter import CTkFont
from tkinter import messagebox
import numpy as np
import pandas as pd
from calculo import calcular

# Definir tema e cores
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def calcular():
    try:
        w1 = float(entry_w1.get())
        w2 = float(entry_w2.get())
        w3 = float(entry_w3.get())
        
        if (w1 + w2 + w3) != 1.0:
            messagebox.showerror("Erro", "A soma dos 3 valores não é igual a 1. Tente novamente.")
            return
        
        matriz = np.array([[0.1*w1, 0.3*w2, 0.2*w3],
                           [0.3*w1, 0.3*w2, 0.3*w3],
                           [0.1*w1, 0.2*w2, 0.2*w3]])
        
        r1 = matriz[0, 0]
        r2 = matriz[0, 1]
        r3 = matriz[0, 2]
        r4 = matriz[1, 0]
        r5 = matriz[1, 1]
        r6 = matriz[1, 2]
        r7 = matriz[2, 0]
        r8 = matriz[2, 1]
        r9 = matriz[2, 2]
        
        dados1 = {
            'nota para a primeira aresta e os três critérios do analista': [0.1, 0.3, 0.2],
            'nota para a segunda aresta e os três critérios do analista': [0.3, 0.3, 0.3],
            'nota para a terceira aresta e os três critérios do analista': [0.1, 0.2, 0.2]
        }
        df1 = pd.DataFrame(dados1)
        df1.to_excel('Dados fornecidos pela avaliação do especialista.xlsx')
        
        dados2 = {
            'nota para a primeira aresta com as preferências do usuário': [r1, r2, r3],
            'nota para a segunda aresta com as preferências do usuário': [r4, r5, r6],
            'nota para a terceira aresta com as preferências do usuário': [r7, r8, r9]
        }
        df2 = pd.DataFrame(dados2)
        df2.to_excel('Notas de cada aresta com as preferências do usuário.xlsx')
        
        matriz1 = np.array([[(r1 + r4) / 2, (r2 + r5) / 2, (r3 + r6) / 2],
                            [r7 / 2, r8 / 2, r9 / 2]])
        
        x1 = matriz1[0][0]
        x2 = matriz1[0][1]
        x3 = matriz1[0][2]
        y1 = matriz1[1][0]
        y2 = matriz1[1][1]
        y3 = matriz1[1][2]

        dados3 = {
            'nota dos 3 critérios para o primeiro trajeto a1': [x1, x2, x3],
            'nota dos 3 critérios para o segundo trajeto a2': [y1, y2, y3]
        }
        df3 = pd.DataFrame(dados3)
        df3.to_excel('Notas finais de cada critério para cada trajeto.xlsx')
        
        x = (x1 + x2 + x3) / 3
        y = (y1 + y2 + y3) / 3
        
        result1_label.configure(text=f"Média para o caminho a1 é: {x:.2f}")
        result2_label.configure(text=f"Média para o caminho a2 é: {y:.2f}")
        
        if x > y:
            result3_label.configure(text="O caminho a1 é o melhor")
        else:
            result3_label.configure(text="O caminho a2 é o melhor")
        
        customtkinter.CTkLabel(janela, text='Criou-se no seu pc 3 planilhas no excel para os resultados com as notas dos especialistas,', font=fonte_cabecalho).pack(padx=10, pady=2)
        customtkinter.CTkLabel(janela, text='notas para cada aresta e notas para os 2 trajetos', font=fonte_cabecalho).pack(padx=10, pady=2)
        customtkinter.CTkLabel(janela, text='Muito obrigado, espero que tenha gostado do meu app, qualquer dúvida entrar em contato.', font=fonte_cabecalho).pack(padx=10, pady=5)
        customtkinter.CTkLabel(janela, text='\u2709 email: kauembergy@gmail.com', font=fonte_cabecalho, fg_color="black", corner_radius=8).pack(padx=10, pady=5)
        customtkinter.CTkLabel(janela, text='\u260E Fone: (84) 99609-2391', font=fonte_cabecalho, fg_color="black", corner_radius=8).pack(padx=10, pady=5)
    except ValueError:
        messagebox.showerror("Erro", "Você não digitou um número, por favor digite um número.")

# Inicialização da janela
janela = customtkinter.CTk()
janela.title('Calculo do melhor trajeto')
janela.geometry('900x700')

# Definindo a fonte
fonte_cabecalho = CTkFont(family='Garamond', size=17, weight='bold')

# Adicionando widgets
texto = customtkinter.CTkLabel(janela, text='Olá, seja bem vindo ao método de tomada de decisão em um grafo fuzzy 3-dimensional para escolha de melhor trajeto', font=fonte_cabecalho)
texto.pack(padx=10, pady=20)

texto2 = customtkinter.CTkLabel(janela, text='Suponha que voce queira ir a um destino e para isso existem 2 possibilidades de trajeto, para ajudar-lo a escolher qual trajeto pegar,')
texto2.pack(padx=10, pady=2)

texto3 = customtkinter.CTkLabel(janela, text='dê uma nota para os 3 critérios a seguir. Lembre-se, a soma das 3 notas devem dar igual a 1!')
texto3.pack(padx=10, pady=2)

entry_w1 = customtkinter.CTkEntry(janela, placeholder_text='Pavimentação')        
entry_w1.pack(padx=10, pady=10)

entry_w2 = customtkinter.CTkEntry(janela, placeholder_text='Sinalização')
entry_w2.pack(padx=10, pady=10)

entry_w3 = customtkinter.CTkEntry(janela, placeholder_text='Distância')
entry_w3.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='calcular', command=calcular, fg_color='dodgerblue', hover_color='skyblue')
botao.pack(padx=10, pady=10)

result1_label = customtkinter.CTkLabel(janela, text="", font=fonte_cabecalho, fg_color="black", corner_radius=8)
result1_label.pack(padx=10, pady=5)

result2_label = customtkinter.CTkLabel(janela, text="", font=fonte_cabecalho, fg_color="black", corner_radius=8)
result2_label.pack(padx=10, pady=5)

result3_label = customtkinter.CTkLabel(janela, text="", font=fonte_cabecalho, fg_color="black", corner_radius=8)
result3_label.pack(padx=10, pady=5)

janela.mainloop()
