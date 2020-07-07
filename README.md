# Green_Rex

### Description:

  I'd like to create a strain recommender that takes in an some user inputs on: how they want to feel, taste, their experiecne with the product etc. It will then return a dictionary with 3 or so strains along with a description of the strains and related strains. I would like to include information on the terpene profiles, and what questions to ask their budtender if they cannot find said strain in the store. In the future, I'd also like to include store locations so that customers can get to the right spot, or if recomendaiton isn't in the store close to them, things at the store that are very similar. 
  
  
  ### Execution
  
   I created a database of the 50 top strains on Leafly based on user reviews. For each strain thea database entry contains all of the user reviews associated with the strain, the flavors, positive and negative effects, and the leafly description of the strain itself as well. I used these descriptions to create an index that i can query when making recommendations. The revies, tastes and effects are used when calculating the similarity scores while the description is returned with the results. 
    
  ### App 
  
   Currently the recoomender works as a stand alone app that you can run in your terminal. Once you are in this repo run  app.py to see the Dash dashboard where you can query for strains. 
   
