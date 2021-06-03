# SuperChef

### An E-commerce site for purchasing of Kitchen accessories.

[View live site here]()

![image]()

This is my fourth and final milestone project for Code institute’s full stack web developer diploma. This project is a **Django web application** made with the use of **HTML**, **CSS**, **JavaScript** and **Python** and utilizing a relational database.
**Stripe** is also used for payment system.
This project is plugged into a **PostgreSQL** database, with **SQlite3** used in development and was deployed using **Heroku**. **AWS S3 bucket** is used to store static and media files. The **Bootstrap** framework and grid system was used for styling across the site.
***

## **Table of Content**

* [Overview](#overview)

* [User Experience](#user-experience)
    
    * [User Goals](#user-goals)
    * [Business Goals](#business-goals)
    * [User Stories](#user-stories)
    * [Business Stories](#business-stories)

* [Planes of Development](#planes-of-development)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Wireframe](#wireframe)
        * [Sitemap](#sitemap)
    * [Surface](#surface)
        * [Color](#color)
        * [Typography](#typography)
        * [Images](#images)

* [Database model](#database-model)

* [Features](#features)
    * [Features Used](#features-used)
    * [Features to be implementd in Future](#features-to-be-implemented-in-future)

* [Technologies used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks](#frameworks)
    * [Extensions and Kits](#extensions-and-kits) 
    * [Project Management](#project-management)
    * [Tools](#tools)

* [Resources](#resources)

* [Testing](#testing)

* [Deployment](#deployment)
    * [Prerequisites](#prerequisites)
    * [How to Clone SuperChef](#how-to-clone-superchef)
    * [How to Deploy to Heroku](#how-to-deploy-to-heroku)

* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)
***

## **Overview**

SuperChef is an online e-commerce store, which offers a collection of Kitchenware in many categories. 
User’s can create their own account, saving their details for faster checkout for future purchases, but are not limited to that,
and can make a purchase as a guest if wanted.
The registered user can edit their personal details and access their shopping history.
Blogs are presented for good reads and site owner can be contacted easily.

[Go Back to Top](#table-of-content)
***

## **User Experience**

### **User Goals**

1.	Somewhere to search for few things which user want to have and do the purchasing in easy steps.
2.	In the current pandemic situation, Users may want to do purchasing from the safe environment of their home.
3.	User-friendly website, where user don’t have to be very technically educated to do the purchasing.

### **Business Goals**

1.	During the current world situation, when everybody is spending most of the time inside and home cooking is the only option available, People want to get some useful kitchen products to help them in cooking and baking.
2.	A kitchenware website, where buyers can easily find the product according to their category.
3.	To make the product’s view based on many sorting types. For example, price- low to high, high to low. Rating- low to high, high to low. Etc.
4.	The Site owner will have full control over the products, He/She can add, edit and delete products.
5.	Site will have Blogs related to kitchen and cooking, for the better involvement of the user.

### **User Stories**

 | User Story ID   | As a/an     | I want to be able to  |  So that I can  |
| ------------- |:----------:| :------:|  :-----:  |
|       Viewing and Navigation         |
| 1 | Site User    | Immediately get an overview of what products this site offers |  Decide if it contains what I am looking for  |
| 2 | Shopper    | View a list of products |  Select some to purchase  |
| 3 | Shopper    | View details about a specific product |  See a detailed description, larger image, price and rating of the product  |
| 4 | Shopper    | See total of all items in my shopping bag |  avoid over expenditure  |
| 5 | Shopper    | See the rating of every product |  see other,s opinion about the product  |
| 6 | Site User    | View the blog about the site |  Learn more about the Superchef  |
| --- |  ---  | ---  |  ---  |
|       Registration and User accounts         |
| 7 | Site User    | Easily register for an account |  Have a personal account to come back and view my profile  |
| 8 | Site User    | Easily Login or Logout |  Access my personal account information  |
| 9 | Site User    | Easily recover my password in case i forget it |  Regain access to my account  |
| 10 | Site User    | Receive a confirmation email after registering an account |  Know that my account registration was successful  |
| 11 | Site User    | have a personalised user profile |  View my order history, see my order confirmation and save my payment information  |
| --- |  ---  | ---  |  ---  |
|       Sorting and Searching         |
| 12 |  Shopper    | Select which category of product to show |  Easily find a product within the category that I am interested in  |
| 13 | Shopper    | Sort products by different parameters |  Easily find the products with the best rating or lowest price  |
| 14 | Shopper    | Search for the product by name or description |  Easily find the specific product that I am looking to buy  |
| 15 | Shopper    | Easily see what I have searched for and the number of results |  Identify misspelling in my search string and quickly overview the search result.  |
| --- |  ---  | ---  |  ---  |
|       Purchasing and Checkout         |
| 16 |  Shopper    | Easily select the number of product when adding it to my shopping bag |  Ensure I do not accidently select the wrong product or quantity  |
| 17 | Shopper    | Easily view all items in my shopping bag |  Identifying the total cost and overview the items to be ordered  |
| 18 | Shopper    | Change the quantity of a product in my shopping bag |  To correct any mistake in the shopping bag before ordering |
| 19 | Shopper    | Easily enter my payment information |  Checkout easily and quickly  |
| 20 |  Shopper    | Know that my personal and payment information is secure |  Feel confident when providing the information needed to make a purchase  |
| 21 | Shopper    | To know if the payment is done successfully or failed |  Check my card validity  |
| 22 | Shopper    | View an order confirmation after checkout |  See that I have not made any mistake in my order |
| 23 | Shopper    | Receive a confirmation email after ordering |  Keep the information about what I have ordered and when, for future needs  |
| 24 | Registered User    | Have my address and billing information prefilled on the checkout page |  Checkout quicker  |
| --- |  ---  | ---  |  ---  |
|       Admin and Store Management         |
| 25 |  Superuser    | Add a product to the site |  Add new items to be sold in my store  |
| 26 | Superuser    | Edit/ Update a product |  Make changes of the products image and description when needed  |
| 27 | Superuser    | Delete a product  |  Remove Items when it is sold or out of stock |
| 28 | Superuser    | Add, Update and Delete blog posts |  Write and maintain a blog about product related topics  |

### **Business stories**

As the Site owner I want/expect/need:
1.	To display the products colourfully.
2.	To manage all the products featured in the site by editing and deleting as required.
3.	To manage the blogs posted by editing and deleting as required.
4.	The User can contact me easily through the contact form or they can find me on social media accounts.

[Go back to Top](#table-of-content)
  ***