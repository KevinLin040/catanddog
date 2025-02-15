
import tensorflow as tf
import numpy as np  
import cv2


#載入模型
model = tf.keras.models.load_model('./model/mymodel121.h5')
#訯定分類碼
inverse_dict = {0:'Cat',1:'Dog'}
#載入圖片並處理
img = cv2.imread('32.jpg')
img2 = img.copy()
img2 = cv2.resize(img2,(224,224))
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img2 = img2 /255
#預測
img2 = (np.expand_dims(img2, 0))
result = np.squeeze(model.predict(img2))
predict_class = np.argmax(result)
#預測結果印在圖片上
txt = str(inverse_dict[int(predict_class)]) + ' ' +str(round((result[predict_class]*100),1)) + '%'
print(txt)
img = cv2.putText(img,txt,(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
#顯示圖片
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
