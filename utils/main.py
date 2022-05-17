from utils.get_data import get_data
from utils.detector import detect_eye
from utils.model import get_model
from keras.callbacks import EarlyStopping
import yaml

config=yaml.safe_load(open('config.yaml'))
img_path=config['img_path']
size=config['size']

#################################### for adding new eye images######################
detect_eye(img_path,size)
####################################################################################

x_train,x_test,x_val,y_train,y_test,y_val=get_data(img_path)

clb=EarlyStopping(patience=4,monitor='val_accuracy',restore_best_weights=True)

model=get_model(size)
model.fit(x_train/255,y_train,validation_data=(x_val/255,y_val),callbacks=clb,epochs=20,batch_size=16)
