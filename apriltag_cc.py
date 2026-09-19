
import cv2
from apriltag import apriltag

# Create detector once
detector = apriltag("tag36h11")

# Open default camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ok, frame = cap.read()

    if not ok:
        print("Failed to read camera frame")
        break

    # AprilTag detector expects grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect AprilTags
    detections = detector.detect(gray)

    for detection in detections:

        # Your library returns a dictionary:
        # {
        #   'hamming': ...,
        #   'margin': ...,
        #   'id': ...,
        #   'center': ...,
        #   'lb-rb-rt-lt': ...,
        #   'homography': ...
        # }

        corners = detection["lb-rb-rt-lt"].astype(int)
        tag_id = detection["id"]
        center = detection["center"].astype(int)

        # Draw tag boundary
        cv2.polylines(
            frame,
            [corners],
            True,
            (0, 255, 0),
            2
        )

        # Draw tag center
        cv2.circle(
            frame,
            tuple(center),
            5,
            (0, 0, 255),
            -1
        )

        # Display Tag ID
        x, y = corners[0]

        cv2.putText(
            frame,
            f"ID: {tag_id}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        print(
            f"Tag ID: {tag_id}, "
            f"Center: {center}, "
            f"Decision Margin: {detection['margin']:.2f}"
        )

    cv2.imshow("AprilTag Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
