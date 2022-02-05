# desktop-lock-unlock.
Ever sick of people looking into your windows devices when you don't want anyone to see it , well I have so this script will help you to automatically lock your pc when someone peeks in your work.
# Prerequisites
1. Setup python env.
2. Open cmd and enter this command:
      pip install -r requirements.txt
3. Camera availability to create dataset and final recognition.
# How to run?
1. First run create_face_datasets.py .This will create dataset folder where it will capture your image in greyscale
2. Now, run training_model.py to train your model using dataset which were previously created
3. Run the lock_unlock_face_recognition.py 

# Note:
Keep all the files in one folder.

# Enjoy!
