<h1>Laptop WebApp</h1>

<p>In this project I build an End-to-End machine learning website. It's main purpose is to help the user to predict the price of a laptop and recommend some laptops from the data set.</p>

<ul><h2>Skills I used:</h2>
  <li>Web Scraping</li>
  <li>Data Analysis</li>
  <li>PowerBI</li>
  <li>Machine learning</li>
  <li>Flask Server</li>
</ul>

<ol><h2>Steps:</h2>
  <li>Provide data for the project using selenium. Inorder to scrape a certain website and save the data to a new csv file</li>
  <li>Clean the data and create new feartures using pandas to use for the machine learning.</li>
  <li>Creating a PowerBi dashboard in order to analysis the data we have and understand the relations bwtween features</li>
  <li>Building a machine learning model functions to be reusable using the sklearn library. I train the Model and save it to a pickle file so i can use later.</li>
  <li>Use the functions and pickle file in a flask server. And emplenment the frontend and the backend for the user to be ready to use.</li>
</ol>

<ul><h2>Running The file:</h2>
  <li>select the data_app.py file</li>
  <li>run the file using "python data_app.py"</li>
  <li>open in local host port:5000</li>
  <li>enter the input you want and explore the result</li>
</ul>

<h2>Description:</h2>
<p>Here I preapare the web driver and open to the file to save data</p>
<img src="https://github.com/user-attachments/assets/4bfaf872-8ed7-4690-9359-b8270832887e" width="80%">

<p>This is a sample of cleaning the code</p> 
<img src="https://github.com/user-attachments/assets/327cc640-65ee-434f-88e6-7f2a47054e66" width="80%">

<p>This function is responsible for recommending the new laptop and open_data loads the data</p>
<img src="https://github.com/user-attachments/assets/c434ca12-c648-469b-b64c-02850ee1a4b8" width="80%">

<p>Here I open the pickle file to use the trained data and create the route</p>
<img src="https://github.com/user-attachments/assets/d85bbcca-37a6-46e5-9b94-135feaef4eda" width="80%">

<h2>Conclusion: </h2>
<p>This project was made by me Hussein Ghandour. The aim of this project is to emplement real life projects so that i can upscale my skills. Also any programmer is welcome to explore the code and use it for learning or anyhting.</p>

<h2>Final Result:</h2>
<img src="https://github.com/user-attachments/assets/b9dff0ae-c2bf-4a53-ad60-7b77bf34974f" width=80%>
<img src="https://github.com/user-attachments/assets/48c0d5f4-bc1a-4ccd-98d4-3a5dd427c9d9" width=80%>

Note: In the code Their should be a app.secret_key inoder for the prediction to come out you can place any you want by( app.secret_key='your_secret_key'
