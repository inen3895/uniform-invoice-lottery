"""
f=open('中獎號碼.txt')
text=f.read()
win=text.split()
print(win)
以上可簡化寫成如下
"""
count = 0
value = 0
win=open('中獎號碼.txt').read().split()
mine=open('我的發票.txt').read().split()
# print(win,mine)
for i, num in enumerate(mine):
    if num in win:
        count+=1
        value+=200 # 假設每張中獎可得200元
        print('第', i+1, '張發票對中', num, '!')

print('中了', count, '張發票！')
print('共', value, '元！')


