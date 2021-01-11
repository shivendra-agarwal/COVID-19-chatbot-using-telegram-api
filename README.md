Main file: telegram/telegram_runner.py


# COVID-19-chatbot-using-telegram-api
**Smart Medical Assistant**
_Theme by Virtusa Technologies_
Build a predictive chatbot enabled digital assistant, backed by data, that can help surgeons,
patients and care teams throughout the patient journey by automating some of the crucial tasks
done manually such as decision making, post-surgery planning, tracking and estimating
recovery-time, and takes patients' feedback. Can you come up with innovative reporting tools or
dashboards for patient data monitoring and Patient engagement by providing customized
counseling?
Or use your ML skills to create a bot to Line of Therapy for patients by gathering patient
information and suggesting pathway and treatment cost, and prepare an optimized insurance plan
for coverage based on the patient's condition and locality.
We, ​ _Chaitra Dhanorkar_ ​ and ​ _Shivendra Agarwal_ ​ Propose
**Natural Language Processing based Chatbot**
For the above mentioned theme.
Contact Details
Chaitra Dhanorkar Shivendra Agarwal
Email: ​chaitrad303@gmail.com​ Email: ​shiv.vitu@gmail.com

## Table of Contents

- Introduction
   - About The Author
   - Objective
   - Chatbot: A definition
   - Motivation
- System Architecture
   - API Calls
   - Client Responsibilities
   - Server Responsibilities
   - System responsibilities
   - Flow chart
   - Keywords
   - Diagram
   - System Requirements
- Algorithms and Data Structure
   - CRISP-DM Model
   - Agile
- Interface
   - Config Page
   - Chat Window Page
- Class Diagram


1. Introduction
    1.1. About The Author
       Our names are ​ _Shivendra Agarwal_ and ​ _Chaitra Dhanorkar_ ​, we are all
final-year master students of Data Science from CHRIST (Deemed to be
University), Bangalore. We know each other from last year and have participated
in multiple completions at national level. We think Artificial Intelligence as a
field is very interesting and are looking forward to having a lot of professional
discussions about the topic through our project work.

    1.2. Objective
       Normally users are not aware of treatments or symptoms regarding the
particular disease. For small problems, the user has to go personally to the
hospital for a check-up which is time-consuming in this fast-paced world.
Handling telephonic calls for the complaints is hectic. Such a problem can be
solved by using a chatbot which can help give guidance at a basic level.
Many diseases can be identified by common symptoms, and disease
prediction, answering general queries and getting information specific to a
healthcare organization can all be made using chatbots that are powered by AI.
The chatbot is an AI chatbot that receives questions from users, tries to
understand the question, and provides appropriate answers. It does this by
converting an English sentence into a machine-friendly query, then going through
relevant data to find the necessary information, and finally returning the answer in
a natural language sentence. In other words, it answers your questions like a
human does, instead of giving you the list of websites that may contain the
answer. For example, when it receives the question "What time does the
consultations begin today?", it will give a response “They start at 10 am today.”
The main objective is creating a Web API and mobile interfaces that demonstrate
the use of the API. The goal is to provide users a quick and easy way to have their
questions answered.
As the industries see a rise in adapting AI into different areas, chatbots are
gradually being adopted into the healthcare industry. But this implementation is
just in the early phase and there is a long way to go, and a lot of room for
improvement and research. According to the market research firm Grand View
Research, by 2025, the global chatbot market will reach around 1.23 billion
dollars.


Healthcare has become an attractive market for companies developing
chatbot applications for clinicians and patients. The majority of current and
emerging use cases appear to focus on checking patient symptoms. Natural
language processing is used to help diagnose a user based on the symptoms he or
she provides. Technical advancements in the healthcare domain are growing at a
rapid pace.

1.3. Chatbot: A definition
According to the Oxford English Dictionary, a chatbot is defined as
follows:
**chatbot (n.):**
_A computer program designed to simulate conversation with human users,
especially over the Internet._
In scientific literature, chatbots are referred to as conversational agents.
The hidden agenda of each chatbot is to connect with clients by means of
instant messages with a sense of understanding the discussion and answer to the
client properly. The cause of personal computers talking with people is as old as
the field of software engineering itself.
Another overall assumption is that clients normally have an objective they
need to accomplish before the finish of the conversation with the chatbot. This at
some point impacts the discussion's stream and to accomplish the defined

