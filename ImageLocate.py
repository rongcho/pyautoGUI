"""
Pyversion : 3.9.6
date : 2021-12-21

실행 시 주의사항
> Image폴더는 반드시 같은 경로에 위치
"""

import time
import pyautogui


#프로세스 시작
start_time = time.time()
print("=" * 100)
print("Process Start")
print("-" * 100)


#마우스를 0.0에 위치 시 강제종료
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 3


#캡처한 이미지를 비교하여 클릭 (이미지 찾기 실패 시 좌표값 미표시)
img_select = pyautogui.locateOnScreen('Image/select_case.png')
print("select case :" + str(img_select))
pyautogui.doubleClick(img_select, duration=0.5)
time.sleep(5)


#단계진입 및 하위메뉴 버튼 클릭
img_scanedit = pyautogui.locateOnScreen("Image/ScanEdit.PNG")
print("단계진입 : " + str(img_scanedit))
pyautogui.click(img_scanedit, duration=0.5)


img_occlusal = pyautogui.locateOnScreen("Image/Occlusal.PNG")
print("하위단계1 : " + str(img_occlusal))
pyautogui.click(img_occlusal, duration=0.5)

img_remscan = pyautogui.locateOnScreen("Image/scanrem.PNG")
print("하위단계2 : " + str(img_remscan))
pyautogui.click(img_remscan, duration=0.5)


img_scanknife = pyautogui.locateOnScreen("Image/scanknife.PNG")
print("하위단계3 : " + str(img_scanknife))
pyautogui.click(img_scanknife, duration=0.5)
img_scanknife_Upper = pyautogui.locateOnScreen("Image/scanknife_Upper.PNG")
print("하위단계4 : " + str(img_scanknife_Upper))
pyautogui.click(img_scanknife_Upper, duration=0.5)
img_scanknife_lower = pyautogui.locateOnScreen("Image/scanknife_Lower.PNG")
print("하위단계5 : " + str(img_scanknife_lower))
pyautogui.click(img_scanknife_lower, duration=0.5)



#다음단계 진입
img_Ready = pyautogui.locateOnScreen("Image/Ready.PNG")
print("단계진입 : " + str(img_Ready))
pyautogui.click(img_Ready, duration=0.5)



#프로세스 종료 및 실행시간 표시
end_time = time.time()
print("-" * 100)
print("Process End")
print("수행시간 : " + str(end_time - start_time) + " seconds")
print("=" * 100)


#실행시간 표시 메세지박스
pyautogui.alert(title = '알림', text = "수행시간 : " + str(end_time - start_time) + " seconds", button='OK')