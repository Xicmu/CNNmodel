import os
from skimage import io,transform
import tensorflow as tf
import numpy as np

dir = "data/xz"
list  = os.listdir(dir)


flower_dict = {0:'healthy',1:'disease'}

result = open('xz.txt','w')

w=100
h=100
c=3

def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)

with tf.Session() as sess:
    data = []
    name = []
    for filename in list:
	name.append(filename)
    	data1 = read_one_image(dir+'/'+filename)
    	data.append(data1)
    '''data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)'''

    saver = tf.train.import_meta_graph('/home/dmclass/yxj/data/modelxz/model.ckpt.meta')
    saver.restore(sess,tf.train.latest_checkpoint('/home/dmclass/yxj/data/modelxz/'))

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(tf.nn.softmax(sess.run(logits,feed_dict)))


    print (classification_result)
    
    print(tf.argmax(classification_result,1).eval())
   
    output = []
    output = tf.argmax(classification_result,1).eval()
    for i in range(len(output)):
        result.write(name[i]+' '+flower_dict[output[i]]+'\n')
        
