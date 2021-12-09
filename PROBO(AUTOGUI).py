"""
Pyversion : python39
date : 2021-11-16
PROBO 매크로 프로그램 주의사항
> 대문자로 시작
> PROBO S/W종료 후 실행
> 모듈: pyautogui
"""

import pyautogui
import time

#프로세스 시작 알림
start_time = time.time()
print("Process Start")


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.3


#window창 실행하여 PROBO 검색 및 프로그램 실행
pyautogui.click(208,1414)
pyautogui.typewrite('PROBO')
pyautogui.press('enter')

#아이디, 비밀번호 입력하여 로그인
pyautogui.click(1227,702); pyautogui.typewrite('ecoadmin', interval = 0.1)
pyautogui.click(1276,785); pyautogui.typewrite('dionavi1234!@', interval = 0.1)
pyautogui.click(1277,895)

#로그인 실패 시 실행종료(추가예정)


#새 프로젝트 생성
time.sleep(2)
pyautogui.click(61,278, interval = 3)
pyautogui.click(1509,896)
pyautogui.typewrite('PROBO Test', interval = 0.1)
pyautogui.click(1501,1194)



##STL추가,복사 및 위치조정
pyautogui.click(2349,679); pyautogui.doubleClick(987,795)
time.sleep(3)
pyautogui.dragTo(435,691,0.4, button='left',)

pyautogui.click(2280,803)
pyautogui.doubleClick(495,750); time.sleep(2)
pyautogui.dragTo(1955,750,0.3, button='left')


#단계이동 및 STL동작
pyautogui.click(62,520); pyautogui.keyDown('shift')
pyautogui.click(2283,125); pyautogui.click(2283,185);pyautogui.keyUp('shift')

pyautogui.click(2377,800) #최소높이
pyautogui.click(2377,683, interval = 1) #상하반전


#서포트 생성 (서포트 생성동안 대기)
pyautogui.click(67, 627); pyautogui.click(2398,654)
pyautogui.press('enter',interval = 10)


#슬라이스 적용 및 확인
pyautogui.click(67,724)
pyautogui.click(2385,1318, interval = 12.5)

pyautogui.moveTo(2112,1281); pyautogui.dragTo(2112,39,3, button='left')


#저장 및 결과물생성
pyautogui.click(66,904, interval = 2)
pyautogui.press('enter',interval = 2)

pyautogui.click(66,1007)
pyautogui.click(2377,1325)

pyautogui.press('enter',interval =2)


#프로세스 종료 및 실행시간 표시
end_time = time.time()
print("Process End")
print("수행시간 : " + str(end_time - start_time) + " seconds")

#실행시간 표시 메세지박스
pyautogui.alert(title = '알림', text = "수행시간 : " + str(end_time - start_time) + " seconds", button='OK')


#for i in range(50):
#    pyautogui.moveTo(2136,1293)
#    pyautogui.scroll(200)
#    if i == 49:
#        break