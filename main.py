#悪用厳禁。悪用したら殺します。
#娯楽機能は全削除済み。


#BerryBot 1.0


import requests
import webbrowser
import json
import re
import time
import ast
import random

maxlen = 100
isrm = 0
miase = input('session key:') #取得するコードを書いたら長くなり、可読性が下がるので割愛しました

webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=【BerryBot】")
admin = {'◆TensichanY':4} #権限リスト。ご自由に変更してください。権限レベルは3(権限持ち)、4(管理者レベル)があります。出禁を1、その他一般を2としています。
dekin = ['◆WBRXcNtpf.']

for yuik in range(1,50000,1):
  time.sleep(0.6)
  url = "https://zinro.net/m/api/?mode=message&id=1233268293"
  cookie = {'session_key':miase}
  res = requests.get(url,cookies=cookie)
  yui = res.text
  dat = json.loads(yui)
  data = str(dat)
  st = data.find("{'")
  st2 = data.find("'},")
  da = data[st:st2+2]
  mia = ast.literal_eval(da)
  url2 = "https://zinro.net/m/api/?mode=players"
  res2 = requests.get(url2,cookies=cookie)
  yui2 = res2.text
  dat2 = json.loads(yui2)
  kickdata = str(dat2)
  st3 = kickdata.find(": {'")
  st4 = kickdata.find("}},")
  da = kickdata[st3+2:st4+2]
  kickmia = ast.literal_eval(da)
  if mia['color'] != 'skyblue':
    araname = mia['from_user']
    val = kickmia[araname]

  if "入室しました" in mia['message']:
    if mia['color'] == "skyblue":
      y = mia['message']
      st3 = y.find("さんが")
      yuri = y[:st3]
      vall = kickmia[yuri]
      if vall['trip'] in dekin:
          gb2 = vall['id']
          url3 = "https://zinro.net/m/player.php?kick="+str(gb2)+"&name="+yuri
          webbrowser.open(url3)
          webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> "+yuri+"さんに自動キックが発動しました(出禁トリップ)")
      else:
         webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> "+yuri +"さん("+ vall['trip']+")よろしくー")
  
  if isrm == 0:     
    if "死ね" in mia['message'] or "カス" in mia['message'] or "bit.ly" in mia['message'] or len(mia['message']) >= 100:
      if mia['color'] != 'white' and mia['color'] != 'skyblue':
        if val['trip'] not in admin: 
          gb = val['id']
          url3 = "https://zinro.net/m/player.php?kick="+str(gb)+"&name="+araname
          webbrowser.open(url3)
          webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> "+araname+"さんに自動キックが発動しました(長文、禁止ワード検知)")
          dekin.append(val['trip'])
    if len(mia['message']) >= 100:
      if mia['color'] != 'white' and mia['color'] != 'skyblue':
        if admin[val['trip']] != 4:
         sk = mia['message']
         aco = sk.encode('unicode-escape')
         akk = str(aco)
         cou = akk.count('u30')
         if cou <= 20:
            gb = val['id']
            url3 = "https://zinro.net/m/player.php?kick="+str(gb)+"&name="+araname
            webbrowser.open(url3)
            webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> "+araname+"さんに自動キックが発動しました(マヨビ検知)")
            dekin.append(val['trip'])
          
    if mia['message'] == "stp":
      if mia['color'] == 'white' or admin[val['trip']] == 4:
        webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> 停止コマンドを発見、botを停止します!")
        break
    if '#maxlen' in mia['message']:
       if mia['color'] == 'white':
         mx = str(mia['message'])
         maxlen = int(mx[8:])
         webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user=ALL&message=<bot> 文字数制限を"+str(maxlen)+'文字に変更しました')

    if mia['message'] == '#info':
      if val['trip'] not in admin:
         lv = 2
      else:
         lv = admin[val['trip']]
      fu = mia['from_user']
      webbrowser.open("https://zinro.net/m/player.php?mode=message&to_user="+fu+"&message=<bot> あなたの権限レベルは、Lv."+str(lv)+"です。")
