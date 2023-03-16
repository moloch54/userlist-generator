# userlist generator  
generate userslist with first name, last name. Ex: john jmith -> j.smith,john-s ....

# Usage  
users.txt must be in this format, first name and last name separated with a space:  

john doe  
albert camus  

```sh
python usergen.py --ul users.txt -o userslist.txt  
```  

# Results for userslist.txt    

j-d  
j-do  
j-doe  
j.d  
j.do  
j.doe  
j_d  
j_do  
j_doe  
jd  
jdo  
jdoe  
jo-d  
jo-do  
jo-doe  
jo.d  
jo.do  
jo.doe  
jo_d  
jo_do  
jo_doe  
jod  
jodo  
jodoe  
joh-d  
joh-do  
joh-doe  
joh.d  
joh.do  
joh.doe  
joh_d  
joh_do  
joh_doe  
johd  
johdo  
johdoe  
john-d  
john-do  
john-doe  
john.d  
john.do  
john.doe  
john_d  
john_do  
john_doe  
johnd  
johndo  
johndoe  






