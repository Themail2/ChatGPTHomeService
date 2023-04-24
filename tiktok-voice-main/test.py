
import os, openai, playsound
import speech_recognition as sr


openai.api_key = "your key here"

mic = sr.Microphone()
r = sr.Recognizer()
# User prompts chatGPT using their voice
while True:
  
  text = ""
  # Listens passively and attempts to convert each "phrase" that it hears
  with mic as source:
    print("Listening")
    audio = r.listen(source, None, 20)
    try:
      text = r.recognize_google(audio)
      
    except:
      print("Could not convert audio to text")
  # When the user speaks the prompt phrase, send that to chatGPT
  if text.find("I need help") != -1:
    text = text[text.find("I need help")+10:]
    print(text)
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=[
        {"role": "user", "content": text}
      ]
    )
    with open("text.txt", 'w') as f:
        
        f.write(completion.choices[0].message.content)
        f.close()
    # We have to delete the voice.mp3 because playsound is blocking and will prevent us 
    # from overwriting it and playing the new file
    os.remove("voice.mp3")
    # Send all relevant info to the tiktok API
    os.system("python3 main.py -v en_us_001 -p -f text.txt -s your tiktok session ID cookie here")
    playsound.playsound("voice.mp3")
