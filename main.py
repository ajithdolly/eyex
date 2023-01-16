import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
pyautogui.FAILSAFE=False
frameR=150

screen_w,screen_h=pyautogui.size()

while True:
    _, frame = cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output= face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks =landmark_points[0].landmark

          #face landmark dectection

        cv2.rectangle(frame, (frameR, frameR), (frame_w - frameR, frame_h - frameR), (255, 0, 255), 0)

        for id, landmark in enumerate(landmarks[53:55]):
            x= int(landmark.x*frame_w)
            y= int(landmark.y*frame_h)
            cv2.circle(frame, (x,y),3,(0,255,0))
            print(x,y)





          #mouse movements


            if id==1:
                a=frame_w-2*frameR
                b=frame_h-2*frameR
                screen_x=(screen_w/a*x)
                screen_y=(screen_h/b*y)
                pyautogui.moveTo(screen_x,screen_y)

               # left eye wink left click

        left =[landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)

            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y - left[1].y)<0.015:
            pyautogui.click()
            pyautogui.sleep(0)


            #right eye wink right click


        right = [landmarks[374], landmarks[386]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)

            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (right[0].y - right[1].y) < 0.015:
            pyautogui.click(button='right')
            pyautogui.sleep(0)


           #mouse scroll down

        scroll = [landmarks[13], landmarks[14]]
        for landmark in scroll:
            x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)

        cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (scroll[1].y - scroll[0].y) > 0.100:
            pyautogui.scroll(100)
        #mouse scroll up

        elif (scroll[1].y - scroll[0].y) > 0.050:
            pyautogui.scroll(-100)



    cv2.imshow('eye controlled mouse',frame)
    cv2.waitKey(1)
