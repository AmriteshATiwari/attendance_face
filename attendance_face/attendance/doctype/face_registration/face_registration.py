# Copyright (c) 2024, Amritesh Tiwari and contributors
# For license information, please see license.txt

import frappe
import face_recognition
import cv2
from frappe.model.document import Document


class FaceRegistration(Document):
    def before_save(self):
        self.capture_face_encoding()

    def capture_face_encoding(self):
        encodings = []
        frame = cv2.imread(frappe.get_site_path('private','files',(str(self.image).split('/')[-1])))
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for encoding in face_encodings:
            encodings.append(encoding)
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        self.registration_data = str(encodings)

# import frappe
# import face_recognition
# import cv2
# from frappe.model.document import Document


# class FaceRegistration(Document):
#     def before_save(self):
#         self.capture_face_encoding()

#     def capture_face_encoding(self):
#         encodings = []
#         frame = cv2.imread(frappe.get_site_path('private','files',(str(self.image).split('/')[-1])))
#         face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, face_locations)
        
#         # Store encodings as strings in a list
#         for encoding in face_encodings:
#             encodings.append(encoding.tolist())  # Convert to list for storage
            
#             top, right, bottom, left = face_locations[0]
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Save the encodings as strings
#         self.registration_data = str(encodings)
