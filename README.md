# **Site Title**
## **Site Overview**
This is where you give a brief overview of the page so, like an intro to the business or project followed by a brief talk about who the page is targeted at for example for a retro gaming arcade.
​
Retro arcade is a local business in the Sheffield area looking to offer young people a place to come and hangout and play old school games in a relaxed and friendly environment. Due to lower turnout than expected they have asked for a page to be built to spread the word in the community and wider areas. Ideally the business is intended to target younger gamers primarily but also be appealing to older people interested in a gaming experience 
​
![Am I responsive screenshot](imagelocation so maybe docs/image.jpg)
​
## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***Wireframes***](#wireframes)
    * [***Color Scheme***](#color-scheme)
    * [***Typography**](#typography)
1. [**Current Features Common to all pages**](#current-features-common-to-all-pages)
    * [***Header Element:***](#header-element)
    * [***The rest of your features***](#features)
    * [**Footer**](#footer)
1. [**Individual Page Content features**](#individual-page-content-features)
    * [**About Page Content**](#about-page-content)
    * [**Teachings Page Content**](#teachings-page-content)
    * [**Community Page Content**](#community-page-content)
    * [**Contact Page Content**](#contact-page-content)
    * [**Form Feedback Page Content**](#form-feedback-page-content)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference**](#general-reference)
    * [**Content**](#content)
    * [**Media**](#media)
​
## **Planning stage**
### **Target Audiences:**
​
This section is a breakdown of the target audience 3 or 4 bullet points so using our example
​
* Users interested in retro gaming 
* Users interested in a safe environment to gather and have fun
* Users interested in activities in the Sheffield area
​
### **User Stories:**
​
User stories are more what the user wants from the site in terms of features and presentation
​
* As a user, I want to see the subject matter of the page.
* As a user, I want to navigate the page to find what I require quickly and easily.
* As a user, I want to learn more about what the business offers
* As a user, I want to reach out and contact the business
​
### **Site Aims:**
​
Hangman in a terminal.
​
### **Color Scheme:**
​
We usually don't have much of a color scheme except White, Red, Blue and green. The exact hexagon codes I can sandly not provide considering I don't remember them fully myself at this point. 
​
## **Typography**
​
Here is a chance to discuss the fonts used and again why, doesn't need to be crazy detail
​
* Throughout the page, there are three fonts used:
  * Oswald - For the title to give it a strong presence.
  * DM sans - For all other headings including the navbar. 
  * Open sans - for all content text.
​
* DM and Open sans were both selected to complement each other and because they have a soft appearance which I thought best suited to the site
* All fonts were sourced from Google fonts, as stated in the credits.
​
## **Current Features Common to all pages**
​
#### *Navigation Bar:*
This is an example of the features section, your going to talk about each section of the page and what it offers for the navbar for example
​
* The user is given links to each section of the page
* Each option is presented in a way that is always obvious and reable
* on smaller screens a hamburger menu is provided to ensure mobile users have an optimal experience
​
#### *features
​
* This is where you will place all of your features think about each section of the page include a screenshot and a few bullet points on how it's presented and why
​
## **Future-Enhancements**
​
A webpage is a living beast it's going to evolve past the initial stages of release generally, it's always good to discuss where you this the page may go in the future
​
* At the time of making this page i didn't have the understanding to actual send e-mails from the contact form so intergration with email.js to send e-mails would improve the users experience
​
* Due to the subject matter, we have discussed the idea of including a small JS game to engage the user
​
## **Testing Phase**

The testing phase was mostly trial and errors. I managed to run into a lot of issues considering I didn't know how to add a spacing between words which usually ended up with me not being able to figure to fit in the 2nd word section. That was helped by my mentor during our last meeting. Otherwise the testing phase was honestly writing out the code and testing. I figured also that my print sections was broken in an early stage as it didn't show the Hangman figure as it should but only showed if a letter was right or wrong. Figured out that was an issue with the print statement and solved it by removing the overlapping text.​

Tested the code through the [Python validator](https://pep8ci.herokuapp.com/) And everything came back clean. Of course the only issues was the remaining invalid escape sequences and the error line on 336 which is noted in bugs section.
​
​
## **Bugs**
​
* There is an issue of a lot of the lines complaining about 'invalid escape sequence '\ 'flake8(W605)
Anomalous backslash in string: '\ '. String constant might be missing an r prefix.pylint(anomalous-backslash-in-string)'
which is unable to be fixed. This is not an error just an complaining from Python however to make the good looking signs they need to be added there :P

* On line 336 there is a complaining section about a 'to long line' however that isn't sadly something that can be solved. Wherever I cut the line it complains in any sort of error and in the end the code is working and running fine.

On line 66 is an empty drawspace. That is currently needed as to not break the entire Logo section. If that line is removed the end sequence is activated and the entire line becomes distorted ruining the Hangman text.
​
***
## **Deployment**
I deployed the page on GitHub pages via the following procedure: -
​
1. From the project's [repository](https://github.com/Fisboll/Hangman), go to the **Settings** tab.
2. From the left-hand menu, select the **Pages** tab.
3. Under the **Source** section, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
​
You  can find the live site via the following URL - [live webpage](https://yoururlhere)
***
​
## **Tech**
​
Here mention what technologies you've used for example
​
-Python
​
## **Credits**
### **Honorable mentions**

[Took the class of colors](https://github.com/gibbo101/hangman/blob/main/run.py)
This one I took the hangman pictures, Of course. I also took the base of how they made their difficult levels. [Where I got most inspiration](https://github.com/Bethieieio/project-three-console-hangman)

And my last mention is of course my amazing Mentor who helped me through it all!
​
It's always nice to mention those that helped you get there, if people gave you support on slack or the local cat scared you into completing give them a mention!
​
### **Content:**
​
If you took any code from online source and by this i mean copy paste with zero changes mention it here!