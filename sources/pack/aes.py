import Crypto.Cipher.AES as AES
import Crypto.Util.Padding as PAD
import tkinter
from tkinter import messagebox
import json
from collections import OrderedDict
import pprint
import os

def read_key():
    from pack import key
    return key.key1["key1"]

def encrypt(ptext):
    key=read_key()
    #key=gen_key()
    key=bytes(key,encoding="utf-8")
    iv = b'0' * 16
    aes = AES.new(key, AES.MODE_CBC, iv)
    data1 = PAD.pad(ptext.encode('ascii'), 16, 'pkcs7')
    cipher = aes.encrypt(data1)
    return cipher

def crypto_text_to_hex(src_text, key):
    if src_text and key:
        xor_code = key
        # keyが短い場合は、繰り返して必要バイト数を準備する
        while len(src_text) > len(xor_code):
            xor_code += key
        return "".join([chr(ord(data) ^ ord(code))
                        for (data, code) in zip(src_text, xor_code)]).encode().hex()

# 複号：引数のHex文字列とkeyをXORして戻した文字列で返す
# hex_text=暗号化されているhex文字列
# key=複号するためのキー文字列
def decrypto_hex_to_text(hex_text, key):
    if hex_text and key:
        try:
            crypt_data = bytes.fromhex(hex_text).decode()
        except ValueError:
            crypt_data = None

        if crypt_data:
            xor_code = key
            # keyが短い場合は、繰り返して必要バイト数を準備する
            while len(crypt_data) > len(xor_code):
                xor_code += key
            return "".join([chr(ord(data) ^ ord(code))
                            for (data, code) in zip(crypt_data, xor_code)])