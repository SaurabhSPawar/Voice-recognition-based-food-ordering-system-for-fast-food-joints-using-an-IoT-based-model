import pygame
from urllib.request import urlopen
#open url for internet check
import speech_recognition as spr
#speech  to text library
import pyttsx3
#text to speech library
from playsound import playsound
#use to play any sound
import time
from django.template.defaultfilters import lower
# use for time 

import pymysql

pygame.init()
display_width = 800
display_height = 600 
black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0) 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GUI Speech Recognition') 
gameDisplay.fill(white)
carImg = pygame.image.load('img.jpg')
gameDisplay.blit(carImg,(0,0)) 
def close():
    pygame.quit() 
    quit() 
def message_display(text):
    gameDisplay.blit(carImg,(0,0))
    largeText = pygame.font.Font('freesansbold.ttf',30) 
    TextSurf, TextRect = text_objects(text, largeText) 
    TextRect.center = ((display_width/2),(display_height/2)) 
    gameDisplay.blit(TextSurf, TextRect) 
    pygame.display.update() 
def text_objects(text, font):
    textSurface = font.render(text, True, alpha) 
    return textSurface, textSurface.get_rect()


db = pymysql.connect("localhost","root","","hoteldb" )
chatbot = pymysql.connect("localhost","root","","chatbot" )
cursor = db.cursor()
cursor1 = chatbot.cursor()
def  recorddata():
    print(" listening ....")
    message_display("listening start in 2 sec....")
    with spr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sound = r.listen(source, timeout=9,phrase_time_limit=9)
            print("Time Over")
            playsound('bell.mp3')
            time.sleep(1)
            print("Text:"+r.recognize_google(sound))
    mode_choice = r.recognize_google(sound)
    mode_choice1 = lower(mode_choice)
    message_display("Text  :"+mode_choice1)
    return mode_choice1
def verify_prod(product):
    product = lower(product)
    if( product =="mac alu tikki" or product == "mcaloo tikki" or product =="aloo tikki"or product =="map aloo tikki" or product == "mat aloo tikki" or product == "make aloo tikki" or product=="tikki" or product=="mac aloo tikki" or product == "101" or product == " one zero one" ):
        product = 'mctikki'
        price = 29
        return price,product
    elif(product == "mac float"  or product=="Mac fruit" or product == "make fruit" or product == "mcfloat" or product== "mc float" or product=="map float" or product == "coklat" or product=="plot"or product== "coke float" or product=="make float" or product == "float" or product == "one zero two" or product == "one zero tu " or product == "102" ):
        product = 'mcfloat'
        price = 25
        return price,product
    elif(product == "mac veggie" or product =="bheji"or  product == "mcveggie" or product == "make veggie" or product == "103" or product == " one zero three" ):
        product ='mcveggie'
        price = 40
        return price,product
    elif(product == "mac chicken"  or product == "mcchicken" or product=="chicken" or product=="mat chicken" or product == "make chicken" or product == "104" or product == "one zero four" ):
        product ='mcchicken'
        price = 80
        return price,product
    elif( product == "maharaja mac" or product =="map maharaja" or product == "maharaja mac" or product == "maharaja" or product == "mac maharaja"or product =="mc maharaja" or product == "raja" or product == "105" or product == "one zero  five" ):
        product = 'maharaja mc'
        price = 100
        return price,product
    else:
        price=0
        product='0'
        return price,product 
def number_ck(number):
    number = lower(number)
    if(number =="1" or number == "one" or number =="on" or number =="van" or number =="world"):
        return 1
    elif(number == "2" or number =="two" or number == "tu" or number == "to" or number =="too" or number=="true"):
        return 2
    elif(number == "3" or number == "three" or number == "tree" or number == "tri" or number =="free"):
        return 3
    elif(number == "4" or number =="four" or number == "for" or number == "favr" or number =="aur"):
        return 4
    elif( number == "5" or number=="five" or number =="fai"):
        return 5
    else:
        return number
def is_internet_available():
    try:
        urlopen('http://216.58.192.142', timeout=5)
        return True
    except:
        return False
    
    
