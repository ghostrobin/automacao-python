import pyautogui
import pyperclip
import time

#vamos em primeiro momento fracionar nosso projeto.
#automatizando envio de email pelo google chrome
# - abrir navegador (clique no icone da barra de tarefas)*,
# - direcionar para gmail (enter)*
# - clicar em escrever* 
# - colocar destinatario (e apertar tab)*
# - colocar assunto (e apertar tab)*
# - corpo da mensagem (e apertar tab)*
# - envio da mensagem (ctrl+enter)
# - fechar navegador (alt+f4)

#abrir navegador (clique no icone da barra de tarefas)


assunto = 'desenvolvimento python, atraves da automacao'
mensagem = 'minha primeira automacao com python'

pyautogui.PAUSE = 3 

pyautogui.position(x=404, y=1061)
pyautogui.click(x=404, y=1061)
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('enter')
pyautogui.click(x=75, y=210)
pyperclip.copy('robmiranda.almeida@gmail.com')
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab')
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab')
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')
pyautogui.hotkey('alt','f4')









