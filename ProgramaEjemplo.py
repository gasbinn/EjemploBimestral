import tkinter as tk
def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos.")
ventana = tk.Tk()
ventana.title("Calculadora de Suma")

label1 = tk.Label(ventana, text="Número 1:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(ventana, text="Número 2:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1, padx=10, pady=10)

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()