import marshal
fp=open("marshal2..py.txt","rb")
data=marshal.load(fp)
exec(data)