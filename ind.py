from PIL import ImageGrab
from PIL import Image
import pytesseract
import time
import requests
import re

Lines = []      #Will store text

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   #Or wherever your tesseract exe is stored

i = 0
while(i < 1):                      #Loop until you want to stop   
    #Get width and height

    left = 496                       
    top = 680
    right = 1455
    bottom = 850

    # image = image.crop((left,top,right,bottom))        
    time.sleep(2)
    image = ImageGrab.grab(bbox=(left, top, right, bottom))
    image.save(r'C:\Users\KALYAN SHARMA\OneDrive\Desktop\TAKING SS AND TEXT GENERATION\screenshot'+str(i)+'.png')
    # open_image=Image.open(image)
    image_to_text  = pytesseract.image_to_string(image)  #Get text from image


    # append text to lines
    # if(len(Lines) > 0):
    #     if(Lines[len(Lines)-1] != image_to_text):
    #         Lines.append(image_to_text)
    # else:
    #     Lines.append(image_to_text)

    i+=1
    time.sleep(4)
    
print("image to text is:")
print(image_to_text)
print("After appending questions texts is:")
appended_text=image_to_text+"who is messi?"
print(appended_text)

def detect_questions(appended_text):
    question_pattern = r'\b(?:who|what|where|when|why|how|which|is|are|will|do|does|did|can|could|should|may|might|would|has|have|had|shall|was|were|been|being)\b.*[?]'
    # Search for questions in the text using the regular expression pattern.
    questions = re.findall(question_pattern, appended_text, re.IGNORECASE)
    return questions

questions = detect_questions(appended_text)
# print("detected questions:")
# print(questions)
# #Example usage:
# #input = "  Hi I am hira.  Hi I am hira. Hi I am hira. Hi I am hira.What is ph oh water?"

# for question in questions:
#     print(questions)

url = "https://api.openai.com/v1/completions"
questionstr = ""
for i,quest in enumerate(questions):
    questionstr+=f"{quest}"
       
payload = {
    "prompt": questionstr +" return answer for each question.",
    "model": "text-davinci-003",
    "temperature": 0,
    "max_tokens": 1000,
    "top_p": 1,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {'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'}"
}

# # Send the POST request

response = requests.post(url, json=payload, headers=headers)

# print(response.json())

chatbot_response = response.json()["choices"][0]["text"]

# # # Print the question and the corresponding answer
# print(f"Question: {questions}")
# print("=>",end="")
print(f"{chatbot_response}")