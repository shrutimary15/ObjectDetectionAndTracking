# Object Tracking and Counting 

Model used : yolov8n

1. Clone the repository.
2. Create a environment with python version 3.10
  ```bash
    conda create -n venv python=3.10 -y
  ```
2. Activate the environment and then install the requirements.
   ```bash
   conda activate venv
   pip install -r requirements.txt
   ```

3. Create a folder named Artifacts and store the .mp4 file in that folder.
   
   ObjectDetectionAndTracking
   
    ├── Artifacts

      │ └── Video.mp4
   
5. Edit the path SOURCE in constants.py.
6. Run
   ```bash
   Python main.py
   ```
