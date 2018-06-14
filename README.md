# HealthCare-Predictions

Processes a collection of physical spine data (which consists of numeric data).
Uses Decision Tree Classifier to predict (give assumption) if a spine is normal or abnormal. 

The system is separated on several parts - classifier, front-end part which
gets the user data, visualizes the result and shows an image of the decision tree
which the classifier has build. 
The server part is developed on Python using the Flask framework. It has the following 
functionality - connects the client part and the classifier by sending the data between them.
The classifier is developed on Python using the scikit-learn library.

Additonal information about the system:
- Client-side validation

Technology Stack:
- Front-end
   - HTML
   - CSS
   - JavaScript
   - jQuery
- Back-end
  -	Python
  -	Flask framework
    - Request – reads request data from the client-side
    - Json – work with json objects
  -	Flask_cors – work with CORS requests
-	Classifier
  -	scikit-learn
    - tree - for the classifier
  -	numpy – work with arrays
  -	pandas – read .csv files
  -	collections – work with list in Python
  -	Graphviz – to generate the tree in .dot file
  -	pydotplus – to visualize the .dot file with the tree
  
  
  Generated image of the tree:
  ![alt text](static/images/tree.png)
