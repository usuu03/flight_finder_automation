import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import random
import requests
import sqlite3
import time
import sched
import os
from dotenv import load_dotenv

load_dotenv()



# Configuration
TEQUILA_API_KEY = os.getenv('TEQUILA_API_KEY')
SENDER_EMAIL= os.getenv('SENDER_EMAIL')