### Objective

Hence, the meaning of a chatbot for the record is a computer program
conveying by text in a humanly way and who offers types of assistance to its
clients so as to achieve a specified objective.

1.4. Motivation
Natural Language Processing aka NLP is a branch of informatics,
mathematical linguistics, machine learning, and artificial intelligence. NLP helps
your chatbot to analyze the human language and generate the text. Our language
is a highly unstructured phenomenon with flexible rules. If we want the computer
algorithms to understand these data, we should convert the human language into a


```
logical form. With the help of natural language understanding (NLU) and natural
language generation (NLG), it is possible to fully automate such processes as
generating financial reports or analyzing statistics.
The machine can interact with people using their language. All we need is
to input the data in our language, and the computer’s response will be clear.
Artificially Intelligent Chatbots are based on NLP which makes these bots very
human-like. ​They react to the meaning of the whole question. The AI-based
chatbot can learn from every interaction and expand their knowledge.
An NLP based chatbot is a computer program or artificial intelligence that
communicates with a customer via textual or sound methods. Such programs are
often designed to support clients on websites or via phone. These are generally
used in messaging applications like Slack, Facebook Messenger, or Telegram.
This field is very young, with small companies raising venture money,
mostly in major technology hubs. Healthcare chatbots currently seem to be a mix
of both patient-only and patient-clinician applications. Business models are in the
early stages, and there is an expected growth. Changing patient and clinician
behavior with a chat interface is a hard problem and one that won’t be solved
overnight. Current user data is sparse. This project focuses on creating a product
available to everyone. The project also focuses on overcoming existing
domain-specific loopholes and errors in the existing 3rd party chatbots.
```

2. System Architecture
    2.1. API Calls
       2.1.1. Client Responsibilities
          2.1.1.1. GET requests by the client with the parameters.
          2.1.1.2. Defining header Content-Type: application/json by the client.
          2.1.1.3. A sentence as an input in the given keyboard language.
          2.1.1.4. The server will reply with either data or an error.
       2.1.2. Server Responsibilities
          2.1.2.1. The server will send all API data in the database and also put the
             request in the queue.


2.1.2.2. The server will respond with a 200 OK status code if a request has
the header Content-Type: application/json and is a valid API
query.

2.1.2.3. The user waits without any notification.

2.1.2.4. The server will respond with a 400 Bad Request status code then
the user has to retry with a new meaningful question.

2.1.3. System responsibilities

2.1.3.1. Maintaining the database is the highest priority.

2.1.3.2. Update flags given at multiple steps.

2.1.3.3. Process the question in all the possible ways.

2.1.3.4. Perform long term scheduler and short term scheduler activities as
per need.

2.1.3.5. Maintain document level conversation.

2.1.3.6. Maintain error log file at server level.

2.1.4. Flow chart

2.1.4.1. Keywords

2.1.4.1.1. Pool of requests: All the waiting users will be queued here
with the questions as the parameter.

2.1.4.1.2. Condition: To save time, questions are pre processed and
checked if answers are already present in the file or not.

2.1.4.1.3. Predefined questions: All the frequently asked questions
are saved here.

2.1.4.1.4. Process the questions: Uniques questions are processed by
the model.

2.1.4.1.5. Save: All the flags and queries are saved in the database.


2.1.4.1.6. Frame the answer: The answers are framed according to the
questions.

2.1.4.1.7. Predefined answers: For predefined questions, predefined
answers are returned.

2.1.4.2. Diagram
**_Fig 1: Query Process Flow Diagram_**

2.1.5. System Requi​rements

2.1.5.1. Assumptions
● 30 - 100 request per minute
● 6 peak hours distributed in 24 hours
● Asynchronous connection between client and server


### System Requirements

