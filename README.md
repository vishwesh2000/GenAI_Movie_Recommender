██████╗░██████╗░██╗███╗░░░███╗███████╗███████╗██╗░░░░░██╗██╗░░██╗
██╔══██╗██╔══██╗██║████╗░████║██╔════╝██╔════╝██║░░░░░██║╚██╗██╔╝
██████╔╝██████╔╝██║██╔████╔██║█████╗░░█████╗░░██║░░░░░██║░╚███╔╝░
██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░██╔══╝░░██║░░░░░██║░██╔██╗░
██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗██║░░░░░███████╗██║██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░╚═╝
### *➵ Generative AI based personalized movie recommendation approach*

Team name: TeleGenAIsis

**Working:**
1. The streamlit multi-page application has 3 pages (Signup, Login and Home).
2. The signup page asks few extra questions such as Age, Gender, Occupation and Genre as user demographics info.
3. Based on these info collected, personalizes the content on homepage for the users upon login.
4. In case, the user has other genres in mind and wants to watch something different... We have Semantic Search utility where users can search anything and fetch related results.

Good amount of prompt engineering has gone into the making of this project! Hope you enjoy!

**Python Dependencies:**
1. google-cloud-aiplatform
2. streamlit

**Setup:**
1. This repository has all the requirements to run the application.
2. The parent folder will be ```multipage_app```. Inside which we will have our python code for the opening page ```Login.py```. We will also have username.txt and users.json here. We will have another folder here ```Pages```.
3. Inside the ```Pages``` folder, we will have ```Home.py``` and ```Signup.py```. We will also have ```temp_file.txt, username.txt, users.json```.
