from translate import Translator
import pyfiglet,termcolor
print ("\033[;092m")
T=pyfiglet.figlet_format ("TRANSLATOR")
print (T)
print ('\033[;094m')
print('■Projected By Abdullah Salah■')
print ()
print ('\033[;092m')
lan='''[1] From English To Arabic 

[2] From Arabic To English

[3] From English To france

[4] From French To English 

[5] From French To Arabic 

[6] From Arabic To French

[7] From Arabic To German

[8] From German To Arabic 

[9] From Arabic To Russian

[10] From Russian To Arabic

[11] From Arabic To Italian

[12] From Italian To Arabic 
'''
print (lan)
print ()
choose=input ('choose  :   ')
print ()
if choose=='1':
    translator= Translator(from_lang="english"
    ,to_lang="arabic")
    
    g=input (' Enter Word To Translate \033[;096m: ') 
    translation= translator.translate(g)
    print ('》'+translation)
    
elif choose=='2':
    translator2= Translator(from_lang="arabic",to_lang="english")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)

elif choose=='3':
    translator2= Translator(from_lang="english",to_lang="french")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)

elif choose=='4':
    translator2= Translator(from_lang="french",to_lang="english")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='5':
    translator2= Translator(from_lang="french",to_lang="arabic")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='6':
    translator2= Translator(from_lang="arabic",to_lang="french")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='7':
    translator2= Translator(from_lang="arabic",to_lang="german")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='8':
    translator2= Translator(from_lang="german",to_lang="arabic")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='9':
    translator2= Translator(from_lang="arabic",to_lang="russian")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='10':
    translator2= Translator(from_lang="russian",to_lang="arabic")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='11':
    translator2= Translator(from_lang="arabic",to_lang="italian")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)
elif choose=='12':
    translator2= Translator(from_lang="italian",to_lang="arabic")
    h=input (' Enter Word To Translate \033[;096m: ')    
    translation2= translator2.translate(h)
    print ('》'+translation2)

else :
    print ('\033[;091merror')

