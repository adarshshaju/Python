
class PasswordMartix():
    def encryption(self,password):
        passChar = []
        passLen = len(password)
        encrypted_password = ""

        for letter in password:
            passChar.append(letter)

        # 33 to 40 are special value and 40 to 254 are common values 
        for i in range(len(passChar)):
            format = [ord(passChar[i])+(2+passLen),
                      (ord(passChar[i])*2)//passLen,
                      ord(passChar[i])+(5-passLen),
                      ord(passChar[i])-3,
                      ord(passChar[i])+passLen,]
            
            if (format[0]<40 or format[0]>254):
                format[0]=33
            if (format[1]<40 or format[1]>254):
                format[1]=34
            if (format[2]<40 or format[2]>254):
                format[2]=35
            if (format[3]<40 or format[3]>254):
                format[3]=36
            if (format[4]<40 or format[4]>254):
                format[4]=37

            encrypted_chars=chr(format[0])+chr(format[1])+chr(format[2])+chr(format[3])+chr(format[4])
            encrypted_password+=encrypted_chars

        return encrypted_password
    
    def decryption(self, password):
        en_pass_lst=[]
        passCount=0
        rangeCount=len(password)//5
        de_password=""

        for i in range(rangeCount):
            en_pass_lst.append(password[passCount]+password[passCount+1]+password[passCount+2]+password[passCount+3]+password[passCount+4])
            passCount=passCount+5

        for i in range(len(en_pass_lst)):
            enPassChar=en_pass_lst[i]

            format = [ord(enPassChar[0])-(2+rangeCount),
                    (ord(enPassChar[1])*rangeCount)//2,
                    ord(enPassChar[2])-(5-rangeCount),
                    ord(enPassChar[3])+3,
                    ord(enPassChar[4])-rangeCount,]
            
            if ((format[0]==format[1]) or (format[0]==format[2]) or (format[0]==format[3]) or (format[0]==format[4]) or 
                (format[1]==format[2]) or (format[1]==format[3]) or (format[1]==format[4]) or
                (format[2]==format[3]) or (format[2]==format[4]) or (format[3]==format[4])):
                dePassChar=chr(format[0])
                de_password+=dePassChar
            else:
                print("Error in decryption")
        
        return de_password
    
