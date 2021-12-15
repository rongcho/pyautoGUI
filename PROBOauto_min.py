"""
Pyversion : python39
date : 2021-11-19

PROBO 매크로 프로그램 주의사항
> 영문(소문자)로 변경
> PROBO 프로그램 시작 후 실행 + STL시 실행 할 파일들이 담긴 폴더로 경로 설정 필수
> 모듈: pyautogui
"""

import pyautogui
import time

#프로세스 시작 알림
start_time = time.time()
print("Process Start")


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.2

#정상 로그인

pyautogui.click(842,670, duration = 0.3); pyautogui.typewrite('<id>', interval = 0.1)
pyautogui.press('tab'); pyautogui.typewrite('<password>', interval = 0.1)
pyautogui.click(842,856, duration = 0.3)


#로그인 실패 시 프로그램 종료(추가 예정)



#새 프로젝트 생성
time.sleep(1.5)
pyautogui.click(61,278, duration = 0.3)
pyautogui.click(1038,840, duration = 0.3)
pyautogui.typewrite('PROBO_SG', interval = 0.1)
pyautogui.click(1015,1134, duration = 0.3)


#스크롤 속도조절
for i in range(5):
    pyautogui.PAUSE = False
    pyautogui.moveTo(679,692, duration = 0.4)
    pyautogui.scroll(100)
    if i == 5:
        break


#STL추가,복사 및 위치조정
time.sleep(1.5)
pyautogui.click(1365,649, duration = 0.3); time.sleep(2)
pyautogui.doubleClick(740,795, duration = 0.3); time.sleep(7)

pyautogui.dragTo(357,672,0.4, button='left',)

pyautogui.click(1310,771, duration = 0.4)
pyautogui.doubleClick(357,672); time.sleep(2)
pyautogui.dragTo(1114,665,0.4, button='left')


#단계이동 및 STL동작
pyautogui.click(76,526, duration = 0.4)

for i in range(5):
    pyautogui.PAUSE = False
    pyautogui.moveTo(679,692, duration = 0.3)
    pyautogui.scroll(-100)
    if i == 5:
        break
pyautogui.keyDown('shift')
pyautogui.click(1355,135,duration = 0.3); pyautogui.click(1355,185,duration = 0.5); pyautogui.keyUp('shift')

pyautogui.click(1389,763,duration = 0.4) #최소높이
pyautogui.click(1389,648,duration = 0.4, interval = 1) #상하반전



#서포트 생성 (서포트 생성동안 대기)
pyautogui.click(74, 630, duration = 0.3)
for i in range(5):
    pyautogui.PAUSE = False
    pyautogui.moveTo(679, 692, duration=0.3)
    pyautogui.scroll(-100)
    if i == 5:
        break
pyautogui.click(1390,622, duration = 0.4)
pyautogui.press('enter',interval = 10)


#슬라이스 적용 및 확인
pyautogui.click(74,735, duration = 0.5)
pyautogui.click(1414,1204, interval = 12.5, duration = 0.6)

pyautogui.moveTo(1141,1160, duration = 0.3); time.sleep(7);
pyautogui.dragTo(1141,41, 3, button='left')



#저장 및 결과물생성
pyautogui.click(79,909, interval = 2, duration = 0.5)
pyautogui.press('enter',interval = 2)

pyautogui.click(79,1025, duration = 0.5)
pyautogui.click(1410,1196, duration = 0.4)

pyautogui.press('enter',interval =2)


#프로세스 종료 및 실행시간 표시
end_time = time.time()
print("Process End")
print("수행시간 : " + str(end_time - start_time) + " seconds")

#실행시간 표시 메세지박스
pyautogui.alert(title = '알림', text = "수행시간 : " + str(end_time - start_time) + " seconds", button='OK')

