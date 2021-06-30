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
        * [Core](#core)
        * [Buttons](#buttons)
        * [Typography](#typography)
        * [Images](#images)

* [Database model](#database-model)

* [Features](#features)
    * [Features Used](#features-used)
    * [Features to be implementd in Future](#features-to-be-implemented-in-future)

* [Technologies used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Libraries, Frameworks and Editors](#libraries-frameworks-and-editors)
    * [Extensions and Kits](#extensions-and-kits) 
    * [Databases](#databases)
    * [Tools](#tools)

* [Bugs](#bugs)
    * [Project barriers and solutions](#project-barriers-and-solutions)
    * [Known Issues](#known-issues)

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
|    |       |    **Viewing and Navigation**         |    |
| 1 | Site User    | Immediately get an overview of what products this site offers |  Decide if it contains what I am looking for  |
| 2 | Shopper    | View a list of products |  Select some to purchase  |
| 3 | Shopper    | View details about a specific product |  See a detailed description, larger image, price and rating of the product  |
| 4 | Shopper    | See total of all items in my shopping bag |  avoid over expenditure  |
| 5 | Shopper    | See the rating of every product |  see other,s opinion about the product  |
| 6 | Site User    | View the blog about the site |  Learn more about the Superchef  |
| --- |  ---  | ---  |  ---  |
|     |     |  **Registration and User accounts**         |      |
| 7 | Site User    | Easily register for an account |  Have a personal account to come back and view my profile  |
| 8 | Site User    | Easily Login or Logout |  Access my personal account information  |
| 9 | Site User    | Easily recover my password in case i forget it |  Regain access to my account  |
| 10 | Site User    | Receive a confirmation email after registering an account |  Know that my account registration was successful  |
| 11 | Site User    | have a personalised user profile |  View my order history, see my order confirmation and save my payment information  |
| --- |  ---  | ---  |  ---  |
|     |      |   **Sorting and Searching**         |      |
| 12 |  Shopper    | Select which category of product to show |  Easily find a product within the category that I am interested in  |
| 13 | Shopper    | Sort products by different parameters |  Easily find the products with the best rating or lowest price  |
| 14 | Shopper    | Search for the product by name or description |  Easily find the specific product that I am looking to buy  |
| 15 | Shopper    | Easily see what I have searched for and the number of results |  Identify misspelling in my search string and quickly overview the search result.  |
| --- |  ---  | ---  |  ---  |
|      |      |    **Purchasing and Checkout**         |      |
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
|       |      |   **Admin and Store Management**         |       |
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

## **Planes of Development**
### **Strategy**

The aim of making this site is to make a website that focuses mainly on kitchen products. 
There are plenty of sites right now but very few focuses only in kitchen tools and accessories. We are going through a pandemic and lockdown situation worldwide. We are bound to stay inside our home and left with very few activities, in that cooking is a good hobby to pursue.
 As we know new cooks are very keen to try new utensils and accessories, so this site might be a good place for them to search the product of their choice.

 ### **Scope**

 I want to make a website that is accessible to everyone. People can search and browse all the products without being registered, 
 so that their will be no hesitation in going through the site. Anyone can do the purchasing by adding his/her details and doing valid payment. 
 
 The detail of every product opens in new page with product rating with it, so it is easier to decide which product to buy. 
 
 Products can be sorted in various ways like price- low to high or high to low, category, ratings etc. users can make their profile, so that when they return back, they will have their details already filled.
Users can go through the blog page and write a comment if they want. And they can contact the site owner with the contact form provided.

### **Structure**

This website will be a multi-page site, where pages are connected through Navigation Bar or Python. 
The navigation bar will have links for the Home page, my account(login, register), bag, and Blog. The navigation links will change and show the logout and My profile Once the user is logged in. 
It will show product management link for the superuser.The navigation bar will be collapsible for Mobile view . 
There will be a footer, which will show the contact details of the admin. It will be sticky and always remain at the end of the page. 2 forms will be there, one for Login and the other for Registration. 
One contact form will also be there for the users to contact the admin. There will be pages for products, product details, shopping bag, checkout, checkout success, blog, blog details, Users will have a my profile page after the register with the site. Superuser will do the product management, he/she can add edit and delete any product. Superuser will post the blog which can be commented by any user .
SQLite3 is used in development and PostgreSQL database is used in production mode. All the static and media file will be stored in AWS s3 bucket it will be deployed by using Heroku.

### **Skeleton**
#### **Wireframe**
The wireframe for this project has been made for Three screen sizes(Mobile View, Tablet View, and Laptop View). Each page is shown in all three 
screen sizes for a better understanding of the responsiveness of the page.

The wireframes for this Project can be seen here.

1. [Home Page](docs/wireframes/HomePage.pdf)

2. [Products Page](docs/wireframes/ProductsPage.pdf)

3. [Product Details Page](docs/wireframes/ProductDetailsPage.pdf)

4. [Category Page](docs/wireframes/CategoryPage.pdf)

5. [My Profile Page](docs/wireframes/MyProfilePage.pdf)

6. [Login Page](docs/wireframes/LoginPage.pdf)

7. [Register Page](docs/wireframes/RegisterPage.pdf)

8. [Bag Page](docs/wireframes/BagPage.pdf)

9. [Checkout Page](docs/wireframes/CheckoutPage.pdf)

10. [Contact page](docs/wireframes/ContactPage.pdf)

11. [Blog Page](docs/wireframes/BlogPage.pdf)

12. [Blog Details Page](docs/wireframes/BlogDetailsPage.pdf)

13. [Product Management Page](docs/wireframes/ProductManagementPage.pdf)

#### **Sitemap**
Sitemap is prepared for this site to understand the navigation of the pages.

Sitemap can be seen here. [Sitemap](docs/wireframes/Sitemap.pdf)

### **Surface**
#### **Color**

The color used for this project are kept very minimum, so that the strong tonal varitaion provides a good contrast. The main color used for the project is Mustard yellow(#E1AD01), which goes very well with the kitchen theme and it is a good contrast with the other two colors Black(#000000) and White(#ffffff).

The colors used are:

![image](docs/Capture.JPG)

Mustard Yellow color is used for delivery Banner and hover over across page. The Text color used are mainly black and changes to mustard yellow when hovered over.
The placeholder text for the form have color Cadet Blue(#AAB7C4) and rating text of the product description is Bootstrap text-muted class Slate Gray(#6C757d)



#### **Core**

The Core of the project is kept Black and White. The navbar is White and Main nav is Black, which has text written in white that changes to mustard yellow when hovered over. 
The Footer is Black with texts of white color. The social media links and Contact link changes to mustard yellow color when hovered over.
The pages of the project are kept white to make a good contrast with the products images.

#### **Buttons**

The Buttons are kept black with text white, which changes to mustard yellow when hovered over.
The edit and delete links have given a consistent coloue with the intuitative suggestions about their functions.
The edit is kept Dodger Blue(#007BFF) and Delete link is Amaranth(#DC3545)
The back to top button is Mustard yellow(#E1AD01)

*  ![#000000](https://via.placeholder.com/15/00000/000000?text=+) `#000000` (Black)
*  ![#007BFF](https://via.placeholder.com/15/007bff/000000?text=+) `#007bff` (Dodger Blue)
*  ![#DC3545](https://via.placeholder.com/15/dc3545/000000?text=+) `#DC3645`(Amaranth)
*  ![#E1AD01](https://via.placeholder.com/15/e1ad01/000000?text=+) `#E1AD01`(Mustard Yellow)

#### **Typography**

[Montserrat](https://fonts.google.com/specimen/Montserrat?query=mon)

Google font **Montserrat** with a fallback of **sans serif** is selected for the entire project.

#### **Images**

Images used are taken from [Unsplash](https://unsplash.com/) and [Google](https://www.google.com). 

[Go back to Top](#table-of-content)
***

## **Database Model**

[Go back to Top](#table-of-content)
***

## **Features**

[Go back to Top](#table-of-content)
***

## **Technologies used**

### **Languages Used**

* [HTML](https://en.wikipedia.org/wiki/HTML) is the main language used to write code for this project.
* [CSS](https://en.wikipedia.org/wiki/CSS) is used to write code for designing and beautifying the site.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) is used to add functionality and make the site more interactive.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is used for the Backend Programming.
  * [jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) is used as the template engine for Python.

### **Libraries, Frameworks and Editors**

 * [Django](https://www.djangoproject.com/) is a Python Web Framework, which is used for development.
 * [AWS S3](https://aws.amazon.com/s3/) cloud storage for static and media files.
 * [VS Code](https://code.visualstudio.com/) main workspace IDE(integrated Development Environment).
 * [jQuery](https://jquery.com/) was used for the interactive features.
 * [Bootstrap](https://getbootstrap.com/) is used to make main structure and layout of the project.
 * [Google Fonts](https://fonts.google.com/) was used for the font 'Montserrat' for this project .
 * [Font Awesome](https://fontawesome.com/) is used to import Social media icons to beautify the footer, and icons for bag and user in every page.
 * [GitHub](https://github.com/) is used to make **Repositories** and for **Version Control**.
 * [Git](https://git-scm.com/) was used for version control by making use of the gitpod terminal to add, commit and push to github..
 * [Heroku](https://www.heroku.com/about) was used for deploying the app.
 * [Unsplash](https://unsplash.com/) was used to get imagesfor background and blogs.
 * [Google Images](https://www.google.com/) was used to get images for the products.

### **Extensions and Kits**

 * [Django allauth](https://django-allauth.readthedocs.io/en/latest/) was used as authentication system.
 * [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to format forms.
 * [Pillow](https://pillow.readthedocs.io/en/stable/) Python imaging library to help store imagery into a database.
 * [psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter for the Python.

### **Databases**

 * [Sqlite 3](https://www.sqlite.org/index.html) Used as development database.
 * [PostgresSQL](https://www.postgresql.org/) used as the database for deployment.

### **Tools**

 * [Stripe](https://stripe.com/ie) used as as the payment infrastucture to take payments on the site.
 * [Am I Responsive?](http://ami.responsivedesign.is/) is used to take a mockup screenshot of the project, which is attached at the beginning of this document.
 * [Autoprefixer](https://autoprefixer.github.io/) is used to make the site compatible with all browsers.
 * [iColorpalette](https://icolorpalette.com/) is used to find a relevant color palette for the site.
 * [W3C Validator](https://validator.w3.org/) is used for testing HTML and CSS for the site.
 * [JSHint](https://jshint.com/) is used for testing javascript code for the site.
 * [PEP8 online](http://pep8online.com/) is used for testing Python codes.
 * [Online Spelling Check](https://www.grammarly.com/), Grammarly is used to check spelling and grammatical errors.
 * [Snipping Tool](https://en.wikipedia.org/wiki/Snipping_Tool) was used to take screenshots of the images and codes.
 * [TinyPNG](https://tinypng.com/) is used to reduce the size of the Hero Image.
 * [Balsamiq](https://balsamiq.com/wireframes/) is used to make wireframes for this project in the skeleton stage.


[Go back to Top](#table-of-content)
***

## **Bugs**

### **Project barriers and solutions**

* While making the index.html page for Home app, I tried to show background images by adding them in media folder, but it was not working. It was working fine when i tried to add the images from static folder. I checked every spelling error in settings.py and project level urls.py file, but I could not find any mistake. I searched in [Django documentation](https://docs.djangoproject.com/en/3.2/) also to check if the code is correct. I found that the code is correct. So, I searched in slack for some related issues and I found one suggestion from a member to add one code in settings.py's context_processor. I tried that code and images started loading perfectly. the code used was 
        
        'django.template.context_processors.media',

* Blog and comments on blog are the 2 extra models which were decided by me to add in the project. Adding Blog , Editing it and Deleting dunctions worked fine but when I added comment model and wrote view for it, the blog detail section started giving error, those errors were unfamiliar to me. So, i contacted Tutor support but could not get any help from there. So I started going line by line and trying to understand it and I found that my comment variable in database has no connection with the blog variable in the view. So, I made the correction and after few trial the view started working. The line which was written wrong and then corrected was 

         'new_comment.post = blog'

### **Known Issues**

[Go back to Top](#table-of-content)
***

## **Testing**

[Go back to Top](#table-of-content)
***

## **Deployment**

[Go back to Top](#table-of-content)
***

## **Credits**

[Go back to Top](#table-of-content)
***


