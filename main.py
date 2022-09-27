import requests, json, time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


global_appointment_cache = []

