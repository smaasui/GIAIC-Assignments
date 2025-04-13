# **Checking Strength of Password**
# Check for basic requirement ie Uppercase, Lowercase, Numeric and Special characters
# State Password Strength ie Weak, Moderate, Strong
# Estimates crack time using brute-force calculations
# Give Suggestion of unfullfilled requirements in basic requirements
# Suggests a strong password if needed
# State Security Tips


import streamlit as st
import re
import time

# Page Configuration
st.set_page_config(
    page_title="Password Sentinel", 
    page_icon="🔐", 
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": """# SMAASU Corporation©️  
        https://g.co/kgs/VvQB8W9
        App Version 0.617"""}
    )


# function for checking each requirement
def have_special_char(s):
    return bool(re.search(r'[^A-Za-z0-9 ]', s))

def have_num(s):
    return bool(re.search(r'[0-9]', s))

def have_upper(s):
    return any(char.isupper() for char in s)

def have_lower(s):
    return any(letter.islower() for letter in s)

def have_least(s):
    return len(s)>7

def have_max(s):
    return len(s)<65

def is_weak_password(password):
    # 🚨 List of Common Weak Passwords (Avoid using these!)
    weak_passwords = [
    # Common Numeric Patterns
    "12345678", "123456789", "1234567890", "987654321", "11223344", "65432100", "00000000", "22222222", "99999999", "12121212", "77777777", "11112222",
    
    # Common Words & Phrases
    "password", "password1", "password123", "letmein123", "welcome123", "trustno1", "football1", "monkey123", "sunshine12", "iloveyou1", "superman1", "batman123", "starwars12", "dragon123", "master123", "shadow123", "freedom12", "ninja1234", "hello1234", "qwerty123", "baseball12", "computer1", "whatever1", "access1234", "secret123", "login12345", "adminadmin",
    
    # Keyboard Patterns
    "qwertyui", "asdfghjk", "zxcvbnm1", "qazwsxed", "1q2w3e4r", "poiuytrew", "mnbvcxz1", "lkjhgfdsa", "qwertyuiop", "asdfghjkl1", "zxcvbnm123", "1qaz2wsx", "3edc4rfv", "5tgb6yhn", "7ujm8ik9",
    
    # Popular Names
    "jennifer1", "michael12", "charlie99", "andrew123", "stephanie1", "daniel123", "robert123", "jessica12", "jordan123", "hunter123", "thomas123", "george123", "harrypotter1",
    
    # Date-Based Passwords
    "20202020", "19901990", "20012002", "20102011", "12319999", "03121985", "07071996", "09092009", "01012020", "12251995", "06061999", "19971997", "19861986", "20032003",
    
    # Company & Tech
    "google123", "facebook1", "linkedin12", "netflix123", "adobe1234", "oracle12", "microsoft1", "samsung12", "apple1234", "amazon123", "tesla1234", "nvidia123",
    
    # Variations with Symbols & Capitalization
    "P@ssword1", "Password!", "Admin1234", "Welcome1!", "Qwerty123!", "1q2w3e4r5t!", "LetMeIn!", "TrustNo1!", "Superman12", "Hello123!", "Password@123", "Pa$$w0rd!", "Mypass@123",
    
    # Repetitive & Commonly Used
    "abcabcabc", "xyzxyzxyz", "testtest12", "passpass12", "default12", "changeme12", "guest1234", "system999", "administrator", "rootroot12", "database1", "backup1234", "secure1234",
    
    # Miscellaneous Common Weak Passwords
    "chocolate1", "pokemon123", "spiderman12", "batmanforever1", "liverpool1", "manutd123", "chelsea123", "arsenal12", "summer2024", "winter2023", "autumn2022", "spring2021", "corona2020", "pandemic2021", "covid1234", "vaccination1", "quarantine1"
]

    return password in weak_passwords

col1, col2, col3 = st.columns([2.5,5,2.5])
with col2:

    st.write("# 🔐 Password Strength Checker")
    passcode = st.text_input("Enter Password", type="password")
    
    placeholder = st.empty()    # Create an empty placeholder
    placeholder.warning("⚡ Strength Checking...")      # Show the message
    time.sleep(.5)       # Wait for half second
    placeholder.empty() # Clear the message
    # st.success("✅ Password strength checked!")     # Continue with password strength evaluation...

    # st.write("###  Strength Checking...")
    
    #Check password strength state
    if (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 5:
        st.info("### Un Crackable !")
    elif (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 4:
        st.success("### Strong !")
    elif (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 2:
        st.warning("### Mediocure !")
    elif len(passcode)==0:
        st.warning("### Enter Password !")
    else :
        st.error("### Hackable !")

    # Initialize progress bar
    progress_bar = st.progress(0)

    progress_bar.progress((have_special_char(passcode) + have_least(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode))/5)  

    # Example: Check all requirements
    if have_least(passcode):
        st.write("✔️ At least 8 characters")
    else:
        st.write("❌ Password should have at least 8 characters")

    if not(have_max(passcode)):
        st.write("❌ Password could be at most 64 characters")

    if have_special_char(passcode):
        st.write("✔️ At least one special character")
    else:
        st.write("❌ Password should have at least one special character")

    if have_num(passcode):
        st.write("✔️ At least one number")
    else:
        st.write("❌ Password should have at least one number")

    if have_upper(passcode):
        st.write("✔️ At least one Uppercase letter")
    else:
        st.write("❌ Password should have at least Uppercase letter")

    if have_lower(passcode):
        st.write("✔️ At least one Lowercase letter")
    else:
        st.write("❌ Password should have at least Lowercase letter")

    if is_weak_password(passcode):
        st.write("❌ Very Common Password !")

    if have_special_char(passcode) and have_least(passcode) and have_max(passcode) and have_num(passcode) and have_upper(passcode) and have_lower(passcode):
        st.info("### Great !")
    else:
        import string
        import random
        random_text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) 
                            for _ in range(12))
        st.info(f"#### Suggested UnCrackable Password :  `{random_text}`")


        
