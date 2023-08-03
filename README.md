██████╗░██████╗░██╗███╗░░░███╗███████╗███████╗██╗░░░░░██╗██╗░░██╗
██╔══██╗██╔══██╗██║████╗░████║██╔════╝██╔════╝██║░░░░░██║╚██╗██╔╝
██████╔╝██████╔╝██║██╔████╔██║█████╗░░█████╗░░██║░░░░░██║░╚███╔╝░
██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══╝░░██╔══╝░░██║░░░░░██║░██╔██╗░
██║░░░░░██║░░██║██║██║░╚═╝░██║███████╗██║░░░░░███████╗██║██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░╚═╝
### *➵ Generative AI based personalized movie recommendation approach*

Disclaimer: ```This project focuses on content recommendation using Google Vertex AI Language models. If you're new to the Google Cloud Platform (GCP) and prefer to explore free alternatives, here's how you can get started:

Navigate to the multipage_app folder in this repository.

Inside the multipage_app folder, you'll find another folder named Pages.

Locate the home.py file inside the Pages folder, which currently utilizes the Google Vertex AI language model.

To use the free alternative, simply replace the existing home.py file with the one available outside the multipage_app folder in this repository. The alternative version uses Cohere language models, which are free but come with a rate limit of 5 API calls per minute (As of August 2023).```

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

**Run the code:**
If you are running from the terminal/shell, set the path to multipage_app and use the command below:
```streamlit run login.py```
