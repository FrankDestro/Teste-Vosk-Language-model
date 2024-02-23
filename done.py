import vosk
import speech_recognition as sr

# Caminho para o modelo Vosk em português
model_path = r"C:\Users\franklyn.damaceno\Desktop\SpeechRecognizer\Volsk\vosk-model-pt-fb-v0.1.1-pruned"

# Carregamento do modelo de linguagem Vosk para português
try:
    print("Carregando o modelo Vosk...")
    model = vosk.Model(model_path)
    print("Modelo Vosk carregado com sucesso.")
except Exception as e:
    # Imprima detalhes do erro
    print(f"Erro ao carregar o modelo: {e}")
    raise

# Caminho para o arquivo de áudio
audio_file = r"C:\Users\franklyn.damaceno\Desktop\SpeechRecognizer\Volsk\audio_teste\call4.wav"  # Use barras invertidas ou duplas para evitar problemas de escape

# Criando um reconhecedor de fala
recognizer = sr.Recognizer()

# Abrindo o arquivo de áudio dentro de um bloco try-except
try:
    with sr.AudioFile(audio_file) as source:
        print("Gravando áudio...")
        # Gravando o áudio
        audio = recognizer.record(source)
        print("Áudio gravado com sucesso.")
except Exception as e:
    # Tratamento de erros ao abrir o arquivo de áudio
    print(f"Erro ao abrir o arquivo de áudio: {e}")
    raise

# Verificando a frequência de amostragem
if audio.sample_rate != 16000:
    # Redimensionando a frequência de amostragem para 16.000 Hz
    audio = audio.set_frame_rate(16000)

# Convertendo para o formato PCM linear
waveform = audio.frame_data  # Correção aqui

# Reconhecendo a fala no áudio
try:
    print("Iniciando o reconhecimento de fala...")
    # Inicializando o reconhecedor do Vosk
    vosk_recognizer = vosk.KaldiRecognizer(model, 16000)

    print("Alimentando o áudio para o Vosk...")
    # Alimentando o áudio para o Vosk
    vosk_recognizer.AcceptWaveform(waveform)

    print("Finalizando o reconhecimento...")
    # Finalizando o reconhecimento
    result = vosk_recognizer.FinalResult()

    print("Obtendo o texto transcrito...")
    # Obtendo o texto transcrito
    text = result
    print(text)

    # Salvando o texto transcrito em um arquivo no diretório desejado
    caminho_do_arquivo = r"C:\Users\franklyn.damaceno\Desktop\SpeechRecognizer\Volsk\transcricao.txt"
    with open(caminho_do_arquivo, "w", encoding="utf-8") as file:
        file.write(text)

    print("Reconhecimento de fala concluído com sucesso.") 
    
    input("Pressione Enter para sair.")
    
except Exception as e:
    # Tratamento de erros durante o reconhecimento de fala
    print(f"Erro durante o reconhecimento de fala: {e}")

