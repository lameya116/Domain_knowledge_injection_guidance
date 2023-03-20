## Domain_knowledge_injection_guidance ##
This work aims to assist data scientist by providing a guidance to inject domain knowledge into data-driven models. The guidance gives suggestions for suitable knowledge injection phases and possible ML models based on a given analytics type and knowledge form. The guidance is developed in combination of a knowledge injection framework and the results of a literature study in which 50 predictive maintanence (PdM) use cases were analyzed. The guidance assists its users
both in a direct and indirect way. Directly, the users get suggestions of suitable phases and probably suitable models. Indirectly, the users can get additional
ideas from the knowledge injection framework on different further possibilities to inject domain knowledge. 
<p align="center">
<img src="/plots/img.PNG"  width="500 " height="200"></p>

### Knowledge Injection Freamework ### 
Inspired by CRISP-DMME [1], the framework is developed based on the informed machine learning framework proposed by Von Rueden et al. [2]

<p align="center">
<img src="/plots/conc.PNG"  width="470 " height="370"></p>

### Development of Knowledge Base ### 
The knowledge base is developed into two steps. 
* Step 1: Categorize each of the use cases based on one of the four analytics type which are- descriptive, diagnosis, predictive, and prescriptive.
* Step 2: Categorize further based on the knowledge injection framework which is depicted earlier.

The knowledge base is provided on ``GUI_App/usecase_resource.csv``.
### GUI inteface Design ###
In order to provide suitable recommendation a graphical user interface(GUI) is developed for the end users. The interface requires two inputs - type of application and form of knowledge to provide suitable recommendation. The recommandation are given from the knowledge base by following an algorithm provided in ``GUI_APP\Proposed_algorithm.pdf``. Some screenshots of the GUI application is depicted below.
<p float="left">
  <img src="/plots/m1.PNG" width="325" />
  <img src="/plots/m2.PNG" width="325" />  
</p>
<p float="left">
 <img src="/plots/m4.PNG" width="325" />
 <img src="/plots/m3.PNG" width="325" />
</p>
<p float="left">
  
  <img src="/plots/m5.PNG" width="325" /> 
  <img src="/plots/m6.PNG" width="325" />
</p>

### Examples for the Application of the Guidance ###
The guidance suggestion is applied on two different types of use cases. Among them the first one is diagnosis and the later one is predictive in nature.
#### Use Case 1: Monitoring Condition Inside a Disk Stack Separator ####
* Type of Application: Diagnosis
* Form of knowledge: Semi-formal
* Applied knowledge Conversion for Injection Purpose: Standard Techniques, Logic Rules, and Human decision
* Injection of Knowledge into the ML Models: Pre-processing, Feature Engineering, and Hypothesis Space Defining
<p align="center">
<img src="/plots/accuracy_all_sets.png"  width="470 " height="370"></p>

#### Use Case 2: Predicting Outer Race Defects of Bearing 1 in NASA IMS Bearing Dataset [3]  ####
* Type of Application: Predictive
* Form of knowledge: Informal
* Applied knowledge Conversion for Injection Purpose: Standard Techniques, and Human decision
* Injection of Knowledge into the ML Models: Pre-processing, Feature Engineering, and Hypothesis Space Defining
<p align="center">
<img src="/plots/prediction.png"  width="470 " height="370"></p>

### References ###
[1] Steffen Huber, Hajo Wiemer, Dorothea Schneider, and Steffen Ihlenfeldt. Dmme: Data mining methodology for engineering applications–a holistic extension to the crisp-dm model. Procedia Cirp, 79:403–408, 2019.

[2] Laura Von Rueden, Sebastian Mayer, Katharina Beckh, Bogdan Georgiev, Sven Giesselbach, Raoul Heese, Birgit Kirsch, MichalWalczak, Julius Pfrommer, Annika
Pick, et al. Informed machine learning-a taxonomy and survey of integrating prior knowledge into learning systems. IEEE Transactions on Knowledge and Data
Engineering, 2021. 

[3] J Lee, H Qiu, G Yu, and J Lin. Ims bearing run-to-failure dataset. 2007.

