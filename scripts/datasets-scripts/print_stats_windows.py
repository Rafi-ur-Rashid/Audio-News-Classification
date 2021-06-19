import win32com.client
sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)
ns = sh.NameSpace('C:\ML\audio_news\corpus\sports')
colnum = 0
columns = []

while True:
    colname=ns.GetDetailsOf(None, colnum)
    if not colname:
        break
    columns.append(colname)
    colnum += 1
    
item = ns.ParseName('700.m4a')
for colnum in range(len(columns)):
  colval=ns.GetDetailsOf(item, colnum)
  if colval:
      print('\t', colnum, columns[colnum], colval)