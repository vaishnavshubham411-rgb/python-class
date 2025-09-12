#  data = {"name":"shubham","True": 1, 1: "one"}
#  print(data)
#  ये dictionary है भाई, इसमें key-value जोड़े जाते हैं। ऊपर वाले में key string और int दोनों डाले हैं।


data1={"name":"shubham","age":19,"city":"jaipur","address":(125,'heera-nagar',"d.c.m"),"location":(125,'heera-nagar',"d.c.m") }
#  यहाँ ek बड़ी dictionary बनाई है, जिसमें naam, age, city और address tuple के रूप में डाला है।

print(data1)              # पूरी dictionary प्रिंट हो जाएगी।
print(len(data1))         # कितने key-value pairs हैं, उसकी गिनती निकलेगी।
print(data1["city"])      # city का value direct निकाला (yeh "jaipur" print karega).
print(data1.get("city"))  # get() से भी वही काम होता है, error भी नहीं देता।
print(data1.get("name"))  # name का value निकला।
print(data1.get("address")) # address tuple निकलेगा।

data1["gender"]="male"    
print(data1)              # dictionary में नया key-value pair जोड़ दिया।

data1.pop("age")          
print(data1)              # "age" key हटा दी dictionary से।

data1.popitem()           
print(data1)              # आख़िरी वाला item हटा दिया।

del data1["name"]         
print(data1)              # "name" key को पूरी तरह delete कर दिया।

data1.clear()             
print(data1)              # पूरी dictionary खाली कर दी।

data2=dict()
print(data2)              # ekदम fresh खाली dictionary बनाई dict() से।

data3 = {"shubham",19,78.59,23}
print(id(data3))          # ये set है भाई! id() memory address दिखा रहा।


data4 = data3
print(id(data4))          # data4 और data3 dono same jagah point kar rahe hain, id same aayega।

data5 = data4.copy()
print(id(data5))          # copy() किया, ab data5 अलग memory par hai।

data5.add("hello")
print(data5)              # set me "hello" डाल दिया।

data5.remove("hello")
print(data5)              # "hello" हटा दिया (agar na ho to error deta)।

data5.discard(19)
print(data5)              # discard() से 19 हटाया, agar na ho to error bhi nahi deta।

data5.discard("SHUBHAM")  # ye case sensitive hai, "shubham" hota tab hi hataata. Error bhi nahi diya।
print(data5)

data5=set()
print(data5)              # fresh ekदम khali set ban gaya।

# dictionary banayi hai, name aur age ka data rakha hai
data6 = {"name":"shubham","age":19}

# check kar rahe hai ki 'age' key dictionary me hai ya nahi
if "age" in data6:
    print("Age key exists in data6")   # agar hai toh yeh chalega
else:
    print("Age key does not exist in data6")  # agar nahi hai toh yeh chalega

# 1 se 10 tak counting print karega, ekdum school wali copy jaisi
for i in range(1,11):
    print(i)

# 3 baar 'hello' bolke thoda swag dikhayega
for i in range(3):
    print("hello")
