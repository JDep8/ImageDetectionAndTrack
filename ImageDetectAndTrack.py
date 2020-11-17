import cv2
import numpy as np
import pantilthat

cap = cv2.VideoCapture(0)
pantilthat.servo_enable(1, True)
pantilthat.servo_enable(2, True)

pantilthat.servo_one(0)
pantilthat.servo_two(0)  



while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
  
    
    # red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    ##Detect biggest red object
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    
    #draw rectangle on biggest contour
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        cv2.rectangle(frame, (x, y),(x + w , y + h), (0 , 255, 0), 2)
        
        #find middle
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        
         ##Draw line on x axis 
        cv2.line(frame, (x_medium,0),(x_medium,480),(0 , 255, 0), 2)
        cv2.line(frame, (0, y_medium),(680, y_medium),(0 , 255, 0), 2)
              
        ##print('X: ' + str(x_medium ) + ' Y: ' + str(y_medium ) )
        
        ##move servoimport cv2
import numpy as np
import pantilthat

cap = cv2.VideoCapture(0)
pantilthat.servo_enable(1, True)
pantilthat.servo_enable(2, True)

pantilthat.servo_one(0)
pantilthat.servo_two(0)  



while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
  
    
    # red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    ##Detect biggest red object
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    
    #draw rectangle on biggest contour
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        cv2.rectangle(frame, (x, y),(x + w , y + h), (0 , 255, 0), 2)
        
        #find middle
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        
         ##Draw line on x axis 
        cv2.line(frame, (x_medium,0),(x_medium,480),(0 , 255, 0), 2)
        cv2.line(frame, (0, y_medium),(680, y_medium),(0 , 255, 0), 2)
              
        ##print('X: ' + str(x_medium ) + ' Y: ' + str(y_medium ) )
        
        ##move servo
        print('X: ' + str(x_medium - 340) + ' Y: ' + str(y_medium ) )
        
        ##X axis
        if (x_medium - 340) > 40:
            if (pantilthat.get_pan() + 1) < 90:
                position = pantilthat.get_pan() + 1             
                pantilthat.servo_one(position)
            
        if (x_medium - 340) < -40:
             if (pantilthat.get_pan() - 1) > -90:
                position = pantilthat.get_pan() - 1         
                pantilthat.servo_one(position)
              
        #y axis
        if (y_medium - 240) < 40:
            if (pantilthat.get_tilt() + 1) < 90:
                position = pantilthat.get_tilt() + 1         
                pantilthat.servo_two(position)
            
        if (y_medium - 240) > -40:
             if (pantilthat.get_tilt() - 1) > -90:
                position = pantilthat.get_tilt() - 1
                pantilthat.servo_two(position)
                 
         
        break
     
    frame = cv2.flip(frame, 0)
    red_mask = cv2.flip(red_mask, 0)
    
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",red_mask) 
    
    #spacebar to stop
    key = cv2.waitKey(1)
    if key == 32:
        break
    
cap.release()
cv2.destroyAllWindows()
pantilthat.servo_enable(1, False)
pantilthat.servo_enable(2, False)



        print('X: ' + str(x_medium - 340) + ' Y: ' + str(y_medium ) )
        
        ##X axis
        if (x_medium - 340) > 1:
            if (pantilthat.get_pan() + 1) < 90:
                position = pantilthat.get_pan() + 1
                print(position)              
                pantilthat.servo_one(position)
            
        if (x_medium - 340) < 1:
             if (pantilthat.get_pan() - 1) > -90:
                position = pantilthat.get_pan() - 1
                print(position)              
                pantilthat.servo_one(position)
              
        #y axis
        if (y_medium - 240) < 1:
            if (pantilthat.get_tilt() + 1) < 90:
                position = pantilthat.get_tilt() + 1         
                pantilthat.servo_two(position)
            
        if (y_medium - 240) > 1:
             if (pantilthat.get_tilt() - 1) > -90:
                position = pantilthat.get_tilt() - 1
                pantilthat.servo_two(position)
                 
         
        break
     
    frame = cv2.flip(frame, 0)
    red_mask = cv2.flip(red_mask, 0)
    
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",red_mask) 
    
    #spacebar to stop
    key = cv2.waitKey(1)
    if key == 32:
        break
    
cap.release()
cv2.destroyAllWindows()
pantilthat.servo_enable(1, False)
pantilthat.servo_enable(2, False)

