# desktop-lock-unlock.
Have you ever grown tired of people peeking into your Windows devices when you don't want them to? I know I have, which is why this script will let you lock your computer when someone sneaks at your work.
1. Setup python env.
2. Open cmd and enter this command:
      pip install -r requirements.txt
3. Camera availability to create dataset and final recognition.
# How to run?
1. First run create_face_datasets.py .This will create dataset folder where it will capture your image in greyscale
2. Now, run training_model.py to train your model using dataset which were previously created
3. Run the lock_unlock_face_recognition.py 
4. Keep all the files in one folder.


