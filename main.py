import subprocess

print("Step 1: Downloading raw data...")
subprocess.run(["python", "src/data_loader.py"])

print("\nStep 2: Processing raw data...")
subprocess.run(["python", "src/process_data.py"])

print("\nStep 3: Merging and feature engineering...")
subprocess.run(["python", "src/merge_data.py"])

print("\nStep 4: Running EDA...")
subprocess.run(["python", "src/eda.py"])

print("\nStep 5: Training model...")
subprocess.run(["python", "src/model.py"])

print("\nDone!")