```
● RAM: Minimum 8 GB, Standard 16 GB
● Storage: HDD minimum 1TB 5400 rpm, SDD standard
1TB
● OS: Windows 10 or Linux based OS
● Python: Python 3.
● Internet: Stable connection with optimum speed
```

3. Algorithms and Data Structure
    3.1. CRISP-DM Model
       The CRoss Industry Standard Process for Data Mining (CRISP-DM) is an
open and structured process model. Founded in 1999 to standardize data mining
processes across industries, it has since become the most common methodology
for data mining, analytics, and data science projects. Data science teams that
combine a loose implementation of CRISP-DM with overarching team-based
agile project management approaches will likely see the best results.
The following diagram gives the life-cycle of a CRISP-DM model.
**_Fig 2: life-cycle of a CRISP-DM model_**


The chat bot is NLP-based. So the CRISP-DM model can be implemented.
The project can be a methodical workflow that has a sequence of steps. The major
steps are depicted in the following figure.
**_Fig 2: Detailed steps in CRISP-DM model_**
We usually start with a corpus of text documents and follow standard
processes of text wrangling and pre-processing, parsing and basic exploratory
data analysis. Based on the initial insights, we usually represent the text using
relevant feature engineering techniques. Depending on the problem at hand, we
either focus on building predictive supervised models or unsupervised models,
which usually focus more on pattern mining and grouping. Finally, we evaluate
the model and the overall success criteria with relevant stakeholders or customers
and deploy the final model for future usage.

3.2. Agile
Since the project is not only NLP alone, and has integration of APIs and
database, there is software development. So, the project has implementation of
CRISP-DM model with agile project management approach.
The aim is to develop an agile methodology using sprints, test with
beta-users, improve the bot flow, the knowledge base, the bot personality. The
minimum viable product can be enriched during each iteration with new phrases
captured by the error management functions. To ensure no bugs are crawling into
the bot, testing should also be performed at each iteration.
While in the first stages manual testing ensures business logic, in later
phases automation can save time and help developers and QA teams get new and
improved versions to market. Companies that have foreseen the power of these
new interfaces are already investing in testing automation and starting to create
value through chatbot-powered conversation.
The following diagram gives an overview of the process.


```
Fig 3: Software development model for chatbot
```

4. Interface
    4.1. Config Page
       This screenshot is taken from the telegram bot page. This is how the
setting page of the chatbot will look. Variations can be expected.


**_Fig 4: Chatbot Setting_**

4.2. Chat Window Page
Chatbox with the virtual agent. Variations can be expected.


```

Fig 5: Chatbot Window
```

5. Class Diagram
    The class ​diagram is the main building block of object-oriented modeling. It is
used for general conceptual modeling of the structure of the application, and for detailed
modeling translating the models into programming code.


```

Fig 5: Class Diagram
```

6. References
    6.1. [http://repository.essex.ac.uk/21238/](http://repository.essex.ac.uk/21238/)
    6.2. https://www.journals.ala.org/index.php/ltr/article/view/4504/
    6.3. https://ieeexplore.ieee.org/abstract/document/
    6.4. https://link.springer.com/chapter/10.1007/978-3-319-91662-0_
    6.5. https://ieeexplore.ieee.org/abstract/document/
    6.6. https://github.com/nullphantom/covid-19-chatbot-engine
    6.7. https://github.com/wearetriple/ai-faqbot-who/blob/master/WHO_FAQ.xlsx
    6.8. https://github.com/deepset-ai/COVID-QA
    6.9. https://towardsdatascience.com/transformers-state-of-the-art-natural-language-processing
       -1d84c4c7462b
    6.10. https://www.uio.no/studier/emner/matnat/ifi/IN5480/h18/deliverables/group-assignment/f
    inal-reports/finalreport-vildehos_annassc_martrim.pdf
    6.11. https://matheo.uliege.be/bitstream/2268.2/4625/6/Thesis_PETERS_Florian.pdf
    6.12. https://towardsdatascience.com/complete-guide-to-enterprise-chatbot-development-c377a
    a5e4ddc
    6.13. https://towardsdatascience.com/5-reasons-why-your-chatbot-needs-natural-language-proc
    essing-ed20fb0a
    
    
    
    Thank you
