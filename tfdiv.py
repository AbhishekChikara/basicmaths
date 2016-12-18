import tensorflow as tf  
# tf.placeholder define the shape of the inputs
a = tf.placeholder('float') #Creates a symbolic variable a 
b = tf.placeholder('float') #Creates a symbolic variable b

y =tf.divide(a,b) #divides the symbollic variables 

with tf.Session() as sess: #creates a session to evalute the symbolic expressions
	
	print("%f should equal to 0.5" % sess.run(y,feed_dict={a:1,b:2})) #we define the values of a and b in the feed_dict it can have any number of values
	print("%f should be equal to 1" % sess.run(y,feed_dict={a:10,b:10}))

