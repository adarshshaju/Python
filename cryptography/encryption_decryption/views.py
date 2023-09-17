from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.urls import reverse

from . import cryptography

class PasswordEncrypt(forms.Form):
    encrypt = forms.CharField(label="Enter your password to encrypt") 

class PasswordDecrypt(forms.Form):
    decrypt = forms.CharField(label="Enter your encrypted password to decrypt")

def encryption(request):
    if request.method == "POST":
        form = PasswordEncrypt(request.POST)
        if form.is_valid():
            encrypt = form.cleaned_data["encrypt"]
            request.session["encrypt"] = [encrypt]
            passwordMatrix=cryptography.PasswordMartix()
            encryptedPassword=passwordMatrix.encryption(encrypt)
            return HttpResponse(encryptedPassword)
        else:
            return render(request, "encryption_decryption/encrypt.html",{
                "form":form
            })

    return render(request, "encryption_decryption/encrypt.html",{
        "form":PasswordEncrypt
    })


def decryption(request):
    if request.method == "POST":
        form = PasswordDecrypt(request.POST)
        if form.is_valid():
            decrypt = form.cleaned_data["decrypt"]
            request.session["decrypt"] = [decrypt]
            passwordMatrix=cryptography.PasswordMartix()
            decryptedPassword=passwordMatrix.decryption(decrypt)
            return HttpResponse(decryptedPassword)
        else:
            return render(request, "encryption_decryption/decrypt.html",{
                "form":form
            })

    return render(request, "encryption_decryption/decrypt.html",{
        "form":PasswordDecrypt
    })