# ------------------------------
# Import Libraries
# ------------------------------
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO
import pyttsx3
import threading
import shutil
import sys
import os

# --- Intialize Pyttsx3 ---
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (from 0.0 to 1.0)

# --- DEFINE THE MODEL ---
model = YOLO("detection/object_detection/yolov8m.pt")

# --- FUNCTION TO DETECT ---
def detection(frame):
    if frame is None: 
        say_text("Frame Not Found")
        return 0
    
    results = model.predict(frame, conf=0.5, save=True, project='detection/object_detection/runs')
    object_counts = get_objects_count(model, results)

    return object_counts


# --- OBJECTS COUNT ---
def get_objects_count(model, results):
 unique_objects = [] # list of unique objects
 object_counts = {} # list of object and its count

 for result in results:
  if result.boxes:
   for box in result.boxes:
    ClassInd = int(box.cls)
    if model.names[ClassInd] not in object_counts:
     unique_objects.append(model.names[ClassInd])
     object_counts[model.names[ClassInd]] = 1
    else:
     object_counts[model.names[ClassInd]] += 1

 return object_counts

# --- Create Text From Object Names ---
def objectNames(object_names_count):
    final_text = ""
    for index, (key, value) in enumerate(object_names_count.items()):
        is_sum = "s" if value > 1 else ""
        is_and = "" if index == len(object_names_count)-1 else "and "
        final_text += f"{value} {key}{is_sum} {is_and}"
    say_text(final_text)

# Speak text
def say_text(text):
    speech_thread = threading.Thread(target=speak, args=(text,))
    speech_thread.start()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# --- REMOVE RUNS FOLDER ---
def remove_folder(folder_name):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        pass

# --- IMAGE DETECTION ---
def image_detection(frame):
    remove_folder('detection/object_detection/runs')
    object_counts = detection(frame)
    objectNames(object_counts)
    return object_counts