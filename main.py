import win32com.client
import speech_recognition as sr
import webbrowser as wb
import datetime
from config import apikey
import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'
os.environ["OPENAI_API_KEY"] = apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Query: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

def ai(text):
    jarvis = Agent(
        role = "jarvis",
        goal = "Answer all questions asked as accurately possible and be as to the poit as you possibly can unless specifically asked otherwise.",
        backstory = "Your name is Jarvis and you are an ai agent who's goal is to answer any question thrown at you as accurately as you possibly can.",
        verbose=True,
        allow_delegation=False,
    )
    respond = Task(
        description=f"Provide an answer to the query: {text}",
        agent=jarvis,
        expected_output= f"A to the point and accurate answer to the query: {text}"
    )

    crew = Crew(
        agents=[jarvis],
        tasks=[respond],
        verbose=2,
        process=Process.sequential
    )

    response = crew.kickoff()
    return response


while 1:
    print("Listening...")
    text = takeCommand()
    text.lower()
    if 'jarvis' in text:

        if 'ai' or 'a i' or 'artificial intelligence' in text.lower():
            response = ai(text)
            print(response)
            speaker.Speak(response)

        sites = [
    ["youtube", "https://www.youtube.com"],
    ["wikipedia", "https://www.wikipedia.com"],
    ["google", "https://www.google.com"],
    ["Facebook", "https://www.facebook.com"],
    ["Twitter", "https://www.twitter.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Instagram", "https://www.instagram.com"],
    ["BBC", "https://www.bbc.com"],
    ["CNN", "https://www.cnn.com"],
    ["The New York Times", "https://www.nytimes.com"],
    ["Reuters", "https://www.reuters.com"],
    ["Amazon", "https://www.amazon.com"],
    ["eBay", "https://www.ebay.com"],
    ["Alibaba", "https://www.alibaba.com"],
    ["Khan Academy", "https://www.khanacademy.org"],
    ["Coursera", "https://www.coursera.org"],
    ["edX", "https://www.edx.org"],
    ["MIT OpenCourseWare", "https://ocw.mit.edu"],
    ["TechCrunch", "https://www.techcrunch.com"],
    ["Wired", "https://www.wired.com"],
    ["Gizmodo", "https://www.gizmodo.com"],
    ["WebMD", "https://www.webmd.com"],
    ["Mayo Clinic", "https://www.mayoclinic.org"],
    ["Healthline", "https://www.healthline.com"],
    ["Bloomberg", "https://www.bloomberg.com"],
    ["Forbes", "https://www.forbes.com"],
    ["Yahoo Finance", "https://finance.yahoo.com"],
    ["Netflix", "https://www.netflix.com"],
    ["Spotify", "https://www.spotify.com"],
    ["Hulu", "https://www.hulu.com"],
    ["TripAdvisor", "https://www.tripadvisor.com"],
    ["Booking.com", "https://www.booking.com"],
    ["Airbnb", "https://www.airbnb.com"],
    ["Pinterest", "https://www.pinterest.com"],
    ["Reddit", "https://www.reddit.com"],
    ["Goodreads", "https://www.goodreads.com"],
    ["Flipkart", "https://www.flipkart.com"],
    ["Myntra", "https://www.myntra.com"],
    ["Snapdeal", "https://www.snapdeal.com"],
    ["Zomato", "https://www.zomato.com"],
    ["Swiggy", "https://www.swiggy.com"],
    ["Paytm", "https://www.paytm.com"],
    ["Google Pay", "https://pay.google.com"],
    ["PhonePe", "https://www.phonepe.com"],
    ["Ola", "https://www.olacabs.com"],
    ["Uber", "https://www.uber.com"],
    ["Hotstar", "https://www.hotstar.com"],
    ["Sony Liv", "https://www.sonyliv.com"],
    ["MakeMyTrip", "https://www.makemytrip.com"],
    ["Yatra", "https://www.yatra.com"],
    ["Cleartrip", "https://www.cleartrip.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Telegram", "https://telegram.org"],
    ["BYJU'S", "https://www.byjus.com"],
    ["Unacademy", "https://unacademy.com"],
    ["Google meet", "https://meet.google.com/"]
    ]

        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                print(f"Opening {site[0]}")
                speaker.Speak(f"Opening {site[0]}")
                wb.open(site[1])

        if 'time' in text.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {strfTime}")
            speaker.Speak(f"The time is {strfTime}")

        if 'terminate' in text.lower():
            break