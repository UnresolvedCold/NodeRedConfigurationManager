curr=$PWD  
cd ~/.node-red  

 if [ "$#" -eq  "0" ]
   then
     python3 changeNoderedProfile.py
 else
     python3 changeNoderedProfile.py --o $1 
 fi

cd $curr