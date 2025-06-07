import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
import random
import time

class RomanNumeralApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprendizaje de Números Romanos")
        self.root.geometry("360x640")
        
        # Configurar color de fondo
        self.root.configure(bg="#F2B900")
        
        # Estilo personalizado
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#F2B900")
        self.style.configure("Custom.TLabel", background="#F2B900", font=("Comic Sans MS", 12))
        self.style.configure("Title.TLabel", background="#F2B900", font=("Comic Sans MS", 16, "bold"))
        self.style.configure("Custom.TButton", font=("Comic Sans MS", 11), padding=5)
        
        # Variables
        self.pregunta_var = tk.StringVar()
        self.respuesta_var = tk.StringVar()
        self.mensaje_var = tk.StringVar()
        self.puntuacion = 0
        self.nivel_dificultad = tk.StringVar(value="Fácil")
        self.tiempo_inicio = 0
        self.mensajes_animo = [
            "¡Tú puedes!",
            "¡Sigue intentando!",
            "¡Casi lo tienes!",
            "¡No te rindas!",
            "¡Confía en ti!"
        ]
        
        # Crear notebook con estilo
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Crear las secciones
        self.crear_seccion_introduccion()
        self.crear_seccion_conversion()
        self.crear_seccion_usos()
        self.crear_seccion_ejercicios()
    
    def crear_seccion_introduccion(self):
        intro_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(intro_frame, text="Introducción")
        
        # Título con estilo
        titulo = ttk.Label(intro_frame, text="Números Romanos", style="Title.TLabel")
        titulo.pack(pady=15)
        
        # Imagen decorativa (deberás agregar la imagen)
        try:
            img = Image.open("roman_numbers.png")
            img = img.resize((200, 100))
            photo = ImageTk.PhotoImage(img)
            img_label = ttk.Label(intro_frame, image=photo)
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            pass
        
        intro_text = """Los números romanos son un sistema de numeración que se originó en la antigua Roma.

Símbolos básicos:
I = 1   ⚔️
V = 5   🛡️
X = 10  ⚔️
L = 50  🛡️
C = 100 ⚔️
D = 500 🛡️
M = 1000 ⚔️

Reglas principales:
1. Se pueden repetir hasta tres veces seguidas
2. Si un símbolo menor va antes que uno mayor, se resta
3. Si un símbolo menor va después de uno mayor, se suma"""
        
        intro_label = ttk.Label(intro_frame, text=intro_text, style="Custom.TLabel", wraplength=340, justify="left")
        intro_label.pack(pady=10)
    
    def crear_seccion_conversion(self):
        conv_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(conv_frame, text="Conversión")
        
        ttk.Label(conv_frame, text="Conversor de Números", style="Title.TLabel").pack(pady=15)
        
        # Sección arábigo a romano
        ttk.Label(conv_frame, text="Número Arábigo:", style="Custom.TLabel").pack(pady=5)
        arabigo_entry = ttk.Entry(conv_frame, font=("Comic Sans MS", 12))
        arabigo_entry.pack(pady=5)
        
        ttk.Button(conv_frame, text="✨ Convertir a Romano ✨", 
                   command=lambda: self.convertir_arabigo_romano(arabigo_entry.get()),
                   style="Custom.TButton").pack(pady=10)
        
        # Sección romano a arábigo
        ttk.Label(conv_frame, text="Número Romano:", style="Custom.TLabel").pack(pady=5)
        romano_entry = ttk.Entry(conv_frame, font=("Comic Sans MS", 12))
        romano_entry.pack(pady=5)
        
        ttk.Button(conv_frame, text="✨ Convertir a Arábigo ✨", 
                   command=lambda: self.convertir_romano_arabigo(romano_entry.get()),
                   style="Custom.TButton").pack(pady=10)
        
        self.resultado_conv = ttk.Label(conv_frame, text="", style="Custom.TLabel")
        self.resultado_conv.pack(pady=15)
    
    def crear_seccion_usos(self):
        usos_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(usos_frame, text="Usos")
        
        ttk.Label(usos_frame, text="Usos Prácticos", style="Title.TLabel").pack(pady=15)
        
        usos_text = """🏛️ Los números romanos se utilizan en:

📚 Capítulos de libros
👑 Nombres de reyes y papas
⌚ Relojes analógicos
📅 Siglos y años
🏆 Eventos históricos
🎭 Numeración de congresos
⚗️ Nomenclatura química
📖 Numeración de volúmenes"""
        
        usos_label = ttk.Label(usos_frame, text=usos_text, style="Custom.TLabel", wraplength=340, justify="left")
        usos_label.pack(pady=10)
    
    def crear_seccion_ejercicios(self):
        ejerc_frame = ttk.Frame(self.notebook, style="Custom.TFrame")
        self.notebook.add(ejerc_frame, text="Ejercicios")
        
        ttk.Label(ejerc_frame, text="¡Practica tus conocimientos!", style="Title.TLabel").pack(pady=15)
        
        # Selector de nivel con estilo
        ttk.Label(ejerc_frame, text="Nivel:", style="Custom.TLabel").pack(pady=5)
        niveles = ttk.Combobox(ejerc_frame, textvariable=self.nivel_dificultad,
                              values=["Fácil", "Medio", "Difícil"],
                              font=("Comic Sans MS", 11))
        niveles.pack(pady=5)
        niveles.bind('<<ComboboxSelected>>', lambda e: self.cambiar_nivel())
        
        # Pregunta
        pregunta_label = ttk.Label(ejerc_frame, textvariable=self.pregunta_var, style="Custom.TLabel")
        pregunta_label.pack(pady=15)
        
        # Entrada de respuesta
        respuesta_entry = ttk.Entry(ejerc_frame, textvariable=self.respuesta_var, font=("Comic Sans MS", 12))
        respuesta_entry.pack(pady=10)
        
        # Botones
        ttk.Button(ejerc_frame, text="✅ Verificar", 
                   command=self.verificar_respuesta,
                   style="Custom.TButton").pack(pady=10)
        ttk.Button(ejerc_frame, text="🔄 Nueva Pregunta", 
                   command=self.generar_pregunta,
                   style="Custom.TButton").pack(pady=10)
        
        # Mensaje y puntuación
        self.mensaje_label = ttk.Label(ejerc_frame, textvariable=self.mensaje_var, style="Custom.TLabel")
        self.mensaje_label.pack(pady=10)
        self.puntuacion_label = ttk.Label(ejerc_frame, 
                                         text=f"🏆 Puntuación: {self.puntuacion}", 
                                         style="Custom.TLabel")
        self.puntuacion_label.pack(pady=10)
        
        # Generar primera pregunta
        self.generar_pregunta()
    
    def cambiar_nivel(self):
        self.generar_pregunta()
    
    def generar_pregunta(self):
        # Rangos según nivel de dificultad
        rangos = {
            "Fácil": (1, 20),
            "Medio": (21, 100),
            "Difícil": (101, 3999)
        }
        rango = rangos[self.nivel_dificultad.get()]
        self.numero_actual = random.randint(rango[0], rango[1])
        
        # Alternar entre conversión a romano y a arábigo
        if random.choice([True, False]):
            self.pregunta_var.set(f"🔄 Convierte a número romano: {self.numero_actual}")
            self.modo_actual = "a_romano"
        else:
            self.pregunta_var.set(f"🔄 Convierte a número arábigo: {self.entero_a_romano(self.numero_actual)}")
            self.modo_actual = "a_arabigo"
        
        self.respuesta_var.set("")
        self.mensaje_var.set("")
        self.tiempo_inicio = time.time()
    
    def verificar_respuesta(self):
        tiempo_respuesta = time.time() - self.tiempo_inicio
        respuesta_usuario = self.respuesta_var.get().upper()
        
        if self.modo_actual == "a_romano":
            respuesta_correcta = self.entero_a_romano(self.numero_actual)
            es_correcta = respuesta_usuario == respuesta_correcta
        else:
            respuesta_correcta = str(self.numero_actual)
            es_correcta = respuesta_usuario == respuesta_correcta
        
        if es_correcta:
            self.mensaje_var.set("🎉 ¡Correcto! 🎉")
            self.puntuacion += 1
        else:
            self.mensaje_var.set(f"❌ Incorrecto. La respuesta correcta es: {respuesta_correcta}")
        
        # Mensaje de ánimo si tarda más de 15 segundos
        if tiempo_respuesta > 15 and not es_correcta:
            self.mensaje_var.set(f"{self.mensaje_var.get()}\n{random.choice(self.mensajes_animo)}")
        
        self.puntuacion_label.config(text=f"🏆 Puntuación: {self.puntuacion}")
    
    def entero_a_romano(self, num):
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        resultado = ""
        i = 0
        while num > 0:
            for _ in range(num // valores[i]):
                resultado += simbolos[i]
                num -= valores[i]
            i += 1
        return resultado
    
    def romano_a_entero(self, romano):
        valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        resultado = 0
        anterior = 0
        
        for letra in reversed(romano.upper()):
            actual = valores[letra]
            if actual >= anterior:
                resultado += actual
            else:
                resultado -= actual
            anterior = actual
        return resultado
    
    def convertir_arabigo_romano(self, numero):
        try:
            num = int(numero)
            if 1 <= num <= 3999:
                self.resultado_conv.config(text=f"✨ Resultado: {self.entero_a_romano(num)} ✨")
            else:
                self.resultado_conv.config(text="❌ Error: Número fuera de rango (1-3999)")
        except ValueError:
            self.resultado_conv.config(text="❌ Error: Ingrese un número válido")
    
    def convertir_romano_arabigo(self, romano):
        try:
            resultado = self.romano_a_entero(romano)
            self.resultado_conv.config(text=f"✨ Resultado: {resultado} ✨")
        except:
            self.resultado_conv.config(text="❌ Error: Número romano inválido")

if __name__ == "__main__":
    root = tk.Tk()
    app = RomanNumeralApp(root)
    root.mainloop()