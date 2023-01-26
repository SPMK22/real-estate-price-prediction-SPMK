# Immoweb_project 

## Description :
In this project, we will be analyzing data to predict prices for real estate sales in Belgium. 
We will use data acquired through scrapping the Immoweb website.
There is multiple steps we have to go through to have a fully functionnal program that can predict prices of a proprety.
<br>(The scraping part was a group project that I did with the helps of colleagues.)
<br>You can find the repo of this part here : (https://github.com/SPMK22/real-estate-price-MLprediction)
<br>We did the scraping , the analysis and the modeling so far (as of 26/01/2023).<br>
You can see all the requirement needed on the requirement.txt file.

### This repo is in different part : 
## First folder (data_analysis) :
With our set of data , it's important to clean and understand it. Cleaning it means that we have to get rid of data that are wrong , missing or not useful.
<br>The best way to understand the data is to make visuals about it. It can easily show you patterns & trends of our data.
<br>We have to make somes graphs coming from the dataset acquired from the previous exercice (immo_data_secondo.csv) and respond to the question that it raises in a short (2 minutes) presentation.
<br>Here we have 2 graphs representing the link between a building states and it's price , and the second one showing the link between the type of building and it's price.
<br>You will find in this folder 2 different folder , both contain the code + the visual for each graph (and the dataset used)
### Graph :

<table>
  <tr>
    <td>
      <img src="https://github.com/SPMK22/Immoweb_graph/blob/main/data_analysis/Graph%201/Graph%201.png" width ="400"
      height=""200">
    </td>
    <td>
      <img src="https://github.com/SPMK22/Immoweb_graph/blob/main/data_analysis/Graph%202/Graph%202.png" width ="400"
      height=""200">
    </td>
  </tr>
</table>
  


## Second part (modeling) : 
To predict real estate prices in Belgium using machine learning, the first step is to choose a model that works well with the data.
Some examples of models are linear regression, decision tree,random forest,...
<br>Next, the model is trained using the data. And after that , we verify the accuracy of our model by testing it using our test set finally , we can evaluate it using the score.
<br>The 2nd folder contain the code for the Machine Learning model used to have the score showing the accuracy of the model.
<br>Once we've understood the data, we will use Machine Learning to predict prices. 
<br>This will involve selecting a model that best fits the data set (in that case I used Linear regression), training the model on the data set, testing the model using a separate set of data (80/20), and evaluating the model through the score.
<br>You will find in this folder the code used for the model.

##### How could you improve this result?
You could improve this result by using different type of models or changing the dataset used.

##### Which part of the process has the most impact on the results?
For me what had the most impact on my result was the features selection , I was struggling with a very low score (7%) until I just played with somes features then I jumped to 55%.

##### How should you divide your time working on this kind of project?
The best way to manage the time in this type of project is to spend more time on cleaning the data in a way it's perfect , so the work left goes really fast.

The result could be improved
#### Where are we on the project ? 
- [x] Scraping
- [x] Analysis
- [x] Modeling 
- [ ] Deployment 

#### Contributor : 
Zakaria ADEM-HASSAN (SPMK22)

#### Timeline: 



Scraping : 02/01/2023 to 06/01/2023

Analysis : 10/01/2023 to 17/01/2023

Modeling : 19/01/2023 to 26/01/2023

Deployment : 27/01/2023 to ??/??/2023


