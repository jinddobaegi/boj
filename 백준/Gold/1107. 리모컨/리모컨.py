import sys


def readLine():
  return sys.stdin.readline().rstrip()


def getPresCnt(channel, brBtn):
  n = len(brBtn)
  channelDigit = len(str(channel))
  cur = 100
  direct = abs(channel - cur)

  if n == 0:
    return min(channelDigit, direct)
  elif n == 10:
    return direct
  elif channel == 100:
    return 0
  else:
    return min(getPresCntBrBtn(channel, brBtn), direct)


def getPresCntBrBtn(channel, brBtn):
  availBtn = getAvailButton(brBtn)
  channelSplt = list(map(int, str(channel)))
  idx = -1
  for i, x in enumerate(channelSplt):
    if x in brBtn:
      idx = i
      break

  if idx == -1:
    return len(channelSplt)
  else:
    return getMinBtnCnt(channelSplt, idx, availBtn)


def getMinBtnCnt(channelSplt, spliter, availBtn):
  channel = int(''.join(map(str, channelSplt)))
  
  back = ''.join(map(str,channelSplt[spliter::]))
  digit = len(back) - 1
  
  minAvailBtn = str(min(availBtn))
  maxAvailBtn = str(max(availBtn))

  minAdd = ''
  maxAdd = ''
  for _ in range(digit):
    minAdd += minAvailBtn
    maxAdd += maxAvailBtn


  availNum = []
  
  
  
  if spliter == 0:
    front = ''
    mid = ''
    AvailBtnNoZero = list(filter(lambda x: x != 0, availBtn))
    if AvailBtnNoZero:
      minAvailBtnNoZero = min(AvailBtnNoZero)
      availNum.append(int(f'{minAvailBtnNoZero}{minAvailBtn}{minAdd}'))

    if digit != 0:
      availNum.append(int(maxAdd))

  elif spliter==1:
    front = ''.join(map(str,channelSplt[:spliter-1:]))
    mid = channelSplt[spliter-1]
    
    minAvailBtnUpMid = list(filter(lambda x: x>mid, availBtn))
    AvailBtnDwMid = list(filter(lambda x: x<mid, availBtn))
    AvailBtnDwMid.append(0)

    if minAvailBtnUpMid:
      minAvailBtnUpMid = min(minAvailBtnUpMid)
      availNum.append(int(f'{front}{minAvailBtnUpMid}{minAvailBtn}{minAdd}'))
      
    maxAvailBtnDwMid = max(AvailBtnDwMid)
    availNum.append(int(f'{front}{maxAvailBtnDwMid}{maxAvailBtn}{maxAdd}'))
    
  else:
    front = ''.join(map(str,channelSplt[:spliter-1:]))
    mid = channelSplt[spliter-1]    
    AvailBtnUpMid = list(filter(lambda x: x>mid, availBtn))
    AvailBtnDwMid = list(filter(lambda x: x<mid, availBtn))
    
    if AvailBtnUpMid:
      minAvailBtnUpMid = min(AvailBtnUpMid)
      availNum.append(int(f'{front}{minAvailBtnUpMid}{minAvailBtn}{minAdd}'))
    if AvailBtnDwMid:
      maxAvailBtnDwMid = max(AvailBtnDwMid)
      availNum.append(int(f'{front}{maxAvailBtnDwMid}{maxAvailBtn}{maxAdd}'))

  
  
  for i in availBtn:
    availNum.append(int(f'{front}{mid}{i}{minAdd}'))
    availNum.append(int(f'{front}{mid}{i}{maxAdd}'))

  minimum = abs(availNum[0]-channel)+len(str(availNum[0]))
  for i in availNum:
    tmp = abs(i-channel) +len(str(i))
    if tmp < minimum:
      minimum = tmp

  return minimum

  
def getAvailButton(brBtn):
  return list(filter(lambda x: (x not in brBtn), list(range(10))))


def main():
  channel = int(readLine())
  n = int(readLine())
  brBtn = set()
  if n != 0:
    brBtn = set(map(int, readLine().split()))

  answer = getPresCnt(channel, brBtn)
  print(answer)


if __name__ == "__main__":
  main()