def datamine(strings):
    try:
        strings= strings.lower()
        data = strings.split()
        size = len(data)
        i = b = 0 
        while(b == 0):
            sql = "SELECT * FROM `solutions` WHERE `question` = %s"
            cursor1.execute(sql,(data[i]))
            result_arr = cursor1.fetchall()
            if(len(result_arr) == 0):
                if(i<size):
                    i=i+1
                    if i<len(data):
                        b = 0
                        continue
                    else:
                        print("sorry I can't understand")
                        engine.say("sorry I can't understand")
                        engine.runAndWait()
                        return None                
            y=0
            while(y == 0):
                if(result_arr[0][3] == 1 or result_arr[0][3] == "1"):
                    answer = result_arr[0][2]
                    print(answer)
                    engine.say(answer)
                    engine.runAndWait()
                    if(i<size-1):
                        i=i+1
                        if i<len(data):
                            b=0
                            y=1                        
                    else:
                        b=1
                        y=1                                   
                if(result_arr[0][3]==2):
                    if(i<size):
                        x=0
                        while(x==0):
                            i=i+1
                            if i < len(data):
                                new_string = result_arr[0][2]
                                #print(new_string)
                                sql="{} WHERE `question` = \"{}\"".format(new_string,data[i])
                                #print(sql)
                                cursor1.execute(sql)
                                result_arr = cursor1.fetchall()
                                if len(result_arr) == 0:
                                    x=0
                                else:
                                    x=1
                                    y=0                                                                                                                      
                            else:
                                print("sorry not understand")  
                                engine.say("sorry not understand")
                                engine.runAndWait() 
                                return 0 
    except:
        print("sorry I can't understand")  
        engine.say("sorry I can't understand")
        engine.runAndWait()
gameDisplay.blit(carImg,(0,0))                                                                  
engine = pyttsx3.init()
engine.setProperty('rate', 170)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)
r = spr.Recognizer()
r.pause_threshold = 0.6
microphone = spr.Microphone()
print(is_internet_available())
if(is_internet_available()!=True):
    pygame.display.update()
    message_display("Internet is so slow")
    engine.say("Internet is so slow")
    engine.runAndWait()
else:
    playsound('bell.mp3')
    time.sleep(1)
