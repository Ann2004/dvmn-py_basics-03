import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

sender_address = os.getenv("EMAIL_LOGIN")
sender_password = os.getenv("EMAIL_PASSWORD")

recipient_address = "slob.anna2004@yandex.ru"
letter_header = "Приглашение!"
website_name = "https://dvmn.org/profession-ref-program/nyuta_aaa/ynOeN/"
friend_name = "Юля"
sender_name = "Слободчикова Анна"

letter = """\
From: {s_a}
To: {r_a}
Subject: {l_h}
Content-Type: text/plain; charset="UTF-8";

Привет, {f_n}! {s_n} приглашает тебя на сайт {w_n}!

{w_n} — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {w_n}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {w_n}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(s_a=sender_address,
r_a=recipient_address, l_h=letter_header, f_n=friend_name, s_n=sender_name, w_n=website_name)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(sender_address, sender_password)
server.sendmail(sender_address, recipient_address, letter)
server.quit()