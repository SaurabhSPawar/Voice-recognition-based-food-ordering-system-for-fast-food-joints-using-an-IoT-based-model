import pymysql 
import webbrowser
#import pyaudio as p 
import speech_recognition as sr
from playsound import playsound
import pyttsx3
import time 
import os 
from BE_PROJECCT_BK.voiceml import usr_choice
def  recorddata():
    time.sleep(2)
    print(" listening ....")
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sound = r.listen(source,phrase_time_limit=10)  
            #sound = r.listen(source, timeout=1,phrase_time_limit=9)
            print("Time Over")
            playsound('bell.mp3')
            time.sleep(1)
            print("Text:"+r.recognize_google(sound))
    mode_choice = r.recognize_google(sound)
    return mode_choice
db = pymysql.connect("localhost","root","","hoteldb" ) #data base connection
cursor=db.cursor()     #cursor created for db handling 
engine = pyttsx3.init()           #for text to speech
engine.setProperty('rate', 120)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)
r = sr.Recognizer()
r.pause_threshold = 0.6
microphone = sr.Microphone()
print("Please wear head phone to start conversation .")
engine.say("Please wear head phone to start conversation .  ")
engine.runAndWait()
time.sleep(5)
engine.say("may I start conversation ?")
engine.runAndWait()
with sr.Microphone() as source:
    print("may I start conversation ?")
    r.adjust_for_ambient_noise(source)
    sound = r.listen(source)
    print("Time Over")
    playsound('bell.mp3')
    time.sleep(1) 
#text=recorddata()  
try:
    print("Text:"+r.recognize_google(sound));
    user_sound = r.recognize_google(sound)
#    user_sound = text
    mainflag = 0  #next changs from below
    while(mainflag !=1):
        if(user_sound == 'ok' or user_sound == 'yes' or user_sound == 'okay' or user_sound == "yes yes"):
            engine.say("lets continue")
            engine.runAndWait()
            flag =0 
            while(flag!=1):
                engine.say("which mode do you want ?")
                engine.runAndWait()
                engine.say("one for booking by conversation.")
                engine.runAndWait()
                engine.say("two for manual booking.")
                engine.runAndWait()
                engine.say("three for inquiry.")
                engine.runAndWait()
                time.sleep(1)
                mode_choice = recorddata()
                if(mode_choice == "1" or mode_choice == "one" or mode_choice=="one one" or mode_choice=="11" or mode_choice=="van"):
                    usr_choice  = 0
                    while(usr_choice!=1):
                        engine.say("Your choice is One")
                        engine.runAndWait()
                        engine.say("Should I confirm ?")
                        engine.runAndWait()
                        reply=recorddata()
                        if(reply == "yes" or reply == "confirm" or reply =="ya" or  reply == "yes yes" or reply =="yeah"):
                            engine.say("Lets continue")
                            engine.runAndWait()
