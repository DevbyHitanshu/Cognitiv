def speech():
    import speech_recognition as s 
    #create a object of Recognizer
    sr=s.Recognizer()

    with s.Microphone() as m:
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        return query
hi = speech()
print(hi)