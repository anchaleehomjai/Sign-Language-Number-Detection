import os
import cv2

DATA_DIR = './data' # Directory to store images
NUMBER_OF_CLASSES = 9  # Numbers 1-9
DATASET_SIZE = 100
CAMERA_ID = 0

#Create directories for data storage
def create_directories():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    for i in range(NUMBER_OF_CLASSES):
        class_dir = os.path.join(DATA_DIR, str(i))
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

def collect_images():
    #Collect and save images for each class
    cap = cv2.VideoCapture(CAMERA_ID)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    try:
        for class_num in range(NUMBER_OF_CLASSES):
            print(f'Collecting data for number {class_num + 1}')
            
            # Wait for user to be ready
            while True:
                ret, frame = cap.read()
                if not ret:
                    continue
                
                cv2.putText(
                    frame,
                    f'Ready to collect images for number {class_num + 1}',
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )
                cv2.putText(
                    frame,
                    'Press "Q" when ready!',
                    (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )
                
                cv2.imshow('Data Collection', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Collect images
            counter = 0
            while counter < DATASET_SIZE:
                ret, frame = cap.read()
                if not ret:
                    continue
                
                cv2.putText(
                    frame,
                    f'Capturing: {counter}/{DATASET_SIZE}',
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )
                
                cv2.imshow('Data Collection', frame)
                cv2.waitKey(25)
                
                # Save image
                img_path = os.path.join(DATA_DIR, str(class_num), f'{counter}.jpg')
                cv2.imwrite(img_path, frame)
                counter += 1

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    create_directories()
    collect_images()
    print("Data collection completed!")