#                            import order_generation
                            flag1 = 0
                            while(flag1!="1"):
                                print("Are you vegetarian or non vegetarian")
                                engine.say("Are you vegetarian or non vegetarian")
                                engine.runAndWait()
                                reply = recorddata()
                                if(reply =="vegetarian"):
                                    flag1=1
                                    print("Thank you ... you are vegetarian")
                                    engine.say("Thank you ... you are vegetarian")
                                    engine.runAndWait()
                                    engine.say("Todays Offers")
                                    engine.runAndWait()
                                    print("Todays offer")
                                    sql="SELECT * FROM veg_offers"
                                    cursor.execute(sql)
                                    myresult = cursor.fetchall()
                                    count=1
                                    for x in myresult:
                                        engine.say("{}  for {} in in  {} rupees".format(count,x[0],x[1]))
                                        engine.runAndWait()
                                        print(x[0])
                                        print(x[1])
                                        count=count+1
                                        time.sleep(2)
                                    engine.say("Do you want to buy from menu ")
                                    engine.runAndWait()
                                    reply=recorddata()
                                    if(reply =="yes" or reply=="ya" or reply=="yes yes" or reply=="ok" or reply=="yaah"):
                                        engine.say("Veg  menu")
                                        engine.runAndWait()
                                        time.sleep(2) 
                                        sql="SELECT * FROM veg_menu"
                                        cursor.execute(sql)
                                        myresult = cursor.fetchall()
                                        count=1
                                        for x in myresult:
                                            engine.say("{}  for {} in in  {} rupees".format(count,x[0],x[1]))
                                            engine.runAndWait()
                                            print(x[0])
                                            print(x[1])
                                            count=count+1
                                            time.sleep(2)
                                        stopwhile=0  
                                        d={}  
                                        while(stopwhile==0):
                                            engine.say("which product do you want to buy? One at a time")
                                            engine.runAndWait()
                                            engine.say(" please tell product number")
                                            engine.runAndWait()
                                            reply1 = recorddata()
                                            if(reply1 == "1" or reply1 == "one" or reply1 =="one one" or reply1 =="11" or reply1=="van"):
                                                reply1=1
                                            elif(reply1 == "2" or reply1 == "two" or reply1 =="22" or reply1 == "Tu" or reply1 =="tu tu" or reply1=="two two" or reply1 =="true"):
                                                reply1=2
                                            elif(reply1 == "3" or reply1 == "three" or reply1 == "33" or reply1=="three three" ):
                                                reply1=3   
                                            engine.say("how many quantity:")
                                            engine.runAndWait()
                                            reply2 = recorddata()
                                            if(reply2 == "1" or reply2 == "one" or reply2 =="one one" or reply2 =="11" or reply2 =="van"):
                                                reply2=1
                                            elif(reply2 == "2" or reply2 == "two" or reply2 =="22" or reply2 == "Tu" or reply2 =="tu tu" or reply2=="two two" or reply2 =="true"):
                                                reply2=2
                                            elif(reply2 == "3" or reply2 == "three" or reply2 == "33" or reply2=="three three" ):
                                                reply2=3  
                                            flag2 = 0
                                            
                                            sql="SELECT * FROM veg_menu"
                                            cursor.execute(sql)
                                            myresult = cursor.fetchall()
                                            print("hii")
                                            if(isinstance(reply1, int) and  isinstance(reply2, int) and reply1 < count+1 ):
                                                print("hii2")
                                                keys =  myresult[reply1-1]
                                                d[keys] = reply2
                                            else:
                                                engine.say("sorry , not understand ")
                                                engine.runAndWait()
                                                continue
                                                
                                            
                                            chkreply = 0
                                            while(chkreply!=1):
                                                engine.say(" do you want to buy other things ?")
                                                engine.runAndWait()
                                                reply = recorddata()
                                                if(reply == "yes" or reply == "confirm" or reply =="ya" or reply == "yes yes"):
                                                    stopwhile = 0
                                                    chkreply=1
                                                elif(reply=="no" or reply =="no no" or reply == "not"):
                                                    stopwhile = 1
                                                    chkreply=1
                                                    sum = 0
                                                    for key,val in d.items():
                                                        print (key, "=>", val)
                                                        sum = sum + int(val)
                                                    engine.say("your total bill is {} rupees ".format(sum))
                                                    engine.runAndWait()    
                                                    print("your total bill is {} rupees ".format(sum))
                                                    engine.say("please pay the bill to the counter")
                                                    engine.runAndWait() 
                                                    print("please pay bills to the counter")   
                                                        
                                                else:
                                                    engine.say("not understand")
                                                    engine.runAndWait()
                                                    engine.say("please say again")
                                                    engine.runAndWait()
                                                    chkreply=0
                                                     
                                                           
                                            
                            usr_choice = 1
                            flag=1
                        elif(reply == "no"):
                            engine.say("Ok")
                            engine.runAndWait()
                            usr_choice = 0
                        else:
                            engine.say("sorry not understand . Please Say again")
                            usr_choice = 0
                    
                elif(mode_choice == "2" or mode_choice == "two" or mode_choice =="22" or mode_choice == "Tu" or mode_choice =="tu tu" or mode_choice=="two two" or mode_choice =="true"):
                    usr_choice =0
                    while(usr_choice != 1):   
                        engine.say("Your choice is Two")
                        engine.runAndWait()
                        engine.say("Should I confirm ?")
                        engine.runAndWait()
                        reply=recorddata()
                        if(reply == "yes" or reply == "confirm" or reply =="ya" or reply == "yes yes"):
                            engine.say("Lets continue")
                            engine.runAndWait()
                            webbrowser.open('file://' + os.path.realpath("C:/Users/saurabh/Desktop/python/file1.html"))
                            usr_choice = 1
                            flag=1
                            mainflag=1
                        elif(reply == "no"):
                            engine.say("Ok")
                            engine.runAndWait()
                            usr_choice = 0
                        else:
                            engine.say("sorry not understand . Please Say again")
                            usr_choice = 0
                elif(mode_choice == "3" or mode_choice == "three" or mode_choice == "33" or mode_choice=="three three" or mode_choice=="free" ):
                    usr_choice=0
                    while( usr_choice!= 1): 
                        engine.say("Your choice is Three")
                        engine.runAndWait()
                        engine.say("Should I confirm ?")
                        engine.runAndWait()
                        reply=recorddata()
                        if(reply == "yes" or reply == "confirm" or reply =="ya" or reply == "yes yes"):
                            engine.say("Lets continue")
                            engine.runAndWait()
                            usr_choice= 1
                            flag=1
                        elif(reply == "no"):
                            engine.say("Ok")
                            engine.runAndWait()
                            usr_choice= 0
                        else:
                            engine.say("sorry not understand . Please Say again")
                            usr_choice= 0
                else:
                    engine.say("sorry, I am not understand")
                    engine.runAndWait()  
                    engine.say("please say again")
                    engine.runAndWait()
                    flag=0
                                   
        elif(user_sound == 'no' ):
            engine.say("okay , thank you for conversation")
            mainflag = 1
        else:
            engine.say("Sorry ,not understand")
            engine.runAndWait() 
            mainflag = 1      
except sr.WaitTimeoutError as e:
        print("Timeout; {0}".format(e))
#except sr.UnknownValueError:
#    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))              
except:
    print("error")
    engine.say("Sorry ,Something Went wrong")
    engine.runAndWait()
    mainflag = 1    