# mobile_gaming_analysis
The project is an imaginary scenario, analysing purchasing data of a mobile gaming company. 

The project's goal is to check patterns of users committing microtransactions in a new mobile game app.
The company had a small test, in order to find which package will be more popular among users.
In the test, the users were divide to three groups: A, B and C- each group corresponds to a different package price.
At first, I took a qiuck glance into the data file I recieved from the company (line 5-9).
The raw data isn't orginized in the most useful way- therefore I converted the data into a contingency table (line 12).
The table now shows a clear view on how many users in each group purchased or declined a purchase offer of a package.
To find if there are any significant differences in the purchase rates between the groups, I conducted a Chi Square Test, and found out that the p value indicated a significant difference between group A, B and C.
The company didn't mentioned what is the price gap between the groups- after quick check with some colleagues, I found out the following:
  
  Group A - received a $0.99 offer.
  Group B - received a $1.99 offer.
  Group C - received a $4.99 offer.
  

Regarding the price differences, it is not too surprising to find that the majority of users who purchased the package are from group A.
But there is a problem! It seems like we asked the wrong question here- rather asking which package is the most popular among users, we should ask ourselves which package price would justify the development of the new package.
The Product manager said, building the features the new package offers must generate at least $1000 per week in order to be profitable for the company.
In order to justify this feature, we will need to calculate the necessary purchase rate for each price point.

I started by calculating the total number of users in the last week (line 42), and than calculating the proportions of weekly users that must buy the package in order to reach the $1000 goal (lines 45-67).
Than, we want to know if the percent of Group A (the $0.99 price point) that purchased an upgrade package is significantly greater than p_sales_needed_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our minimum revenue target of $1,000).

To answer this question, we want to focus on just the visitors in group A. Then, we want to compare the number of purchases in that group to p_sales_needed_099.
Since we have a single sample of categorical data and want to compare it to a hypothetical population value, a binomial test is appropriate. I did the same to groups B and C (lines 69-125).
After the binominal test, we must compare the p values that emerged (131-137).

In this case, I discovered that the price that will justify the development of the new features-packge, according to the purchase rates of the different package prices will be $4.99 .
