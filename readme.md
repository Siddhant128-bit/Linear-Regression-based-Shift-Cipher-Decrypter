<h1 align='center'> Linear regression Based Shift Cipher Decrypter </h1>

<p>In this repo I am just experimenting with the idea that if we have a normal text and cipher text we fine tune the dataset and train it on Linear Regression model with continous value output can we use the model to break the encryption </p>

<h3> Idea </h3>
<ul>
    <li> Initially we take a very large corpus with all possible texts, We loop over each character encode with shift cipher of key=5 </li>
    <li> We take the original characters as Y array and Encrypted characters as X array and save it as mydata.npz </li>
    <li> We fit it to the linear model where ascii value of each encrypted texts are in X and ascii value of each normal text is in Y </li>
    <li> As the model is trained we now calculate the Mean Squred Error to see how well its performing </li>
    <li> Finally we create inference testing capability such that we take in any encrypted text and get the actual text from it </li>
</ul>

<h3> Theoritical Informations </h3><br>
<h4> <b>Shift Cipher </b> </h4>
<p>The Shift Cipher is a simple and widely-used encryption technique in which each letter of a message is replaced with another letter that is a fixed number of positions down the alphabet. For example, with a shift of three, "A" would be replaced by "D", "B" would become "E", and so on. This is also known as a Caesar Cipher, named after Julius Caesar, who is said to have used this method to encode his private correspondence. Although the Shift Cipher is very easy to implement and understand, it is also very easy to crack, as there are only 26 possible shifts. In addition, it is vulnerable to frequency analysis attacks, in which an attacker can use the frequency of letters in the encrypted message to determine the shift used to encrypt it. Therefore, the Shift Cipher is not suitable for secure communications, but it can be used for educational purposes or as a starting point for more complex encryption algorithms. </p>
<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuZ4ytRGB1af8if-bpISkmrNeJ-shEqB1wL2GYkOlzIw&s'>
<h4> <b>Linear Regression  </b> </h4><br>
<p>Linear Regression is a statistical method used to find the relationship between two continuous variables. It assumes that there is a linear relationship between the dependent variable (also called the response or target variable) and one or more independent variables (also called the predictors or features). Linear Regression finds the best-fitting line that describes the relationship between these variables by minimizing the sum of the squared differences between the predicted and actual values of the dependent variable. The resulting line can be used to predict future values of the dependent variable based on the values of the independent variables. Linear Regression is widely used in various fields, such as finance, economics, social sciences, and engineering, to analyze and model the relationships between variables.</p>
<img src='https://static.javatpoint.com/tutorial/machine-learning/images/linear-regression-in-machine-learning.png'>
<br>
<h3><b> Performance of  Model</b></h3><br>
<img src='Results\mse.png'><br><br>
<a href='https://cryptii.com/pipes/caesar-cipher'> Use Shift Cipher here </a>
<img src='Results\cipher_text.png'>
As seen in the figure above we have cipher text encrypted with key 5 is </br><br>
<b>Encrypted Text</b>: FUUQJ <br>
<b>Plain  Text</b>: APPLE

<br>
Now we are going to feed the encrypted text in our model to check out the results and seen reult is shown below: 
<br><br>
<img src='Results\result_ciphering.png'>
<h3>More Results </h3>
<br><br>
<img width='500' height='50'src='Results\result_ciphering_1.png'>

<br><br>
<img width='500' height='50' src='Results\result_ciphering_2.png'>

<b>Note: This site works on shift cipher based on alphabets only and doesn't work on ASCII based shift cipher so it might have slight error for genearting encrypted text you can use <i>createdataset.py</i> to encrypt with key 5 and get the text </b>