pygame.display.update()
message_display("welcome")        
engine.say("Welcome")
engine.runAndWait()
time.sleep(2)
usr_choice = 1
flag=1
nu1 = 0
while(nu1 != 1 ):
    with spr.Microphone() as source:
        message_display("Do you want to continue ?") 
        engine.say("Do you want to continue ?")
        engine.runAndWait()
        #print("Do you want to continue ?")
        #print("listening.... ")
        message_display("Listening")
        r.adjust_for_ambient_noise(source)
        sound = r.listen(source, timeout=9,phrase_time_limit=9)
        playsound('bell.mp3')
        time.sleep(1)
        engine.say("ok")
        message_display("ok")
        engine.runAndWait()
        #print("ok")
    try:
        #print("Text"+r.recognize_google(sound))
        user_sound = r.recognize_google(sound)
        message_display("Text"+user_sound)
        if(user_sound == "yes" or user_sound == "ya" or user_sound == "yes yes" or user_sound=="yash" or user_sound=="s"):
            nu2 = 0
            productlist = []
            while(nu2 != 1):
                message_display("which product do you want to buy")
                #print("which product do you want to buy , please say product code or product name:")
                engine.say("which product do you want to buy , please say product code or product name")
                engine.runAndWait()
                product = recorddata()
                price , product = verify_prod(product)
                #print("test")
                #print(price)
                #print(product)
                #print("\n")
                if(price != 0):
                    print("test")
                    x="product verified product price is"
                    y = x+ str(price)
                    print(y)
                    message_display(y)
                    #print("product verified product price is",price)
                    engine.say(x)
                    engine.runAndWait()
                    engine.say(price)
                    engine.runAndWait()
                    message_display("how much quantity")
                    engine.say("how much quantity")
                    engine.runAndWait()
                    quantity1 = recorddata()
                    quantity = number_ck(quantity1)
                    #quantity check if else not added 
                    nu2=1                    
                    nu3 = 0
                    while(nu3 != 1):
                        message_display("Do you want to confirm")
                        print("Do you want to confirm")
                        engine.say("Do you want to confirm")
                        engine.runAndWait() 
                        confirm_dic1=recorddata()
                        if(confirm_dic1 == "yes" or confirm_dic1 == "yes yes" or confirm_dic1 == "ya"):
                            productlist.append(product)
                            productlist.append(price)
                            productlist.append(quantity)
                            message_display("Thank you ... do you want any more")
                            print("Thank you ... do you want any more")
                            engine.say("thank you do you want any more")
                            engine.runAndWait()
                            confirm_dic2=recorddata()
                            if(confirm_dic2=="yes"or confirm_dic2=="yes yes" or confirm_dic2=="ya"):
                                nu3=1
                                nu2=0
                            elif(confirm_dic2=="no" or confirm_dic2=="lo" or  confirm_dic2=="lo lo" or confirm_dic2=="nop" or confirm_dic2 == "no no" or confirm_dic2 == "no lo" or confirm_dic2 == "lo no"):
                                nu3=1
                                nu2=1
                                list_size = len(productlist)
                                print(list_size)
                                if(list_size != 0):
                                    message_display("do you want to quit or discard process")
                                    print("do you want to quit or discard process")
                                    engine.say("do you want to quit or discard process")
                                    engine.runAndWait()
                                    confirm_dic3=recorddata()
                                    if(confirm_dic3=="yes" or confirm_dic3=="yes yes" or confirm_dic3=="ya"):
                                        message_display("thank you for visit")
                                        print("thank you for visit:")
                                        engine.say("thank you for visit")
                                        engine.runAndWait()
                                        nu1=1
                                        nu2=1
                                        nu3=1
                                        break
                                    else:
                                        sum1 = 0
                                        product_name=[]
                                        sum_price = 0
                                        print(list_size)
                                        for x in range(0,list_size, 3):
                                            product_name.append(productlist[x])
                                            sum1 = sum1 + (productlist[x+1] * productlist[x+2])
                                        message_display("product list is")
                                        print("Product list is")
                                        engine.say("Product list is")
                                        engine.runAndWait()
                                        gameDisplay.blit(carImg,(0,0))
                                        l = 0
                                        for x in product_name:
                                            largeText = pygame.font.Font('freesansbold.ttf',30) 
                                            TextSurf, TextRect = text_objects(x, largeText) 
                                            TextRect.center = ((display_width/2),(display_height/2)+l) 
                                            gameDisplay.blit(TextSurf, TextRect) 
                                            pygame.display.update()
                                            print(x)
                                            engine.say(x)
                                            engine.runAndWait()
                                            l=l+100
                                            time.sleep(1)    
                                        message_display("total amount is :"+str(sum1))   
                                        print("total amount is")
                                        print(sum1)    
                                        engine.say("total amount is")
                                        engine.runAndWait()
                                        engine.say(sum1)
                                        engine.runAndWait()
                                        message_display("confirm all the products") 
                                        print("confirm all products")
                                        engine.say("confirm all the product")
                                        engine.runAndWait()
                                        confirm_dic4  = recorddata()
                                        if(confirm_dic4 == "yes" or confirm_dic4 == "yes yes" or confirm_dic4 =="yup"):
                                            message_display("thank you")
                                            print("thank you")
                                            engine.say("thank you")
                                            engine.runAndWait()
                                            
                                            string1=''
                                           
                                            for x in product_name:
                                                string1 =string1 + ' ,' + x
                                            print(string1)
                                            statusflag = 0 
                                            sql = "INSERT INTO `order_list` (`product_list`, `amount`, `status`) VALUES (%s, %s, %s)" 
                                            cursor.execute(sql, (string1, sum1, statusflag ))
                                            #flag = cursor.execute("INSERT INTO order_list (product_list, amount, status) VALUES(%s, %s, %s)", (string1, sum1, statusflag))   
                                            db.commit()
                                            time.sleep(3)
                                            cursor.execute("SELECT max(`order_key`) FROM `order_list`")
                                            token_no = cursor.fetchall()
                                            if(flag == True):
                                                message_display("order list inserted successfully")
                                                print("order list inserted successfully")
                                                engine.say("order list inserted successfully")
                                                engine.runAndWait()
                                                x= "your token is:"+str(token_no)
                                                message_display(x)
                                                engine.say("your token is :")
                                                engine.runAndWait()
                                                engine.say(token_no)
                                                engine.runAndWait()
                                                print("your token number is : %s",token_no)
                                            
                                            else:
                                                message_display("sorry not inserted")
                                                print("sorry not inserted")    
                                        elif(confirm_dic4 == "no" or confirm_dic4 == "9 no" or confirm_dic4 == "no no" or confirm_dic4 == "nop" or confirm_dic4=="lo" or confirm_dic4 =="lo lo" or confirm_dic4=="no lo" or confirm_dic4 =="lo no"):
                                            #print("hii")
                                            loop = 0
                                            while(loop!=1):
                                                print("select mode \n 1.delete product from cart \n 2. edit product \n 3. discard all product and end \n ")
                                                
                                                x="select mode : say one for delete product from cart"
                                                gameDisplay.blit(carImg,(0,0))
                                                largeText = pygame.font.Font('freesansbold.ttf',30) 
                                                TextSurf, TextRect = text_objects(x, largeText) 
                                                TextRect.center = ((display_width/2),(display_height/2)) 
                                                gameDisplay.blit(TextSurf, TextRect) 
                                                pygame.display.update()
                                                engine.say("select mode:")
                                                engine.runAndWait() 
                                                engine.say("say one for delete product from cart ")
                                                engine.runAndWait()  
                                                x=" : say two for edit product from cart"
                                                largeText = pygame.font.Font('freesansbold.ttf',30) 
                                                TextSurf, TextRect = text_objects(x, largeText) 
                                                TextRect.center = ((display_width/2),(display_height/2)+100) 
                                                gameDisplay.blit(TextSurf, TextRect) 
                                                pygame.display.update()
                                                engine.say("say two for edit product")
                                                engine.runAndWait()
                                                x=" : say three for discard all product from cart"
                                                largeText = pygame.font.Font('freesansbold.ttf',30) 
                                                TextSurf, TextRect = text_objects(x, largeText) 
                                                TextRect.center = ((display_width/2),(display_height/2)+200) 
                                                gameDisplay.blit(TextSurf, TextRect) 
                                                pygame.display.update()
                                                engine.say("say three for  discard all product and exit")
                                                engine.runAndWait()
                                                number1 = recorddata()
                                                confirm_dic5 = number_ck(number1)
                                                print(confirm_dic5)
                                                if(confirm_dic5 == "one" or confirm_dic5 == 1 or confirm_dic5 == "1"):
                                                    nock = 0
                                                    while(nock!=1):
                                                        print("ck1")
                                                        message_display("which product you want to delete")
                                                        print("which product you want to delete")
                                                        engine.say("which product you want to delete")
                                                        engine.runAndWait()
                                                        product2 = recorddata()
                                                        price3,product3 = verify_prod(product2)
                                                        if(price !=0):
                                                            #print("ck1")
                                                            product_list_no = productlist.index(product3)
                                                            #print("ck2 :product_list_no",product_list_no)
                                                            product_name_no = product_name.index(product3)
                                                            #print("ck3: product_name_no",product_name_no)
                                                            product_quantity =productlist[product_list_no+2]
                                                            #print("ck4 :product_quantity ",product_quantity)
                                                            old_price = product_quantity * price3
                                                            message_display("old price"+str(old_price))
                                                            print("old_price",old_price)
                                                            sum1 = sum1 - old_price
                                                            #print("ck5: ")
                                                            productlist.pop(product_list_no+2)  
                                                            #print("ck6")
                                                            productlist.pop(product_list_no + 1)
                                                            productlist.pop(product_list_no)
                                                            product_name.pop(product_name_no)
                                                            #print("ck7")
                                                            message_display("operation done successfully")
                                                            print("operation done successfully")
                                                            engine.say("operation done successfully")
                                                            engine.runAndWait()
                                                            message_display("new product list will be")
                                                            engine.say("new product list will be")
                                                            engine.runAndWait()
                                                            string1=''
                                                            l=0
                                                            for x in product_name:
                                                                largeText = pygame.font.Font('freesansbold.ttf',30) 
                                                                TextSurf, TextRect = text_objects(x, largeText) 
                                                                TextRect.center = ((display_width/2),(display_height/2)+l) 
                                                                gameDisplay.blit(TextSurf, TextRect) 
                                                                pygame.display.update()
                                                                print(x)
                                                                string1 =string1 + ' ,' + x
                                                                engine.say(x)
                                                                engine.runAndWait()
                                                                l=l+100
                                                                time.sleep(1)    
                                                            message_display("total cost is"+str(sum1))   
                                                            print("total cost is")    
                                                            engine.say("total cast is")
                                                            engine.runAndWait()
                                                            print(sum1)
                                                            engine.say(sum1)
                                                            engine.runAndWait()
                                                            message_display("so, do you want to confirm")
                                                            engine.say("so, do you want to confirm")
                                                            engine.runAndWait()
                                                            confirm_dic6 = recorddata()
                                                            if(confirm_dic6 == "yes" or confirm_dic6 =="yes yes" or confirm_dic6 == "ya"):
                                                                message_display("thank you")
                                                                print("thank you")
                                                                engine.say("thank you")
                                                                engine.runAndWait()
                                                                print(string1)
                                                                statusflag = 0 
                                                                sql = "INSERT INTO `order_list` (`product_list`, `amount`, `status`) VALUES (%s, %s, %s)" 
                                                                flagc=cursor.execute(sql, (string1, sum1, statusflag ))
                                                                #flag = cursor.execute("INSERT INTO order_list (product_list, amount, status) VALUES(%s, %s, %s)", (string1, sum1, statusflag))   
                                                                db.commit()
                                                                time.sleep(3)
                                                                cursor.execute("SELECT max(`order_key`) FROM `order_list`")
                                                                token_no = cursor.fetchall()
                                                                if(flagc == True):
                                                                    message_display("order list inserted successfully")
                                                                    print("order list is inserted successfully ")
                                                                    engine.say("order list is inserted successfully ")
                                                                    engine.runAndWait()
                                                                    message_display("your token number is "+str(token_no))
                                                                    print("your token number is : %s",token_no)
                                                                    engine.say("your token number is ")
                                                                    engine.runAndWait()
                                                                    engine.say(token_no)
                                                                    engine.runAndWait()
                                                                loop =  1
                                                                nock = 1
                                                            else:
                                                                loop= 0 
                                                        else:
                                                            nock = 0  
                                                            datamine(product2)
                                                            #print("sorry not understand")
                                                            #engine.say("sorry not understand")
                                                            #engine.runAndWait()                                                                 
                                                elif(confirm_dic5 == "two" or confirm_dic5 == 2 or confirm_dic5 == "2"):
                                                    nock2=0
                                                    while(nock2!=1):
                                                        message_display("which product you want to edit")    
                                                        print("which product quantity you want to edit")
                                                        engine.say("which product quantity you want to edit")
                                                        engine.runAndWait()
                                                        product = recorddata()
                                                        price,product = verify_prod(product)
                                                    
                                                        if(price != 0):
                                                            nock2=1  
                                                            message_display("how much quantity you want to set")  
                                                            print("how much quantity you want to set")
                                                            engine.say("how much quantity you want to set")
                                                            engine.runAndWait()
                                                            number5 = recorddata()
                                                            new_quantity = number_ck(number5)
                                                           
                                                            new_set_price = new_quantity*price
                                                            product_index = productlist.index(product)
                                                            old_quantity = productlist[product_index+2]  
                                                            old_set_quantity=old_quantity*price 
                                                            sum1 = sum1- old_set_quantity + new_set_price
                                                            message_display("new price is :"+str(sum1))
                                                            print("new price is")
                                                            engine.say("new price is:")
                                                            engine.runAndWait()
                                                            print(sum1)
                                                            engine.say(sum1)
                                                            engine.runAndWait()
                                                            string1=''
                                           
                                                            for x in product_name:
                                                                string1 =string1 + ' ,' + x
                                                            message_display(string1)    
                                                            print(string1)
                                                            statusflag = 0 
                                                            sql = "INSERT INTO `order_list` (`product_list`, `amount`, `status`) VALUES (%s, %s, %s)" 
                                                            flag1=cursor.execute(sql, (string1, sum1, statusflag ))
                                                            #flag = cursor.execute("INSERT INTO order_list (product_list, amount, status) VALUES(%s, %s, %s)", (string1, sum1, statusflag))   
                                                            db.commit()
                                                            time.sleep(3)
                                                            cursor.execute("SELECT max(`order_key`) FROM `order_list`")
                                                            token_no = cursor.fetchall()
                                                            
                                                            if(flag1==True):
                                                                message_display("data inserted successfully")
                                                                print("data inserted successfully")
                                                                engine.say("data inserted successfully")
                                                                engine.runAndWait()
                                                                message_display("your token number is"+str(token_no))
                                                                engine.say("your token number is")
                                                                engine.runAndWait()
                                                                engine.say(token_no)
                                                                engine.runAndWait()
                                                                
                                                            loop =1
                                                        else:
                                                            datamine(product)
                                                            #print("sorry not understand")
                                                            #engine.say("sorry not understand")
                                                            #engine.runAndWait()  
                                                            nock2=0  
                                                elif(confirm_dic5 == "three" or confirm_dic5 == 3 or confirm_dic5 =="3"):
                                                    message_display("exiting whole process")
                                                    engine.say("exiting whole process")
                                                    engine.runAndWait()
                                                    loop = 1
                                                    nu3=1
                                                    nu2=1
                                                    nu1=1
                                                    message_display("thank you for visit:")
                                                    engine.say("thank you for visit")
                                                    engine.runAndWait()
                                                    close()
                                                    break
                                                    
                                                    
                                                            
                                                        
                                                else:
                                                    datamine(confirm_dic5)
                                                    #print("sorry not understand")
                                                    #engine.say("sorry not understand")
                                                    #engine.runAndWait() 
                                                    loop = 0      
                                                             
                                                      
                                                
                                else:
                                    message_display("you selected none .. Thank you for visit")
                                    print("you selected none .. Thank you for visit")
                                    engine.say("you selected none and Thank you for visit")
                                    engine.runAndWait()
                            else:
                                datamine(confirm_dic2)
                                #print("sorry please say again")
                                #engine.say("sorry please say again")
                                #engine.runAndWait()    
                        elif(confirm_dic1 == "no" or confirm_dic1 == "nop" or confirm_dic1=="no lo" or confirm_dic1=="lo" or confirm_dic1=="lo lo"  or confirm_dic1=="lo no"):
                            #discard this product remaining
                            message_display("say another one")
                            print("say another one")
                            engine.say("say another one")
                            engine.runAndWait()               
                            nu2=0 
                            nu3=1       
                        else:
                            datamine(confirm_dic1)
                            #print("sorry please say again")
                            #engine.say("sorry please say again")
                            #engine.runAndWait() 
                            nu3 =0
                else:
                    datamine(product)
                    #print("sorry not understand please say again")
                    #engine.say("sorry not understand please say again")
                    #engine.runAndWait()
                    nu2=0
            break        
        elif(user_sound == "no" or user_sound == "nop" or user_sound == "no no" ):
            message_display("thank you for visit:")
            print("thank you for visit:")
            engine.say("thank you for visit:")
            engine.runAndWait()
            break
        else:
            #print("ck1")
            datamine(user_sound)
            
            #print("sorry,I am not understand")  
            #engine.say("Not understand")
            #engine.runAndWait()
            continue 
    except:
        message_display("error")
        print("error")
        engine.say("Sorry ,Something Went wrong... System restart again")
        engine.runAndWait()
        continue